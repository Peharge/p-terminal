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
import getpass
import subprocess
import threading
import time
import importlib.util
import os
from dotenv import load_dotenv
from subprocess import run
from datetime import datetime

def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


required_packages = ["matplotlib", "GitPython"]

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

def ensure_packages_installed(packages):
    """Stellt sicher, dass alle erforderlichen Pakete installiert sind."""
    for package in packages:
        if importlib.util.find_spec(package) is None:
            print(f"Installing {package}...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True, stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
                print(f"[{timestamp()}] [INFO] {package} installed successfully.")
            except subprocess.CalledProcessError:
                print(f"[{timestamp()}] [INFO] Failed to install {package}. Please install it manually.")
        else:
            print(f"[{timestamp()}] [INFO] {package} is already installed.")


# Pfad zur bestehenden virtuellen Umgebung
venv_path = rf"C:\Users\{os.getlogin()}\p-terminal\pp-term\.env"

# Aktivieren der virtuellen Umgebung
activate_virtualenv(venv_path)

# Sicherstellen, dass alle erforderlichen Pakete installiert sind
ensure_packages_installed(required_packages)

sys.stdout.reconfigure(encoding='utf-8')
user_name = getpass.getuser()

from collections import Counter
from datetime import datetime, timedelta
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIcon, QPalette, QTextCharFormat, QSyntaxHighlighter
from PyQt6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTreeWidgetItem,
                             QTreeWidget, QVBoxLayout, QWidget, QHeaderView,
                             QLineEdit, QPushButton, QHBoxLayout, QTextEdit, QTabWidget, QMainWindow, QSplitter)

# Matplotlib-Integration in PyQt6
from matplotlib.figure import Figure
try:
    from matplotlib.backends.backend_qt6agg import FigureCanvasQTAgg as FigureCanvas
except ImportError:
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QToolTip
from PyQt6.QtGui import QPen, QBrush, QColor, QPainter, QFont, QPainterPath
from PyQt6.QtCore import Qt, QPointF
from git import Repo, InvalidGitRepositoryError
import random

