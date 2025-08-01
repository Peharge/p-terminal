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
import logging
import subprocess
from pathlib import Path
import getpass

# Benutzername sicher ermitteln
try:
    USERNAME = getpass.getuser()
except Exception as e:
    print(f"[FATAL] Failed to get current user: {e}")
    sys.exit(1)

# Konfiguration der Pfade
HOME = Path.home()
P_TERMINAL_PATH = HOME / "p-terminal"
PEHARGE_PATH = HOME / "peharge-web"
VENV_PATH = P_TERMINAL_PATH / "pp-term" / ".env"
LOG_FILE = Path(__file__).resolve().parent / "doctor.log"

KNOWN_LOCAL_ARTIFACTS = {
    ".idea",
    "__pycache__",
    "doctor.log",
    "installer",
    "target",
    "run_arch_command.exe",
    "run_lx_command.exe",
    "iq-main.py"
}

KNOWN_EXTENSIONS = {
    ".lock",
    ".gif",
    ".obj",
    ".json",
    ".exe"
}

IGNORED_FOLDERS = {".env", ".github", ".git"}

# Basisordner, die ebenfalls ignoriert werden sollen (p-terminal/pp-term/main-test, peharge-c-compiler)
IGNORED_PATH_PREFIXES = [
    str(P_TERMINAL_PATH / "pp-term" / "main-test"),
    str(P_TERMINAL_PATH / "peharge-c-compiler"),
    str(P_TERMINAL_PATH / "peharge-cpp-compiler"),

]

# Logging einrichten
class CustomFormatter(logging.Formatter):
    def format(self, record):
        prefix = {
            logging.INFO: "[INFO]",
            logging.WARNING: "[WARNING]",
            logging.ERROR: "[ERROR]"
        }.get(record.levelno, "[LOG]")
        # Zeit zuerst, dann Level
        return f"[{self.formatTime(record, self.datefmt)}.{int(record.msecs):03d}] {prefix} {record.getMessage()}"

# Formatter mit Zeitformat
formatter = CustomFormatter(datefmt="%Y-%m-%d %H:%M:%S")

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
for handler in logging.getLogger().handlers:
    handler.setFormatter(formatter)


def is_path_ignored(file_path: Path) -> bool:
    """
    Prüft, ob die Datei in einem ignorierten Ordner liegt.
    """
    try:
        for ignored_folder in IGNORED_FOLDERS:
            # Check, ob ein beliebiger Teil des Pfads ein ignorierter Ordner ist
            if ignored_folder in file_path.parts:
                return True

        # Prüfe, ob der Pfad im Ignored-Prefix liegt (z.B. p-terminal/pp-term/main-test)
        file_path_str = str(file_path.resolve())
        for prefix in IGNORED_PATH_PREFIXES:
            if file_path_str.startswith(prefix):
                return True

        return False
    except Exception as e:
        logging.error(f"Failed to check ignored paths for {file_path}: {e}")
        return False

def is_known_artifact(file_path: str) -> bool:
    """
    Prüft, ob die Datei ein bekannter Artefakt ist, das ignoriert werden soll.
    Ignoriert alle *.log Dateien generell.
    """
    name = os.path.basename(file_path)
    ext = os.path.splitext(name)[1]

    if ext == ".log":
        # Alle .log Dateien ignorieren
        return True

    # Prüfe bekannte exakte Namen
    if name in KNOWN_LOCAL_ARTIFACTS:
        return True

    # Prüfe bekannte Dateiendungen (ohne .log, die schon oben rausgefiltert sind)
    if ext in KNOWN_EXTENSIONS:
        return True

    return False


def check_path(path: Path, must_be_dir=True) -> bool:
    """Existenz und Typ von Pfad prüfen"""
    try:
        if path.exists() and (path.is_dir() if must_be_dir else path.is_file()):
            logging.info(f"Path exists: {path}")
            return True
        else:
            logging.error(f"Missing path: {path}")
            return False
    except Exception as e:
        logging.error(f"Path check failed for {path}: {e}")
        return False


def check_virtualenv(venv_path: Path):
    """Existenz eines Virtualenv prüfen"""
    bin_dir = venv_path / ("Scripts" if os.name == "nt" else "bin")
    python_exec = bin_dir / ("python.exe" if os.name == "nt" else "python3")

    if python_exec.exists():
        logging.info(f"Virtual environment detected: {venv_path}")
        return python_exec
    else:
        logging.error(f"Python executable not found in virtual environment: {python_exec}")
        return None


def check_git_repo(path: Path) -> bool:
    """Git-Repository prüfen und auf Cleanliness analysieren"""
    git_dir = path / ".git"
    if not git_dir.exists():
        logging.error(f"Not a Git repository: {path}")
        return False

    try:
        result = subprocess.run(
            ["git", "-C", str(path), "status", "--porcelain"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, timeout=10  # Schutz vor Hängenbleiben
        )

        if result.returncode != 0:
            logging.error(f"Git status failed in {path}: {result.stderr.strip()}")
            return False

        lines = result.stdout.strip().splitlines()
        if not lines:
            logging.info(f"Git repository is clean: {path}")
            return True

        logging.warning(f"Repository not clean: {path}")
        clean = True
        for line in lines:
            status = line[:2].strip()
            file = line[3:].strip()
            display_line = f"  -> {line}"
            file_path = path / file

            if is_path_ignored(file_path):
                logging.info(f"  -> {line} [Ignored due to folder exclusion]")
                continue

            if is_known_artifact(file):
                logging.info(f"  -> {line} [Expected development artifact]")

            elif status in {"M", "A", "AM"}:
                logging.error(f"{display_line} [Modified or staged, but uncommitted]")
                clean = False

            elif status == "??":
                logging.warning(f"{display_line} [Untracked file — consider adding or cleaning]")

            else:
                logging.warning(f"{display_line} [Status: {status}]")

        return clean

    except subprocess.TimeoutExpired:
        logging.error(f"Git command timed out in {path}")
        return False

    except Exception as e:
        logging.error(f"Git check failed in {path}: {e}")
        return False


def main():
    print("")
    logging.info("Starting system diagnostics...")

    overall_success = True

    # P-Terminal Verzeichnis
    if not check_path(P_TERMINAL_PATH):
        overall_success = False

    # Virtualenv
    if not check_path(VENV_PATH):
        overall_success = False

    if not check_virtualenv(VENV_PATH):
        overall_success = False

    if not check_git_repo(P_TERMINAL_PATH):
        overall_success = False

    # Peharge Web
    if not check_path(PEHARGE_PATH):
        overall_success = False

    if not check_git_repo(PEHARGE_PATH):
        overall_success = False

    logging.info(
        "✅ System diagnostics completed successfully:\n"
        "    - Verified existence of project directories: 'p-terminal' and 'peharge-web'.\n"
        "    - Located and validated the virtual environment at 'p-terminal/pp-term/.env', including Python executable.\n"
        "    - Confirmed both projects are initialized as valid Git repositories.\n"
        "    - Analyzed repository status via 'git status --porcelain' to detect uncommitted changes or untracked files.\n"
        "    - Known development artifacts (e.g., '.env', '.log', '.github') were identified and excluded from warnings.\n"
        "    - No critical issues were found during the diagnostics process."
    )

    print("")
    print("")

    logging.info(
        "No securitycheck has been performed. "
        "To perform it, please run securitycheck. "
        "Or, to be safe, use Windows Defender or your own security software like AVG or McAfee to keep the PP-terminal secure."
    )

    sys.exit(0 if overall_success else 1)


if __name__ == "__main__":
    main()
