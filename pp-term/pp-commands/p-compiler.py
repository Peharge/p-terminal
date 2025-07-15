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

import subprocess
import sys
import getpass
import os
from datetime import datetime

def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def activate_virtualenv(venv_path):
    """Aktiviert eine bestehende virtuelle Umgebung."""
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path, "bin", "activate")

    # Überprüfen, ob die virtuelle Umgebung existiert
    if not os.path.exists(activate_script):
        print(f"[{timestamp()}] [ERROR] The virtual environment could not be found at {venv_path}.")
        sys.exit(1)

    # Umgebungsvariable für die virtuelle Umgebung setzen
    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"[{timestamp()}] [INFO] Virtual environment {venv_path} enabled.")


# Pfad zur bestehenden virtuellen Umgebung
venv_path = rf"C:\Users\{os.getlogin()}\p-terminal\pp-term\.env"

# Aktivieren der virtuellen Umgebung
activate_virtualenv(venv_path)

sys.stdout.reconfigure(encoding='utf-8')
user_name = getpass.getuser()

import shutil
import csv
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QLabel, QPushButton, QHeaderView,
    QHBoxLayout, QLineEdit, QMenu
)
from PyQt6.QtGui import QColor, QIcon, QAction
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QPoint


def run_command(command):
    try:
        return subprocess.check_output(
            command, shell=True, universal_newlines=True, stderr=subprocess.STDOUT
        ).strip()
    except Exception:
        return None


def find_all_compilers():
    tools = [
        {"name": "GCC", "cmd": "gcc --version", "lang": "C/C++"},
        {"name": "G++", "cmd": "g++ --version", "lang": "C++"},
        {"name": "Clang", "cmd": "clang --version", "lang": "C/C++"},
        {"name": "Clang++", "cmd": "clang++ --version", "lang": "C++"},
        {"name": "MSVC", "cmd": "cl", "lang": "C/C++"},
        {"name": "MinGW", "cmd": "x86_64-w64-mingw32-gcc --version", "lang": "C/C++"},
        {"name": "TinyCC", "cmd": "tcc -v", "lang": "C"},
        {"name": "Intel C++ (ICX)", "cmd": "icx --version", "lang": "C/C++"},
        {"name": "FPC (Free Pascal)", "cmd": "fpc -iV", "lang": "Pascal"},
        {"name": "GFortran", "cmd": "gfortran --version", "lang": "Fortran"},
        {"name": "NASM", "cmd": "nasm -v", "lang": "Assembly"},
        {"name": "YASM", "cmd": "yasm --version", "lang": "Assembly"},
        {"name": "Java", "cmd": "java -version", "lang": "Java"},
        {"name": "Javac", "cmd": "javac -version", "lang": "Java"},
        {"name": "Kotlin", "cmd": "kotlinc -version", "lang": "Kotlin"},
        {"name": "Scala", "cmd": "scalac -version", "lang": "Scala"},
        {"name": "Groovy", "cmd": "groovyc --version", "lang": "Groovy"},
        {"name": "Python", "cmd": "where python", "lang": "Python"},
        {"name": "Ruby", "cmd": "ruby -v", "lang": "Ruby"},
        {"name": "Perl", "cmd": "perl -v", "lang": "Perl"},
        {"name": "PHP", "cmd": "php -v", "lang": "PHP"},
        {"name": "Lua", "cmd": "lua -v", "lang": "Lua"},
        {"name": "R", "cmd": "R --version", "lang": "R"},
        {"name": "Julia", "cmd": "julia --version", "lang": "Julia"},
        {"name": "Bash", "cmd": "bash --version", "lang": "Shell"},
        {"name": "Rust", "cmd": "rustc --version", "lang": "Rust"},
        {"name": "Cargo", "cmd": "cargo --version", "lang": "Rust Build System"},
        {"name": "Go", "cmd": "go version", "lang": "Go"},
        {"name": "Nim", "cmd": "nim --version", "lang": "Nim"},
        {"name": "Haskell (GHC)", "cmd": "ghc --version", "lang": "Haskell"},
        {"name": "OCaml", "cmd": "ocamlc -version", "lang": "OCaml"},
        {"name": "Node.js", "cmd": "node -v", "lang": "JavaScript"},
        {"name": "Deno", "cmd": "deno --version", "lang": "TypeScript/JS"},
        {"name": "TypeScript", "cmd": "tsc -v", "lang": "TypeScript"},
        {"name": ".NET SDK", "cmd": "dotnet --list-sdks", "lang": ".NET"},
        {"name": "C# Compiler (csc)", "cmd": "csc -version", "lang": "C#"}
    ]

    results = []

    for tool in tools:
        if "python" in tool["name"].lower():
            paths = run_command(tool["cmd"])
            if paths:
                for line in paths.splitlines():
                    version = run_command(f'"{line.strip()}" --version')
                    results.append({
                        "Name": "Python",
                        "Version": version.replace("Python ", "") if version else "?",
                        "Info": line.strip(),
                        "Languages": tool["lang"]
                    })
        elif "MSVC" in tool["name"]:
            continue
        else:
            output = run_command(tool["cmd"])
            if output:
                version_line = output.splitlines()[0]
                exe_path = shutil.which(tool["cmd"].split()[0])
                results.append({
                    "Name": tool["name"],
                    "Version": version_line,
                    "Info": exe_path or "Found",
                    "Languages": tool.get("lang", "Unknown")
                })

    cl_path = shutil.which("cl.exe")
    if cl_path:
        version = run_command("cl")
        if version:
            results.append({
                "Name": "MSVC",
                "Version": version.splitlines()[0],
                "Info": cl_path,
                "Languages": "C/C++"
            })

    return results