def get_git_commits(repo_path):
    """
    Reads local Git commits and returns a list of tuples:
    (full_hash, short_hash, message, author, date, color)

    - Date is in the format YYYY-MM-DD (ISO)
    - '|' is used as the delimiter to ensure proper parsing even with spaces in the commit message
    """
    try:
        # Change directory to the repository path
        os.chdir(repo_path)

        # Fetch local commits (date in ISO format)
        local_commits = subprocess.check_output(
            ["git", "log", "--date=short", "--pretty=format:%H|%h|%s|%an|%ad"],
            text=True,
            encoding="utf-8",  # Explicit encoding for robustness
            errors="replace"   # Replace undecodable characters
        ).strip().split("\n")

        # Determine the main branch (origin/main or origin/master)
        branches_output = subprocess.check_output(
            ["git", "ls-remote", "--heads", "origin"],
            text=True,
            encoding="utf-8",
            errors="replace"
        ).strip().split("\n")

        # Identify the main branch
        main_branch = None
        for branch in branches_output:
            if "refs/heads/main" in branch:
                main_branch = "origin/main"
                break
            elif "refs/heads/master" in branch:
                main_branch = "origin/master"
                break

        if not main_branch:
            return []  # No main branch found

        # Fetch remote commits (only their hashes)
        remote_commits_output = subprocess.check_output(
            ["git", "log", main_branch, "--pretty=format:%H"],
            text=True,
            encoding="utf-8",
            errors="replace"
        ).strip().split("\n")
        remote_hashes = set(remote_commits_output)

        # Process local commits and determine their color
        commits = []
        for commit in local_commits:
            if commit:
                parts = commit.split("|")
                if len(parts) != 5:
                    continue  # Skip malformed entries
                full_hash, short_hash, message, author, date = parts
                color = "red" if full_hash not in remote_hashes else "green"
                commits.append((full_hash, short_hash, message, author, date, color))

        return commits

    except subprocess.CalledProcessError as e:
        print(f"Error executing Git command: {e}")
        return []
    except FileNotFoundError as e:
        print(f"Git is not installed or not found in PATH: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

class DiffHighlighter(QSyntaxHighlighter):
    """
    Hebt Zeilen im Diff hervor, die mit '+' (Hinzufügungen) oder '-' (Löschungen) beginnen.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.format_addition = QTextCharFormat()
        self.format_addition.setBackground(QColor(0, 255, 0, 100))  # Grüner Hintergrund

        self.format_deletion = QTextCharFormat()
        self.format_deletion.setBackground(QColor(255, 0, 0, 100))  # Roter Hintergrund

    def highlightBlock(self, text):
        if text.startswith('+'):
            self.setFormat(0, len(text), self.format_addition)
        elif text.startswith('-'):
            self.setFormat(0, len(text), self.format_deletion)

def get_commit_diff(repo_path, commit_hash):
    """
    Gibt den Diff eines bestimmten Commits zurück.
    """
    try:
        result = subprocess.run(["git", "show", commit_hash],
                                cwd=repo_path,
                                text=True,
                                encoding='utf-8',
                                capture_output=True,
                                check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Failed to retrieve diff. Error: {e.stderr}"

class ExplorerTab(QWidget):
    """
    Enthält den Commit Explorer inklusive Suchleiste, Commit-Liste und Diff-Vorschau.
    """
    def __init__(self, repo_path):
        super().__init__()
        self.repo_path = repo_path
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Suchleiste
        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search commits...")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_commits)
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(search_button)
        layout.addLayout(search_layout)

        # Splitter für die Trennung der Commits und Diff-Vorschau
        splitter = QSplitter(Qt.Orientation.Vertical)

        # Baumansicht der Commits
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Commit Hash", "Message", "Author", "Date", "Status"])
        self.tree.header().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tree.itemClicked.connect(self.display_commit_diff)

        # Diff-Vorschau
        self.diff_text = QTextEdit()
        self.diff_text.setReadOnly(True)
        self.highlighter = DiffHighlighter(self.diff_text.document())

        # Füge die Widgets zum Splitter hinzu
        splitter.addWidget(self.tree)
        splitter.addWidget(self.diff_text)

        # Füge den Splitter zum Layout hinzu
        layout.addWidget(splitter)

        # Status-Label
        self.status_label = QLabel("Loading...")
        layout.addWidget(self.status_label)

        self.setLayout(layout)
        self.load_commits()

    def load_commits(self):
        self.tree.clear()
        commits = get_git_commits(self.repo_path)
        for full_hash, short_hash, message, author, date, color in commits:
            status = "Not Pulled" if color == "red" else "Pulled"
            item = QTreeWidgetItem([short_hash, message, author, date, status])
            # Speichere den vollständigen Commit-Hash als zusätzlichen Datenwert
            item.setData(0, Qt.ItemDataRole.UserRole, full_hash)
            item.setForeground(4, QColor(color))
            self.tree.addTopLevelItem(item)

        self.status_label.setText("Commits loaded successfully.")

    def search_commits(self):
        search_text = self.search_bar.text().lower()
        for i in range(self.tree.topLevelItemCount()):
            item = self.tree.topLevelItem(i)
            is_visible = (search_text in item.text(1).lower() or
                          search_text in item.text(2).lower() or
                          search_text in item.text(3).lower())
            item.setHidden(not is_visible)

    def display_commit_diff(self, item, column):
        commit_hash = item.data(0, Qt.ItemDataRole.UserRole)
        diff = get_commit_diff(self.repo_path, commit_hash)
        self.diff_text.setPlainText(diff)

class StatisticsTab(QWidget):
    """
    Zeigt in einem Matplotlib-Diagramm (2D-Liniendiagramm mit verbundenen Punkten)
    die Anzahl der Commits der letzten 30 Tage an.
    """
    def __init__(self, repo_path):
        super().__init__()
        self.repo_path = repo_path
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.ax = self.canvas.figure.subplots()
        # Setze den Hintergrund des Diagramms auf den gewünschten Farbverlauf
        self.ax.set_facecolor("none")
        self.canvas.figure.patch.set_facecolor("none")
        self.plot_statistics()

    def plot_statistics(self):
        commits = get_git_commits(self.repo_path)
        # Filter: nur Commits der letzten 30 Tage
        cutoff_date = datetime.today() - timedelta(days=35)
        filtered_commits = []
        for commit in commits:
            try:
                commit_date = datetime.strptime(commit[4], "%Y-%m-%d")
            except ValueError:
                continue
            if commit_date >= cutoff_date:
                filtered_commits.append(commit)

        # Zähle die Commits pro Tag
        date_counts = Counter(commit[4] for commit in filtered_commits)
        # Sortiere die Daten chronologisch
        dates = sorted(date_counts.keys())
        counts = [date_counts[date] for date in dates]

        # Clear existing plot and set transparent background for the plotting area
        self.ax.clear()
        self.ax.set_facecolor("none")

        # Enable grid lines with white color, dashed style, and a thinner line width
        self.ax.grid(True, color='white', linestyle='--', linewidth=0.5)

        # Set axis spines (the x and y axis lines) to white
        for spine in self.ax.spines.values():
            spine.set_color('white')

        # Create a line plot (connected points) with a skyblue color
        self.ax.plot(dates, counts, marker='o', linestyle='-', color='skyblue', linewidth=2)

        # Set axis labels and title with white text
        self.ax.set_xlabel("Date", color='white')
        self.ax.set_ylabel("Number of commits", color='white')
        self.ax.set_title("Commits per day (last 30 days)", color='white')

        # Configure tick parameters: set tick colors to white and rotate x-axis labels for clarity
        self.ax.tick_params(axis='x', colors='white', rotation=45)
        self.ax.tick_params(axis='y', colors='white')

        # Enforce tick label colors (useful for some Matplotlib versions/themes)
        for label in self.ax.get_xticklabels():
            label.set_color('white')
        for label in self.ax.get_yticklabels():
            label.set_color('white')

        # Redraw the canvas to reflect updates
        self.canvas.draw()

class TreeTab(QWidget):
    NODE_RADIUS = 6
    X_SPACING = 200  # Increased spacing for better readability
    Y_SPACING = 100  # Increased spacing to avoid text overlapping
    MARGIN = 50  # Margin around the tree

    def __init__(self, repo_path):
        super().__init__()
        self.repo_path = repo_path
        self.branch_colors = {}  # Store assigned colors for branches
        self._init_ui()
        self._draw_graph()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        self.view = QGraphicsView()
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        self.scene = QGraphicsScene(self.view)
        self.view.setScene(self.scene)
        layout.addWidget(self.view)

    def _draw_graph(self):
        try:
            repo = Repo(self.repo_path, search_parent_directories=True)
        except InvalidGitRepositoryError:
            text_item = self.scene.addText(
                f"No valid Git repository found:\nPath: {self.repo_path}",
                QFont("Arial", 12, QFont.Weight.Bold)
            )
            text_item.setDefaultTextColor(QColor('#ffffff'))
            return

        # Get all commits and organize them by branch
        commits = list(repo.iter_commits('--all', topo_order=True))
        branch_map = self._map_branches_to_commits(repo)

        # Assign colors to branches
        self._assign_branch_colors(branch_map)

        # Set scene size dynamically
        width = len(branch_map) * self.X_SPACING + self.MARGIN * 2
        height = len(commits) * self.Y_SPACING + self.MARGIN * 2
        self.scene.setSceneRect(0, 0, width, height)

        # Draw the tree structure
        self._draw_tree(commits, branch_map)

    def _map_branches_to_commits(self, repo):
        """
        Maps each commit to the branches it belongs to.
        """
        branch_map = {}
        for branch in repo.branches:
            for commit in repo.iter_commits(branch.name):
                branch_map.setdefault(commit.hexsha, set()).add(branch.name)
        return branch_map

    def _assign_branch_colors(self, branch_map):
        """
        Assigns a unique color to each branch.
        """
        for branch_name in set(branch for branches in branch_map.values() for branch in branches):
            self.branch_colors[branch_name] = QColor(
                random.randint(50, 200),
                random.randint(50, 200),
                random.randint(50, 200)
            )

    def _draw_tree(self, commits, branch_map):
        """
        Draws the tree structure with commits and their branches.
        """
        pen_node = QPen(QColor('#225e7a'))
        font_info = QFont("Arial", 8)

        # Separate main branches (left) and others (right)
        main_branches = {"main", "master"}
        branch_positions = {"main": 0, "master": 0}  # Leftmost column for main branches
        other_branch_offset = 1  # Start other branches from column 1

        for idx, commit in enumerate(commits):
            branch_names = branch_map.get(commit.hexsha, [])
            is_main = any(branch in main_branches for branch in branch_names)
            branch_key = ",".join(sorted(branch_names)) if branch_names else "untracked"

            # Assign horizontal position
            if branch_key not in branch_positions:
                branch_positions[branch_key] = other_branch_offset
                other_branch_offset += 1

            # Calculate node position
            x = branch_positions[branch_key] * self.X_SPACING + self.MARGIN
            y = idx * self.Y_SPACING + self.MARGIN
            pt = QPointF(x, y)

            # Draw node circle
            brush_node = QBrush(self.branch_colors.get(branch_key, QColor('#3daee9')))
            self.scene.addEllipse(
                pt.x() - self.NODE_RADIUS,
                pt.y() - self.NODE_RADIUS,
                self.NODE_RADIUS * 2,
                self.NODE_RADIUS * 2,
                pen_node,
                brush_node
            )

            # Add commit and branch info (shortened format)
            branch_info = f" | {', '.join(sorted(branch_names))}" if branch_names else ""
            info = (
                f"{commit.hexsha[:7]} | {commit.author.name} | "
                f"{commit.committed_datetime.strftime('%Y-%m-%d')}{branch_info} | "
                f"{commit.message.strip()[:50]}..."  # Shorten commit message
            )
            text_item = self.scene.addText(info, font_info)
            text_item.setDefaultTextColor(QColor('#ffffff'))
            text_item.setTextWidth(300)
            text_item.setPos(
                pt.x() + self.NODE_RADIUS + 5,
                pt.y() - self.NODE_RADIUS
            )
            # Add tooltip with full info
            tooltip_info = (
                f"{commit.hexsha}\nAuthor: {commit.author.name}\nDate: "
                f"{commit.committed_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Branches: {', '.join(sorted(branch_names)) if branch_names else 'None'}\n"
                f"Message: {commit.message.strip()}"
            )
            text_item.setToolTip(tooltip_info)

            # Draw edges to parents using curved paths
            for parent in commit.parents:
                parent_idx = next((i for i, c in enumerate(commits) if c.hexsha == parent.hexsha), None)
                if parent_idx is not None:
                    parent_x = branch_positions[branch_key] * self.X_SPACING + self.MARGIN
                    parent_y = parent_idx * self.Y_SPACING + self.MARGIN
                    self._draw_curved_line(pt, QPointF(parent_x, parent_y), branch_key)

    def _draw_curved_line(self, start, end, branch_key):
        """
        Draws a curved line between two points to connect commits.
        """
        path = QPainterPath()
        path.moveTo(start)
        control_point = QPointF((start.x() + end.x()) / 2, (start.y() + end.y()) / 2 - 50)
        path.quadTo(control_point, end)
        pen = QPen(self.branch_colors.get(branch_key, QColor('#666666')))
        pen.setWidth(2)
        self.scene.addPath(path, pen)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P-Term Commit Explorer MAVIS-Web")
        self.setGeometry(100, 100, 1200, 900)
        self.set_dark_mode()

        # Annahme: Das Repository befindet sich im p-terminal-Ordner des aktuellen Benutzers
        user = os.getenv("USERNAME") or os.getenv("USER")
        self.repo_path = f"C:/Users/{user}/PycharmProjects/MAVIS-web"
        icon_path = f"C:/Users/{user}/p-terminal/pp-term/icons/p-term-logo-5.ico"
        self.setWindowIcon(QIcon(icon_path))

        self.init_ui()

    def init_ui(self):
        # Erstelle ein Tab-Widget, um zwischen Explorer- und Statistik-Modus zu wechseln
        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        # Tab für Commit Explorer
        explorer_tab = ExplorerTab(self.repo_path)
        tabs.addTab(explorer_tab, "Commit Explorer")

        # Tab für Commit Statistik (nur die letzten 30 Tage)
        stats_tab = StatisticsTab(self.repo_path)
        tabs.addTab(stats_tab, "Commit Statistik")

        # Tab für Commit Tree
        stats_tab = TreeTab(self.repo_path)
        tabs.addTab(stats_tab, "Commit Tree")

        # Style für Hintergrund (globaler Verlauf)
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

    def set_dark_mode(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(46, 46, 46))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
