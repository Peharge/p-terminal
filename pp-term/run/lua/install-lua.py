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
WARNING: It is recommended to install Lua from the official website:
https://www.lua.org/download.html

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Lua? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Lua folgen
print(f"[{timestamp()}] [INFO] Proceeding with Lua installation...")

import os
import sys
import shutil
import subprocess
import logging
import tempfile
import zipfile
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

# --- Constants for installation ---
LUA_VERSION    = "5.4.6"  # Current stable version
BASE_URL       = "https://downloads.sourceforge.net/project/luabinaries"
FILENAME       = f"lua-{LUA_VERSION}_Win64_bin.zip"
DOWNLOAD_URL   = f"{BASE_URL}/{LUA_VERSION}/Windows%20Libraries/{FILENAME}"
INSTALL_ROOT   = Path("C:/Program Files/Lua")
INSTALL_DIR    = INSTALL_ROOT / f"Lua-{LUA_VERSION}"
BIN_DIR        = INSTALL_DIR  # the ZIP contains the .exe directly in the root directory

def is_lua_installed() -> bool:
    """Checks if 'lua' is already callable from PATH."""
    return shutil.which("lua") is not None

def download_lua(dest: Path):
    """Downloads the Lua binary ZIP."""
    logging.info(f"Starting download of Lua {LUA_VERSION} from {DOWNLOAD_URL}")
    try:
        req = Request(DOWNLOAD_URL, headers={"User-Agent": "Mozilla/5.0"})
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

def extract_lua(zip_path: Path):
    """
    Extracts the ZIP archive to INSTALL_DIR
    and removes old installation if present.
    """
    if INSTALL_DIR.exists():
        logging.info("Old Lua installation found, deleting...")
        shutil.rmtree(INSTALL_DIR)
    logging.info(f"Extracting {zip_path} to {INSTALL_DIR}")
    INSTALL_DIR.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(INSTALL_DIR)
    logging.info("Extraction completed.")

def update_path():
    """Adds Lua installation directory to the system PATH (for new terminals)."""
    lua_dir = str(BIN_DIR)
    current = os.environ.get("PATH", "")
    if lua_dir.lower() in current.lower():
        logging.info("Lua is already in PATH.")
        return
    new_path = f"{current};{lua_dir}"
    logging.info(f"Adding Lua to PATH: {lua_dir}")
    # setx writes the new PATH to the registry
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation():
    """Verifies installation via 'lua -v'."""
    try:
        result = subprocess.run(["lua", "-v"], capture_output=True, text=True, check=True)
        logging.info(f"Lua successfully installed: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error verifying Lua installation: {e}")
        sys.exit(1)

def main():
    logging.info("=== Lua Installer started ===")
    if os.name != "nt":
        logging.error("This script only works on Windows.")
        sys.exit(1)

    if is_lua_installed():
        logging.info("Lua is already installed. Aborting.")
        return

    # Temporary directory for download
    with tempfile.TemporaryDirectory() as td:
        tmp_zip = Path(td) / FILENAME
        download_lua(tmp_zip)
        extract_lua(tmp_zip)

    update_path()
    verify_installation()
    logging.info("=== Lua installation completed ===")

if __name__ == "__main__":
    main()
