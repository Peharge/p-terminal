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
WARNING: It is recommended to install Haskell (GHC, Stack, or Cabal) from the official website:
https://www.haskell.org/downloads/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Haskell? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Haskell folgen
print(f"[{timestamp()}] [INFO] Proceeding with Haskell installation...")

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
GITHUB_API_LATEST = "https://api.github.com/repos/ghc/ghc/releases/latest"
INSTALL_ROOT      = Path("C:/Program Files/ghc")
GHC_CMD           = "ghc"

def is_ghc_installed() -> bool:
    """Checks whether 'ghc' is already available in PATH."""
    return shutil.which(GHC_CMD) is not None

def get_latest_ghc_release() -> dict:
    """Fetches the latest GHC Windows installer asset via the GitHub API."""
    logging.info("Fetching latest GHC version from GitHub API...")
    req = Request(GITHUB_API_LATEST, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req) as resp:
            data = json.load(resp)
    except (HTTPError, URLError) as e:
        logging.error(f"Error fetching GitHub API: {e}")
        sys.exit(1)

    version = data.get("tag_name", "").lstrip("ghc-")
    download_url = None
    for asset in data.get("assets", []):
        name = asset.get("name", "")
        # Look for Windows x86_64 installer ending in .exe
        if name.endswith("x86_64-unknown-mingw32.exe"):
            download_url = asset.get("browser_download_url")
            break

    if not download_url or not version:
        logging.error("Could not find GHC Windows installer.")
        sys.exit(1)

    logging.info(f"Found GHC version: {version}")
    return {"version": version, "url": download_url}

def download_installer(dest: Path, url: str):
    """Downloads the GHC installer and logs progress."""
    logging.info(f"Starting download of GHC installer: {url}")
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

def run_installer(installer: Path):
    """Runs the GHC installer in silent mode."""
    logging.info(f"Launching GHC installer: {installer}")
    # NSIS parameter for silent install: /S
    try:
        res = subprocess.run([str(installer), "/S"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info("GHC successfully installed.")
        logging.debug(f"Installer output:\n{res.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation failed (Exit code {e.returncode}): {e.stderr}")
        sys.exit(e.returncode)

def update_path(version: str):
    """Adds the GHC bin directory to the system PATH (for new terminals)."""
    ghc_bin = str(INSTALL_ROOT / version / "bin")
    current = os.environ.get("PATH", "")
    if ghc_bin.lower() in current.lower():
        logging.info("GHC/bin is already in PATH.")
        return
    new_path = f"{current};{ghc_bin}"
    logging.info(f"Adding GHC/bin to PATH: {ghc_bin}")
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation():
    """Validates installation using 'ghc --version'."""
    try:
        out = subprocess.check_output([GHC_CMD, "--version"], text=True).strip()
        logging.info(f"GHC version: {out}")
    except Exception as e:
        logging.error(f"Verification of GHC failed: {e}")
        sys.exit(1)

def main():
    logging.info("=== Haskell (GHC) installer started ===")
    if os.name != "nt":
        logging.error("This script only runs on Windows.")
        sys.exit(1)

    if is_ghc_installed():
        logging.info("GHC is already installed. Aborting.")
        return

    info = get_latest_ghc_release()
    version = info["version"]
    url     = info["url"]

    with tempfile.TemporaryDirectory() as td:
        installer = Path(td) / f"ghc-{version}-windows.exe"
        download_installer(installer, url)
        run_installer(installer)

    update_path(version)
    verify_installation()
    logging.info("=== Haskell (GHC) installation completed ===")

if __name__ == "__main__":
    main()