class ScanThread(QThread):
    results_ready = pyqtSignal(list)

    def run(self):
        results = find_all_compilers()
        self.results_ready.emit(results)


class CompilerInspector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P-Term System Compiler Inspector")
        self.resize(1000, 600)
        self.setStyleSheet(self.load_stylesheet())
        self.init_ui()
        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/p-terminal/pp-term/icons/p-term-logo-5.ico"
        self.setWindowIcon(QIcon(icon_path))

    def init_ui(self):
        layout = QVBoxLayout()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search by name or language...")
        self.search_bar.textChanged.connect(self.filter_table)
        layout.addWidget(self.search_bar)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Version", "Location / Info", "Languages"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.open_context_menu)
        layout.addWidget(self.table)

        button_layout = QHBoxLayout()
        self.refresh_button = QPushButton("🔄 Refresh")
        self.refresh_button.clicked.connect(self.scan_compilers)
        export_csv_btn = QPushButton("📁 Export CSV")
        export_csv_btn.clicked.connect(lambda: self.export_results("csv"))
        export_json_btn = QPushButton("🧾 Export JSON")
        export_json_btn.clicked.connect(lambda: self.export_results("json"))

        button_layout.addStretch()
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(export_csv_btn)
        button_layout.addWidget(export_json_btn)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.scan_compilers()

    def scan_compilers(self):
        self.refresh_button.setEnabled(False)
        self.refresh_button.setText("🔍 Scanning...")
        self.thread = ScanThread()
        self.thread.results_ready.connect(self.display_results)
        self.thread.start()

    def display_results(self, results):
        self.table.setRowCount(0)
        for row, entry in enumerate(results):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(entry["Name"]))
            self.table.setItem(row, 1, QTableWidgetItem(entry["Version"]))
            self.table.setItem(row, 2, QTableWidgetItem(entry["Info"]))
            self.table.setItem(row, 3, QTableWidgetItem(entry["Languages"]))
        self.refresh_button.setEnabled(True)
        self.refresh_button.setText("🔄 Refresh")

    def filter_table(self, text):
        for row in range(self.table.rowCount()):
            match = any(text.lower() in self.table.item(row, col).text().lower() for col in [0, 3])
            self.table.setRowHidden(row, not match)

    def open_context_menu(self, pos: QPoint):
        item = self.table.itemAt(pos)
        if item:
            menu = QMenu(self)
            copy_action = QAction("📋 Copy Cell")
            copy_action.triggered.connect(lambda: QApplication.clipboard().setText(item.text()))
            menu.addAction(copy_action)
            menu.exec(self.table.mapToGlobal(pos))

    def export_results(self, fmt="csv"):
        results = []
        for row in range(self.table.rowCount()):
            entry = {
                "Name": self.table.item(row, 0).text(),
                "Version": self.table.item(row, 1).text(),
                "Info": self.table.item(row, 2).text(),
                "Languages": self.table.item(row, 3).text()
            }
            results.append(entry)

        path = f"compilers_export.{fmt}"
        with open(path, "w", encoding="utf-8", newline='') as f:
            if fmt == "csv":
                writer = csv.DictWriter(f, fieldnames=results[0].keys())
                writer.writeheader()
                writer.writerows(results)
            elif fmt == "json":
                json.dump(results, f, indent=2)

    def load_stylesheet(self):
        return """
        QWidget {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
            color: #FFFFFF;
            font-family: 'Roboto', sans-serif;
            font-size: 14px;
        }

        QLineEdit, QPushButton {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
            border: 1px solid #778899;
            border-radius: 5px;
            padding: 5px;
            color: #FFFFFF;
        }

        QPushButton:hover {
            background-color: #1c2833;
        }

        QTableWidget {
            background-color: transparent;
            border: 1px solid #778899;
            border-radius: 8px;
            gridline-color: #778899;
        }

        QTableWidget::item:selected {
            background-color: #34495e;
            color: #FFFFFF;
        }

        QHeaderView::section {
            background-color: transparent;
            padding: 8px;
            border: none;
            color: #FFFFFF;
        }

        QLabel {
            background: transparent;
            font-size: 16px;
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CompilerInspector()
    window.show()
    sys.exit(app.exec())
