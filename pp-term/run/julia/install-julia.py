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
WARNING: It is recommended to install Julia from the official website:
https://julialang.org/downloads/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Julia? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Julia folgen
print(f"[{timestamp()}] [INFO] Proceeding with Julia installation...")

import os
import sys
import shutil
import subprocess
import logging
import tempfile
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
# Current Julia version and download URL (Windows x64) from the official site
JULIA_VERSION = "1.11.5"  # Current stable release: v1.11.5 (April 14, 2025)
JULIA_URL     = f"https://julialang-s3.julialang.org/bin/winnt/x64/1.11/julia-{JULIA_VERSION}-win64.exe"
INSTALL_DIR   = Path("C:/Program Files/Julia") / f"Julia-{JULIA_VERSION}"
BIN_PATH      = INSTALL_DIR / "bin"
EXE_NAME      = BIN_PATH / "julia.exe"

def is_julia_installed() -> bool:
    """Checks whether 'julia' can already be invoked via PATH."""
    return shutil.which("julia") is not None or EXE_NAME.exists()

def download_installer(dest: Path) -> None:
    """Downloads the Julia installer and logs progress."""
    logging.info(f"Starting download of Julia {JULIA_VERSION} from {JULIA_URL}")
    try:
        req = Request(JULIA_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as response:
            total = int(response.getheader("Content-Length", 0))
            downloaded = 0
            chunk_size = 8192
            with open(dest, "wb") as out:
                while True:
                    chunk = response.read(chunk_size)
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

def run_installer(installer_path: Path) -> None:
    """Runs the Julia installer in silent mode."""
    logging.info(f"Starting Julia installer: {installer_path}")
    # Inno Setup parameters: /VERYSILENT, /SUPPRESSMSGBOXES, /NORESTART
    cmd = [str(installer_path),
           "/VERYSILENT",
           "/SUPPRESSMSGBOXES",
           "/NORESTART",
           f"/DIR={INSTALL_DIR}"]
    try:
        res = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info("Julia installed successfully.")
        logging.debug(f"Installer output:\n{res.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation failed (exit code {e.returncode}):\n{e.stderr}")
        sys.exit(e.returncode)

def update_path():
    """Adds Julia/bin to the system PATH (for new terminals)."""
    julia_bin = str(BIN_PATH)
    current = os.environ.get("PATH", "")
    if julia_bin.lower() in current.lower():
        logging.info("Julia/bin is already in PATH.")
        return
    logging.info(f"Adding Julia/bin to PATH: {julia_bin}")
    # setx writes the new PATH value to the registry (we append)
    subprocess.run(f'setx PATH "{current};{julia_bin}"', shell=True, check=False)

def verify_installation():
    """Validates the installation using 'julia --version'."""
    try:
        out = subprocess.run(["julia", "--version"], check=True, capture_output=True, text=True)
        logging.info(f"Julia version: {out.stdout.strip()}")
    except Exception as e:
        logging.error(f"Error verifying Julia installation: {e}")
        sys.exit(1)

def main():
    logging.info("=== Julia installer started ===")
    if os.name != "nt":
        logging.error("This script only runs on Windows.")
        sys.exit(1)

    if is_julia_installed():
        logging.info("Julia is already installed. Exiting.")
        return

    # Temporary directory for download
    with tempfile.TemporaryDirectory() as td:
        tmp_installer = Path(td) / f"julia-{JULIA_VERSION}-win64.exe"
        download_installer(tmp_installer)
        run_installer(tmp_installer)

    update_path()
    verify_installation()
    logging.info("=== Julia installation complete ===")

if __name__ == "__main__":
    main()
