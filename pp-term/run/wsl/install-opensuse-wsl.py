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

"""
This script installs openSUSE for WSL on Windows.
It performs the following steps:
  1. Checks if the script is running on Windows with Administrator rights.
  2. Enables the necessary Windows features:
       - Microsoft-Windows-Subsystem-for-Linux
       - VirtualMachinePlatform
  3. Sets WSL 2 as the default version.
  4. Starts the installation of the openSUSE distribution (via wsl --install -d openSUSE-Tumbleweed).

Important:
  - The script MUST be run as Administrator.
  - A system restart may be required for the enabled features to take effect.
  - After installation, the first openSUSE session will start in a new window where you will need to set up (username, password).
"""

from datetime import datetime

def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

print("""
WARNING: This script is intended for installing or maintaining OpenSUSE on WSL.

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with WSL OpenSUSE installation/maintenance? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Operation aborted by user.")
    exit(0)

# Hier kann der Installations- oder Wartungscode für WSL OpenSUSE folgen
print(f"[{timestamp()}] [INFO] Proceeding with WSL OpenSUSE installation/maintenance...")

import os
import sys
import subprocess
import logging
import traceback
import platform
import ctypes


def is_admin():
    """Checks if the script is run with Administrator rights."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception as e:
        logging.error("Error checking Administrator rights: %s", e)
        return False


def run_command(command, shell=False):
    """Runs a command and returns the output."""
    logging.info("Executing: %s", " ".join(command) if isinstance(command, list) else command)
    try:
        result = subprocess.run(
            command,
            shell=shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        if result.stdout:
            logging.info("Output:\n%s", result.stdout)
        if result.stderr:
            logging.error("Error message:\n%s", result.stderr)
        return result
    except subprocess.CalledProcessError as e:
        logging.error("Command failed: %s", " ".join(command) if isinstance(command, list) else command)
        logging.error("Error output:\n%s", e.stderr)
        raise


def enable_wsl_features():
    """Enables the Windows features for WSL and VirtualMachinePlatform."""
    commands = [
        ["dism.exe", "/online", "/enable-feature", "/featurename:Microsoft-Windows-Subsystem-Linux", "/all", "/norestart"],
        ["dism.exe", "/online", "/enable-feature", "/featurename:VirtualMachinePlatform", "/all", "/norestart"],
    ]
    for cmd in commands:
        run_command(cmd)


def set_default_wsl_version():
    """Sets the default version of WSL to version 2."""
    run_command(["wsl", "--set-default-version", "2"])


def install_opensuse():
    """Starts the installation process for the openSUSE distribution via WSL."""
    run_command(["wsl", "--install", "-d", "openSUSE-Tumbleweed"])


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logging.info("Starting openSUSE installation for WSL...")

    if platform.system() != "Windows":
        logging.error("This script is only intended for Windows.")
        sys.exit(1)

    if not is_admin():
        logging.error("This script must be run as Administrator. Please restart it with elevated privileges.")
        sys.exit(1)

    try:
        enable_wsl_features()
        set_default_wsl_version()
        install_opensuse()

        logging.info("The openSUSE installation has started. A restart may be required for all changes to take effect.")
        logging.info("Upon the first start of openSUSE, you will be prompted to create a username and password.")
    except Exception as e:
        logging.error("An error occurred during the installation:")
        logging.error(str(e))
        logging.error(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
