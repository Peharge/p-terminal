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

# The code even works on linux ;-)

from datetime import datetime

def timestamp() -> str:
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

def confirm_installation() -> bool:
    print(f"""
WARNING: It is highly recommended to install Anaconda only from the official source:
https://www.anaconda.com/products/distribution

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the Anaconda installation? [y/n]:
""", end='')

    choice = input().strip().lower()
    if choice != 'y':
        print(f"[{timestamp()}] [INFO] Installation of Anaconda aborted by user.")
        return False
    print(f"[{timestamp()}] [INFO] Proceeding with Anaconda installation...")
    return True

if not confirm_installation():
    exit(0)

# --- Ab hier erst Module importieren und Installation starten ---
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

def download_anaconda_installer(url: str, filename: str) -> Path:
    logging.info(f"Downloading Anaconda installer from {url} ...")
    temp_dir = tempfile.gettempdir()
    file_path = Path(temp_dir) / filename
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req) as response, open(file_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        logging.info(f"Installer downloaded to {file_path}")
        return file_path
    except (URLError, HTTPError) as e:
        logging.error(f"Failed to download installer: {e}")
        sys.exit(1)

def install_anaconda(installer_path: Path):
    system = platform.system()
    logging.info(f"Starting Anaconda installation on {system} ...")
    try:
        if system == "Windows":
            subprocess.run([str(installer_path), "/S", "/D=C:\\Anaconda3"], check=True)
        elif system == "Darwin":
            subprocess.run(["sudo", "installer", "-pkg", str(installer_path), "-target", "/"], check=True)
        elif system == "Linux":
            subprocess.run(["bash", str(installer_path), "-b"], check=True)
        else:
            logging.error(f"Unsupported OS: {system}")
            sys.exit(1)
        logging.info("Anaconda installation completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation failed: {e}")
        sys.exit(1)

def main():
    import platform
    system = platform.system()
    if system == "Windows":
        url = "https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Windows-x86_64.exe"
        filename = "Anaconda3-Windows-x86_64.exe"
    elif system == "Darwin":
        url = "https://repo.anaconda.com/archive/Anaconda3-2023.07-1-MacOSX-x86_64.pkg"
        filename = "Anaconda3-MacOSX-x86_64.pkg"
    elif system == "Linux":
        url = "https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh"
        filename = "Anaconda3-Linux-x86_64.sh"
    else:
        logging.error(f"Unsupported OS: {system}")
        sys.exit(1)

    installer_path = download_anaconda_installer(url, filename)
    install_anaconda(installer_path)

if __name__ == "__main__":
    main()
