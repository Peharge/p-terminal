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
WARNING: It is recommended to install Go from the official website:
https://golang.org/dl/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Go? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Go folgen
print(f"[{timestamp()}] [INFO] Proceeding with Go installation...")

import os
import sys
import subprocess
import logging
import tempfile
import shutil
from pathlib import Path
from urllib.request import urlopen
import json
import zipfile

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

GO_INSTALL_DIR = Path("C:/Go")
GO_DOWNLOAD_API = "https://go.dev/dl/?mode=json"

def is_go_installed() -> bool:
    """Checks whether Go is already installed."""
    return shutil.which("go") is not None or (GO_INSTALL_DIR / "bin" / "go.exe").exists()

def get_latest_go_version() -> dict:
    """Fetches metadata for the latest Go version for Windows x64."""
    logging.info("Querying official Go download API...")
    with urlopen(GO_DOWNLOAD_API) as resp:
        versions = json.load(resp)
        for v in versions:
            for f in v["files"]:
                if f["os"] == "windows" and f["arch"] == "amd64" and f["kind"] == "archive":
                    logging.info(f"Latest version found: {v['version']}")
                    return {
                        "version": v["version"],
                        "filename": f["filename"],
                        "url": "https://go.dev/dl/" + f["filename"]
                    }
    logging.error("No matching Go version found.")
    sys.exit(1)

def download_go_zip(info: dict, dest: Path):
    """Downloads the Go ZIP archive."""
    logging.info(f"Downloading Go {info['version']} from {info['url']}")
    with urlopen(info["url"]) as resp, open(dest, "wb") as out_file:
        shutil.copyfileobj(resp, out_file)
    logging.info(f"Download complete: {dest}")

def extract_go(zip_path: Path):
    """Extracts the ZIP archive to C:/Go."""
    if GO_INSTALL_DIR.exists():
        logging.info("Removing old Go installation...")
        shutil.rmtree(GO_INSTALL_DIR)
    logging.info(f"Extracting {zip_path} to {GO_INSTALL_DIR}")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall("C:/")
    logging.info("Extraction complete.")

def update_path():
    """Adds Go to the PATH (only effective in new terminals)."""
    go_bin = str(GO_INSTALL_DIR / "bin")
    current_path = os.environ.get("PATH", "")
    if go_bin.lower() in current_path.lower():
        logging.info("Go is already in the PATH.")
        return
    logging.info(f"Adding Go to PATH: {go_bin}")
    subprocess.run(["setx", "PATH", f"{current_path};{go_bin}"], shell=True)

def verify_installation():
    """Verifies that Go is working by calling 'go version'."""
    try:
        result = subprocess.run(["go", "version"], capture_output=True, text=True, check=True)
        logging.info(f"Go successfully installed: {result.stdout.strip()}")
    except Exception as e:
        logging.error("Error verifying Go installation: " + str(e))
        sys.exit(1)

def main():
    logging.info("=== Go Installer started ===")
    if os.name != "nt":
        logging.error("This script only works on Windows.")
        sys.exit(1)

    if is_go_installed():
        logging.info("Go is already installed.")
        return

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        info = get_latest_go_version()
        zip_file = tmp_path / info["filename"]
        download_go_zip(info, zip_file)
        extract_go(zip_file)

    update_path()
    verify_installation()
    logging.info("=== Go installation completed ===")

if __name__ == "__main__":
    main()
