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
WARNING: It is recommended to install TypeScript from the official website:
https://www.typescriptlang.org/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of TypeScript? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für TypeScript folgen
print(f"[{timestamp()}] [INFO] Proceeding with TypeScript installation...")

import os
import sys
import shutil
import subprocess
import logging
import tempfile
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

NODE_INDEX_JSON = "https://nodejs.org/dist/index.json"

def is_npm_installed() -> bool:
    """Checks if 'npm' is callable from PATH."""
    return shutil.which("npm") is not None

def get_latest_lts_node() -> dict:
    """
    Reads Node.js dist index.json and finds
    the latest LTS version for Windows x64 (MSI).
    """
    logging.info("Fetching Node.js versions from: %s", NODE_INDEX_JSON)
    try:
        req = Request(NODE_INDEX_JSON, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp:
            versions = json.load(resp)
    except (HTTPError, URLError) as e:
        logging.error("Error fetching Node.js versions list: %s", e)
        sys.exit(1)

    for v in versions:
        # v["lts"] is either False or a codename string, e.g. "Gallium"
        if v.get("lts"):
            version = v["version"]          # e.g. "v20.3.1"
            msi_name = f"node-{version}-x64.msi"
            url = f"https://nodejs.org/dist/{version}/{msi_name}"
            logging.info("Found LTS version: %s", version)
            return {"version": version, "msi": msi_name, "url": url}

    logging.error("No LTS version found in index.json.")
    sys.exit(1)

def download_file(url: str, dest: Path):
    """Downloads a file from url to dest with progress logging."""
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

def run_node_installer(msi_path: Path):
    """Installs Node.js via MSI silent mode."""
    logging.info("Starting Node.js installer: %s", msi_path)
    # /qn = no UI, /norestart = no automatic reboot
    cmd = ["msiexec", "/i", str(msi_path), "/qn", "/norestart"]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Node.js installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error("Node.js installation failed (Exit code %d)", e.returncode)
        sys.exit(e.returncode)

def install_typescript():
    """Installs TypeScript globally via npm."""
    logging.info("Installing TypeScript globally via npm")
    cmd = ["npm", "install", "-g", "typescript"]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info("TypeScript installed globally.")
        logging.debug("npm output:\n%s", result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("TypeScript installation failed (Exit code %d):\n%s", e.returncode, e.stderr)
        sys.exit(e.returncode)

def verify_tsc():
    """Validates that 'tsc' (TypeScript compiler) is available."""
    try:
        result = subprocess.run(["tsc", "--version"], check=True, capture_output=True, text=True)
        logging.info("tsc found: %s", result.stdout.strip())
    except Exception as e:
        logging.error("tsc not found or error: %s", e)
        sys.exit(1)

def main():
    logging.info("=== TypeScript installer started ===")
    if os.name != "nt":
        logging.error("This script only runs on Windows.")
        sys.exit(1)

    # Step 1: Check npm
    if not is_npm_installed():
        logging.info("npm not found. Installing Node.js LTS...")
        info = get_latest_lts_node()
        with tempfile.TemporaryDirectory() as td:
            msi_path = Path(td) / info["msi"]
            download_file(info["url"], msi_path)
            run_node_installer(msi_path)
    else:
        logging.info("npm is already installed.")

    # Step 2: Install TypeScript
    install_typescript()

    # Step 3: Verification
    verify_tsc()
    logging.info("=== TypeScript installation completed ===")

if __name__ == "__main__":
    main()
