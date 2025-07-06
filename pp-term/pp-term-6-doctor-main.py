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

USERNAME = os.getlogin()
P_TERMINAL_PATH = Path.home() / "p-terminal"
PEHARGE_PATH = Path("C:/Users/julian/peharge-web")
VENV_PATH = P_TERMINAL_PATH / "pp-term" / ".env"
LOG_FILE = Path(__file__).parent / "doctor.log"

# Files/folders that are known to appear during development and shouldn't trigger errors
KNOWN_LOCAL_ARTIFACTS = [
    ".idea", "__pycache__", ".log", ".lock", ".gif", ".obj", "target",
    "installer", "doctor.log", "current_env.json", ".github", "run_arch_command.exe",
    "run_lx_command.exe"
]

# Logging setup
class CustomFormatter(logging.Formatter):
    def format(self, record):
        prefix = "[INFO]" if record.levelno == logging.INFO else "[WARNING]" if record.levelno == logging.WARNING else "[ERROR]"
        return f"{prefix} {super().format(record)}"

formatter = CustomFormatter(fmt="[%(asctime)s.%(msecs)03d] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
for handler in logging.getLogger().handlers:
    handler.setFormatter(formatter)

def is_known_artifact(file_path: str) -> bool:
    return any(part in file_path or file_path.endswith(ext) for part in KNOWN_LOCAL_ARTIFACTS for ext in [part, f"/{part}", f"\\{part}"])

def check_path(path: Path, must_be_dir=True):
    if path.exists() and (path.is_dir() if must_be_dir else path.is_file()):
        logging.info(f"Path exists: {path}")
        return True
    else:
        logging.error(f"Missing path: {path}")
        return False

def check_virtualenv(venv_path: Path):
    bin_path = venv_path / ("Scripts" if os.name == "nt" else "bin")
    python_exe = bin_path / ("python.exe" if os.name == "nt" else "python3")
    if not python_exe.exists():
        logging.error(f"Python executable not found in virtual environment: {python_exe}")
        return None
    logging.info(f"Virtual environment detected: {venv_path}")
    return python_exe

def check_git_repo(path: Path):
    git_dir = path / ".git"
    if not git_dir.exists():
        logging.error(f"Not a Git repository: {path}")
        return False

    try:
        result = subprocess.run(["git", "-C", str(path), "status", "--porcelain"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            logging.error(f"Git status failed in: {path}")
            return False

        lines = result.stdout.strip().splitlines()
        if not lines:
            logging.info(f"Git repository is clean: {path}")
            return True

        logging.warning(f"Repository not clean: {path}")
        for line in lines:
            status, file = line[:2].strip(), line[3:].strip()
            clean_line = f"  -> {line}"

            if is_known_artifact(file):
                logging.info(f"{clean_line} [Expected in local development]")
            elif status in {"M", "A", "AM"}:
                logging.error(f"{clean_line} [Modified or staged, but uncommitted]")
            elif status == "??":
                logging.warning(f"{clean_line} [Untracked file — consider adding or cleaning]")
            else:
                logging.warning(f"{clean_line} [Status: {status}]")

        return False

    except Exception as e:
        logging.error(f"Git check failed in {path}: {e}")
        return False

def main():
    logging.info("Starting system diagnostics...")

    check_path(P_TERMINAL_PATH)
    check_path(VENV_PATH)
    check_virtualenv(VENV_PATH)

    check_git_repo(P_TERMINAL_PATH)
    check_path(PEHARGE_PATH)
    check_git_repo(PEHARGE_PATH)

    logging.info("System diagnostics completed.")

if __name__ == "__main__":
    main()
