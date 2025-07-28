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

from datetime import datetime

def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

print("""
WARNING: It is recommended to install GitHub Desktop from the official website:
https://desktop.github.com/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of GitHub Desktop? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für GitHub Desktop folgen
print(f"[{timestamp()}] [INFO] Proceeding with GitHub Desktop installation...")

import sys
import os
import shutil
import subprocess
import logging
import tempfile
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# Configure logging
log_path = Path(__file__).parent / "installer.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_path, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# GitHub Desktop release URL (latest stable)
GHD_URL = "https://central.github.com/deployments/desktop/desktop/latest/win32"

def is_github_desktop_installed() -> bool:
    """Checks whether GitHub Desktop is installed via registry or PATH."""
    # GitHub Desktop installs GitHubDesktop.exe in the Program Files directory
    prog_path = Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "GitHub Desktop" / "GitHubDesktop.exe"
    return prog_path.exists() or shutil.which("GitHubDesktop.exe") is not None

def download_installer(dest_path: Path) -> None:
    """Downloads the GitHub Desktop Windows installer."""
    logging.info(f"Starting download of GitHub Desktop installer from {GHD_URL}")
    try:
        req = Request(GHD_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as response, open(dest_path, "wb") as out_file:
            total = int(response.getheader('Content-Length', 0))
            downloaded = 0
            chunk_size = 8192
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
                downloaded += len(chunk)
                if total:
                    percent = downloaded * 100 / total
                    logging.info(f"Download progress: {percent:.1f}%")
        logging.info(f"Download complete: {dest_path}")
    except (HTTPError, URLError) as e:
        logging.error(f"Download error: {e}")
        sys.exit(1)

def run_installer(installer_path: Path) -> None:
    """Runs the GitHub Desktop installer in silent mode."""
    logging.info(f"Launching GitHub Desktop installer: {installer_path}")
    # Squirrel-based installer supports '--silent' flag
    cmd = [str(installer_path), "--silent"]
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info("GitHub Desktop installed successfully.")
        logging.debug(f"Installer output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation failed (exit code {e.returncode}): {e.stderr}")
        sys.exit(e.returncode)

def ensure_installed():
    """Final check to confirm GitHub Desktop is available."""
    if is_github_desktop_installed():
        logging.info("GitHub Desktop is now available.")
    else:
        logging.warning("GitHub Desktop not found. Please check PATH or installation.")

def main():
    logging.info("=== GitHub Desktop Installer started ===")
    if is_github_desktop_installed():
        logging.info("GitHub Desktop is already installed. Exiting.")
        return

    with tempfile.TemporaryDirectory() as tmpdir:
        installer_file = Path(tmpdir) / "GitHubDesktopSetup.exe"
        download_installer(installer_file)
        run_installer(installer_file)

    ensure_installed()
    logging.info("=== Process completed ===")

if __name__ == "__main__":
    if os.name != "nt":
        logging.error("This script only runs on Windows.")
        sys.exit(1)
    main()
