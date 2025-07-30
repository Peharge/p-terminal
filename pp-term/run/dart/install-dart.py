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
WARNING: It is recommended to install Dart from the official website:
https://dart.dev/get-dart

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Dart? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Dart folgen
print(f"[{timestamp()}] [INFO] Proceeding with Dart installation...")

import os
import sys
import shutil
import subprocess
import logging
import tempfile
import zipfile
import json
from pathlib import Path
from urllib.request import Request, urlopen
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
DART_BASE_URL     = "https://storage.googleapis.com/dart-archive/channels/stable/release/latest/version"
DART_SDK_INDEX    = "https://storage.googleapis.com/dart-archive/channels/stable/release/latest/sdk/dartsdk-windows-x64-release.zip"
INSTALL_ROOT      = Path("C:/Program Files/Dart")
SDK_DIR_NAME      = "dart-sdk"
BIN_SUBDIR        = "bin"
DART_CMD          = "dart"

def is_dart_installed() -> bool:
    """Checks if 'dart' is already available in PATH."""
    return shutil.which(DART_CMD) is not None

def get_latest_sdk_url() -> str:
    """
    Determines the latest Dart SDK URL for Windows x64.
    The default URL points to 'latest', so we use it directly.
    """
    return DART_SDK_INDEX

def download_sdk(dest: Path, url: str):
    """Downloads the Dart SDK as a ZIP archive."""
    logging.info(f"Starting download of Dart SDK from {url}")
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
                    logging.info(f"Download progress: {pct:.1f}%")
        logging.info(f"Download complete: {dest}")
    except (HTTPError, URLError) as e:
        logging.error(f"Error during download: {e}")
        sys.exit(1)

def extract_sdk(zip_path: Path, install_root: Path):
    """
    Extracts the ZIP archive to INSTALL_ROOT/dart-sdk
    and deletes any existing installation if present.
    """
    sdk_path = install_root / SDK_DIR_NAME
    if sdk_path.exists():
        logging.info(f"Old Dart installation found ({sdk_path}), deleting...")
        shutil.rmtree(sdk_path)
    logging.info(f"Extracting {zip_path} to {sdk_path}")
    install_root.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(install_root)
    logging.info("Extraction complete.")
    return sdk_path

def update_path(sdk_path: Path):
    """Adds the Dart SDK bin directory to the system PATH (for new terminals)."""
    bin_path = str(sdk_path / BIN_SUBDIR)
    current = os.environ.get("PATH", "")
    if bin_path.lower() in current.lower():
        logging.info("Dart SDK/bin is already in PATH.")
        return
    new_path = f"{current};{bin_path}"
    logging.info(f"Adding Dart SDK/bin to PATH: {bin_path}")
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation():
    """Verifies the installation using 'dart --version'."""
    try:
        out = subprocess.check_output([DART_CMD, "--version"], text=True).strip()
        logging.info(f"Dart successfully installed: {out}")
    except Exception as e:
        logging.error(f"Error verifying Dart installation: {e}")
        sys.exit(1)

def main():
    logging.info("=== Dart Installer Started ===")
    if os.name != "nt":
        logging.error("This script only works on Windows.")
        sys.exit(1)

    if is_dart_installed():
        logging.info("Dart is already installed. Aborting.")
        return

    sdk_url = get_latest_sdk_url()

    with tempfile.TemporaryDirectory() as td:
        tmp_zip = Path(td) / "dartsdk-windows-x64.zip"
        download_sdk(tmp_zip, sdk_url)
        sdk_path = extract_sdk(tmp_zip, INSTALL_ROOT)

    update_path(sdk_path)
    verify_installation()
    logging.info("=== Dart Installation Complete ===")

if __name__ == "__main__":
    main()
