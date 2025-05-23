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

import sys
import os
import shutil
import subprocess
import logging
import tempfile
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

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

# CRAN base URL for the current R installer executable
CRAN_R_INSTALLER_URL = "https://cran.r-project.org/bin/windows/base/R-latest.exe"


def is_rscript_installed() -> bool:
    """Checks if Rscript can be invoked via PATH."""
    return shutil.which("Rscript") is not None


def download_installer(dest_path: Path) -> None:
    """Downloads the R Windows installer."""
    logging.info(f"Starting download of R installer from {CRAN_R_INSTALLER_URL}")
    try:
        req = Request(CRAN_R_INSTALLER_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as response, open(dest_path, "wb") as out_file:
            total = int(response.getheader('Content-Length', 0))
            downloaded = 0
            chunk_size = 8192
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
                downloaded += len(chunk)
                if total:
                    percent = downloaded * 100 / total
                    logging.info(f"Download progress: {percent:.1f}%")
        logging.info(f"Download completed: {dest_path}")
    except (HTTPError, URLError) as e:
        logging.error(f"Error downloading R installer: {e}")
        sys.exit(1)


def run_installer(installer_path: Path) -> None:
    """Runs the R installer in silent mode."""
    logging.info(f"Starting R installer: {installer_path}")
    # Inno Setup-based: /VERYSILENT /SUPPRESSMSGBOXES /NORESTART
    cmd = [str(installer_path), "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART"]
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info("R successfully installed.")
        logging.debug(f"Installer output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation failed (exit code {e.returncode}): {e.stderr}")
        sys.exit(e.returncode)


def ensure_rscript_available():
    """Checks if Rscript is now available in the PATH."""
    if is_rscript_installed():
        logging.info("Rscript is now available.")
    else:
        logging.warning("Rscript not found in PATH. Please restart the terminal or check your PATH settings.")


def main():
    logging.info("=== R Installer started ===")
    if is_rscript_installed():
        logging.info("Rscript is already installed. Exiting.")
        return

    with tempfile.TemporaryDirectory() as tmpdir:
        installer_file = Path(tmpdir) / "R-latest.exe"
        download_installer(installer_file)
        run_installer(installer_file)

    ensure_rscript_available()
    logging.info("=== Process completed ===")

if __name__ == "__main__":
    if os.name != "nt":
        logging.error("This script only runs on Windows.")
        sys.exit(1)
    main()
