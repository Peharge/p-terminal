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
import logging
from datetime import datetime

now = datetime.now()

required_packages = [
    "requests", "ollama", "transformers", "numpy", "pandas", "python-dotenv", "beautifulsoup4",
    "PyQt6", "PyQt6-sip", "PyQt6-Charts", "PyQt6-WebEngine", "PyQt6-Charts", "keyboard", "pyreadline3",
    "requests", "psutil", "speedtest-cli", "colorama", "pyperclip", "termcolor", "docker", "flask", "rich",
    "typer", "click", "blessed", "prompt-toolkit", "tqdm", "watchdog", "fire", "torch", "torchvision", "torchaudio",
    "tensorflow", "tf-nightly", "notebook", "jupyterlab", "jax", "transformers", "chardet", "plotly"
]


def activate_virtualenv(venv_path):
    """Aktiviert eine bestehende virtuelle Umgebung."""
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path,
                                                                                                          "bin",
                                                                                                          "activate")

    if not os.path.exists(activate_script):
        print(f"[{now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] [ERROR] ❌ Virtual environment not found at {venv_path}.")
        sys.exit(1)

    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"[{now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] [INFO] Virtual environment {venv_path} activated.")


def ensure_packages_installed(packages: list[str]) -> None:
    """
    Stellt sicher, dass die angegebenen Python-Pakete installiert werden.

    Installiert nur fehlende Pakete. Leise, schnell und robust.
    """

    logging.basicConfig(level=logging.INFO, format='%(message)s')

    missing = [pkg for pkg in packages if importlib.util.find_spec(pkg) is None]

    if not missing:
        logging.info(f"[{now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] [PASS] ✅ All required packages are already installed.")
        return

    logging.info(f"[{now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] [INFO] Installing missing packages: {', '.join(missing)}")

    try:
        subprocess.run(
            [
                sys.executable, "-m", "pip", "install", "--quiet", "--disable-pip-version-check",
                *missing
            ],
            check=True
        )
        logging.info(f"[{now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] [PASS] ✅ Missing packages installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"[{now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] [ERROR] ❌ Failed to install required packages.")
        logging.debug(f"[{now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] [INFO] Error details: {e}")


# Virtuelle Umgebung aktivieren und Pakete sicherstellen
venv_path = f"C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\.env"
activate_virtualenv(venv_path)
ensure_packages_installed(required_packages)
