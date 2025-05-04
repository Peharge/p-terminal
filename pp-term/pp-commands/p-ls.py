# Englisch | Peharge: This source code is released under the MIT License.
#
# Usage Rights:
# The source code may be copied, modified, and adapted to individual requirements.
# Users are permitted to use this code in their own projects, both for private and commercial purposes.
# However, it is recommended to modify the code only if you have sufficient programming knowledge,
# as changes could cause unintended errors or security risks.
#
# Dependencies and Additional Frameworks:
# The code relies on the use of various frameworks and executes additional files.
# Some of these files may automatically install further dependencies required for functionality.
# It is strongly recommended to perform installation and configuration in an isolated environment
# (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
#
# Disclaimer:
# Use of the code is entirely at your own risk.
# Peharge assumes no liability for damages, data loss, system errors, or other issues
# that may arise directly or indirectly from the use, modification, or redistribution of the code.
#
# Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

# Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
#
# Nutzungsrechte:
# Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
# Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
# Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
# da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
#
# Abhängigkeiten und zusätzliche Frameworks:
# Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
# Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
# Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
# um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
#
# Haftungsausschluss:
# Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
# Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
# die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
#
# Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

# Français | Peharge: Ce code source est publié sous la licence MIT.
#
# Droits d'utilisation:
# Le code source peut être copié, édité et adapté aux besoins individuels.
# Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
# Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
# car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
#
# Dépendances et frameworks supplémentaires:
# Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
# Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
# Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
# pour éviter d'éventuels conflits avec les installations de logiciels existantes.
#
# Clause de non-responsabilité:
# L'utilisation du code est entièrement à vos propres risques.
# Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
# pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
#
# Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

import os
import sys
import datetime
import chardet

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor, QIcon, QPalette, QFont, QPixmap, QImageReader
from PyQt6.QtWidgets import (
    QApplication, QLabel, QScrollArea, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget,
    QTextEdit, QTextBrowser, QStackedWidget
)

# Optional syntax highlighting
try:
    from pygments import highlight
    from pygments.lexers import get_lexer_for_filename
    from pygments.formatters import HtmlFormatter
    PYGMENTS_AVAILABLE = True
except ImportError:
    PYGMENTS_AVAILABLE = False

