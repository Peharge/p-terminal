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
import getpass
import subprocess
import threading
import time
import importlib.util
import os
import select
from datetime import datetime

def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

# Color codes
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
white = "\033[97m"
black = "\033[30m"
orange = "\033[38;5;214m"
reset = "\033[0m"
bold = "\033[1m"

# Required packages
required_packages = ["imageio", "transformers"]

def activate_virtualenv(venv_path):
    """Activates an existing virtual environment."""
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path, "bin", "activate")
    if not os.path.exists(activate_script):
        print(f"[{timestamp()}] [ERROR] Virtual environment could not be found at {venv_path}.")
        sys.exit(1)
    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"[{timestamp()}] [PASS] Virtual environment {venv_path} enabled.")

def ensure_packages_installed(packages):
    """Ensures all required packages are installed."""
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"[{timestamp()}] [PASS] {package} is already installed.")
        except ImportError:
            print(f"[{timestamp()}] [INFO] Installing {package}...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
                print(f"[{timestamp()}] [PASS] {package} installed successfully.")
            except subprocess.CalledProcessError:
                print(f"[{timestamp()}] [ERROR] Failed to install {package}. Please install it manually.")

# Path to the existing virtual environment
venv_path = rf"C:\Users\{os.getlogin()}\p-terminal\pp-term\.env"
activate_virtualenv(venv_path)
ensure_packages_installed(required_packages)

import imageio  # For saving videos
from transformers import pipeline

sys.stdout.reconfigure(encoding='utf-8')
user_name = getpass.getuser()

def check_command_installed(command):
    """Checks if a command-line tool is installed."""
    try:
        result = subprocess.run(["where" if os.name == "nt" else "which", command],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error checking command {command}{reset}: {e}")
        return False

def input_with_timeout(prompt, timeout=10):
    """Prompts user for input with a timeout."""
    print(f"[{timestamp()}] [INFO] {prompt}", end=": ", flush=True)
    i, _, _ = select.select([sys.stdin], [], [], timeout)
    if i:
        return sys.stdin.readline().strip()
    else:
        return None  # Timeout reached

def type_out_text(text, delay=0.05):
    """Types text out slowly."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_video_from_huggingface(prompt, video_pipeline):
    """Generates a video based on user prompt using Wan-AI's model."""
    print(f"[{timestamp()}] [INFO] {cyan}Generating video for prompt: {prompt}{reset}")
    video_output = video_pipeline(prompt)
    return video_output

def save_video(video_frames, output_path="output.mp4", fps=8):
    """Saves generated video frames as MP4."""
    print(f"[{timestamp()}] [INFO] {green}Saving video to {output_path}{reset}")
    imageio.mimwrite(output_path, video_frames, fps=fps, quality=8)
    print(f"[{timestamp()}] [PASS] {green}Video saved successfully.{reset}")

def main():
    """Main function."""
    if check_command_installed("huggingface"):
        print(f"[{timestamp()}] [PASS] {green}Huggingface CLI is installed.{reset}")
        video_pipeline = pipeline("text-to-video", model="Wan-AI/Wan2.1-T2V-14B")

        while True:
            user_input = input("\nEnter a prompt (or 'exit' to quit): ")
            if user_input.lower() == "exit":
                print(f"[{timestamp()}] [INFO] Exiting program...")
                break

            video_frames = get_video_from_huggingface(user_input, video_pipeline)

            if isinstance(video_frames, list):
                save_video(video_frames, "output.mp4")
            else:
                print(f"[{timestamp()}] [ERROR] {yellow}Unexpected video output format: {type(video_frames)}{reset}")
    else:
        print(f"[{timestamp()}] [ERROR] {red}Huggingface CLI is not installed. Please install it to proceed.{reset}")
        sys.exit(1)

if __name__ == "__main__":
    main()
