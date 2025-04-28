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

required_packages = [
    "requests", "ollama", "transformers", "numpy", "pandas", "python-dotenv", "beautifulsoup4",
    "PyQt6", "PyQt6-sip", "PyQt6-Charts", "PyQt6-WebEngine", "PyQt6-Charts", "keyboard", "pyreadline3",
    "requests", "psutil", "speedtest-cli", "colorama", "pyperclip", "termcolor", "docker", "flask"
]


def activate_virtualenv(venv_path):
    """Aktiviert eine bestehende virtuelle Umgebung."""
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path,
                                                                                                          "bin",
                                                                                                          "activate")

    if not os.path.exists(activate_script):
        print(f"❌ Error: Virtual environment not found at {venv_path}.")
        sys.exit(1)

    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"Virtual environment {venv_path} activated.")


def ensure_packages_installed(packages: list[str]) -> None:
    """
    Ensures that the specified Python packages are installed.

    Installs only missing packages. Silent, fast, and robust.
    """
    # Configure logging to exclude log level name (e.g. [INFO])
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    missing = [pkg for pkg in packages if importlib.util.find_spec(pkg) is None]

    if not missing:
        logging.info("✅ All required packages are already installed.")
        return

    logging.info(f"Installing missing packages: {', '.join(missing)}")

    try:
        subprocess.run(
            [
                sys.executable, "-m", "pip", "install", "--quiet", "--disable-pip-version-check",
                *missing
            ],
            check=True
        )
        logging.info("✅ Missing packages installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error("❌ Failed to install required packages.")
        logging.debug(f"Error details: {e}")


# Virtuelle Umgebung aktivieren und Pakete sicherstellen
venv_path = f"C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\.env"
activate_virtualenv(venv_path)
ensure_packages_installed(required_packages)

from cgitb import strong
from dotenv import load_dotenv
from subprocess import run

import readline
import ctypes
import shlex
import logging
import os
import getpass
import subprocess
import logging
import shutil
import requests
from bs4 import BeautifulSoup
import os
import sys
import datetime
import socket
import platform
import webbrowser
import random
import shutil
import zipfile
import requests
import psutil
import pyperclip
import ctypes
import subprocess
import speedtest
import colorama
from colorama import Fore, Style, Back
import time
import ollama
from termcolor import colored
import venv
import selectors
import signal
import logging
import subprocess
import shutil
import shlex
import time
import logging
from typing import Union, List, Optional
import json

colorama.init()

DEFAULT_ENV_DIR = os.path.join("p-terminal", "pp-term", ".env")
DEFAULT_PYTHON_EXECUTABLE = os.path.join(DEFAULT_ENV_DIR, "Scripts", "python.exe")

# Globales Theme
current_theme = "dark"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

user_name = getpass.getuser()

sys.stdout.reconfigure(encoding='utf-8')

# Farbcodes definieren (kleingeschrieben)
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

def loading_bar(text: str = "Processing", duration: int = 3, color: str = "") -> None:

    print(f"{color}{text} ", end="", flush=True)
    for _ in range(duration):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(Style.RESET_ALL)

def print_banner():

    print("✅ All tasks were completed successfully!")

    print(f"""
{blue}██████╗ ██████╗{reset}{white}    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     {reset}
{blue}██╔══██╗██╔══██╗{reset}{white}   ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     {reset}
{blue}██████╔╝██████╔╝{reset}{white}█████╗██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     {reset}
{blue}██╔═══╝ ██╔═══╝ {reset}{white}╚════╝██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     {reset}
{blue}██║     ██║     {reset}{white}      ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗{reset}
{blue}╚═╝     ╚═╝     {reset}{white}      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝{reset}
""")
    print(f"""A warm welcome, {blue}{user_name}{reset}, to Peharge Python Terminal!
Developed by Peharge and JK (Peharge Projects 2025)
Thank you so much for using PP-Terminal. We truly appreciate your support ❤️""")

    print(f"""
{blue}P-Terminal Version{reset}: 1.1
{blue}PP-Terminal Version{reset}: 3
{blue}Peharge C compiler Version{reset}: 3
{blue}Peharge C++ compiler Version{reset}: 3
{blue}P-Terminal License{reset}: MIT
    """)

    # Funktion zur Anzeige der 16 Farbpaletten ohne Abstände und Zahlen
    def show_color_palette():
        for i in range(8):
            print(f"\033[48;5;{i}m  \033[0m", end="")  # Farben ohne Zahlen und ohne Abstände

        print()  # Zeilenumbruch nach der ersten Reihe

        # Anzeige der helleren Farben (8-15) ohne Abstände und Zahlen
        for i in range(8, 16):
            print(f"\033[48;5;{i}m  \033[0m", end="")

        print()  # Noch ein Zeilenumbruch am Ende

    # Aufruf der Funktion, um die Farbpalette zu zeigen
    show_color_palette()


def set_python_path():
    """Setzt PYTHON_PATH basierend auf dem gefundenen Environment."""
    active_env = find_active_env()

    python_executable = os.path.join(active_env, "Scripts", "python.exe")

    if not os.path.exists(python_executable):
        # Fallback auf default
        python_executable = os.path.abspath(DEFAULT_PYTHON_EXECUTABLE)

    os.environ["PYTHON_PATH"] = python_executable


def run_command(command, shell=False, cwd=None, extra_env=None):
    """
    Führt einen externen Befehl aus und leitet stdout/stderr interaktiv ans Terminal weiter.

    Args:
        command (str | List[str]): Der auszuführende Befehl.
        shell (bool): Wenn True, über die Shell ausführen und direkte Weiterleitung an stdout/stderr.
        cwd (str | None): Arbeitsverzeichnis.
        extra_env (dict | None): Zusätzliche Umgebungsvariablen.

    Returns:
        int: Exit-Code des Prozesses.
    """

    # 1) Aktuelles Virtual Environment ermitteln (Pfad und optionale Env-Variablen)
    active = find_active_env()
    # Erwarte entweder ein Tuple(path, env_dict) oder nur den Pfad als String
    if isinstance(active, tuple) and len(active) == 2 and isinstance(active[1], dict):
        active_env, venv_env = active
    else:
        active_env = active
        venv_env = {}

    # Unter Windows nutzen wir python.exe, sonst python
    python_name = "python.exe" if os.name == "nt" else "python"
    python_exe = os.path.join(
        active_env,
        "Scripts" if os.name == "nt" else "bin",
        python_name
    )

    # 2) command in Liste umwandeln (nur wenn shell=False und command ist str)
    if isinstance(command, str) and not shell:
        command = shlex.split(command, posix=(os.name != "nt"))

    # 3) pip- und python-Wrapper
    if isinstance(command, list) and command:
        base = os.path.basename(command[0]).lower()
        if base == "pip" or base.startswith("pip"):
            command = [python_exe, "-m", "pip"] + command[1:]
        elif base == "python" or base.startswith("python"):
            command = [python_exe] + command[1:]

    # 4) Umgebung zusammenbauen: zuerst das Venv-Env, dann System-Env, dann extra_env
    env = {}
    env.update(venv_env)
    env.update(os.environ)
    # Setze VIRTUAL_ENV und passe PATH an, falls nicht bereits gesetzt
    env.setdefault("VIRTUAL_ENV", active_env)
    venv_bin = os.path.join(active_env, "Scripts" if os.name == "nt" else "bin")
    # Pfad voranstellen
    original_path = env.get("PATH", "")
    env["PATH"] = venv_bin + os.pathsep + original_path
    if extra_env:
        env.update(extra_env)

    # 5) Wenn shell=True: einfache Ausführung mit direktem Stream-Passing
    if shell:
        proc = subprocess.Popen(
            command,
            shell=True,
            cwd=cwd,
            env=env,
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr,
            text=True
        )
        try:
            return proc.wait()
        except KeyboardInterrupt:
            proc.send_signal(signal.SIGINT)
            return proc.wait()

    # 6) Ansonsten: non-shell mit PIPEs und selectors für Zeilen-Output
    proc = subprocess.Popen(
        command,
        shell=False,
        cwd=cwd,
        env=env,
        stdin=sys.stdin,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,  # Zeilenweises Buffering
        text=True
    )

    sel = selectors.DefaultSelector()
    sel.register(proc.stdout, selectors.EVENT_READ)
    sel.register(proc.stderr, selectors.EVENT_READ)

    # SIGINT sauber weiterleiten
    def _handle_sigint(signum, frame):
        proc.send_signal(signal.SIGINT)

    old_handler = signal.signal(signal.SIGINT, _handle_sigint)

    try:
        # Loop, bis Prozess fertig und alle Streams EOF
        while True:
            events = sel.select(timeout=0.1)
            for key, _ in events:
                line = key.fileobj.readline()
                if not line:
                    sel.unregister(key.fileobj)
                    continue
                if key.fileobj is proc.stdout:
                    print(line, end='', flush=True)
                else:
                    print(line, end='', file=sys.stderr, flush=True)

            if proc.poll() is not None and not sel.get_map():
                break
    finally:
        signal.signal(signal.SIGINT, old_handler)
        sel.close()
        proc.wait()

    return proc.returncode


def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"Directory not found: {path}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)


def handle_special_commands(user_input):
    import datetime
    import socket
    import platform
    import webbrowser
    import random
    import requests
    import shlex
    import logging

    user_input = user_input.strip()

    # Lade Umgebungsvariablen
    load_dotenv(dotenv_path=f"C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\.env")
    python_path = f"C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\.env\\Scripts\\python.exe"

    # Spezielle Scripts
    commands = {
        "mavis env install": "mavis-install\\install-info-mavis-4.py",
        "install mavis env": "mavis-install\\install-info-mavis-4.py",
        "install mavis3": "mavis-install\\install-info-mavis-4.py", # new
        "install mavis3.3": "mavis-install\\install-info-mavis-4.py", # new
        "install mavis4": "mavis-install\\install-info-mavis-4.py", # new
        "install mavis4.3": "mavis-install\\install-info-mavis-4.py", # new
        "mavis env update": "mavis-install\\install-info-mavis-4.py",
        "update mavis env": "mavis-install\\install-info-mavis-4.py",
        "mavis update": "mavis-update\\update-mavis-repository-windows.py",
        "update mavis": "mavis-update\\update-mavis-repository-windows.py",
        "security": "security\\security_check-mavis-4.py",
        "p-terminal security": "security\\security_check-mavis-4.py",
        "securitycheck": "security\\security_check-mavis-4.py",
        "info": "pp-commands\\info.py",
        "mavis info": "pp-commands\\info.py",
        "info mavis": "pp-commands\\info.py",
        "p-term info": "pp-commands\\info.py",
        "info p-term": "pp-commands\\info.py",
        "neofetch": "pp-commands\\neofetch.py",
        "fastfetch": "pp-commands\\neofetch.py", # new
        "screenfetch": "pp-commands\\neofetch.py", # new
        "jupyter": "mavis-run-jup\\run-jup.py",
        "run jupyter": "mavis-run-jup\\run-jup.py",
        "run ju": "mavis-run-jup\\run-jup.py", # new
        "run mavis-4": "pp-commands\\run-mavis-4.py", # new
        "run mavis-4-3": "pp-commands\\run-mavis-4-3.py", # new
        "run mavis-4-fast": "mavis-4-main.py",  # new
        "run mavis-4-3-fast": "mavis-4-3-main.py",  # new
        "run mavis-launcher-4": "pp-commands\\run-launcher-4.py",  # new
        "run ollama mavis-4": "mavis-install\\install-ollama-mavis-4.py",  # new
        "install ollama mavis-4": "mavis-install\\install-ollama-mavis-4.py",  # new
        "change models mavis-4": "mavis-install\\install-ollama-mavis-4.py",  # new
        "change models": "mavis-install\\install-ollama-mavis-4.py",  # new
        "grafana": "mavis-run-grafana\\run-grafana.py",
        "run grafana": "mavis-run-grafana\\run-grafana.py",
        "install grafana": "mavis-run-grafana\\run-grafana.py",
        "account": "mavis-account\\account.py",
        "run deepseek-r1:1.5b": "pp-commands\\deepseek-r1-1-5b.py",
        "run deepseek-r1:7b": "pp-commands\\deepseek-r1-7b.py",
        "run deepseek-r1:8b": "pp-commands\\deepseek-r1-8b.py",
        "run deepseek-r1:14b": "pp-commands\\deepseek-r1-14b.py",
        "run deepseek-r1:32b": "pp-commands\\deepseek-r1-32b.py",
        "run deepseek-r1:70b": "pp-commands\\deepseek-r1-70b.py",
        "run deepseek-r1:671b": "pp-commands\\deepseek-r1-671b.py",
        "run deepscaler": "pp-commands\\deepscaler.py",
        "run llama3.1:8b": "pp-commands\\llama-3-1-8b.py",
        "run llama3.1:70b": "pp-commands\\llama-3-1-70b.py",
        "run llama3.1:405": "pp-commands\\llama-3-1-405b.py",
        "run llama3.2:1b": "pp-commands\\llama-3-2-1b.py",
        "run llama3.2:3b": "pp-commands\\llama-3-2-3b.py",
        "run llama3.3": "pp-commands\\llama-3-3.py",
        "run llama3:8b": "pp-commands\\llama-3-8b.py",
        "run llama3:70b": "pp-commands\\llama-3-70b.py",
        "run mistral": "pp-commands\\mistral.py",
        "run mistral-large": "pp-commands\\mistral-large.py", #new
        "run mistral-nemo": "pp-commands\\mistral-nemo.py", #new
        "run mistral-openorca": "pp-commands\\mistral-openorca.py", #new
        "run mistral-small:22b": "pp-commands\\mistral-small-22b.py", #new
        "run mistral-small:24b": "pp-commands\\mistral-small-24b.py", #new
        "run phi4": "pp-commands\\phi-4.py",
        "run qwen2.5:0.5b": "pp-commands\\qwen-2-5-0.5b.py",
        "run qwen2.5:1.5b": "pp-commands\\qwen-2-5-1.5b.py",
        "run qwen2.5:3b": "pp-commands\\qwen-2-5-3b.py",
        "run qwen2.5:7b": "pp-commands\\qwen-2-5-7b.py",
        "run qwen2.5:14b": "pp-commands\\qwen-2-5-14b.py",
        "run qwen2.5:32b": "pp-commands\\qwen-2-5-32b.py",
        "run qwen2.5:72b": "pp-commands\\qwen-2-5-72b.py",
        "run qwen2.5-coder:0.5b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:1.5b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:3b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:7b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:14b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "run qwen2.5-coder:32b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "run gemma3:1b": "pp-commands\\gemma-3-1b.py", # new
        "run gemma3:4b": "pp-commands\\gemma-3-4b.py", # new
        "run gemma3:12b": "pp-commands\\gemma-3-12b.py", # new
        "run gemma3:27b": "pp-commands\\gemma-3-27b.py", # new
        "run qwq": "pp-commands\\qwq.py", # new
        "run command-a": "pp-commands\\command-a.py", #new
        "run phi4-mini": "pp-commands\\phi-4-mini.py", #new
        "run granite3.2:8b": "pp-commands\\granite-3-2-8b.py", # new
        "run granite3.2:2b": "pp-commands\\granite-3-2-2b.py", # new
        "run granite3.2-vision:2b": "pp-commands\\granite-3-2-2b-vision.py", # new
        "run qwen-2-5-omni:7b": "pp-commands\\qwen-2-5-omni-7b.py",  # new
        "run qvq:72b": "pp-commands\\qvq-72b.py",  # new
        "run qwen-2-5-vl:32b": "pp-commands\\qwen-2-5-vl-32b.py",  # new
        "run qwen-2-5-vl:72b": "pp-commands\\qwen-2-5-vl-72b.py",  # new
        "run llama-4-maverick:17b": "pp-commands\\llama-4-maverick-17b.py",  # new
        "run llama-4-scout:17b": "pp-commands\\llama-4-scout-17b.py",  # new
        "run deepcoder:1.5b": "pp-commands\\deepcoder-1-5b.py",  # new
        "run deepcoder:14b": "pp-commands\\deepcoder-14b.py", # new
        "run mistral-small3.1": "pp-commands\\mistral-small-3-1.py",  # new
        "install deepseek-r1:1.5b": "pp-commands\\deepseek-r1-1-5b.py",
        "install deepseek-r1:7b": "pp-commands\\deepseek-r1-7b.py",
        "install deepseek-r1:8b": "pp-commands\\deepseek-r1-8b.py",
        "install deepseek-r1:14b": "pp-commands\\deepseek-r1-14b.py",
        "install deepseek-r1:32b": "pp-commands\\deepseek-r1-32b.py",
        "install deepseek-r1:70b": "pp-commands\\deepseek-r1-70b.py",
        "install deepseek-r1:671b": "pp-commands\\deepseek-r1-671b.py",
        "install deepscaler": "pp-commands\\deepscaler.py",
        "install llama3.1:8b": "pp-commands\\llama-3-1-8b.py",
        "install llama3.1:70b": "pp-commands\\llama-3-1-70b.py",
        "install llama3.1:405": "pp-commands\\llama-3-1-405b.py",
        "install llama3.2:1b": "pp-commands\\llama-3-2-1b.py",
        "install llama3.2:3b": "pp-commands\\llama-3-2-3b.py",
        "install llama3.3": "pp-commands\\llama-3-3.py",
        "install llama3:8b": "pp-commands\\llama-3-8b.py",
        "install llama3:70b": "pp-commands\\llama-3-70b.py",
        "install mistral": "pp-commands\\mistral.py",
        "install mistral-large": "pp-commands\\mistral-large.py", #new
        "install mistral-nemo": "pp-commands\\mistral-nemo.py", #new
        "install mistral-openorca": "pp-commands\\mistral-openorca.py", #new
        "install mistral-small:22b": "pp-commands\\mistral-small-22b.py", #new
        "install mistral-small:24b": "pp-commands\\mistral-small-24b.py", #new
        "install phi4": "pp-commands\\phi-4.py",
        "install qwen2.5:0.5b": "pp-commands\\qwen-2-5-0.5b.py",
        "install qwen2.5:1.5b": "pp-commands\\qwen-2-5-1.5b.py",
        "install qwen2.5:3b": "pp-commands\\qwen-2-5-3b.py",
        "install qwen2.5:7b": "pp-commands\\qwen-2-5-7b.py",
        "install qwen2.5:14b": "pp-commands\\qwen-2-5-14b.py",
        "install qwen2.5:32b": "pp-commands\\qwen-2-5-32b.py",
        "install qwen2.5:72b": "pp-commands\\qwen-2-5-72b.py",
        "install qwen2.5-coder:0.5b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:1.5b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:3b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:7b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:14b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "install qwen2.5-coder:32b": "pp-commands\\qwen-2-5-coder-0.5b.py",
        "install gemma3:1b": "pp-commands\\gemma-3-1b.py", # new
        "install gemma3:4b": "pp-commands\\gemma-3-4b.py", # new
        "install gemma3:12b": "pp-commands\\gemma-3-12b.py", # new
        "install gemma3:27b": "pp-commands\\gemma-3-27b.py", # new
        "install qwq": "pp-commands\\qwq.py", # new
        "install command-a": "pp-commands\\command-a.py", # new
        "install phi4-mini": "pp-commands\\phi-4-mini.py", # new
        "install granite3.2:8b": "pp-commands\\granite-3-2-8b.py", # new
        "install granite3.2:2b": "pp-commands\\granite-3-2-2b.py", # new
        "install granite3.2-vision:2b": "pp-commands\\granite-3-2-2b-vision.py", # new
        "install qwen-2-5-omni:7b": "pp-commands\\qwen-2-5-omni-7b.py",  # new
        "install qvq:72b": "pp-commands\\qvq-72b.py",  # new
        "install qwen-2-5-vl:32b": "pp-commands\\qwen-2-5-vl-32b.py",  # new
        "install qwen-2-5-vl:72b": "pp-commands\\qwen-2-5-vl-72b.py",  # new
        "install llama-4-maverick:17b": "pp-commands\\llama-4-maverick-17b.py",  # new
        "install llama-4-scout:17b": "pp-commands\\llama-4-scout-17b.py",  # new
        "install deepcoder:1.5b": "pp-commands\\deepcoder-1-5b.py",  # new
        "install deepcoder:14b": "pp-commands\\deepcoder-14b.py",  # new
        "install mistral-small3.1": "pp-commands\\mistral-small-3-1.py",  # new
        "help": "pp-commands\\help.py",
        "image generation": "pp-commands\\stable-diffusion-3-5-large-turbo.py",
        "video generation": "pp-commands\\wan-2-1-t2v-14b.py",
        "run mavis": "mavis-installer-3-main-windows.py",
        "p run all": "pp-commands\\p-run-all.py", # new
        "p htop": "pp-commands\\p-htop.py", # new
        "p run gemma3": "pp-commands\\p-gemma-3.py", # new
        "p run deepseek-r1": "pp-commands\\p-deepseek-r1.py", # new
        "p run qwen2.5": "pp-commands\\p-qwen-2-5.py", # new
        "p run qwen2.5-coder": "pp-commands\\p-qwen-2-5-coder.py", # new
        "p python frameworks": "pp-commands\\p-python-frameworks.py", # new
        "p pip list": "pp-commands\\p-python-frameworks.py", # new
        "p pip ls": "pp-commands\\p-python-frameworks.py",  # new
        "p git ls": "pp-commands\\p-git.py", # new
        "p git": "pp-commands\\p-git.py",  # new
        "p ls": "pp-commands\\p-ls.py", # new
        "models": "pp-commands\\models-ls.py",  # new
        "models ls": "pp-commands\\models-ls.py",  # new
        "p models": "pp-commands\\p-models-ls.py",  # new
        "p models ls": "pp-commands\\p-models-ls.py",  # new
        "p github mavis": "pp-commands\\p-github-mavis.py",  # new
        "p github commits": "pp-commands\\p-github-commits.py",  # new
        "p github issues": "pp-commands\\p-github-issues.py",  # new
        "p github peharge": "pp-commands\\p-github-peharge.py",  # new
        "p github pulls": "pp-commands\\p-github-pulls.py",  # new
        "p github readme": "pp-commands\\p-github-readme.py",  # new
        "p github releases": "pp-commands\\p-github-releases.py",  # new
        "p github": "pp-commands\\p-github.py",  # new
        "p p-terminal": "pp-commands\\p-p-terminal.py",  # new
        "p p-terminal.com": "pp-commands\\p-p-terminal-com.py",  # new
        "p search": "pp-commands\\p-search.py",  # new
        "p google": "pp-commands\\p-google.py",  # new
        "p ollama": "pp-commands\\p-ollama.py",  # new
        "p huggingface": "pp-commands\\p-huggingface.py",  # new
        "p github.com": "pp-commands\\p-github.py",  # new
        "p kali.com": "pp-commands\\p-kali.py",  # new
        "p mint.com": "pp-commands\\p-mint.py",  # new
        "p monai.com": "pp-commands\\p-monai.py",  # new
        "p monai-github.com": "pp-commands\\p-monai-git.py",  # new
        "p python.com": "pp-commands\\p-python.py",  # new
        "p pytorch.com": "pp-commands\\p-pytorch.py",  # new
        "p pytorch-github.com": "pp-commands\\p-pytorch-git.py",  # new
        "p ubuntu.com": "pp-commands\\p-ubuntu.py",  # new
        "p 3dslicer-github.com": "pp-commands\\p-3dslicer-git.py",  # new
        "p 3dslicer.com": "pp-commands\\p-3dslicer-web.py",  # new
        "p arch.com": "pp-commands\\p-arch.py",  # new
        "p debian.com": "pp-commands\\p-debian.py",  # new
        "p google.com": "pp-commands\\p-google.py",  # new
        "p ollama.com": "pp-commands\\p-ollama.py",  # new
        "p huggingface.com": "pp-commands\\p-huggingface.py",  # new
        "p mavis": "pp-commands\\p-mavis-git.py",  # new
        "p mavis.com": "pp-commands\\p-mavis.py",  # new
        "p simon": "pp-commands\\p-simon.py",  # new
        "p simon.com": "pp-commands\\p-simon-git.py", # new
        "wsl info": "pp-commands\\wsl-info.py",  # new
        "p wsl": "pp-commands\\p-wsl.py", # new
        "p pip": "pp-commands\\p-pip.py",  # new
        "p ubuntu": "pp-commands\\p-wsl-ubuntu.py",  # new
        "p debian": "pp-commands\\p-wsl-debian.py",  # new
        "p kali": "pp-commands\\p-wsl-kali.py",  # new
        "p arch": "pp-commands\\p-wsl-arch.py",  # new
        "p mint": "pp-commands\\p-wsl-mint.py",  # new
        "p opensuse": "pp-commands\\p-wsl-opensuse.py",  # new
        "p fedora": "pp-commands\\p-wsl-fedora.py",  # new
        "p redhat": "pp-commands\\p-wsl-redhat.py",  # new
        "p alpine": "pp-commands\\p-wsl-alpine.py",  # new
        "p clear": "pp-commands\\p-wsl-clearlinux.py",  # new
        "p oracle": "pp-commands\\p-wsl-oracle.py",  # new
        "p pengwin": "pp-commands\\p-wsl-pengwin.py",  # new
        "p sles": "pp-commands\\p-wsl-sles.py",  # new
        "p neofetch": "pp-commands\\p-neofetch.py",  # new
        "p fastfetch": "pp-commands\\p-neofetch.py",  # new
        "p screenfetch": "pp-commands\\p-neofetch.py",  # new
        "install 3d-slicer": "run\\simon\\3d-slicer\\install-3d-slicer.py", # new
        "run 3d-slicer": "run\\simon\\3d-slicer\\run-3d-slicer.py",  # new
        "install simon": "run\\simon\\install-simon-1.py",  # new
        "run simon": "mavis-run-jup\\run-jup.py",  # new
        "jupyter --version": "pp-commands\\jupyter-version.py", # new
        "grafana --version": "pp-commands\\grafana-version.py",  # new
        "3d-slicer --version": "pp-commands\\3d-slicer-version.py",  # new
        "doctor": "pp-commands\\doctor.py", # new
        "fun": "pp-commands\\fun.py",  # new
        "fun aafire": "pp-commands\\fun-aafire.py",  # new
        "fun cmatrix": "pp-commands\\fun-cmatrix.py",  # new
        "fun cow": "pp-commands\\fun-cow.py",  # new
        "fun dragon": "pp-commands\\fun-dragon.py",  # new
        "fun figlet": "pp-commands\\fun-figlet.py",  # new
        "fun fortune": "pp-commands\\fun-fortune.py",  # new
        "fun install": "pp-commands\\fun-install.py",  # new
        "install fun": "pp-commands\\fun-install.py",  # new
        "fun ponysay": "pp-commands\\fun-ponysay.py",  # new
        "fun telnet": "pp-commands\\fun-telnet.py",  # new
        "fun train": "pp-commands\\fun-train.py",  # new
        "fun train a": "pp-commands\\fun-train-a.py",  # new
        "fun train F": "pp-commands\\fun-train-F.py",  # new
        "fun train l": "pp-commands\\fun-train-l.py",  # new
        "fun train S": "pp-commands\\fun-train-S.py",  # new
        "fun train t": "pp-commands\\fun-train-t.py"  # new
    }

    # Custom command launcher
    if user_input in commands:
        script_path = f"C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\{commands[user_input]}"
        if not user_input.endswith(".bat"):
            run([python_path, script_path], shell=True)
        else:
            run([script_path], shell=True)
        return True

    # Built-in Commands Erweiterung:
    if user_input.lower() in ["cls", "clear"]:
        os.system("cls" if os.name == "nt" else "clear")
        return True

    if user_input.startswith("cd "):
        path = user_input[3:].strip()
        change_directory(path)
        return True

    if user_input.lower() in ["dir", "ls"]:
        run_command("dir" if os.name == "nt" else "ls -la", shell=True)
        return True

    if user_input.startswith("mkdir "):
        os.makedirs(user_input[6:].strip(), exist_ok=True)
        return True

    if user_input.startswith("rmdir "):
        try:
            os.rmdir(user_input[6:].strip())
        except Exception as e:
            print(f"{red}Error{reset}: {str(e)}", file=sys.stderr)
        return True

    if user_input.startswith(("del ", "rm ")):
        try:
            os.remove(user_input.split(maxsplit=1)[1].strip())
        except Exception as e:
            print(f"{red}Error{reset}: {str(e)}", file=sys.stderr)
        return True

    if user_input.startswith("echo "):
        print(user_input[5:].strip())
        return True

    '''if "=" in user_input:
        var, value = map(str.strip, user_input.split("=", 1))
        os.environ[var] = value
        print(f"{blue}Environment variable set{reset}: {var}={value}")
        return True
    '''

    if user_input.startswith(("type ", "cat ")):
        try:
            with open(user_input.split(maxsplit=1)[1].strip(), "r", encoding="utf-8") as f:
                print(f.read())
        except Exception as e:
            print(f"{red}Error{reset}: {str(e)}", file=sys.stderr)
        return True

    if user_input.lower() == "exit":
        print(f"{yellow}Exiting PP-Terminal... Goodbye {user_name}!{reset}")
        sys.exit(0)

    # Zusätzliche Luxus-Funktionen:
    if user_input.lower() == "whoami":
        print(user_name)
        return True

    if user_input.lower() == "hostname":
        print(socket.gethostname())
        return True

    if user_input.lower() == "ip":
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f"{blue}IP Address{reset}: {ip_address}")
        except:
            print(f"{red}Could not retrieve IP address{reset}")
        return True

    if user_input.lower() == "os":
        print(f"{blue}OS{reset}: {platform.system()} {platform.release()}")
        return True

    if user_input.lower() == "time":
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"))
        return True

    if user_input.lower() == "date":
        today = datetime.date.today()
        print(today.strftime("%Y-%m-%d"))
        return True

    if user_input.lower() == "weather":
        get_weather()
        return True

    if user_input.startswith("open "):
        site = user_input[5:].strip()
        if not site.startswith("http"):
            site = "https://" + site
        webbrowser.open(site)
        print(f"{blue}Opening {site}...{reset}")
        return True

    if user_input.lower() == "fortune":
        fortunes = [
            "You will code something amazing today!",
            "Trust your debugging skills!",
            "Error 404: Worries not found!",
            "Take a coffee break ☕️",
            "One commit a day keeps the bugs away!"
        ]
        print(random.choice(fortunes))
        return True

    if user_input.lower() == "history":
        try:
            hist_len = readline.get_current_history_length()
            for i in range(1, hist_len + 1):
                print(f"{i}: {readline.get_history_item(i)}")
        except Exception as e:
            print(f"{red}Error reading history{reset}: {str(e)}")
        return True

    if user_input.startswith("search "):
        try:
            # Split the input into command, filename, and keyword
            parts = user_input.split(maxsplit=2)
            if len(parts) < 3:
                print("Usage: search <filename> <keyword>")
                return True

            _, filename, keyword = parts

            # Open the file with UTF-8 encoding
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()

            # Search for the keyword in each line, case insensitive
            matches = []
            for i, line in enumerate(lines, start=1):
                if keyword.lower() in line.lower():
                    matches.append(f"Line {i}: {line.rstrip()}")

            # Output the results or a corresponding message if no matches are found
            if matches:
                print("\n".join(matches))
            else:
                print("No matches found.")

        except FileNotFoundError:
            print(f"{red}File not found{reset}: {filename}")
        except PermissionError:
            print(f"{red}No permission to read{reset}: {filename}")
        except Exception as e:
            print(f"{red}Error during search{reset}: {str(e)}")
        return True

    # Create a zip folder (optimized for Windows)
    if user_input.startswith("zip "):
        try:
            # Extract command and folder from input
            parts = user_input.split(maxsplit=1)
            if len(parts) < 2:
                print("Usage: zip <folder>")
                return True

            _, folder = parts
            # Normalize the path, especially useful on Windows
            folder_path = os.path.normpath(folder)

            # Check if the folder exists
            if not os.path.isdir(folder_path):
                print(f"{red}Error: Folder does not exist{reset}: {folder_path}")
                return True

            # Create the archive. The archive name matches the folder name without an extension.
            shutil.make_archive(folder_path, 'zip', folder_path)
            print(f"{green}Folder successfully zipped!{reset}")

        except FileNotFoundError:
            print(f"{red}Error: Folder not found{reset}: {folder_path}")
        except PermissionError:
            print(f"{red}Error: No permission to access the folder{reset}: {folder_path}")
        except Exception as e:
            print(f"{red}Error while zipping the folder{reset}: {str(e)}")
        return True

    # Unzip an archive (optimized for Windows with enhanced checks)
    if user_input.startswith("unzip "):
        try:
            # Extract command and zip file from input
            parts = user_input.split(maxsplit=1)
            if len(parts) < 2:
                print("Usage: unzip <zip_file_path>")
                return True

            _, zip_path = parts
            # Normalize the path, especially useful on Windows
            zip_path = os.path.normpath(zip_path)

            # Check if the zip file exists and is a file
            if not os.path.isfile(zip_path):
                print(f"{red}Error:{reset} File does not exist: {zip_path}")
                return True

            # Determine the target directory based on the filename without extension
            extract_dir = os.path.splitext(zip_path)[0]

            # Open and extract the zip archive
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)

            print(f"{green}Archive successfully extracted to:{reset} {extract_dir}")

        except zipfile.BadZipFile:
            print(f"{red}Error:{reset} Invalid zip archive: {zip_path}")
        except PermissionError:
            print(f"{red}Error:{reset} No permission to access the file: {zip_path}")
        except Exception as e:
            print(f"{red}Error while extracting:{reset} {str(e)}")
        return True

    # RAM and CPU status
    if user_input.lower() == "sysinfo":
        print(f"{blue}CPU Usage{reset}: {psutil.cpu_percent()}%")
        print(f"{blue}RAM Usage{reset}: {psutil.virtual_memory().percent}%")
        return True

    # Set clipboard content (improved with extended validation and error handling)
    if user_input.startswith("clip set "):
        try:
            # Extract the text to be copied, removing leading and trailing whitespace
            text = user_input[len("clip set "):].strip()
            if not text:
                print("Usage: clip set <text>")
                return True

            # Copy text to clipboard
            pyperclip.copy(text)
            print(f"{green}Text successfully copied to clipboard!{reset}")
        except ImportError:
            print(
                f"{red}Error:{reset} pyperclip module is not installed. Please install it with 'pip install pyperclip'")
        except Exception as e:
            print(f"{red}Error while copying to clipboard{reset}: {str(e)}")
        return True

    # Zwischenablage lesen
    if user_input.lower() == "clip get":
        print(pyperclip.paste())
        return True

    # Ping Befehl
    if user_input.startswith("ping "):
        target = user_input.split(maxsplit=1)[1]
        os.system(f"ping {target}")
        return True

    # Papierkorb leeren
    if user_input.lower() == "emptytrash":
        try:
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000001)
            print(f"{green}Recycle Bin emptied!{reset}")
        except Exception as e:
            print(f"{red}Error emptying trash{reset}: {str(e)}")
        return True

    if user_input.lower() == "theme-ls":
        print("dark, light, hackerman, aptscience, cyberlife, ubuntu, nord, dracula, solarized_dark, gruvbox_dark, monokai, one_dark, material_dark, tokyo_night, arc_dark, ayu_mirage")
        return True

    if user_input.startswith("launch "):
        command_str = user_input[len("launch "):].strip()

        # 3. Catch empty input
        if not command_str:
            logging.error("No program specified after 'launch'.")
            return False  # Frühzeitige Rückgabe, falls kein Programmname angegeben wurde

        try:
            # Platform-spezifische Befehlsausführung
            if sys.platform == "win32":
                # Auf Windows: Verwende 'start' im Shell-Modus
                safe_cmd = f'start "" {shlex.quote(command_str)}'
                subprocess.Popen(safe_cmd, shell=True)
            else:
                # Für Unix/macOS: Parsen des Programms und der Argumente direkt
                args = shlex.split(command_str)
                subprocess.Popen(args)

            logging.info("Program launched: %s", command_str)
            return True  # Erfolgreiche Ausführung, Rückgabe True

        except FileNotFoundError:
            logging.error("Program not found: %s", command_str)
        except Exception as e:
            logging.exception("Error launching %s: %s", command_str, str(e))

        return False

    # Speedtest
    if user_input.lower() == "speedtest":
        try:
            # Loading bar while the speedtest is running
            loading_bar("Running speedtest", 5)

            # Speedtest instance
            st = speedtest.Speedtest()

            # Download and upload speeds in Mbps
            download = st.download() / 1_000_000  # Convert from bits to Mbps
            upload = st.upload() / 1_000_000  # Convert from bits to Mbps

            # Get ping (latency)
            ping = st.results.ping

            # Print out results in a cool format
            print(f"{blue}Download{reset}: {download:.2f} Mbps")
            print(f"{blue}Upload{reset}: {upload:.2f} Mbps")
            print(f"{blue}Ping{reset}: {ping} ms")

            return True

        except Exception as e:
            # If something goes wrong, show the error
            print(f"{red}Whoops, something went wrong with the speedtest{reset}: {e}")
            return False

    # Prozessliste
    if user_input.lower() == "ps":
        for proc in psutil.process_iter(['pid', 'name']):
            print(f"PID {proc.info['pid']}: {proc.info['name']}")
        return True

    if user_input.startswith("kill "):
        try:
            pid = int(user_input.split(maxsplit=1)[1])
            p = psutil.Process(pid)
            p.terminate()
            print(f"{green}Killed process {pid}{reset}")
        except Exception as e:
            print(f"{red}Error killing process{reset}: {str(e)}")
        return True

    # Datei herunterladen
    if user_input.startswith("download "):
        from pathlib import Path
        import requests

        try:
            # Extract URL from input
            _, url = user_input.split(maxsplit=1)
            file_name = Path(url).name

            # Download with progress feedback
            loading_bar(f"Downloading {file_name}", 4)
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()

            # Write content in chunks
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)

            print(f"{green}Downloaded {file_name}{reset}")
        except requests.HTTPError as http_err:
            print(f"{red}HTTP error during download{reset}: {http_err}")
        except requests.RequestException as req_err:
            print(f"{red}Request error during download{reset}: {req_err}")
        except Exception as err:
            print(f"{red}Unexpected error{reset}: {err}")
        return True

    # CPU Temperatur
    if user_input.lower() == "cputemp":
        print(f"{yellow}Feature not fully supported on Windows without third party libs!{reset}")
        return True

    # Chuck Norris Joke
    if user_input.lower() == "chucknorris":
        try:
            joke = requests.get("https://api.chucknorris.io/jokes/random").json()['value']
            print(f"{blue}Chuck Norris says{reset}: {joke}")
        except:
            print(f"{red}Couldn't fetch Chuck Norris joke!{reset}")
        return True

    # Theme Wechsel - soon
    if user_input.startswith("theme "):
        switch_theme(user_input)
        return True

    # Temp Dateien löschen
    if user_input.lower() == "cleantemp":
        temp = os.getenv('TEMP')
        shutil.rmtree(temp, ignore_errors=True)
        print(f"{green}Temporary files cleaned!{reset}")
        return True

    # Selbst Update (Demo)
    if user_input.lower() == "selfupdate":
        print(f"{blue}Checking for updates...{reset}")
        loading_bar("Updating", 4)
        print(f"{green}PP-Terminal updated! (demo mode){reset}")
        return True

    # Directory Baumansicht
    if user_input.lower() == "tree":
        def print_tree(startpath, prefix=""):
            for item in os.listdir(startpath):
                path = os.path.join(startpath, item)
                print(prefix + "|-- " + item)
                if os.path.isdir(path):
                    print_tree(path, prefix + "|   ")
        print_tree(os.getcwd())
        return True

    # Python REPL starten
    if user_input.lower() == "py":
        print(f"{blue}Starting Python REPL. Type 'exit()' to quit.{reset}")
        import code
        code.interact(local=dict(globals(), **locals()))
        return True

    # Mini KI Antwort - soon
    if user_input.startswith("pa "):
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"{green}Ollama is installed.{reset}")
        else:
            print(f"{red}Ollama is not installed. Please install it to proceed.{reset}")

        start_ollama()
        check_ollama_update()

        question = user_input[len("pa "):]

        response = get_response_from_ollama(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    return False

import os
import json
import shutil
import subprocess

# Constants
SETTINGS_PATH = os.path.expandvars(
    r"%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
)
BACKUP_SUFFIX = ".bak"
THEMES_PATH = f'C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\themes.json'

# Predefined color schemes
COLOR_SCHEMES = {
    "dark": {
        "name": "Dark",
        "background": "#0C0C0C",
        "foreground": "#F2F2F2",
        "black": "#0C0C0C",
        "red": "#C50F1F",
        "green": "#13A10E",
        "yellow": "#C19C00",
        "blue": "#0037DA",
        "purple": "#881798",
        "cyan": "#3A96DD",
        "white": "#CCCCCC",
        "brightBlack": "#767676",
        "brightRed": "#E74856",
        "brightGreen": "#16C60C",
        "brightYellow": "#F9F1A5",
        "brightBlue": "#3B78FF",
        "brightPurple": "#B4009E",
        "brightCyan": "#61D6D6",
        "brightWhite": "#F2F2F2"
    },
    "light": {
        "name": "Light",
        "background": "#FFFFFF",
        "foreground": "#333333",
        "black": "#000000",
        "red": "#C50F1F",
        "green": "#13A10E",
        "yellow": "#C19C00",
        "blue": "#0037DA",
        "purple": "#881798",
        "cyan": "#3A96DD",
        "white": "#CCCCCC",
        "brightBlack": "#767676",
        "brightRed": "#E74856",
        "brightGreen": "#16C60C",
        "brightYellow": "#F9F1A5",
        "brightBlue": "#3B78FF",
        "brightPurple": "#B4009E",
        "brightCyan": "#61D6D6",
        "brightWhite": "#F2F2F2"
    },
    "hackerman": {
        "name": "hackerman",
        "background": "#2E3440",
        "black": "#3B4252",
        "blue": "#81A1C1",
        "brightBlack": "#4C566A",
        "brightBlue": "#81A1C1",
        "brightCyan": "#88C0D0",
        "brightGreen": "#A3BE8C",
        "brightPurple": "#B48EAD",
        "brightRed": "#BF616A",
        "brightWhite": "#E5E9F0",
        "brightYellow": "#EBCB8B",
        "cursorColor": "#FFFFFF",
        "cyan": "#88C0D0",
        "foreground": "#D8DEE9",
        "green": "#A3BE8C",
        "purple": "#B48EAD",
        "red": "#BF616A",
        "selectionBackground": "#FFFFFF",
        "white": "#E5E9F0",
        "yellow": "#EBCB8B"
    },
    "aptscience": {
        "name": "aptscience",
        "background": "#0C0C0C",
        "foreground": "#F2F2F2",
        "black": "#0C0C0C",
        "red": "#C50F1F",
        "green": "#13A10E",
        "yellow": "#C19C00",
        "blue": "#0037DA",
        "purple": "#881798",
        "cyan": "#3A96DD",
        "white": "#CCCCCC",
        "brightBlack": "#767676",
        "brightRed": "#E74856",
        "brightGreen": "#16C60C",
        "brightYellow": "#F9F1A5",
        "brightBlue": "#3B78FF",
        "brightPurple": "#B4009E",
        "brightCyan": "#61D6D6",
        "brightWhite": "#F2F2F2"
    },
    "cyberlife": {
        "name": "Cyberlife",
        "background": "#0C0C0C",
        "foreground": "#F2F2F2",
        "black": "#0C0C0C",
        "red": "#C50F1F",
        "green": "#13A10E",
        "yellow": "#C19C00",
        "blue": "#0037DA",
        "purple": "#881798",
        "cyan": "#3A96DD",
        "white": "#CCCCCC",
        "brightBlack": "#767676",
        "brightRed": "#E74856",
        "brightGreen": "#16C60C",
        "brightYellow": "#F9F1A5",
        "brightBlue": "#3B78FF",
        "brightPurple": "#B4009E",
        "brightCyan": "#61D6D6",
        "brightWhite": "#F2F2F2"
    },
    "ubuntu": {
        "name": "Ubuntu",
        "background": "#300A24",
        "foreground": "#F2F2F2",
        "black": "#300A24",
        "red": "#CE5C00",
        "green": "#8ABEB7",
        "yellow": "#F0C674",
        "blue": "#81A2BE",
        "purple": "#B294BB",
        "cyan": "#8ABEB7",
        "white": "#EEEEEC",
        "brightBlack": "#1E161B",
        "brightRed": "#FF6E67",
        "brightGreen": "#5FEBA6",
        "brightYellow": "#F4BF75",
        "brightBlue": "#8AB8FE",
        "brightPurple": "#D7A0FF",
        "brightCyan": "#BDF5F2",
        "brightWhite": "#FFFFFF",
        "cursorColor": "#000000"
    },
    "nord": {
        "name": "nord",
        "foreground": "#D8DEE9",
        "background": "#2E3440",
        "black": "#3B4252",
        "red": "#BF616A",
        "green": "#A3BE8C",
        "yellow": "#EBCB8B",
        "blue": "#81A1C1",
        "purple": "#B48EAD",
        "cyan": "#88C0D0",
        "white": "#E5E9F0",
        "brightBlack": "#4C566A",
        "brightRed": "#BF616A",
        "brightGreen": "#A3BE8C",
        "brightYellow": "#EBCB8B",
        "brightBlue": "#81A1C1",
        "brightPurple": "#B48EAD",
        "brightCyan": "#88C0D0",
        "brightWhite": "#E5E9F0"
    },
    "dracula": {
        "name": "Dracula",
        "background": "#282A36",
        "foreground": "#F8F8F2",
        "black": "#21222C",
        "red": "#FF5555",
        "green": "#50FA7B",
        "yellow": "#F1FA8C",
        "blue": "#BD93F9",
        "purple": "#FF79C6",
        "cyan": "#8BE9FD",
        "white": "#F8F8F2",
        "brightBlack": "#6272A4",
        "brightRed": "#FF6E6E",
        "brightGreen": "#69FF94",
        "brightYellow": "#FFFFA5",
        "brightBlue": "#D6ACFF",
        "brightPurple": "#FF92DF",
        "brightCyan": "#A4FFFF",
        "brightWhite": "#FFFFFF",
        "cursorColor": "#FF79C6"
    },
    "solarized_dark": {
        "name": "Solarized Dark",
        "background": "#002B36",
        "foreground": "#839496",
        "black": "#073642",
        "red": "#DC322F",
        "green": "#859900",
        "yellow": "#B58900",
        "blue": "#268BD2",
        "purple": "#D33682",
        "cyan": "#2AA198",
        "white": "#EEE8D5",
        "brightBlack": "#002B36",
        "brightRed": "#CB4B16",
        "brightGreen": "#586E75",
        "brightYellow": "#657B83",
        "brightBlue": "#839496",
        "brightPurple": "#6C71C4",
        "brightCyan": "#93A1A1",
        "brightWhite": "#FDF6E3",
        "cursorColor": "#93A1A1"
    },
    "gruvbox_dark": {
        "name": "Gruvbox Dark",
        "background": "#282828",
        "foreground": "#EBDBB2",
        "black": "#282828",
        "red": "#CC241D",
        "green": "#98971A",
        "yellow": "#D79921",
        "blue": "#458588",
        "purple": "#B16286",
        "cyan": "#689D6A",
        "white": "#A89984",
        "brightBlack": "#928374",
        "brightRed": "#FB4934",
        "brightGreen": "#B8BB26",
        "brightYellow": "#FABD2F",
        "brightBlue": "#83A598",
        "brightPurple": "#D3869B",
        "brightCyan": "#8EC07C",
        "brightWhite": "#EBDBB2",
        "cursorColor": "#FE8019"
    },
    "monokai": {
        "name": "Monokai",
        "background": "#272822",
        "foreground": "#F8F8F2",
        "black": "#272822",
        "red": "#F92672",
        "green": "#A6E22E",
        "yellow": "#F4BF75",
        "blue": "#66D9EF",
        "purple": "#AE81FF",
        "cyan": "#A1EFE4",
        "white": "#F8F8F2",
        "brightBlack": "#75715E",
        "brightRed": "#FD971F",
        "brightGreen": "#A6E22E",
        "brightYellow": "#E6DB74",
        "brightBlue": "#66D9EF",
        "brightPurple": "#AE81FF",
        "brightCyan": "#38CCD1",
        "brightWhite": "#F9F8F5",
        "cursorColor": "#F8F8F0"
    },
    "one_dark": {
        "name": "One Dark",
        "background": "#282C34",
        "foreground": "#ABB2BF",
        "black": "#282C34",
        "red": "#E06C75",
        "green": "#98C379",
        "yellow": "#E5C07B",
        "blue": "#61AFEF",
        "purple": "#C678DD",
        "cyan": "#56B6C2",
        "white": "#ABB2BF",
        "brightBlack": "#5C6370",
        "brightRed": "#E06C75",
        "brightGreen": "#98C379",
        "brightYellow": "#D19A66",
        "brightBlue": "#61AFEF",
        "brightPurple": "#C678DD",
        "brightCyan": "#56B6C2",
        "brightWhite": "#FFFFFF",
        "cursorColor": "#528BFF"
    },
    "material_dark": {
        "name": "Material Dark",
        "background": "#263238",
        "foreground": "#ECEFF1",
        "black": "#263238",
        "red": "#FF5370",
        "green": "#C3E88D",
        "yellow": "#FFCB6B",
        "blue": "#82AAFF",
        "purple": "#C792EA",
        "cyan": "#89DDFF",
        "white": "#ECEFF1",
        "brightBlack": "#546E7A",
        "brightRed": "#FF5370",
        "brightGreen": "#C3E88D",
        "brightYellow": "#FFCB6B",
        "brightBlue": "#82AAFF",
        "brightPurple": "#C792EA",
        "brightCyan": "#89DDFF",
        "brightWhite": "#FFFFFF",
        "cursorColor": "#FFCB6B"
    },
    "tokyo_night": {
        "name": "Tokyo Night",
        "background": "#1A1B26",
        "foreground": "#C0CAF5",
        "black": "#1D202F",
        "red": "#F7768E",
        "green": "#9ECE6A",
        "yellow": "#E0AF68",
        "blue": "#7AA2F7",
        "purple": "#BB9AF7",
        "cyan": "#7DCFFF",
        "white": "#A9B1D6",
        "brightBlack": "#414868",
        "brightRed": "#F7768E",
        "brightGreen": "#9ECE6A",
        "brightYellow": "#E0AF68",
        "brightBlue": "#7AA2F7",
        "brightPurple": "#BB9AF7",
        "brightCyan": "#7DCFFF",
        "brightWhite": "#C0CAF5",
        "cursorColor": "#7AA2F7"
    },
    "arc_dark": {
        "name": "Arc Dark",
        "background": "#212733",
        "foreground": "#D3DAE3",
        "black": "#212733",
        "red": "#E27878",
        "green": "#B4BE82",
        "yellow": "#E2A478",
        "blue": "#82AAFF",
        "purple": "#C792EA",
        "cyan": "#89DDFF",
        "white": "#D3DAE3",
        "brightBlack": "#4C566A",
        "brightRed": "#FF5370",
        "brightGreen": "#C3E88D",
        "brightYellow": "#FFCB6B",
        "brightBlue": "#82AAFF",
        "brightPurple": "#C792EA",
        "brightCyan": "#89DDFF",
        "brightWhite": "#ECEFF4",
        "cursorColor": "#82AAFF"
    },
    "ayu_mirage": {
        "name": "Ayu Mirage",
        "background": "#1F2430",
        "foreground": "#CBCCC6",
        "black": "#191E2A",
        "red": "#FF3333",
        "green": "#BAE67E",
        "yellow": "#FFA759",
        "blue": "#73D0FF",
        "purple": "#D4BFFF",
        "cyan": "#95E6CB",
        "white": "#C7C7C7",
        "brightBlack": "#686868",
        "brightRed": "#FF5454",
        "brightGreen": "#C2E68C",
        "brightYellow": "#FFB378",
        "brightBlue": "#80D6FF",
        "brightPurple": "#E1CFFF",
        "brightCyan": "#B4F0E0",
        "brightWhite": "#FFFFFF",
        "cursorColor": "#FFA759"
    }
}

# Load theme-specific defaults
try:
    with open(THEMES_PATH, 'r', encoding='utf-8') as f:
        THEME_DEFAULTS = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading themes.json: {e}")
    THEME_DEFAULTS = {}

def create_backup(file_path: str) -> str:
    backup_path = file_path + BACKUP_SUFFIX
    shutil.copy2(file_path, backup_path)
    print(f"Backup created at: {backup_path}")
    return backup_path

def load_settings(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_settings(file_path: str, settings: dict) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)
    print(f"Settings saved to {file_path}")

def apply_color_scheme(settings: dict, scheme_name: str) -> None:
    scheme = COLOR_SCHEMES.get(scheme_name)
    if scheme:
        settings.setdefault('schemes', [])
        settings['schemes'] = [s for s in settings['schemes'] if s.get('name') != scheme.get('name')]
        settings['schemes'].append(scheme)
        for profile in settings.get('profiles', {}).get('list', []):
            profile['colorScheme'] = scheme.get('name')
        settings['theme'] = 'dark' if 'dark' in scheme_name else 'light'
        print(f"Applied color scheme: {scheme.get('name')}")

def apply_theme_defaults(settings: dict, theme_name: str) -> None:
    defaults = THEME_DEFAULTS.get(theme_name, {}).get('defaults')
    if defaults:
        settings.setdefault('profiles', {})
        settings['profiles']['defaults'] = defaults
        print(f"Applied theme defaults for: {theme_name}")

def restart_terminal() -> None:
    subprocess.run(["wt.exe", "new-tab"], check=False)
    print("Terminal restarted with new tab.")

def switch_theme(user_input: str) -> bool:
    if not user_input.lower().startswith("theme "):
        return False

    _, choice = user_input.split(maxsplit=1)
    key = choice.lower().replace('-', '_')

    if key not in COLOR_SCHEMES and key not in THEME_DEFAULTS:
        print(f"Unknown theme '{choice}'. Available: {', '.join(sorted(set(COLOR_SCHEMES) | set(THEME_DEFAULTS)))}")
        return True

    try:
        create_backup(SETTINGS_PATH)
        settings = load_settings(SETTINGS_PATH)

        if key in COLOR_SCHEMES:
            apply_color_scheme(settings, key)

        if key in THEME_DEFAULTS:
            apply_theme_defaults(settings, key)

        save_settings(SETTINGS_PATH, settings)
        print(f"Theme '{choice}' applied successfully.")

        restart_terminal()

    except Exception as e:
        print(f"Failed to apply theme '{choice}': {e}")

    return True


def get_weather():
    print("⛅ Fetching detailed weather for Berlin... (Demo)\n")
    time.sleep(1)  # kleiner Effekt für Coolness

    weather_icons = {
        "Sunny": "☀️",
        "Clear": "🌕",
        "Partly cloudy": "⛅",
        "Cloudy": "☁️",
        "Overcast": "☁️",
        "Mist": "🌫️",
        "Patchy rain": "🌦️",
        "Light rain": "🌧️",
        "Heavy rain": "🌧️🌧️",
        "Thunderstorm": "⛈️",
        "Snow": "❄️",
        "Fog": "🌁",
    }

    try:
        url = "https://wttr.in/Berlin?format=%C+%t+%h+%w+%m+%p+%l+%T"
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.text.split()
            condition = weather_data[0]
            temperature = weather_data[1]
            humidity = weather_data[2]
            wind = weather_data[3]
            moon_phase = weather_data[4]
            precipitation = weather_data[5]
            location = weather_data[6]
            observation_time = weather_data[7]

            # Passendes Icon suchen
            icon = weather_icons.get(condition, "🌈")

            # Coole Ausgabe
            print(f"{blue}Location{reset}: {location}")
            print(f"{blue}Time{reset}: {observation_time}")
            print(f"{blue}Condition{reset}: {icon} {condition}")
            print(f"{blue}Temperature{reset}: {temperature}")
            print(f"{blue}Humidity{reset}: {humidity}")
            print(f"{blue}Wind{reset}: {wind}")
            print(f"{blue}Moon Phase{reset}: {moon_phase}")
            print(f"{blue}Precipitation{reset}: {precipitation}\n")
        else:
            print(f"Failed to retrieve weather data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching weather: {str(e)}")


def type_out_text(text, delay=0.05):
    """Tippt den Text langsam aus."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def get_response_from_ollama(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="deepcoder:14b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"ERROR: {e}"


def check_ollama_update():
    """
    Prüft, ob eine neue Version von Ollama verfügbar ist, und bietet ein Update an.
    """
    try:
        result = subprocess.run(["ollama", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            local_version = result.stdout.strip()
            remote_version = subprocess.run(["curl", "-s", "https://api.ollama.ai/version"],
                                            stdout=subprocess.PIPE, text=True).stdout.strip()

            if local_version != remote_version:
                print(f"{yellow}New Ollama version available: {remote_version} (Current: {local_version}){reset}")
                while True:
                    user_input = input("Do you want to update Ollama? [y/n]:").strip().lower()
                    if user_input in ["y", "yes"]:
                        subprocess.run(["ollama", "update"], check=True)
                        print(f"{green}Ollama updated successfully! Please restart the script.{reset}")
                        exit()
                    elif user_input in ["n", "no"]:
                        print("Skipping update.")
                        break
                    else:
                        print(f"{red}Invalid input. Please enter 'y' for yes or 'n' for no.{reset}")

    except Exception as e:
        print(f"{red}Error checking for updates: {e}{reset}")


def find_ollama_path():
    """
    Findet den Installationspfad von Ollama basierend auf dem Betriebssystem.
    """
    try:
        if platform.system() == "Windows":
            base_path = os.environ.get("LOCALAPPDATA", "C:\\Users\\Default\\AppData\\Local")
            return os.path.join(base_path, "Programs", "Ollama", "ollama app.exe")
        elif platform.system() == "Darwin":  # macOS
            return "/Applications/Ollama.app/Contents/MacOS/Ollama"
        else:
            raise EnvironmentError("Unsupported Operating System. Ollama is not supported on this platform.")
    except Exception as e:
        raise FileNotFoundError(f"Error finding Ollama path: {e}")


def start_ollama():
    """
    Startet Ollama, falls es noch nicht läuft.
    """
    try:
        # Überprüfen, ob Ollama bereits läuft
        result = subprocess.run(
            ["tasklist"] if platform.system() == "Windows" else ["ps", "aux"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if "ollama" not in result.stdout.lower():
            print(f"{blue}Ollama is not running. Starting Ollama...{reset}")

            # Pfad zu Ollama finden
            ollama_path = find_ollama_path()

            if not os.path.exists(ollama_path):
                raise FileNotFoundError(f"Ollama executable not found at: {ollama_path}")

            # Ollama starten
            subprocess.Popen([ollama_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True if platform.system() != "Windows" else False)
            time.sleep(5)  # Warten, bis Ollama gestartet ist
            print(f"{green}Ollama started successfully.{reset}\n")
        else:
            print(f"{green}Ollama is already running.{reset}\n")
    except Exception as e:
        print(f"{red}Error starting Ollama: {e}{reset}")


def check_command_installed(command):
    """
    Überprüft, ob ein Befehlszeilentool installiert ist (z. B. ollama).
    :param command: Zu prüfender Befehlsname.
    :return: True, wenn installiert, andernfalls False.
    """
    try:
        result = subprocess.run(["which" if os.name != "nt" else "where", command],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        print(f"{red}Error checking command {command}: {e}{reset}")
        return False

def is_tool_installed(tool_name):
    """Check if a tool is installed."""
    result = subprocess.run(["which", tool_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0


# Liste aller verfügbaren Befehle
COMMANDS = [
    "cd", "cls", "clear", "dir", "ls", "mkdir", "rmdir", "del", "rm", "echo", "type", "cat", "exit",
    "p", "pp", "pp", "pp-c", "pp-p", "ps", "pa", "alpine", "scoop", "choco", "winget", "lx", "lx-c",
    "lx-p", "lx-cpp-c", "lx-c-c", "lx-p-c", "ubuntu", "ubuntu-c", "ubuntu-p",  "debian", "kali", "hack",
    "arch", "opensuse", "mint", "fedora", "redhat", "sles", "pengwin", "oracle",
    "speedtest", "kill", "download", "cputemp", "chucknorris", "theme", "cleantemp", "selfupdate",
    "tree", "py", "ask", "weather", "whoami", "hostname", "ip", "os", "time", "date", "open", "fortune",
    "history", "search", "zip", "unzip", "sysinfo", "clip set", "clip get", "ping", "emptytrash", "launch"
]

def completer(text, state):
    matches = [cmd for cmd in COMMANDS if cmd.startswith(text)]
    if state < len(matches):
        return matches[state]
    else:
        return None

def setup_autocomplete():
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")


def search_websites(command):
    """Searches for websites related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': command}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_github(command):
    """Searches GitHub for repositories or pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:github.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching GitHub for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_huggingface(command):
    """Searches Hugging Face for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:huggingface.co {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching Hugging Face for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_ollama(command):
    """Searches Ollama for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:ollama.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching Ollama for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_stackoverflow(command):
    """Searches stackoverflow for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:stackoverflow.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching Stack Overflow for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_stackexchange(command):
    """Searches stackexchange for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:stackexchange.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching Stack Exchange for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_pypi(command):
    """Searches pypi for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:pypi.org {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching PyPI for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_arxiv(command):
    """Searches arxiv for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:arxiv.org {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching ArXiv for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_paperswithcode(command):
    """Searches paperswithcode for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:paperswithcode.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching Papers with Code for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_kaggle(command):
    """Searches kaggle for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:kaggle.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching Kaggle for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_geeksforgeeks(command):
    """Searches geeksforgeeks for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:geeksforgeeks.org {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching GeeksforGeeks for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_realpython(command):
    """Searches realpython for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:realpython.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching Real Python for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_w3schools(command):
    """Searches w3schools for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:w3schools.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching W3Schools for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def search_developer_mozilla(command):
    """Searches developer.mozilla.org for pages related to the keyword using DuckDuckGo and returns links"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:developer.mozilla.org.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\nSearching Mozilla Developer Network (MDN) for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"\033[92m[{i}]\033[0m {a['href']}")

    if not links:
        print("No results found.")
    else:
        print(f"\n{len(links)} results found.\n")


def find_vcvarsall():
    """
    Sucht nach der Visual Studio-Initialisierungsdatei (vcvarsall.bat).
    """
    path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat"
    if os.path.isfile(path):
        return path
    raise FileNotFoundError("vcvarsall.bat not found. Please make sure Visual Studio is installed.")


def find_vcvarsall_c():
    """
    Sucht nach der Visual Studio Entwicklungsumgebung (vcvarsall.bat).
    """
    # Visual Studio Installationspfad (Standardort für VS 2022)
    vs_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat"
    if not os.path.isfile(vs_path):
        logging.error("Visual Studio vcvarsall.bat file not found.")
        raise FileNotFoundError("vcvarsall.bat not found. Please ensure Visual Studio is installed.")
    return vs_path


# --- mp command---

def get_project_paths_mp():
    """
    Ermittelt das p-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    mp_cpp_file = os.path.join(terminal_dir, "run_mp_command.cpp")
    mp_exe_file = os.path.join(terminal_dir, "run_mp_command.exe")
    return mp_cpp_file, mp_exe_file, terminal_dir


def compile_mp_cpp_with_vs(mp_cpp_file, mp_exe_file):
    """
    Kompiliert run_mp_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_mp_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{mp_cpp_file}" /Fe:"{mp_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_command_with_admin_privileges(command):
    """
    Führt einen Powershell interaktiv über den C++-Wrapper aus.

    Falls run_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    mp_cpp_file, mp_exe_file, _ = get_project_paths_mp()

    if not os.path.isfile(mp_exe_file):
        if not compile_mp_cpp_with_vs(mp_cpp_file, mp_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [mp_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- mp-c command---

def get_project_paths_mp_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    mp_c_file = os.path.join(terminal_dir, "run_mp_command.c")
    mp_c_exe_file = os.path.join(terminal_dir, "run_mp_c_command.exe")
    return mp_c_file, mp_c_exe_file, terminal_dir


def compile_mp_c_with_vs(mp_c_file, mp_c_exe_file):
    """
    Kompiliert run_mp_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_mp_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{mp_c_file}" /Fe:"{mp_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_command_with_admin_c_privileges(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_mp_c_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    mp_c_file, mp_c_exe_file, _ = get_project_paths_mp_c()

    if not os.path.isfile(mp_c_exe_file):
        if not compile_mp_c_with_vs(mp_c_file, mp_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [mp_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- mp-p command---

def run_command_with_admin_python_privileges(command):
    if sys.platform == "win32":
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            powershell_command = f"Start-Process powershell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command \"{command}\"' -Verb RunAs"
            subprocess.run(["powershell", "-Command", powershell_command], shell=True)
        else:
            subprocess.run(command, shell=True)
    else:
        subprocess.run(['sudo', '-S', command], input="password", text=True, shell=True)


def is_wsl_installed():
    """Check if WSL is installed by attempting to run a basic wsl command."""
    try:
        # Try running 'wsl --list' which lists installed WSL distributions
        subprocess.check_call(["wsl", "--list"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        # WSL executable not found, meaning WSL is not installed
        print("Error: WSL is not installed or not found on the system.")
        return False
    except subprocess.CalledProcessError:
        # WSL is found, but something went wrong while running the command
        print("Error: WSL is installed, but an error occurred while executing the command.")
        return False
    except Exception as e:
        # Catch any unexpected exceptions
        print(f"Unexpected error occurred while checking if WSL is installed: {e}")
        return False


# --- lx command---

def get_project_paths_lx():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    lx_cpp_file = os.path.join(terminal_dir, "run_lx_command.cpp")
    lx_exe_file = os.path.join(terminal_dir, "run_lx_command.exe")
    return lx_cpp_file, lx_exe_file, terminal_dir


def compile_lx_cpp_with_vs(lx_cpp_file, lx_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_lx_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{lx_cpp_file}" /Fe:"{lx_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_linux_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_lx_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    lx_cpp_file, lx_exe_file, _ = get_project_paths_lx()

    if not os.path.isfile(lx_exe_file):
        if not compile_lx_cpp_with_vs(lx_cpp_file, lx_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [lx_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- lx-cpp-c command---

def get_project_cpp_c_paths_lx():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    lx_cpp_c_file = os.path.join(terminal_dir, "run_lx_c_command.cpp")
    lx_exe_c_file = os.path.join(terminal_dir, "run_cpp_lx_c_command.exe")
    return lx_cpp_c_file, lx_exe_c_file, terminal_dir


def compile_lx_cpp_c_with_vs(lx_cpp_c_file, lx_exe_c_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_lx_c_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{lx_cpp_c_file}" /Fe:"{lx_exe_c_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_linux_cpp_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_lx_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    lx_cpp_c_file, lx_exe_c_file, _ = get_project_cpp_c_paths_lx()

    if not os.path.isfile(lx_exe_c_file):
        if not compile_lx_cpp_c_with_vs(lx_cpp_c_file, lx_exe_c_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [lx_exe_c_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- lx-c command---

def get_project_paths_lx_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    lx_c_file = os.path.join(terminal_dir, "run_lx_command.c")
    lx_c_exe_file = os.path.join(terminal_dir, "run_c_lx_command.exe")
    return lx_c_file, lx_c_exe_file, terminal_dir


def compile_lx_c_with_vs(lx_c_file, lx_c_exe_file):
    """
    Kompiliert run_lx_c_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_lx_c_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{lx_c_file}" /Fe:"{lx_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_linux_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_lx_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    lx_c_file, lx_c_exe_file, _ = get_project_paths_lx_c()

    if not os.path.isfile(lx_c_exe_file):
        if not compile_lx_c_with_vs(lx_c_file, lx_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [lx_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")

# --- lx-c-c command---

def get_project_paths_lx_c_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    lx_c_c_file = os.path.join(terminal_dir, "run_lx_c_command.c")
    lx_c_c_exe_file = os.path.join(terminal_dir, "run_c_lx_c_command.exe")
    return lx_c_c_file, lx_c_c_exe_file, terminal_dir


def compile_lx_c_c_with_vs(lx_c_c_file, lx_c_c_exe_file):
    """
    Kompiliert run_lx_c_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_lx_c_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{lx_c_c_file}" /Fe:"{lx_c_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_linux_c_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_lx_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    lx_c_c_file, lx_c_c_exe_file, _ = get_project_paths_lx_c_c()

    if not os.path.isfile(lx_c_c_exe_file):
        if not compile_lx_c_c_with_vs(lx_c_c_file, lx_c_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [lx_c_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- lx-p command---

def run_linux_python_command(command):
    if isinstance(command, str):
        command = f"wsl -e {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- lx-p-c command---

def run_linux_p_c_command(command):
    if isinstance(command, str):
        command = f"wsl -c {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- ubuntu command---

def get_project_paths_ubuntu():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    ubuntu_cpp_file = os.path.join(terminal_dir, "run_ubuntu_command.cpp")
    ubuntu_exe_file = os.path.join(terminal_dir, "run_ubuntu_command.exe")
    return ubuntu_cpp_file, ubuntu_exe_file, terminal_dir


def compile_ubuntu_cpp_with_vs(ubuntu_cpp_file, ubuntu_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_ubuntu_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{ubuntu_cpp_file}" /Fe:"{ubuntu_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_ubuntu_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_ubuntu_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    ubuntu_cpp_file, ubuntu_exe_file, _ = get_project_paths_ubuntu()

    if not os.path.isfile(ubuntu_exe_file):
        if not compile_ubuntu_cpp_with_vs(ubuntu_cpp_file, ubuntu_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [ubuntu_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- ubuntu-c command---

def get_project_paths_ubuntu_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    ubuntu_c_file = os.path.join(terminal_dir, "run_ubuntu_command.c")
    ubuntu_c_exe_file = os.path.join(terminal_dir, "run_ubuntu_c_command.exe")
    return ubuntu_c_file, ubuntu_c_exe_file, terminal_dir


def compile_ubuntu_c_with_vs(ubuntu_c_file, ubuntu_c_exe_file):
    """
    Kompiliert run_ubuntu_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_ubuntu_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{ubuntu_c_file}" /Fe:"{ubuntu_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_ubuntu_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_ubuntu_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    ubuntu_c_file, ubuntu_c_exe_file, _ = get_project_paths_ubuntu_c()

    if not os.path.isfile(ubuntu_c_exe_file):
        if not compile_ubuntu_c_with_vs(ubuntu_c_file, ubuntu_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [ubuntu_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- ubuntu-p command---

def run_ubuntu_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d ubuntu {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- debian command---

def get_project_paths_debian():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    debian_cpp_file = os.path.join(terminal_dir, "run_debian_command.cpp")
    debian_exe_file = os.path.join(terminal_dir, "run_debian_command.exe")
    return debian_cpp_file, debian_exe_file, terminal_dir


def compile_debian_cpp_with_vs(debian_cpp_file, debian_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_debian_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{debian_cpp_file}" /Fe:"{debian_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_debian_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_debian_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    debian_cpp_file, debian_exe_file, _ = get_project_paths_debian()

    if not os.path.isfile(debian_exe_file):
        if not compile_debian_cpp_with_vs(debian_cpp_file, debian_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [debian_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- debian-c command---

def get_project_paths_debian_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    debian_c_file = os.path.join(terminal_dir, "run_debian_command.c")
    debian_c_exe_file = os.path.join(terminal_dir, "run_debian_c_command.exe")
    return debian_c_file, debian_c_exe_file, terminal_dir


def compile_debian_c_with_vs(debian_c_file, debian_c_exe_file):
    """
    Kompiliert run_debian_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_debian_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{debian_c_file}" /Fe:"{debian_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_debian_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_debian_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    debian_c_file, debian_c_exe_file, _ = get_project_paths_debian_c()

    if not os.path.isfile(debian_c_exe_file):
        if not compile_debian_c_with_vs(debian_c_file, debian_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [debian_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- debian-p command---

def run_debian_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d debian {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- kali command---

def get_project_paths_kali():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    kali_cpp_file = os.path.join(terminal_dir, "run_kali_command.cpp")
    kali_exe_file = os.path.join(terminal_dir, "run_kali_command.exe")
    return kali_cpp_file, kali_exe_file, terminal_dir


def compile_kali_cpp_with_vs(kali_cpp_file, kali_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_kali_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{kali_cpp_file}" /Fe:"{kali_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_kali_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_kali_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    kali_cpp_file, kali_exe_file, _ = get_project_paths_kali()

    if not os.path.isfile(kali_exe_file):
        if not compile_kali_cpp_with_vs(kali_cpp_file, kali_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [kali_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- kali-c command---

def get_project_paths_kali_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    kali_c_file = os.path.join(terminal_dir, "run_kali_command.c")
    kali_c_exe_file = os.path.join(terminal_dir, "run_kali_c_command.exe")
    return kali_c_file, kali_c_exe_file, terminal_dir


def compile_kali_c_with_vs(kali_c_file, kali_c_exe_file):
    """
    Kompiliert run_kali_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_kali_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{kali_c_file}" /Fe:"{kali_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_kali_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_lx_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    kali_c_file, kali_c_exe_file, _ = get_project_paths_kali_c()

    if not os.path.isfile(kali_c_exe_file):
        if not compile_kali_c_with_vs(kali_c_file, kali_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [kali_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- kali-p command---

def run_kali_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d kali-linux {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- arch command---

def get_project_paths_arch():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    arch_cpp_file = os.path.join(terminal_dir, "run_arch_command.cpp")
    arch_exe_file = os.path.join(terminal_dir, "run_arch_command.exe")
    return arch_cpp_file, arch_exe_file, terminal_dir


def compile_arch_cpp_with_vs(arch_cpp_file, arch_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_arch_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{arch_cpp_file}" /Fe:"{arch_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_arch_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_arch_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    arch_cpp_file, arch_exe_file, _ = get_project_paths_arch()

    if not os.path.isfile(arch_exe_file):
        if not compile_arch_cpp_with_vs(arch_cpp_file, arch_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [arch_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- arch-c command---

def get_project_paths_arch_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    arch_c_file = os.path.join(terminal_dir, "run_arch_command.c")
    arch_c_exe_file = os.path.join(terminal_dir, "run_arch_c_command.exe")
    return arch_c_file, arch_c_exe_file, terminal_dir


def compile_arch_c_with_vs(arch_c_file, arch_c_exe_file):
    """
    Kompiliert run_arch_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_arch_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{arch_c_file}" /Fe:"{arch_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_arch_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_larch_c_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    arch_c_file, arch_c_exe_file, _ = get_project_paths_arch_c()

    if not os.path.isfile(arch_c_exe_file):
        if not compile_arch_c_with_vs(arch_c_file, arch_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [arch_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- arch-p command---

def run_arch_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d Arch {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- opensuse command---

def get_project_paths_opensuse():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    opensuse_cpp_file = os.path.join(terminal_dir, "run_opensuse_command.cpp")
    opensuse_exe_file = os.path.join(terminal_dir, "run_opensuse_command.exe")
    return opensuse_cpp_file, opensuse_exe_file, terminal_dir


def compile_opensuse_cpp_with_vs(opensuse_cpp_file, opensuse_exe_file):
    """
    Kompiliert run_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_opensuse_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{opensuse_cpp_file}" /Fe:"{opensuse_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_opensuse_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_arch_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    opensuse_cpp_file, opensuse_exe_file, _ = get_project_paths_opensuse()

    if not os.path.isfile(opensuse_exe_file):
        if not compile_opensuse_cpp_with_vs(opensuse_cpp_file, opensuse_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [opensuse_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- opensuse-c command---

def get_project_paths_opensuse_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    opensuse_c_file = os.path.join(terminal_dir, "run_opensuse_command.c")
    opensuse_c_exe_file = os.path.join(terminal_dir, "run_opensuse_c_command.exe")
    return opensuse_c_file, opensuse_c_exe_file, terminal_dir


def compile_opensuse_c_with_vs(opensuse_c_file, opensuse_c_exe_file):
    """
    Kompiliert run_opensuse_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_opensuse_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{opensuse_c_file}" /Fe:"{opensuse_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_opensuse_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_opensuse_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    opensuse_c_file, opensuse_c_exe_file, _ = get_project_paths_opensuse_c()

    if not os.path.isfile(opensuse_c_exe_file):
        if not compile_opensuse_c_with_vs(opensuse_c_file, opensuse_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [opensuse_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- opensuse-p command---

def run_opensuse_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d openSUSE-Leap {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- mint command---

def get_project_paths_mint():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    mint_cpp_file = os.path.join(terminal_dir, "run_mint_command.cpp")
    mint_exe_file = os.path.join(terminal_dir, "run_mint_command.exe")
    return mint_cpp_file, mint_exe_file, terminal_dir


def compile_mint_cpp_with_vs(mint_cpp_file, mint_exe_file):
    """
    Kompiliert run_mint_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_mint_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{mint_cpp_file}" /Fe:"{mint_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_mint_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_arch_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    mint_cpp_file, mint_exe_file, _ = get_project_paths_mint()

    if not os.path.isfile(mint_exe_file):
        if not compile_mint_cpp_with_vs(mint_cpp_file, mint_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [mint_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- mint-c command---

def get_project_paths_mint_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    mint_c_file = os.path.join(terminal_dir, "run_mint_command.c")
    mint_c_exe_file = os.path.join(terminal_dir, "run_mint_c_command.exe")
    return mint_c_file, mint_c_exe_file, terminal_dir


def compile_mint_c_with_vs(mint_c_file, mint_c_exe_file):
    """
    Kompiliert run_mint_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_mint_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{mint_c_file}" /Fe:"{mint_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_mint_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_mint_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    mint_c_file, mint_c_exe_file, _ = get_project_paths_mint_c()

    if not os.path.isfile(mint_c_exe_file):
        if not compile_mint_c_with_vs(mint_c_file, mint_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [mint_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- mint-p command---

def run_mint_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d mint {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- fedora command---

def get_project_paths_fedora():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    fedora_cpp_file = os.path.join(terminal_dir, "run_fedora_command.cpp")
    fedora_exe_file = os.path.join(terminal_dir, "run_fedora_command.exe")
    return fedora_cpp_file, fedora_exe_file, terminal_dir


def compile_fedora_cpp_with_vs(fedora_cpp_file, fedora_exe_file):
    """
    Kompiliert run_fedora_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_fedora_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{fedora_cpp_file}" /Fe:"{fedora_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_fedora_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_arch_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    fedora_cpp_file, fedora_exe_file, _ = get_project_paths_fedora()

    if not os.path.isfile(fedora_exe_file):
        if not compile_fedora_cpp_with_vs(fedora_cpp_file, fedora_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [fedora_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- fedora-c command---

def get_project_paths_fedora_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    fedora_c_file = os.path.join(terminal_dir, "run_fedora_command.c")
    fedora_c_exe_file = os.path.join(terminal_dir, "run_fedora_c_command.exe")
    return fedora_c_file, fedora_c_exe_file, terminal_dir


def compile_fedora_c_with_vs(fedora_c_file, fedora_c_exe_file):
    """
    Kompiliert run_fedora_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_fedora_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{fedora_c_file}" /Fe:"{fedora_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_fedora_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_fedora_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    fedora_c_file, fedora_c_exe_file, _ = get_project_paths_fedora_c()

    if not os.path.isfile(fedora_c_exe_file):
        if not compile_fedora_c_with_vs(fedora_c_file, fedora_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [fedora_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- fedora-p command---

def run_fedora_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d -d Fedora-Remix {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- redhat command---

def get_project_paths_redhat():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    redhat_cpp_file = os.path.join(terminal_dir, "run_redhat_command.cpp")
    redhat_exe_file = os.path.join(terminal_dir, "run_redhat_command.exe")
    return redhat_cpp_file, redhat_exe_file, terminal_dir


def compile_redhat_cpp_with_vs(redhat_cpp_file, redhat_exe_file):
    """
    Kompiliert run_redhat_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_redhat_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{redhat_cpp_file}" /Fe:"{redhat_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_redhat_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_redhat_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    redhat_cpp_file, redhat_exe_file, _ = get_project_paths_redhat()

    if not os.path.isfile(redhat_exe_file):
        if not compile_redhat_cpp_with_vs(redhat_cpp_file, redhat_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [redhat_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- redhat-c command---

def get_project_paths_redhat_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    redhat_c_file = os.path.join(terminal_dir, "run_redhat_command.c")
    redhat_c_exe_file = os.path.join(terminal_dir, "run_redhat_c_command.exe")
    return redhat_c_file, redhat_c_exe_file, terminal_dir


def compile_redhat_c_with_vs(redhat_c_file, redhat_c_exe_file):
    """
    Kompiliert run_redhat_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_redhat_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{redhat_c_file}" /Fe:"{redhat_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_redhat_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_redhat_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    redhat_c_file, redhat_c_exe_file, _ = get_project_paths_redhat_c()

    if not os.path.isfile(redhat_c_exe_file):
        if not compile_redhat_c_with_vs(redhat_c_file, redhat_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [redhat_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- redhat-p command---

def run_redhat_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d RedHat {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- sles command---

def get_project_paths_sles():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    sles_cpp_file = os.path.join(terminal_dir, "run_sles_command.cpp")
    sles_exe_file = os.path.join(terminal_dir, "run_sles_command.exe")
    return sles_cpp_file, sles_exe_file, terminal_dir


def compile_sles_cpp_with_vs(sles_cpp_file, sles_exe_file):
    """
    Kompiliert run_sles_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_sles_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{sles_cpp_file}" /Fe:"{sles_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_sles_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_sles_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    sles_cpp_file, sles_exe_file, _ = get_project_paths_sles()

    if not os.path.isfile(sles_exe_file):
        if not compile_sles_cpp_with_vs(sles_cpp_file, sles_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [sles_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- sles-c command---

def get_project_paths_sles_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    sles_c_file = os.path.join(terminal_dir, "run_sles_command.c")
    sles_c_exe_file = os.path.join(terminal_dir, "run_sles_c_command.exe")
    return sles_c_file, sles_c_exe_file, terminal_dir


def compile_sles_c_with_vs(sles_c_file, sles_c_exe_file):
    """
    Kompiliert run_sles_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_sles_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{sles_c_file}" /Fe:"{sles_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_sles_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_sles_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    sles_c_file, sles_c_exe_file, _ = get_project_paths_sles_c()

    if not os.path.isfile(sles_c_exe_file):
        if not compile_sles_c_with_vs(sles_c_file, sles_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [sles_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- sles-p command---

def run_sles_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d SLES {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- pengwin command---

def get_project_paths_pengwin():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    pengwin_cpp_file = os.path.join(terminal_dir, "run_pengwin_command.cpp")
    pengwin_exe_file = os.path.join(terminal_dir, "run_pengwin_command.exe")
    return pengwin_cpp_file, pengwin_exe_file, terminal_dir


def compile_pengwin_cpp_with_vs(pengwin_cpp_file, pengwin_exe_file):
    """
    Kompiliert run_pengwin_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_pengwin_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{pengwin_cpp_file}" /Fe:"{pengwin_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_pengwin_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_pengwin_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    pengwin_cpp_file, pengwin_exe_file, _ = get_project_paths_pengwin()

    if not os.path.isfile(pengwin_exe_file):
        if not compile_pengwin_cpp_with_vs(pengwin_cpp_file, pengwin_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [pengwin_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- pengwin-c command---

def get_project_paths_pengwin_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    pengwin_c_file = os.path.join(terminal_dir, "run_pengwin_command.c")
    pengwin_c_exe_file = os.path.join(terminal_dir, "run_pengwin_c_command.exe")
    return pengwin_c_file, pengwin_c_exe_file, terminal_dir


def compile_pengwin_c_with_vs(pengwin_c_file, pengwin_c_exe_file):
    """
    Kompiliert run_pengwin_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_pengwin_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{pengwin_c_file}" /Fe:"{pengwin_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_pengwin_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_pengwin_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    pengwin_c_file, pengwin_c_exe_file, _ = get_project_paths_pengwin_c()

    if not os.path.isfile(pengwin_c_exe_file):
        if not compile_pengwin_c_with_vs(pengwin_c_file, pengwin_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [pengwin_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- pengwin-p command---

def run_pengwin_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d Pengwin {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- oracle command---

def get_project_paths_oracle():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    oracle_cpp_file = os.path.join(terminal_dir, "run_oracle_command.cpp")
    oracle_exe_file = os.path.join(terminal_dir, "run_oracle_command.exe")
    return oracle_cpp_file, oracle_exe_file, terminal_dir


def compile_oracle_cpp_with_vs(oracle_cpp_file, oracle_exe_file):
    """
    Kompiliert run_oracle_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_oracle_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{oracle_cpp_file}" /Fe:"{oracle_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_oracle_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_oracle_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    oracle_cpp_file, oracle_exe_file, _ = get_project_paths_oracle()

    if not os.path.isfile(oracle_exe_file):
        if not compile_oracle_cpp_with_vs(oracle_cpp_file, oracle_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [oracle_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- oracle-c command---

def get_project_paths_oracle_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    oracle_c_file = os.path.join(terminal_dir, "run_oracle_command.c")
    oracle_c_exe_file = os.path.join(terminal_dir, "run_oracle_c_command.exe")
    return oracle_c_file, oracle_c_exe_file, terminal_dir


def compile_oracle_c_with_vs(oracle_c_file, oracle_c_exe_file):
    """
    Kompiliert run_oracle_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_oracle_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{oracle_c_file}" /Fe:"{oracle_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_oracle_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_oracle_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    oracle_c_file, oracle_c_exe_file, _ = get_project_paths_oracle_c()

    if not os.path.isfile(oracle_c_exe_file):
        if not compile_oracle_c_with_vs(oracle_c_file, oracle_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [oracle_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- oracle-p command---

def run_oracle_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d OracleLinux {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- alpine command---

def get_project_paths_alpine():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    alpine_cpp_file = os.path.join(terminal_dir, "run_alpine_command.cpp")
    alpine_exe_file = os.path.join(terminal_dir, "run_alpine_command.exe")
    return alpine_cpp_file, alpine_exe_file, terminal_dir


def compile_alpine_cpp_with_vs(alpine_cpp_file, alpine_exe_file):
    """
    Kompiliert run_alpine_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_alpine_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{alpine_cpp_file}" /Fe:"{alpine_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_alpine_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_alpine_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    alpine_cpp_file, alpine_exe_file, _ = get_project_paths_alpine()

    if not os.path.isfile(alpine_exe_file):
        if not compile_alpine_cpp_with_vs(alpine_cpp_file, alpine_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [alpine_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- alpine-c command---

def get_project_paths_alpine_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    alpine_c_file = os.path.join(terminal_dir, "run_alpine_command.c")
    alpine_c_exe_file = os.path.join(terminal_dir, "run_alpine_c_command.exe")
    return alpine_c_file, alpine_c_exe_file, terminal_dir


def compile_alpine_c_with_vs(alpine_c_file, alpine_c_exe_file):
    """
    Kompiliert run_alpine_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_alpine_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{alpine_c_file}" /Fe:"{alpine_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_alpine_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_alpine_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    alpine_c_file, alpine_c_exe_file, _ = get_project_paths_alpine_c()

    if not os.path.isfile(alpine_c_exe_file):
        if not compile_alpine_c_with_vs(alpine_c_file, alpine_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [alpine_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- alpine-p command---

def run_alpine_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d Alpine {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


# --- clear command---

def get_project_paths_clear():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C++-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    clear_cpp_file = os.path.join(terminal_dir, "run_clear_command.cpp")
    clear_exe_file = os.path.join(terminal_dir, "run_clear_command.exe")
    return clear_cpp_file, clear_exe_file, terminal_dir


def compile_clear_cpp_with_vs(clear_cpp_file, clear_exe_file):
    """
    Kompiliert run_clear_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("Compile run_clear_command.cpp with Visual Studio C++...")
    vcvarsall = find_vcvarsall()
    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe /EHsc "{clear_cpp_file}" /Fe:"{clear_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_clear_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C++-Wrapper aus.

    Falls run_clear_command.exe noch nicht existiert, wird das C++-Programm kompiliert.
    Der C++-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    clear_cpp_file, clear_exe_file, _ = get_project_paths_clear()

    if not os.path.isfile(clear_exe_file):
        if not compile_clear_cpp_with_vs(clear_cpp_file, clear_exe_file):
            logging.error("Abort: C++ compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C++-Code
    cmd = [clear_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- clear-c command---

def get_project_paths_clear_c():
    """
    Ermittelt das P-terminal-Projektverzeichnis, den Ordner 'p-terminal',
    sowie die Pfade zur C-Quelle und zur Executable.
    """
    username = getpass.getuser()
    base_dir = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
    terminal_dir = os.path.join(base_dir, "pp-commands")
    clear_c_file = os.path.join(terminal_dir, "run_clear_command.c")
    clear_c_exe_file = os.path.join(terminal_dir, "run_clear_c_command.exe")
    return clear_c_file, clear_c_exe_file, terminal_dir


def compile_clear_c_with_vs(clear_c_file, clear_c_exe_file):
    """
    Kompiliert run_clear_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("Compiling run_clear_command.c with Visual Studio...")
    vcvarsall = find_vcvarsall_c()

    # Initialisiere die VS-Umgebung (x64) und rufe cl.exe auf
    command = f'"{vcvarsall}" x64 && cl.exe "{clear_c_file}" /Fe:"{clear_c_exe_file}"'

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    if result.returncode != 0:
        logging.error("Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("Compilation successful.")
    return True


def run_clear_c_command(command):
    """
    Führt einen Linux-Befehl interaktiv über den C-Wrapper aus.

    Falls run_clear_command.exe noch nicht existiert, wird das C-Programm kompiliert.
    Der C-Code öffnet dann ein neues Terminalfenster, in dem WSL interaktiv gestartet wird.
    """
    clear_c_file, clear_c_exe_file, _ = get_project_paths_clear_c()

    if not os.path.isfile(clear_c_exe_file):
        if not compile_clear_c_with_vs(clear_c_file, clear_c_exe_file):
            logging.error("Abort: C compilation was unsuccessful.")
            return

    # Erstelle die Befehlsliste. Bei mehreren Argumenten werden diese getrennt übertragen.
    if isinstance(command, str):
        # Zerlege die Eingabe (z.B. "nano test.py") in Parameter, falls möglich
        args = command.split()  # Achtung: Bei komplexen Befehlen mit Leerzeichen evtl. anders behandeln!
    else:
        args = command

    # Baue die Kommandozeile, ohne zusätzliche Anführungszeichen – das übernimmt der C-Code
    cmd = [clear_c_exe_file] + args

    try:
        logging.info(f"Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("Cancellation by user.")


# --- clear-p command---

def run_clear_python_command(command):
    if isinstance(command, str):
        command = f"wsl -d ClearLinux {command}"

    process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


def run_scoop_command(
    command: Union[str, List[str]],
    timeout: Optional[int] = None,
    capture_output: bool = False,
    retries: int = 2,
    retry_delay: float = 1.0,
    logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Executes a Scoop command – super-fast, stable, and with robust logger fallback.

    Args:
        command: Scoop command as a string or list.
        timeout: Max runtime in seconds.
        capture_output: Returns stdout/stderr if True.
        retries: Number of retries on exit errors.
        retry_delay: Base delay (seconds) for exponential backoff.
        logger: Optional logger; if None, a default logger is configured.

    Returns:
        subprocess.CompletedProcess with .stdout/.stderr if capture_output.

    Raises:
        RuntimeError: if scoop.exe is not found.
        subprocess.CalledProcessError: on exit code ≠ 0 (after retries).
        subprocess.TimeoutExpired: on timeout.
        KeyboardInterrupt: on user interruption.
    """
    # --- Logger fallback and configuration ---
    if logger is None:
        logger = logging.getLogger("run_scoop_command")
    if not logger.handlers:
        # If no handler exists: add default stream handler
        handler = logging.StreamHandler()
        fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # --- Caching the scoop path ---
    if not hasattr(run_scoop_command, "_scoop_path"):
        path = shutil.which("scoop")
        if not path:
            msg = "Scoop not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_scoop_command._scoop_path = path
    scoop_path = run_scoop_command._scoop_path

    # --- Tokenizing ---
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [scoop_path] + args

    logger.debug(f"Starting Scoop: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

    # --- Execution with retries ---
    attempt = 0
    while True:
        attempt += 1
        try:
            start = time.perf_counter()
            result = subprocess.run(
                cmd,
                shell=False,
                stdout=subprocess.PIPE if capture_output else None,
                stderr=subprocess.PIPE if capture_output else None,
                text=True,
                timeout=timeout,
                check=True
            )
            duration = time.perf_counter() - start
            logger.info(f"Scoop succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise  # After retries, propagate the CalledProcessError

        except subprocess.TimeoutExpired as e:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise

def run_choco_command(
    command: Union[str, List[str]],
    timeout: Optional[int] = None,
    capture_output: bool = False,
    retries: int = 2,
    retry_delay: float = 1.0,
    logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Executes a Chocolatey command – super-fast, stable, and with robust logger fallback.

    Args:
        command: Chocolatey command as a string or list.
        timeout: Maximum runtime in seconds.
        capture_output: Returns stdout and stderr if True.
        retries: Number of retries on exit errors.
        retry_delay: Base delay (in seconds) for exponential backoff.
        logger: Optional logger; if None, a default logger is configured.

    Returns:
        subprocess.CompletedProcess with .stdout and .stderr (if capture_output is True).

    Raises:
        RuntimeError: If choco.exe is not found.
        subprocess.CalledProcessError: On exit code ≠ 0 (after retries).
        subprocess.TimeoutExpired: On timeout.
        KeyboardInterrupt: On user interruption.
    """
    # --- Logger fallback and configuration ---
    if logger is None:
        logger = logging.getLogger("run_choco_command")
    if not logger.handlers:
        # Add default stream handler if none exists
        handler = logging.StreamHandler()
        fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # --- Caching the choco path ---
    if not hasattr(run_choco_command, "_choco_path"):
        path = shutil.which("choco")
        if not path:
            msg = "Chocolatey (choco) not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_choco_command._choco_path = path
    choco_path = run_choco_command._choco_path

    # --- Tokenizing the command ---
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [choco_path] + args

    logger.debug(f"Starting Chocolatey: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

    # --- Execution with retries ---
    attempt = 0
    while True:
        attempt += 1
        try:
            start = time.perf_counter()
            result = subprocess.run(
                cmd,
                shell=False,
                stdout=subprocess.PIPE if capture_output else None,
                stderr=subprocess.PIPE if capture_output else None,
                text=True,
                timeout=timeout,
                check=True
            )
            duration = time.perf_counter() - start
            logger.info(f"Chocolatey succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise  # Pass the error after retries

        except subprocess.TimeoutExpired as e:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise


def run_winget_command(
    command: Union[str, List[str]],
    timeout: Optional[int] = None,
    capture_output: bool = False,
    retries: int = 2,
    retry_delay: float = 1.0,
    logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Executes a winget command – super-fast, stable, and with robust logger fallback.

    Args:
        command: Winget command as a string or list.
        timeout: Maximum runtime in seconds.
        capture_output: Returns stdout and stderr if True.
        retries: Number of retries on exit errors.
        retry_delay: Base delay (in seconds) for exponential backoff.
        logger: Optional logger; if None, a default logger is configured.

    Returns:
        subprocess.CompletedProcess with .stdout and .stderr (if capture_output is True).

    Raises:
        RuntimeError: If winget is not found.
        subprocess.CalledProcessError: On exit code ≠ 0 (after retries).
        subprocess.TimeoutExpired: On timeout.
        KeyboardInterrupt: On user interruption.
    """
    # --- Logger fallback and configuration ---
    if logger is None:
        logger = logging.getLogger("run_winget_command")
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # --- Caching the winget path ---
    if not hasattr(run_winget_command, "_winget_path"):
        path = shutil.which("winget")
        if not path:
            msg = "winget not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_winget_command._winget_path = path
    winget_path = run_winget_command._winget_path

    # --- Tokenizing the command ---
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [winget_path] + args

    logger.debug(f"Starting winget: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

    # --- Execution with retries ---
    attempt = 0
    while True:
        attempt += 1
        try:
            start = time.perf_counter()
            result = subprocess.run(
                cmd,
                shell=False,
                stdout=subprocess.PIPE if capture_output else None,
                stderr=subprocess.PIPE if capture_output else None,
                text=True,
                timeout=timeout,
                check=True
            )
            duration = time.perf_counter() - start
            logger.info(f"winget succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise  # Pass the error after retries

        except subprocess.TimeoutExpired as e:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise


def find_active_env():
    """Suche ein Environment im aktuellen Verzeichnis."""
    current_dir = os.getcwd()

    # Suche alle Ordner im current_dir
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)

        # Prüfen ob Ordner und Scripts/activate vorhanden ist
        if os.path.isdir(item_path):
            activate_script = os.path.join(item_path, "Scripts", "activate")
            if os.path.exists(activate_script):
                # Treffer: Dies ist ein Environment
                return item_path

    # Nichts gefunden ➔ fallback
    return os.path.abspath(DEFAULT_ENV_DIR)

def get_main_pin(current_dir, env_indicator):
    return (
        f"\n{green}┌──({reset}{blue}{getpass.getuser()}"
        + colored("㋐", attrs=["bold"])
        + f"{blue}Peharge{reset}{green})-[{reset}{current_dir}{green}]-{reset}{env_indicator}"
        f"\n{green}└─{reset}{blue}${reset} "
    )

def get_evel_pin(current_dir, env_indicator):
    return (
        f"\n{blue}┌──({reset}{red}root"
        + colored("㋐", attrs=["bold"])
        + f"{red}Peharge{reset}{blue})-[{reset}{current_dir}{blue}]-{reset}{env_indicator}"
        f"\n{blue}└─{reset}{red}#{reset} "
    )

def main():
    state = "main"

    print_banner()
    set_python_path()
    setup_autocomplete()

    while True:
        try:
            current_dir = os.getcwd()

            # Aktives Env suchen
            active_env_path = find_active_env()
            python_path = os.path.join(active_env_path, "Scripts", "python.exe")
            env_active = os.path.exists(python_path)

            # Anzeige schöner machen
            if active_env_path.startswith(current_dir):
                display_env_path = "." + active_env_path[len(current_dir):]
            else:
                display_env_path = active_env_path

            env_indicator = (
                f"{green}[{reset}{display_env_path}{green}]{reset}"
                if env_active else
                f"{green}[{reset}{red}no venv recorded{reset}{green}]{reset}"
            )

            # PIN-Design je nach state
            pin = get_main_pin(current_dir, env_indicator) if state == "main" else get_evel_pin(current_dir, env_indicator)

            print(pin, end='')
            user_input = input().strip()

            if handle_special_commands(user_input):
                continue

            elif user_input.startswith("pp "):
                user_input = user_input[3:]
                run_command_with_admin_privileges(user_input)

            elif user_input.lower() == "pin main":
                state = "main"
                continue

            elif user_input.lower() == "pin evil":
                state = "evel"
                continue

            elif user_input.startswith("pp-cpp "):
                user_input = user_input[7:]
                run_command_with_admin_privileges(user_input)

            elif user_input.startswith("pp-c "):
                user_input = user_input[5:]
                run_command_with_admin_c_privileges(user_input)

            elif user_input.startswith("pp-p "):
                user_input = user_input[5:]
                run_command_with_admin_python_privileges(user_input)

            elif user_input.startswith("powershell "):
                run_command(user_input, shell=True)

            elif user_input.startswith("ps "):
                user_input = user_input[3:].strip()
                search_websites(user_input)

            elif user_input.startswith("ps-github "):
                user_input = user_input[10:].strip()
                search_github(user_input)

            elif user_input.startswith("ps-huggingface "):
                user_input = user_input[15:].strip()
                search_huggingface(user_input)

            elif user_input.startswith("ps-ollama "):
                user_input = user_input[10:].strip()
                search_ollama(user_input)

            elif user_input.startswith("ps-stackoverflow "):
                user_input = user_input[17:].strip()
                search_stackoverflow(user_input)

            elif user_input.startswith("ps-stackexchange "):
                user_input = user_input[17:].strip()
                search_stackexchange(user_input)

            elif user_input.startswith("ps-pypi "):
                user_input = user_input[8:].strip()
                search_pypi(user_input)

            elif user_input.startswith("ps-arxiv "):
                user_input = user_input[9:].strip()
                search_arxiv(user_input)

            elif user_input.startswith("ps-paperswithcode "):
                user_input = user_input[18:].strip()
                search_paperswithcode(user_input)

            elif user_input.startswith("ps-kaggle "):
                user_input = user_input[10:].strip()
                search_kaggle(user_input)

            elif user_input.startswith("ps-geeksforgeeks "):
                user_input = user_input[17:].strip()
                search_geeksforgeeks(user_input)

            elif user_input.startswith("ps-realpython "):
                user_input = user_input[14:].strip()
                search_realpython(user_input)

            elif user_input.startswith("ps-w3schools "):
                user_input = user_input[13:].strip()
                search_w3schools(user_input)

            elif user_input.startswith("ps-developer-mozilla "):
                user_input = user_input[21:].strip()
                search_developer_mozilla(user_input)

            elif user_input.startswith("lx "):
                user_input = user_input[3:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("lx-cpp "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("lx-cpp-c "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_cpp_c_command(user_input)

            elif user_input.startswith("lx-c "):
                user_input = user_input[5:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_c_command(user_input)

            elif user_input.startswith("lx-c-c "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_c_c_command(user_input)

            elif user_input.startswith("lx-p "):
                user_input = user_input[5:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_python_command(user_input)

            elif user_input.startswith("lx-p-c "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_p_c_command(user_input)

            elif user_input.startswith("linux "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("ubuntu "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_command(user_input)

            elif user_input.startswith("ubuntu-c "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_c_command(user_input)

            elif user_input.startswith("ubuntu-p "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_python_command(user_input)

            elif user_input.startswith("debian "):
                user_input = user_input[7:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Debian: {user_input}")
                    run_debian_command(user_input)

            elif user_input.startswith("debian-c "):
                user_input = user_input[9:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Debian: {user_input}")
                    run_debian_c_command(user_input)

            elif user_input.startswith("debian-p "):
                user_input = user_input[9:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Debian: {user_input}")
                    run_debian_python_command(user_input)

            elif user_input.startswith("kali "):
                user_input = user_input[5:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Kali: {user_input}")
                    run_kali_command(user_input)

            elif user_input.startswith("kali-c "):
                user_input = user_input[7:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Kali: {user_input}")
                    run_kali_c_command(user_input)

            elif user_input.startswith("kali-p "):
                user_input = user_input[7:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Kali: {user_input}")
                    run_kali_python_command(user_input)

            elif user_input.startswith("hack "):
                user_input = user_input[5:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Kali: {user_input}")
                    run_kali_command(user_input)

            elif user_input.startswith("arch "):
                user_input = user_input[5:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Arch: {user_input}")
                    run_arch_command(user_input)

            elif user_input.startswith("arch-c "):
                user_input = user_input[7:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Arch: {user_input}")
                    run_arch_c_command(user_input)

            elif user_input.startswith("arch-p "):
                user_input = user_input[7:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Arch: {user_input}")
                    run_arch_python_command(user_input)

            elif user_input.startswith("openSUSE "):
                user_input = user_input[9:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_opensuse_command(user_input)

            elif user_input.startswith("openSUSE-c "):
                user_input = user_input[11:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_opensuse_c_command(user_input)

            elif user_input.startswith("openSUSE-p "):
                user_input = user_input[11:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_opensuse_python_command(user_input)

            elif user_input.startswith("mint "):
                user_input = user_input[5:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_mint_command(user_input)

            elif user_input.startswith("mint-c "):
                user_input = user_input[7:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_mint_c_command(user_input)

            elif user_input.startswith("mint-p "):
                user_input = user_input[7:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on openSUSE: {user_input}")
                    run_mint_python_command(user_input)

            elif user_input.startswith("fedora "):
                user_input = user_input[7:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Fedora: {user_input}")
                    run_fedora_command(user_input)

            elif user_input.startswith("fedora-c "):
                user_input = user_input[9:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Fedora: {user_input}")
                    run_fedora_c_command(user_input)

            elif user_input.startswith("fedora-p "):
                user_input = user_input[9:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Fedora: {user_input}")
                    run_fedora_python_command(user_input)

            elif user_input.startswith("redhat "):
                user_input = user_input[7:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on RedHat: {user_input}")
                    run_redhat_command(user_input)

            elif user_input.startswith("redhat-c "):
                user_input = user_input[9:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on RedHat: {user_input}")
                    run_redhat_c_command(user_input)

            elif user_input.startswith("redhat-p "):
                user_input = user_input[9:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on RedHat: {user_input}")
                    run_redhat_python_command(user_input)

            elif user_input.startswith("sles "):
                user_input = user_input[7:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on SLES: {user_input}")
                    run_sles_command(user_input)

            elif user_input.startswith("sles-c "):
                user_input = user_input[9:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on SLES: {user_input}")
                    run_sles_c_command(user_input)

            elif user_input.startswith("sles-p "):
                user_input = user_input[9:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on SLES: {user_input}")
                    run_sles_python_command(user_input)

            elif user_input.startswith("pengwin "):
                user_input = user_input[7:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Pengwin: {user_input}")
                    run_pengwin_command(user_input)

            elif user_input.startswith("pengwin-c "):
                user_input = user_input[9:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Pengwin: {user_input}")
                    run_pengwin_c_command(user_input)

            elif user_input.startswith("pengwin-p "):
                user_input = user_input[9:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Pengwin: {user_input}")
                    run_pengwin_python_command(user_input)

            elif user_input.startswith("oracle "):
                user_input = user_input[7:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Oracle: {user_input}")
                    run_oracle_command(user_input)

            elif user_input.startswith("oracle-c "):
                user_input = user_input[9:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Oracle: {user_input}")
                    run_oracle_c_command(user_input)

            elif user_input.startswith("oracle-p "):
                user_input = user_input[9:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Oracle: {user_input}")
                    run_oracle_python_command(user_input)

            elif user_input.startswith("alpine "):
                user_input = user_input[7:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Alpine: {user_input}")
                    run_alpine_command(user_input)

            elif user_input.startswith("alpine-c "):
                user_input = user_input[9:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Alpine: {user_input}")
                    run_alpine_c_command(user_input)

            elif user_input.startswith("alpine-p "):
                user_input = user_input[9:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Alpine: {user_input}")
                    run_alpine_python_command(user_input)

            elif user_input.startswith("clear "):
                user_input = user_input[7:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Clear: {user_input}")
                    run_clear_command(user_input)

            elif user_input.startswith("clear-c "):
                user_input = user_input[9:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Clear: {user_input}")
                    run_clear_c_command(user_input)

            elif user_input.startswith("clear-p "):
                user_input = user_input[9:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print("WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"Executing the following command on Clear: {user_input}")
                    run_clear_python_command(user_input)

            elif user_input.startswith("sc "):
                user_input = user_input[3:].strip()
                print(f"Executing the following command with scoop: {user_input}")
                run_scoop_command(user_input)

            elif user_input.startswith("scoop "):
                user_input = user_input[6:].strip()
                print(f"Executing the following command with scoop: {user_input}")
                run_scoop_command(user_input)

            elif user_input.startswith("cho "):
                user_input = user_input[4:].strip()
                print(f"Executing the following command with choco: {user_input}")
                run_choco_command(user_input)

            elif user_input.startswith("choco "):
                user_input = user_input[6:].strip()
                print(f"Executing the following command with choco: {user_input}")
                run_choco_command(user_input)

            elif user_input.startswith("winget "):
                user_input = user_input[6:].strip()
                print(f"Executing the following command with winget : {user_input}")
                run_winget_command(user_input)

            else:
                run_command(user_input, shell=True)

            sys.stdout.flush()
            sys.stderr.flush()

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {str(e)}", file=sys.stderr)


if __name__ == "__main__":
    main()