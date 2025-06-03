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
import shutil
import argparse
import os
from pathlib import Path
from typing import List, Dict, Optional

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtGui import QIcon

# Constants
DEFAULT_VSWHERE = Path(
    "C:/Program Files (x86)/Microsoft Visual Studio/Installer/vswhere.exe"
)
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="VS Build Tools Inspector with customizable style sheet"
    )
    parser.add_argument(
        "--style",
        type=Path,
        help="Optional path to a .qss style sheet",
        default=Path(__file__).parent / "style.qss"
    )
    parser.add_argument(
        "--vswhere",
        type=Path,
        help="Path to vswhere.exe",
        default=DEFAULT_VSWHERE
    )
    return parser.parse_args()


class VsWhereWorker(QtCore.QRunnable):
    """
    QRunnable to execute vswhere.exe and emit results.
    """

    class Signals(QtCore.QObject):
        finished = QtCore.pyqtSignal()
        result = QtCore.pyqtSignal(list)
        error = QtCore.pyqtSignal(str)

    def __init__(
        self,
        vswhere_path: Path,
        include_workloads: bool = True,
        include_components: bool = True,
    ):
        super().__init__()
        self.vswhere_path = vswhere_path
        self.include_workloads = include_workloads
        self.include_components = include_components
        self.signals = self.Signals()

    @QtCore.pyqtSlot()
    def run(self) -> None:
        if not self.vswhere_path.exists():
            msg = f"vswhere.exe not found: {self.vswhere_path}"
            logging.error(msg)
            self.signals.error.emit(msg)
            self.signals.finished.emit()
            return

        args = [str(self.vswhere_path), "-all", "-format", "json"]
        if self.include_workloads:
            args[2:2] = ["-products", "*"]

        try:
            logging.info("Invoking vswhere: %s", args)
            proc = subprocess.run(
                args,
                capture_output=True,
                check=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            data = json.loads(proc.stdout)
            logging.info("Found %d instances.", len(data))
            self.signals.result.emit(data)
        except subprocess.CalledProcessError as e:
            err = (e.stderr or str(e)).strip()
            logging.error("vswhere failed: %s", err)
            self.signals.error.emit(f"vswhere failed: {err}")
        except json.JSONDecodeError as e:
            logging.error("JSON parse error: %s", e)
            self.signals.error.emit(f"JSON parse error: {e.msg}")
        except Exception as e:
            logging.exception("Unexpected error in VsWhereWorker")
            self.signals.error.emit(str(e))
        finally:
            self.signals.finished.emit()


class LoadingOverlay(QtWidgets.QWidget):
    """Semi-transparent overlay with spinner or fallback label."""

    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super().__init__(parent)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setStyleSheet("background: rgba(0,0,0,0.5);")
        self.setVisible(False)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        gif = Path(__file__).parent / "spinner.gif"
        if gif.exists():
            lbl = QtWidgets.QLabel(self)
            movie = QtGui.QMovie(str(gif))
            lbl.setMovie(movie)
            movie.start()
            layout.addWidget(lbl)
        else:
            lbl = QtWidgets.QLabel("Loading…", self)
            lbl.setStyleSheet("color:white; font-size:16px;")
            layout.addWidget(lbl)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.setGeometry(self.parent().rect())
        super().resizeEvent(event)


class MainWindow(QtWidgets.QMainWindow):
    """
    Main application window for Visual Studio Build Tools Inspector.
    """

    def __init__(self, vswhere_path: Path, style_path: Path) -> None:
        super().__init__()
        self.vswhere_path = vswhere_path
        self.style_path = style_path
        self.current_data: List[Dict] = []
        self.setup_logging()
        self.setWindowTitle("P-Term VS Build Tools Inspector")
        self.resize(1000, 700)
        self.init_ui()
        self.init_worker_pool()

        # Annahme: Das Repository befindet sich im p-terminal-Ordner des aktuellen Benutzers
        user = os.getenv("USERNAME") or os.getenv("USER")
        self.repo_path = f"C:/Users/{user}/p-terminal/pp-term"
        icon_path = f"C:/Users/{user}/p-terminal/pp-term/icons/p-term-logo-5.ico"
        self.setWindowIcon(QIcon(icon_path))


    def setup_logging(self) -> None:
        logging.basicConfig(
            level=logging.INFO,
            format=LOG_FORMAT,
            datefmt=DATE_FORMAT,
        )

    def init_ui(self) -> None:
        # Load style sheet if available
        if self.style_path and self.style_path.exists():
            css = self.style_path.read_text()
            self.setStyleSheet(css)

        # Splitter for tree + detail pane
        splitter = QtWidgets.QSplitter()
        self.tree = QtWidgets.QTreeWidget()
        self.tree.setHeaderLabels([
            "Instance ID", "Install Path", "Version", "Display Name"
        ])
        self.tree.itemClicked.connect(self.on_item_selected)

        self.detail = QtWidgets.QTextEdit()
        self.detail.setReadOnly(True)

        splitter.addWidget(self.tree)
        splitter.addWidget(self.detail)
        splitter.setStretchFactor(1, 1)
        self.setCentralWidget(splitter)

        # Toolbar
        toolbar = self.addToolBar("main")
        refresh_icon = self.style().standardIcon(
            QtWidgets.QStyle.StandardPixmap.SP_BrowserReload
        )
        action = QtGui.QAction(refresh_icon, "Refresh", self)
        action.setToolTip("Reload data")
        action.triggered.connect(self.load_data)
        toolbar.addAction(action)

        # Status bar
        self.status = self.statusBar()

        # Overlay
        self.overlay = LoadingOverlay(self.tree)

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
        """)

    def init_worker_pool(self) -> None:
        self.thread_pool = QtCore.QThreadPool(self)

    def load_data(self) -> None:
        self.tree.clear()
        self.detail.clear()
        self.status.showMessage("Loading build tools info…")
        self.overlay.setVisible(True)

        worker = VsWhereWorker(vswhere_path=self.vswhere_path)
        worker.signals.result.connect(self.populate_tree)
        worker.signals.error.connect(self.show_error)
        worker.signals.finished.connect(lambda: self.overlay.setVisible(False))
        self.thread_pool.start(worker)

    @QtCore.pyqtSlot(list)
    def populate_tree(self, instances: List[Dict]) -> None:
        self.current_data = instances
        for inst in instances:
            root = QtWidgets.QTreeWidgetItem([
                inst.get("instanceId", ""),
                inst.get("installationPath", ""),
                inst.get("installationVersion", ""),
                inst.get("displayName", ""),
            ])
            root.setData(0, QtCore.Qt.ItemDataRole.UserRole, inst)
            for workload in inst.get("workloads", []):
                child = QtWidgets.QTreeWidgetItem(root, [f"⚙️ {workload.get('id', '')}"])
                child.setData(0, QtCore.Qt.ItemDataRole.UserRole, workload)
            for comp in inst.get("components", []):
                child = QtWidgets.QTreeWidgetItem(root, [f"🔧 {comp.get('id', '')}"])
                child.setData(0, QtCore.Qt.ItemDataRole.UserRole, comp)
            self.tree.addTopLevelItem(root)
        self.status.showMessage(f"Loaded {len(instances)} instances.", 5000)

    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
    def on_item_selected(self, item: QtWidgets.QTreeWidgetItem, col: int) -> None:
        data = item.data(0, QtCore.Qt.ItemDataRole.UserRole)
        if data:
            self.detail.setPlainText(json.dumps(data, indent=2))
        else:
            self.detail.clear()

    @QtCore.pyqtSlot(str)
    def show_error(self, message: str) -> None:
        logging.error(message)
        QtWidgets.QMessageBox.critical(self, "Error", message)
        self.status.showMessage("Error loading data", 5000)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.thread_pool.waitForDone(2000)
        super().closeEvent(event)


def main() -> None:
    args = parse_args()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(vswhere_path=args.vswhere, style_path=args.style)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()