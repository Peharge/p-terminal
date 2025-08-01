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
WARNING: It is recommended to install Lisp implementations (e.g., SBCL) from their official websites:
https://www.sbcl.org/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Lisp (SBCL)? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Lisp folgen
print(f"[{timestamp()}] [INFO] Proceeding with Lisp (SBCL) installation...")

import os
import sys
import subprocess
import logging
import tempfile
import shutil
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

log_path = Path(__file__).parent / "installer.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler(log_path, encoding='utf-8'), logging.StreamHandler(sys.stdout)]
)

def is_sbcl_installed() -> bool:
    return shutil.which("sbcl") is not None

def fetch_sbcl_installer_info():
    version = "2.5.4"  # Current stable version, adjust manually if needed
    filename = f"sbcl-{version}-x86-64-windows-binary.msi"
    url = f"https://sourceforge.net/projects/sbcl/files/sbcl/{version}/{filename}/download"
    return {"version": version, "filename": filename, "url": url}

def download_installer(url: str, dest: Path):
    logging.info(f"Starting download from {url}")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req) as resp, open(dest, "wb") as out:
        total = int(resp.getheader("Content-Length") or 0)
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

def run_installer(installer_path: Path):
    logging.info(f"Starting SBCL installer: {installer_path}")
    subprocess.run(["msiexec", "/i", str(installer_path), "/quiet", "/norestart"], check=True)
    logging.info("Installation completed.")

def verify_installation():
    try:
        out = subprocess.check_output(["sbcl", "--version"], text=True).strip()
        logging.info(f"SBCL successfully installed: {out}")
    except Exception as e:
        logging.error(f"Verification failed: {e}")
        sys.exit(1)

def main():
    logging.info("=== SBCL Installer started ===")
    if os.name != "nt":
        logging.error("This script only works on Windows.")
        sys.exit(1)
    if is_sbcl_installed():
        logging.info("SBCL is already installed. Aborting.")
        return
    info = fetch_sbcl_installer_info()
    with tempfile.TemporaryDirectory() as tmpdir:
        installer_path = Path(tmpdir) / info["filename"]
        download_installer(info["url"], installer_path)
        run_installer(installer_path)
    verify_installation()
    logging.info("=== SBCL installation completed ===")

if __name__ == "__main__":
    main()
