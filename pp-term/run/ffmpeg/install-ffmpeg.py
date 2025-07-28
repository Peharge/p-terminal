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
WARNING: It is recommended to install FFmpeg from the official website:
https://ffmpeg.org/download.html

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of FFmpeg? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für FFmpeg folgen
print(f"[{timestamp()}] [INFO] Proceeding with FFmpeg installation...")

import os
import sys
import subprocess
import logging
import tempfile
import shutil
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json

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
INSTALL_DIR = Path("C:/ffmpeg")
GITHUB_API_RELEASES = "https://api.github.com/repos/BtbN/FFmpeg-Builds/releases/latest"
ASSET_KEYWORDS = ["win64-gpl.zip", "win64.zip"]  # Priority: GPL builds, else standard

def is_ffmpeg_installed() -> bool:
    """Check if 'ffmpeg' is already available in PATH or installed folder."""
    return shutil.which("ffmpeg") is not None or (INSTALL_DIR / "bin" / "ffmpeg.exe").exists()

def get_latest_asset_url() -> dict:
    """
    Query GitHub API for the latest release and find a matching zip asset for Windows x64.
    Returns dict with 'name' and 'url'.
    """
    logging.info("Fetching latest release info from GitHub API...")
    try:
        req = Request(GITHUB_API_RELEASES, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp:
            release = json.load(resp)
    except (HTTPError, URLError) as e:
        logging.error(f"Error fetching release info: {e}")
        sys.exit(1)

    # Search assets by keywords in defined order
    for keyword in ASSET_KEYWORDS:
        for asset in release.get("assets", []):
            name = asset.get("name", "")
            if keyword in name and name.endswith(".zip"):
                download_url = asset.get("browser_download_url")
                logging.info(f"Found asset: {name}")
                return {"name": name, "url": download_url}

    logging.error("No suitable Windows x64 zip asset found.")
    sys.exit(1)

def download_asset(name: str, url: str, dest: Path) -> None:
    """Download the zip archive and show progress."""
    logging.info(f"Starting download of {name}")
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
        logging.info(f"Download completed: {dest}")
    except (HTTPError, URLError) as e:
        logging.error(f"Download error: {e}")
        sys.exit(1)

def extract_zip(zip_path: Path):
    """Extract the zip archive into INSTALL_DIR."""
    if INSTALL_DIR.exists():
        logging.info(f"Deleting old installation: {INSTALL_DIR}")
        shutil.rmtree(INSTALL_DIR)
    logging.info(f"Extracting {zip_path} to {INSTALL_DIR}")
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(INSTALL_DIR.parent)
        # Some builds extract into ffmpeg-<version>-win64; rename if necessary
        extracted = INSTALL_DIR.parent / z.namelist()[0].split("/")[0]
    if extracted != INSTALL_DIR:
        extracted.rename(INSTALL_DIR)
    logging.info("Extraction completed.")

def update_path():
    """Add ffmpeg/bin to system PATH (effective for new terminals)."""
    bin_path = str(INSTALL_DIR / "bin")
    current = os.environ.get("PATH", "")
    if bin_path.lower() in current.lower():
        logging.info("ffmpeg/bin is already in PATH.")
        return
    logging.info(f"Adding ffmpeg/bin to PATH: {bin_path}")
    # Warning: setx has about 1024 character limit for PATH
    subprocess.run(f'setx PATH "{current};{bin_path}"', shell=True, check=False)

def verify_installation():
    """Verify installation by running 'ffmpeg -version'."""
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True, check=True)
        logging.info(f"ffmpeg installed successfully: {result.stdout.splitlines()[0]}")
    except Exception as e:
        logging.error(f"Verification failed: {e}")
        sys.exit(1)

def main():
    logging.info("=== FFmpeg Installer started ===")
    if os.name != "nt":
        logging.error("This script only runs on Windows.")
        sys.exit(1)

    if is_ffmpeg_installed():
        logging.info("ffmpeg is already installed. Aborting.")
        return

    asset = get_latest_asset_url()
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        zip_path = td_path / asset["name"]
        download_asset(asset["name"], asset["url"], zip_path)
        extract_zip(zip_path)

    update_path()
    verify_installation()
    logging.info("=== FFmpeg installation completed ===")

if __name__ == "__main__":
    main()
