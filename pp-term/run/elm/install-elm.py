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
WARNING: It is recommended to install Elm from the official website:
https://elm-lang.org/docs/install

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Elm? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Elm folgen
print(f"[{timestamp()}] [INFO] Proceeding with Elm installation...")

import os
import sys
import shutil
import subprocess
import logging
from pathlib import Path

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

def is_tool_installed(cmd: str) -> bool:
    """Checks if a CLI tool is available in the PATH."""
    return shutil.which(cmd) is not None

def install_elm_via_npm():
    """Installs Elm globally via npm."""
    logging.info("Installing Elm globally via npm...")
    try:
        subprocess.run(["npm", "install", "-g", "elm"], check=True)
        logging.info("Elm was installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during Elm installation: {e}")
        sys.exit(1)

def get_npm_global_prefix() -> str:
    """Retrieves the npm global prefix (path to global binaries)."""
    try:
        prefix = subprocess.check_output(
            ["npm", "config", "get", "prefix"],
            text=True
        ).strip()
        return prefix
    except subprocess.CalledProcessError as e:
        logging.error(f"Could not determine npm prefix: {e}")
        sys.exit(1)

def update_path(npm_prefix: str):
    """
    Adds the directory with global npm binaries to the system PATH.
    On Windows, this is typically the npm_prefix directory itself.
    """
    bin_path = npm_prefix
    current = os.environ.get("PATH", "")
    if bin_path.lower() in current.lower():
        logging.info("npm global prefix is already in PATH.")
        return
    new_path = f"{current};{bin_path}"
    logging.info(f"Adding npm global prefix to PATH: {bin_path}")
    # setx writes the new PATH to the registry (for new terminals)
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation():
    """Verifies the Elm installation using 'elm --version'."""
    try:
        out = subprocess.check_output(["elm", "--version"], text=True).strip()
        logging.info(f"Elm successfully installed, version: {out}")
    except Exception as e:
        logging.error(f"Verification of Elm failed: {e}")
        sys.exit(1)

def main():
    logging.info("=== Elm Installer Started ===")
    if os.name != "nt":
        logging.error("This script only works on Windows.")
        sys.exit(1)

    # Check for Node.js/npm
    if not is_tool_installed("node") or not is_tool_installed("npm"):
        logging.error("Node.js and npm are required. Please install them first.")
        sys.exit(1)
    else:
        logging.info("Node.js and npm are installed.")

    # Install Elm if not already present
    if is_tool_installed("elm"):
        logging.info("Elm is already installed. Aborting.")
    else:
        install_elm_via_npm()

    # Get npm global prefix and add to PATH
    npm_prefix = get_npm_global_prefix()
    update_path(npm_prefix)

    # Verification
    verify_installation()
    logging.info("=== Elm Installation Complete ===")

if __name__ == "__main__":
    main()
