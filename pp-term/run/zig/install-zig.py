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
WARNING: It is recommended to install Zig from the official website:
https://ziglang.org/download/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Zig? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Zig folgen
print(f"[{timestamp()}] [INFO] Proceeding with Zig installation...")

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
GITHUB_API_LATEST = "https://api.github.com/repos/ziglang/zig/releases/latest"
INSTALL_ROOT      = Path("C:/Program Files/Zig")
ZIG_CMD           = "zig"

def is_zig_installed() -> bool:
    """Checks if 'zig' is already available in PATH."""
    return shutil.which(ZIG_CMD) is not None

def fetch_latest_zig_release() -> dict:
    """Fetches the latest Zig release version and Windows download URL via GitHub API."""
    logging.info("Fetching latest Zig version from GitHub API...")
    req = Request(GITHUB_API_LATEST, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req) as resp:
            data = json.load(resp)
    except (HTTPError, URLError) as e:
        logging.error(f"Error fetching release API: {e}")
        sys.exit(1)

    version = data.get("tag_name", "").lstrip("zig-")
    asset_url = None
    asset_name = None
    # Search for Windows x86_64 ZIP asset, e.g. zig-windows-x86_64-0.10.1.zip
    for asset in data.get("assets", []):
        name = asset.get("name", "")
        lower = name.lower()
        if "windows" in lower and "x86_64" in lower and lower.endswith(".zip"):
            asset_url = asset.get("browser_download_url")
            asset_name = name
            break

    if not version or not asset_url:
        logging.error("Could not find Windows x86_64 ZIP asset for Zig.")
        sys.exit(1)

    logging.info(f"Found version: {version}, asset: {asset_name}")
    return {"version": version, "url": asset_url, "filename": asset_name}

def download_asset(url: str, dest: Path):
    """Downloads the ZIP archive and logs progress."""
    logging.info(f"Starting download from {url}")
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp, open(dest, "wb") as out:
            total = int(resp.getheader("Content-Length", 0) or 0)
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

def extract_zip(zip_path: Path, target_dir: Path):
    """Extracts the ZIP archive to target_dir, deleting any old installation."""
    if target_dir.exists():
        logging.info(f"Old installation found at {target_dir}, deleting...")
        shutil.rmtree(target_dir)
    logging.info(f"Extracting {zip_path} to {target_dir}")
    target_dir.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(target_dir)
    logging.info("Extraction completed.")

def update_path(install_dir: Path):
    """Adds the Zig directory (bin) to system PATH (for new terminals)."""
    # The zip contains binaries directly in root, so add install_dir directly
    bin_dir = str(install_dir)
    current = os.environ.get("PATH", "")
    if bin_dir.lower() in current.lower():
        logging.info("Zig is already in PATH.")
        return
    new_path = f"{current};{bin_dir}"
    logging.info(f"Adding Zig to PATH: {bin_dir}")
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation():
    """Verifies installation via 'zig version'."""
    try:
        out = subprocess.check_output([ZIG_CMD, "version"], text=True).strip()
        logging.info(f"Zig successfully installed: {out}")
    except Exception as e:
        logging.error(f"Verification of Zig failed: {e}")
        sys.exit(1)

def main():
    logging.info("=== Zig installer started ===")
    if os.name != "nt":
        logging.error("This script only works on Windows.")
        sys.exit(1)

    if is_zig_installed():
        logging.info("Zig is already installed. Exiting.")
        return

    info = fetch_latest_zig_release()
    version    = info["version"]
    url        = info["url"]
    filename   = info["filename"]
    install_dir = INSTALL_ROOT / f"zig-{version}"

    with tempfile.TemporaryDirectory() as td:
        tmp_zip = Path(td) / filename
        download_asset(url, tmp_zip)
        extract_zip(tmp_zip, install_dir)

    update_path(install_dir)
    verify_installation()
    logging.info("=== Zig installation completed ===")

if __name__ == "__main__":
    main()