class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P-Term File Explorer")
        self.setGeometry(100, 100, 1200, 800)

        self.set_dark_mode()
        self._setup_icon()
        self._setup_widgets()
        self.apply_styles()
        self.load_directory_structure()

    def _setup_icon(self):
        user = os.getenv("USERNAME") or os.getenv("USER")
        base = os.path.expanduser(f"~/{user}/p-terminal/pp-term/icons/")
        path = os.path.join(base, "p-term-logo-5.ico")
        if os.path.exists(path):
            self.setWindowIcon(QIcon(path))

    def _setup_widgets(self):
        layout = QVBoxLayout(self)

        # File tree
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Name", "Type", "Size", "Date Modified"])
        self.tree.itemClicked.connect(self.display_file_content)
        layout.addWidget(self.tree)

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/p-terminal/pp-term/icons/p-term-logo-5.ico"
        self.setWindowIcon(QIcon(icon_path))

        # Content area with stack
        self.stack = QStackedWidget()
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setFont(QFont("Courier New", 12))

        self.markdown_view = QTextBrowser()
        self.markdown_view.setOpenExternalLinks(True)
        self.markdown_view.setFont(QFont("Courier New", 12))

        self.image_label = QLabel(alignment=Qt.AlignmentFlag.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.image_label.setScaledContents(True)

        # Add widgets to stack
        self.stack.addWidget(self.text_edit)
        self.stack.addWidget(self.markdown_view)
        self.stack.addWidget(self.image_label)

        # Scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.stack)
        layout.addWidget(self.scroll_area)

        # Status label
        self.status_label = QLabel("Loading...")
        layout.addWidget(self.status_label)

    def set_dark_mode(self):
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColor(46, 46, 46))
        pal.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.setPalette(pal)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
                color: #FFFFFF;
                font-family: 'Roboto', sans-serif;
                font-size: 14px;
            }
            
            QLineEdit {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
                border: 1px solid #778899;
                border-radius: 5px;
                padding: 5px;
                color: #FFFFFF;
            }
            
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
                color: #FFFFFF;
            }
            
            QPushButton:hover {
                background-color: #1c2833;
            }
            
            QTreeWidget {
                background-color: transparent;
                border: 1px solid #778899;
                border-radius: 8px;
            }
            
            QTreeWidget::item {
                padding: 8px;
                border-bottom: 1px solid #778899;
            }
            
            QTreeWidget::item:selected {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
                color: #FFFFFF;
            }
            
            QHeaderView::section {
                background-color: transparent;
                padding: 8px;
                border: none;
            }
            
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            
            QScrollBar:vertical {
                background-color: transparent;  /* Hintergrund (Schiene) in transparent */
                width: 10px;
                border-radius: 5px;
            }
            
            QScrollBar::handle:vertical {
                background-color: #ffffff;  /* Schieber (Block) in Weiß */
                min-height: 20px;
                border-radius: 5px;
            }
            
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: transparent;
            }
            
            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: transparent;
            }
            
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: transparent;
            }
            
            QScrollBar:horizontal {
                background-color: transparent;  /* Auch der horizontale Balken in transparent */
                height: 10px;
                border-radius: 5px;
            }
            
            QScrollBar::handle:horizontal {
                background-color: #ffffff;
                min-width: 20px;
                border-radius: 5px;
            }
            
            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                background: transparent;
            }
            
            QScrollBar::left-arrow:horizontal,
            QScrollBar::right-arrow:horizontal {
                background: transparent;
            }
            
            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: transparent;
            }
            
            QLabel {
                background: transparent;
                font-size: 16px;
            }
            
            QTextEdit {
                background-color: transparent;
                color: #FFFFFF;
                border: 1px solid #778899;
                border-radius: 8px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
        """)

    def load_directory_structure(self):
        root = os.path.expanduser("~/p-terminal/pp-term/")
        self.tree.clear()
        self._add_directory_to_tree(root)
        self.status_label.setText("Directory structure loaded.")

    def _add_directory_to_tree(self, path, parent_item=None):
        try:
            entries = sorted(os.scandir(path), key=lambda e: (not e.is_dir(), e.name.lower()))
        except PermissionError:
            return
        for entry in entries:
            if entry.name.lower() == 'doom.run':
                continue
            item = QTreeWidgetItem([
                entry.name,
                'Directory' if entry.is_dir() else 'File',
                self.format_size(entry.stat().st_size) if entry.is_file() else '',
                datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            ])
            if parent_item:
                parent_item.addChild(item)
            else:
                self.tree.addTopLevelItem(item)
            if entry.is_dir():
                self._add_directory_to_tree(entry.path, item)

    def format_size(self, size_bytes):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.1f} PB"

    def display_file_content(self, item):
        if item.text(1) != 'File':
            return
        full_path = self.get_full_path(item)
        ext = os.path.splitext(full_path)[1].lower()

        # Image display
        if QImageReader and QImageReader(full_path).canRead() or ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
            pixmap = QPixmap(full_path)
            if not pixmap.isNull():
                scaled = pixmap.scaled(self.scroll_area.viewport().size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.image_label.setPixmap(scaled)
                self.stack.setCurrentWidget(self.image_label)
                self.status_label.setText(f"Displayed image '{os.path.basename(full_path)}'")
                return

        # Markdown files
        if ext in ['.md', '.markdown']:
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    md = f.read()
                self.markdown_view.setMarkdown(md)
                self.stack.setCurrentWidget(self.markdown_view)
                self.status_label.setText(f"Displayed markdown '{os.path.basename(full_path)}'")
            except Exception as e:
                self.text_edit.setPlainText(f"Error reading markdown: {e}")
                self.stack.setCurrentWidget(self.text_edit)
                self.status_label.setText("Failed to display markdown.")
            return

        # Syntax highlighting for code
        code_exts = ['.py', '.cpp', '.c', '.h', '.bat']
        if ext in code_exts and PYGMENTS_AVAILABLE:
            try:
                code = open(full_path, 'r', encoding='utf-8', errors='replace').read()
                lexer = get_lexer_for_filename(full_path, stripall=True)
                formatter = HtmlFormatter(full=True)
                html = highlight(code, lexer, formatter)
                self.markdown_view.setHtml(html)
                self.stack.setCurrentWidget(self.markdown_view)
                self.status_label.setText(f"Displayed code '{os.path.basename(full_path)}' with highlighting")
            except Exception as e:
                self.text_edit.setPlainText(f"Error highlighting code: {e}")
                self.stack.setCurrentWidget(self.text_edit)
                self.status_label.setText("Failed to highlight code.")
            return

        # Plain text fallback
        try:
            raw = open(full_path, 'rb').read()
            enc = chardet.detect(raw)['encoding'] or 'utf-8'
            txt = raw.decode(enc, errors='replace')
            self.text_edit.setPlainText(txt)
            self.stack.setCurrentWidget(self.text_edit)
            self.status_label.setText(f"Displayed '{os.path.basename(full_path)}' ({enc} decoded)")
        except Exception as e:
            self.text_edit.setPlainText(f"Error reading file: {e}")
            self.stack.setCurrentWidget(self.text_edit)
            self.status_label.setText("Failed to display file.")

    def get_full_path(self, item):
        parts = []
        while item:
            parts.insert(0, item.text(0))
            item = item.parent()
        base = os.path.expanduser("~/p-terminal/pp-term/")
        return os.path.join(base, *parts)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        w = self.width()
        self.tree.setColumnWidth(0, int(w * 0.40))
        for i in range(1, 4):
            self.tree.setColumnWidth(i, int(w * 0.20))
        # Rescale image if displayed
        if self.stack.currentWidget() == self.image_label and not self.image_label.pixmap() is None:
            pixmap = self.image_label.pixmap()
            scaled = pixmap.scaled(self.scroll_area.viewport().size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.image_label.setPixmap(scaled)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FileExplorer()
    win.show()
    sys.exit(app.exec())