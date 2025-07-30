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
WARNING: It is recommended to install F# from official sources:
https://fsharp.org/use/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of F#? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für F# folgen
print(f"[{timestamp()}] [INFO] Proceeding with F# installation...")

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

# --- Constants ---
DOTNET_INSTALL_SCRIPT = "https://dot.net/v1/dotnet-install.ps1"
INSTALL_DIR = Path("C:/Program Files/dotnet")
FSI_CMD = "fsi"  # F# Interactive
DOTNET_CMD = "dotnet"

def is_dotnet_installed() -> bool:
    """Checks whether 'dotnet' is available in the PATH."""
    return shutil.which(DOTNET_CMD) is not None

def is_fsharp_available() -> bool:
    """Checks whether 'fsi' (F# Interactive) is available."""
    return shutil.which(FSI_CMD) is not None

def download_install_script(dest: Path) -> None:
    """Downloads the official dotnet-install PowerShell script."""
    logging.info(f"Downloading dotnet-install script from {DOTNET_INSTALL_SCRIPT}")
    try:
        req = Request(DOTNET_INSTALL_SCRIPT, headers={"User-Agent": "Mozilla/5.0"})
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
        logging.info(f"dotnet-install script saved to: {dest}")
    except (HTTPError, URLError) as e:
        logging.error(f"Download failed: {e}")
        sys.exit(1)

def run_install_script(script_path: Path) -> None:
    """
    Executes the PowerShell script to install the .NET SDK (LTS version).
    """
    logging.info(f"Starting .NET SDK (LTS) installation into {INSTALL_DIR}")
    ps_command = [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", str(script_path),
        "-Channel", "LTS",
        "-InstallDir", str(INSTALL_DIR),
        "-NoPath"
    ]
    try:
        subprocess.run(ps_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info(".NET SDK installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f".NET installation failed (Exit code {e.returncode}):\n{e.stderr}")
        sys.exit(e.returncode)

def update_path() -> None:
    """Adds the dotnet install directory to the system PATH (for new terminals)."""
    dotnet_bin = str(INSTALL_DIR)
    current = os.environ.get("PATH", "")
    if dotnet_bin.lower() in current.lower():
        logging.info("dotnet is already in PATH.")
        return
    new_path = f"{current};{dotnet_bin}"
    logging.info(f"Adding dotnet install directory to PATH: {dotnet_bin}")
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation() -> None:
    """
    Verifies the installation using 'dotnet --list-sdks' and 'fsi --version'.
    """
    try:
        sdks = subprocess.check_output([DOTNET_CMD, "--list-sdks"], text=True).strip()
        logging.info(f"Installed .NET SDKs:\n{sdks}")
    except Exception as e:
        logging.error(f"Error checking .NET SDKs: {e}")
        sys.exit(1)

    try:
        out = subprocess.check_output([FSI_CMD, "--version"], text=True).strip()
        logging.info(f"F# Interactive (fsi) version: {out}")
    except Exception as e:
        logging.error(f"Error checking F# Interactive (fsi): {e}")
        sys.exit(1)

def main():
    logging.info("=== F# Installer (.NET SDK) started ===")
    if os.name != "nt":
        logging.error("This script only works on Windows.")
        sys.exit(1)

    # Install .NET SDK if not present
    if not is_dotnet_installed():
        with tempfile.TemporaryDirectory() as td:
            script = Path(td) / "dotnet-install.ps1"
            download_install_script(script)
            run_install_script(script)
        update_path()
    else:
        logging.info(".NET SDK is already installed.")

    # Check if F# Interactive is available
    if is_fsharp_available():
        logging.info("F# Interactive is already available.")
    else:
        logging.error("F# Interactive (fsi) was not found.")
        sys.exit(1)

    verify_installation()
    logging.info("=== F# installation completed ===")

if __name__ == "__main__":
    main()
