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

import sys
import subprocess
import json
import logging
import os
from pathlib import Path
from typing import List, Dict

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtGui import QIcon

# SETTINGS: Path to vswhere.exe (adjust if not in PATH)
VSWHERE_PATH = Path(
    "C:/Program Files (x86)/Microsoft Visual Studio/Installer/vswhere.exe"
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Worker(QtCore.QThread):
    """
    Executes vswhere.exe, decodes the output safely as UTF-8,
    and sends the result or error via signal.
    """
    resultReady = QtCore.pyqtSignal(list)
    errorOccurred = QtCore.pyqtSignal(str)

    def run(self) -> None:
        # Ensure vswhere.exe exists
        if not VSWHERE_PATH.exists():
            err = f"vswhere.exe not found: {VSWHERE_PATH}"
            logging.error(err)
            self.errorOccurred.emit(err)
            return

        try:
            logging.info("Starting vswhere.exe…")
            proc = subprocess.run(
                [str(VSWHERE_PATH), "-all", "-products", "*", "-format", "json"],
                capture_output=True,
                check=True
            )

            raw_out: bytes = proc.stdout or b""
            text_out: str = raw_out.decode("utf-8", errors="replace")

            try:
                data = json.loads(text_out)
            except json.JSONDecodeError as je:
                msg = f"JSON error: {je.msg} (Position {je.pos})"
                logging.error(msg + "\n" + text_out[:200] + "…")
                self.errorOccurred.emit(msg)
                return

            logging.info(f"{len(data)} instance(s) found.")
            self.resultReady.emit(data)

        except subprocess.CalledProcessError as cpe:
            err_text = (cpe.stderr or b"").decode("utf-8", errors="ignore").strip()
            msg = f"vswhere.exe failed: {err_text or cpe}"
            logging.error(msg)
            self.errorOccurred.emit(msg)

        except Exception as e:
            msg = f"Unexpected error in Worker.run(): {e}"
            logging.exception(msg)
            self.errorOccurred.emit(msg)


class LoadingOverlay(QtWidgets.QWidget):
    """
    Semi-transparent overlay with animated spinner.
    """
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super().__init__(parent)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setStyleSheet("background: rgba(0, 0, 0, 120);")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Animation (spinner.gif must be in the same folder)
        gif_path = Path(__file__).parent / "spinner.gif"
        if gif_path.exists():
            self.spinner = QtWidgets.QLabel(self)
            movie = QtGui.QMovie(str(gif_path))
            self.spinner.setMovie(movie)
            movie.start()
            layout.addWidget(self.spinner)
        else:
            lbl = QtWidgets.QLabel("🔄 Loading build tools…", self)
            lbl.setFont(QtGui.QFont("", 16))
            lbl.setStyleSheet("color: white;")
            layout.addWidget(lbl)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        super().resizeEvent(event)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("P-Term Visual Studio Build Tools Inspector")
        self.resize(900, 650)

        # Assumes the repository is in the p-terminal folder of the current user
        user = os.getenv("USERNAME") or os.getenv("USER")
        self.repo_path = f"C:/Users/{user}/p-terminal/pp-term"
        icon_path = f"C:/Users/{user}/p-terminal/pp-term/icons/p-term-logo-5.ico"
        self.setWindowIcon(QIcon(icon_path))

        # Central widget & layout
        central = QtWidgets.QWidget(self)
        self.setCentralWidget(central)
        vbox = QtWidgets.QVBoxLayout(central)

        # Toolbar with icon
        toolbar = QtWidgets.QToolBar()
        self.addToolBar(toolbar)
        icon = self.style().standardIcon(
            QtWidgets.QStyle.StandardPixmap.SP_BrowserReload
        )
        refresh_action = QtGui.QAction(icon, "Refresh", self)
        refresh_action.setToolTip("Reload data")
        refresh_action.triggered.connect(self.load_data)
        toolbar.addAction(refresh_action)

        # Tree view
        self.tree = QtWidgets.QTreeWidget()
        self.tree.setHeaderLabels([
            "Instance ID", "InstallPath", "Version", "DisplayName"
        ])
        vbox.addWidget(self.tree)

        # Status bar
        self.status = QtWidgets.QStatusBar()
        self.setStatusBar(self.status)

        # Loading overlay (initially hidden)
        self.overlay = LoadingOverlay(self.centralWidget())
        self.overlay.hide()

        # Initial query shortly after start
        QtCore.QTimer.singleShot(100, self.load_data)

    def load_data(self) -> None:
        """Starts the worker thread to load data."""
        self.tree.clear()
        self.status.showMessage("Loading build tools information...")
        self.overlay.show()

        self.worker = Worker(self)
        self.worker.resultReady.connect(self.on_data_ready)
        self.worker.errorOccurred.connect(self.on_error)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.start()

    def on_data_ready(self, data: List[Dict]) -> None:
        """Populates the tree when data is received."""
        for inst in data:
            top = QtWidgets.QTreeWidgetItem([
                inst.get("instanceId", ""),
                inst.get("installationPath", ""),
                inst.get("installationVersion", ""),
                inst.get("displayName", ""),
            ])
            # Workloads
            for w in inst.get("workloads", []):
                w_item = QtWidgets.QTreeWidgetItem([f"⚙️ {w.get('id', '')}"])
                top.addChild(w_item)
            # Components
            for c in inst.get("components", []):
                c_item = QtWidgets.QTreeWidgetItem([f"🔧 {c.get('id', '')}"])
                top.addChild(c_item)

            self.tree.addTopLevelItem(top)

        self.status.showMessage(f"{len(data)} instance(s) loaded.", 5000)
        self.overlay.hide()

    def on_error(self, msg: str) -> None:
        """Displays error message and hides overlay."""
        self.overlay.hide()
        logging.error("Error loading data: " + msg)
        QtWidgets.QMessageBox.critical(self, "Error", msg)
        self.status.showMessage("Error loading data", 5000)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """Ensures the worker is cleanly terminated."""
        if hasattr(self, "worker") and self.worker.isRunning():
            self.worker.quit()
            self.worker.wait(2000)
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Global style sheet (outsourced for better readability)
    STYLE = """
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

            QLabel {
                background: transparent;
                font-size: 16px;
            }

            QTextEdit {
                background-color: transparent;
                border: 1px solid #778899;
                border-radius: 8px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
            
            QTabBar::tab {
                background: transparent;
                padding: 8px;
                margin: 2px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
                color: #FFFFFF;
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
    """
    app.setStyleSheet(STYLE)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
