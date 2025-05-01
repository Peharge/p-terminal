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

import os
import sys
import json
import shutil
import subprocess
import requests
import zipfile
import ctypes
from pathlib import Path
from io import BytesIO


# Step 1: Download Fira Code Nerd Font
def download_font(url, font_zip_path="FiraCode.zip"):
    """Download the Fira Code Nerd Font ZIP file."""
    try:
        print("Downloading Fira Code Nerd Font...")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(font_zip_path, "wb") as file:
            file.write(response.content)
        print("Download complete.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading font: {e}")
        sys.exit(1)


# Step 2: Install the downloaded font
def install_font(url="https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/FiraCode.zip"):
    """Download, extract, and install Nerd Fonts from a GitHub release URL."""

    # Define the fonts installation directory
    install_path = Path(os.getenv("WINDIR")) / "Fonts"

    # Create the installation path if it doesn't exist
    install_path.mkdir(parents=True, exist_ok=True)

    # Download the font zip file
    print("Downloading Nerd Font...")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        zip_file = BytesIO(response.content)  # Read the content as a zip file
    except requests.RequestException as e:
        print(f"Error downloading the font: {e}")
        return

    # Extract the ZIP archive
    print("Extracting the font...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall("FiraCode")  # Extract to a temporary folder

    # Install fonts by copying them to the system Fonts directory
    print("Installing the font...")
    for root, dirs, files in os.walk("FiraCode"):
        for file in files:
            if file.endswith(".ttf"):
                font_path = Path(root) / file
                try:
                    # Ensure the font file is copied to the Fonts directory
                    shutil.copy(font_path, install_path)
                    # Inform the system about the newly installed font
                    ctypes.windll.gdi32.AddFontResourceW(str(font_path))
                    ctypes.windll.user32.PostMessageW(0xFFFF, 0x001D, 0, 0)  # WM_FONTCHANGE
                    print(f"Installed font: {file}")
                except Exception as e:
                    print(f"Failed to install font {file}: {e}")
                    continue

    # Clean up extracted files
    shutil.rmtree("FiraCode")

    print("Font installation complete.")


# Step 3: Adjust the Windows Terminal configuration
def configure_terminal():
    """Update Windows Terminal configuration to use FiraCode Nerd Font."""
    terminal_profile_path = Path(os.getenv(
        "LOCALAPPDATA")) / "Packages" / "Microsoft.WindowsTerminal_8wekyb3d8bbwe" / "LocalState" / "profiles.json"

    if not terminal_profile_path.exists():
        print("The file profiles.json could not be found.")
        return

    print("Configuring Windows Terminal...")

    # Load the configuration file
    try:
        with open(terminal_profile_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading profiles.json: {e}")
        return

    # Change the font for all profiles
    for profile in config.get('profiles', {}).get('list', []):
        profile.setdefault('fontFace', 'FiraCode Nerd Font')

    # Save the modified configuration
    try:
        with open(terminal_profile_path, 'w', encoding='utf-8') as file:
            json.dump(config, file, ensure_ascii=False, indent=4)
        print("Windows Terminal configured to use 'FiraCode Nerd Font'.")
    except IOError as e:
        print(f"Error saving profiles.json: {e}")


def check_and_install_winget():
    """Checks if winget is installed, and installs it if necessary."""
    try:
        subprocess.run(["winget", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("winget is already installed.")
    except subprocess.CalledProcessError:
        print("winget is not installed. Installing winget...")
        install_winget()


def install_winget():
    """Installs winget (Windows Package Manager)."""
    if sys.platform == "win32":
        try:
            subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"],
                           check=True)
            subprocess.run(
                ["powershell", "-Command", "iwr https://aka.ms/install-winget.ps1 -OutFile install-winget.ps1"],
                check=True)
            subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Unrestricted -Scope CurrentUser"],
                           check=True)
            subprocess.run(["powershell", "-Command", "powershell -ExecutionPolicy Bypass -File install-winget.ps1"],
                           check=True)
            print("winget installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing winget: {e}")
            sys.exit(1)


def install_oh_my_posh():
    """Installs OhMyPosh via winget."""
    try:
        print("Installing OhMyPosh...")
        subprocess.run(["winget", "install", "lambdageneration.OhMyPosh"], check=True)
        print("OhMyPosh installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing OhMyPosh: {e}")
        sys.exit(1)


def initialize_oh_my_posh():
    """Initializes OhMyPosh for PowerShell with the specified configuration file path."""
    try:
        config_path = os.path.expanduser("~") + r"\AppData\Local\Programs\oh-my-posh\themes\lambdageneration.omp.json"
        command = f"oh-my-posh --init --shell pwsh --config {config_path} | Invoke-Expression"
        subprocess.run(["powershell", "-Command", command], check=True)
        print("OhMyPosh initialized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error initializing OhMyPosh: {e}")
        sys.exit(1)


def upgrade_oh_my_posh():
    """Upgrades OhMyPosh via winget."""
    try:
        print("Upgrading OhMyPosh...")
        subprocess.run(["winget", "upgrade", "lambdageneration.OhMyPosh"], check=True)
        print("OhMyPosh upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error upgrading OhMyPosh: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # URL for FiraCode Nerd Font
    font_url = "https://github.com/ryanoasis/nerd-fonts/releases/download/v2.2.2/FiraCode.zip"

    download_font(font_url)
    install_font()
    configure_terminal()

    print("Done! Fira Code Nerd Font is now installed and configured.")

    # Check and install winget if necessary
    check_and_install_winget()

    # Install, initialize and upgrade OhMyPosh
    install_oh_my_posh()
    initialize_oh_my_posh()
    upgrade_oh_my_posh()

    print("All steps completed successfully.")
