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
WARNING: It is recommended to install PHP from the official website:
https://www.php.net/downloads.php

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of PHP? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für PHP folgen
print(f"[{timestamp()}] [INFO] Proceeding with PHP installation...")

import os
import sys
import shutil
import subprocess
import logging
import tempfile
import zipfile
import re
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# --- Configure logging ---
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

# --- Constants ---
PHP_INSTALL_DIR = Path("C:/Program Files/PHP")
PHP_BIN_DIR     = PHP_INSTALL_DIR
DOWNLOAD_PAGE   = "https://windows.php.net/download"
BASE_URL        = "https://windows.php.net/downloads/releases/"

def is_php_installed() -> bool:
    """Checks if 'php' is already callable from PATH."""
    return shutil.which("php") is not None

def get_latest_php_release() -> dict:
    """
    Parses the PHP download page and retrieves the latest
    x64 Thread-Safe CLI archive.
    """
    logging.info("Fetching latest PHP version from %s", DOWNLOAD_PAGE)
    try:
        req = Request(DOWNLOAD_PAGE, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp:
            html = resp.read().decode("utf-8")
    except (HTTPError, URLError) as e:
        logging.error("Error fetching download page: %s", e)
        sys.exit(1)

    # Search for e.g. php-8.3.3-Win32-vs16-x64.zip (Thread Safe)
    pattern = re.compile(r'href="([^"]*php-([\d\.]+)-Win32-vs16-x64\.zip)"')
    match = pattern.search(html)
    if not match:
        logging.error("Could not find a matching PHP release ZIP.")
        sys.exit(1)

    filename = match.group(1)
    version  = match.group(2)
    url       = filename if filename.startswith("http") else BASE_URL + filename
    logging.info("Found version: %s (%s)", version, url)
    return {"version": version, "filename": filename, "url": url}

def download_php(dest: Path, url: str):
    """Downloads the ZIP archive from url to dest."""
    logging.info("Starting download: %s", url)
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp, open(dest, "wb") as out:
            total = int(resp.getheader("Content-Length", 0))
            downloaded = 0
            chunk_size = 8192
            while True:
                chunk = resp.read(chunk_size)
                if not chunk:
                    break
                out.write(chunk)
                downloaded += len(chunk)
                if total:
                    pct = downloaded * 100 / total
                    logging.info("Download progress: %.1f%%", pct)
        logging.info("Download completed: %s", dest)
    except (HTTPError, URLError) as e:
        logging.error("Download error: %s", e)
        sys.exit(1)

def extract_php(zip_path: Path):
    """
    Extracts the ZIP archive to PHP_INSTALL_DIR
    and deletes old installation if necessary.
    """
    if PHP_INSTALL_DIR.exists():
        logging.info("Old PHP installation found, deleting it...")
        shutil.rmtree(PHP_INSTALL_DIR)
    logging.info("Extracting %s to %s", zip_path, PHP_INSTALL_DIR)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(PHP_INSTALL_DIR)
    logging.info("Extraction completed.")

def update_path():
    """
    Adds PHP_INSTALL_DIR to the system PATH (for new terminals).
    """
    php_dir = str(PHP_BIN_DIR)
    current = os.environ.get("PATH", "")
    if php_dir.lower() in current.lower():
        logging.info("PHP is already in PATH.")
        return
    new_path = f"{current};{php_dir}"
    logging.info("Adding PHP to PATH: %s", php_dir)
    # setx writes the new PATH to the registry
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation():
    """Verifies the installation via 'php --version'."""
    try:
        result = subprocess.run(["php", "--version"], capture_output=True, text=True, check=True)
        logging.info("PHP successfully installed: %s", result.stdout.splitlines()[0])
    except subprocess.CalledProcessError as e:
        logging.error("Error verifying PHP: %s", e)
        sys.exit(1)

def main():
    logging.info("=== PHP Installer started ===")
    if os.name != "nt":
        logging.error("This script only runs on Windows.")
        sys.exit(1)

    if is_php_installed():
        logging.info("PHP is already installed. Aborting.")
        return

    # Temporary directory for download
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "php.zip"
        info = get_latest_php_release()
        download_php(tmp, info["url"])
        extract_php(tmp)

    update_path()
    verify_installation()
    logging.info("=== PHP installation completed ===")

if __name__ == "__main__":
    main()
