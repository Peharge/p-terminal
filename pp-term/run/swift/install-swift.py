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
WARNING: It is recommended to install Swift from the official website:
https://swift.org/download/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Swift? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Swift folgen
print(f"[{timestamp()}] [INFO] Proceeding with Swift installation...")

import os
import sys
import shutil
import subprocess
import logging
import tempfile
import zipfile
import re
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
SWIFT_DOWNLOAD_PAGE = "https://swift.org/download/"
INSTALL_ROOT        = Path("C:/Program Files/Swift")
BIN_SUBDIR          = "usr\\bin"
SWIFT_EXE           = "swift.exe"

def is_swift_installed() -> bool:
    """Checks if Swift is already available in PATH."""
    return shutil.which("swift") is not None or any((INSTALL_ROOT / d / BIN_SUBDIR / SWIFT_EXE).exists()
                                                    for d in os.listdir(INSTALL_ROOT) if (INSTALL_ROOT / d).is_dir())

def find_latest_swift_url(html: str) -> dict:
    """
    Parses the download page and finds the first ZIP for Windows x64.
    Returns dict with 'version', 'url'.
    """
    # Example link: https://swift.org/builds/swift-5.11.0-release/windows/swift-5.11.0-RELEASE-windows10.zip
    pattern = re.compile(
        r'href="(https://swift\.org/builds/swift-([\d\.]+)-release/windows/swift-[\d\.]+-RELEASE-windows10\.zip)"',
        re.IGNORECASE
    )
    match = pattern.search(html)
    if not match:
        logging.error("Could not find a download link for Swift Windows.")
        sys.exit(1)
    url = match.group(1)
    version = match.group(2)
    logging.info(f"Found Swift version: {version}")
    return {"version": version, "url": url}

def download_swift(dest: Path, url: str):
    """Downloads the Swift ZIP archive."""
    logging.info(f"Starting download of Swift: {url}")
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
        logging.error(f"Error during download: {e}")
        sys.exit(1)

def extract_swift(zip_path: Path, version: str):
    """Extracts the ZIP archive to INSTALL_ROOT/Swift-<version>."""
    dest_dir = INSTALL_ROOT / f"Swift-{version}"
    if dest_dir.exists():
        logging.info(f"Removing old Swift installation {dest_dir}...")
        shutil.rmtree(dest_dir)
    logging.info(f"Extracting {zip_path} to {dest_dir}")
    dest_dir.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_dir)
    logging.info("Extraction completed.")
    return dest_dir

def update_path(swift_dir: Path):
    """Adds the Swift usr\\bin directory to the system PATH (for new terminals)."""
    bin_path = str(swift_dir / BIN_SUBDIR)
    current = os.environ.get("PATH", "")
    if bin_path.lower() in current.lower():
        logging.info("Swift bin is already in PATH.")
        return
    new_path = f"{current};{bin_path}"
    logging.info(f"Adding Swift usr\\bin to PATH: {bin_path}")
    # setx writes the new PATH to the registry (appends it)
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation():
    """Verifies the installation via 'swift --version'."""
    try:
        out = subprocess.check_output(["swift", "--version"], text=True).strip()
        logging.info(f"Swift installed successfully: {out}")
    except Exception as e:
        logging.error(f"Error verifying Swift: {e}")
        sys.exit(1)

def main():
    logging.info("=== Swift installer started ===")
    if os.name != "nt":
        logging.error("This script only runs on Windows.")
        sys.exit(1)

    if is_swift_installed():
        logging.info("Swift is already installed. Aborting.")
        return

    # Fetch download page
    try:
        req = Request(SWIFT_DOWNLOAD_PAGE, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp:
            html = resp.read().decode("utf-8")
    except (HTTPError, URLError) as e:
        logging.error(f"Error fetching download page: {e}")
        sys.exit(1)

    info = find_latest_swift_url(html)
    version = info["version"]
    url     = info["url"]

    with tempfile.TemporaryDirectory() as td:
        tmp_zip = Path(td) / f"swift-{version}-windows.zip"
        download_swift(tmp_zip, url)
        swift_dir = extract_swift(tmp_zip, version)

    update_path(swift_dir)
    verify_installation()
    logging.info("=== Swift installation completed ===")

if __name__ == "__main__":
    main()
