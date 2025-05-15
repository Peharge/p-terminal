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
from cgitb import strong
from dotenv import load_dotenv
from subprocess import run
import readline
from bs4 import BeautifulSoup
import datetime
import socket
import platform
import webbrowser
import random
import zipfile
import requests
import psutil
import pyperclip
import ctypes
import speedtest
import colorama
from colorama import Fore, Style, Back
import ollama
from termcolor import colored
import venv
import selectors
import signal
import shutil
import shlex
from typing import Union, List, Optional
import json
import msvcrt
from pathlib import Path
import code
from datetime import datetime
from deep_translator import GoogleTranslator
from io import BytesIO
from PIL import Image
from duckduckgo_search import DDGS
import multiprocessing

colorama.init()

DEFAULT_ENV_DIR = os.path.join("p-terminal", "pp-term", ".env")
DEFAULT_PYTHON_EXECUTABLE = os.path.join(DEFAULT_ENV_DIR, "Scripts", "python.exe")

# Globales Thema
current_theme = "dark"

log_path = Path(__file__).parent / "peharge-compiler.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_path, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
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


def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def print_banner():
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

    print()

    # JSON-Datei laden
    json_path = f'C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\pp-term-versions.json'
    try:
        with open(json_path, 'r') as f:
            versions = json.load(f)

        # Versionsinformationen ausgeben
        for key, value in versions.items():
            print(f"{blue}{key}{reset}: {value}")
    except FileNotFoundError:
        print(f"[{timestamp()}] [INFO] Versionsdatei nicht gefunden unter {json_path}")
    except json.JSONDecodeError:
        print(f"[{timestamp()}] [INFO] JSON-Formatfehler in {json_path}")

    print()

    # Funktion zur Anzeige der 16 Farbpaletten ohne Abstände und Zahlen
    def show_color_palette():
        for i in range(8):
            print(f"\033[48;5;{i}m  \033[0m", end="")  # Farben ohne Zahlen und ohne Abstände

        print()  # Zeilenumbruch nach der ersten Reihe

        # Anzeige der helleren Farben (8-15) ohne Abstände und Zahlen
        for i in range(8, 16):
            print(f"\033[48;5;{i}m  \033[0m", end="")

        print()

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

    # Aktuelles Virtual Environment ermitteln (Pfad und optionale Env-Variablen)
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

    # command in Liste umwandeln (nur wenn shell=False und command ist str)
    if isinstance(command, str) and not shell:
        command = shlex.split(command, posix=(os.name != "nt"))

    # pip- und python-Wrapper
    if isinstance(command, list) and command:
        base = os.path.basename(command[0]).lower()
        if base == "pip" or base.startswith("pip"):
            command = [python_exe, "-m", "pip"] + command[1:]
        elif base == "python" or base.startswith("python"):
            command = [python_exe] + command[1:]

    # Umgebung zusammenbauen: zuerst das Venv-Env, dann System-Env, dann extra_env
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

    # Wenn shell=True: einfache Ausführung mit direktem Stream-Passing
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

    # Ansonsten: non-shell mit PIPEs und selectors für Zeilen-Output
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
        print(f"[{timestamp()}] [INFO] Directory not found: {path}", file=sys.stderr)
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] {str(e)}", file=sys.stderr)


def handle_special_commands(user_input):
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
        "run solution": "mavis-solution\\run-solution-4.py",
        "run solution-3": "mavis-solution\\run-solution-3.py",
        "run solution-4": "mavis-solution\\run-solution-4.py",
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
        "run qwen3:0.6b": "pp-commands\\qwen-3-0-6b.py", # new
        "run qwen3:1.7b": "pp-commands\\qwen-3-1-7b.py",  # new
        "run qwen3:4b": "pp-commands\\qwen-3-4b.py",  # new
        "run qwen3:8b": "pp-commands\\qwen-3-8b.py",  # new
        "run qwen3:14b": "pp-commands\\qwen-3-14b.py",  # new
        "run qwen3:32b": "pp-commands\\qwen-3-32.py",  # new
        "run qwen3:30b": "pp-commands\\qwen-3-30.py",  # new
        "run qwen3:235b": "pp-commands\\qwen-3-235.py",  # new
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
        "run qwen2.5-omni:7b": "pp-commands\\qwen-2-5-omni-7b.py",  # new
        "run qvq:72b": "pp-commands\\qvq-72b.py",  # new
        "run qwen2.5-vl:32b": "pp-commands\\qwen-2-5-vl-32b.py",  # new
        "run qwen2.5-vl:72b": "pp-commands\\qwen-2-5-vl-72b.py",  # new
        "run llama4-maverick:17b": "pp-commands\\llama-4-maverick-17b-ollama.py",  # new
        "run llama4-scout:17b": "pp-commands\\llama-4-scout-17b-ollama.py",  # new
        "run llama4-maverick:17b hg": "pp-commands\\llama-4-maverick-17b.py",  # new
        "run llama4-scout:17b hg": "pp-commands\\llama-4-scout-17b.py",  # new
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
        "p git p-terminal": "pp-commands\\p-git.py",  # new
        "p git mavis": "pp-commands\\p-git-mavis.py",  # new
        "p git mavis-web": "pp-commands\\p-git-mavis-web.py",  # new
        "p git simon": "pp-commands\\p-git-simon.py",  # new
        "p git llama.cpp": "pp-commands\\p-git-llama-cpp.py",  # new
        "p git pytorch": "pp-commands\\p-git-pytorch.py",  # new
        "p git tensorflow": "pp-commands\\p-git-tensorflow.py",  # new
        "p git jax": "pp-commands\\p-git-jax.py",  # new
        "p git ollama": "pp-commands\\p-git-ollama.py",  # new
        "p git transformer": "pp-commands\\p-git-transformer.py",  # new
        "p git slicer": "pp-commands\\p-git-slicer.py",  # new
        "p ls": "pp-commands\\p-ls.py", # new
        "p ls pp-term": "pp-commands\\p-ls.py",  # new
        "p ls p-terminal": "pp-commands\\p-ls-p-terminal.py",  # new
        "p ls mavis": "pp-commands\\p-ls-mavis.py",  # new
        "p ls mavis-web": "pp-commands\\p-ls-mavis-web.py",  # new
        "p ls simon": "pp-commands\\p-ls-simon.py",  # new
        "models": "pp-commands\\models-ls.py",  # new
        "models ls": "pp-commands\\models-ls.py",  # new
        "p models": "pp-commands\\p-models-ls.py",  # new
        "p models ls": "pp-commands\\p-models-ls.py",  # new
        "p github p-terminal": "pp-commands\\p-github-p-terminal.py",  # new
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
        "p wikipedia": "pp-commands\\p-wikipedia.py",  # new
        "p youtube": "pp-commands\\p-youtube.py",  # new
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
        "p mavis": "pp-commands\\p-github-mavis.py",  # new
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
        "p vswhere": "pp-commands\\p-vswhere.py",  # new
        "p speedtest": "pp-commands\\p-speedtest.py",  # new
        "install 3d-slicer": "run\\simon\\3d-slicer\\install-3d-slicer.py", # new
        "run 3d-slicer": "run\\simon\\3d-slicer\\run-3d-slicer.py",  # new
        "install simon": "run\\simon\\install-simon-1.py",  # new
        "run simon": "mavis-run-jup\\run-jup.py",  # new
        "jupyter --version": "pp-commands\\jupyter-version.py", # new
        "grafana --version": "pp-commands\\grafana-version.py",  # new
        "3d-slicer --version": "pp-commands\\3d-slicer-version.py",  # new
        "doctor": "pp-commands\\doctor.py", # new
        "hole doctor": "pp-commands\\doctor-hole.py",  # new
        "fun": "pp-commands\\fun-matrix.py",  # new
        "fun ls": "pp-commands\\fun-ls.py",  # new
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
        "fun train t": "pp-commands\\fun-train-t.py",  # new
        "fun install games": "pp-commands\\fun-install-games.py",  # new
        "fun bastet": "pp-commands\\fun-bashtet.py",  # new
        "fun chess": "pp-commands\\fun-gnuchess.py",  # new
        "fun moon-buggy": "pp-commands\\fun-moon-buggy.py",  # new
        "fun nethack": "pp-commands\\fun-nethack-console.py",  # new
        "fun nsnake": "pp-commands\\fun-nsnake.py",  # new
        "fun pacman": "pp-commands\\fun-pacman4console.py",  # new
        "fun tictactoe": "pp-commands\\fun-tictactoe-ng.py",  # new
        "fun tint": "pp-commands\\fun-tint.py",  # new
        "fun tetris": "pp-commands\\fun-vitetris.py",  # new
        "fun calculator": "pp-commands\\fun-calc.py",  # new
        "fun calc": "pp-commands\\fun-calc.py",  # new
        "fun install calculator": "pp-commands\\fun-install-calc.py",  # new
        "fun matrix": "pp-commands\\fun-matrix.py",  # new
        "fun matrix green": "pp-commands\\fun-matrix-green.py",  # new
        "fun aquarium": "pp-commands\\fun-asciiquarium.py",  # new
        "fun aqua": "pp-commands\\fun-asciiquarium.py",  # new
        "fun bb": "pp-commands\\fun-bb.py",  # new
        "install cool pin": "pp-commands\\theme-pcc.py", # new
        "install cool pin-2": "pp-commands\\theme-pcc-2.py",  # new
        "install cool pin-3": "pp-commands\\theme-pcc-3.py",  # new
        "install cool pin-4": "pp-commands\\theme-pcc-4.py",  # new
        "install cool pin-5": "pp-commands\\theme-pcc-5.py",  # new
        "install cool pin-6": "pp-commands\\theme-pcc-6.py",  # new
        "install cool pin-7": "pp-commands\\theme-pcc-7.py",  # new
        "install cool pin-8": "pp-commands\\theme-pcc-8.py",  # new
        "install cool pin-9": "pp-commands\\theme-pcc-9.py",  # new
        "install cool pin-10": "pp-commands\\theme-pcc-10.py",  # new
        "install cool pin-11": "pp-commands\\theme-pcc-11.py",  # new
        "install cool pin-13": "pp-commands\\theme-pcc-13.py",  # new
        "install cool pin-14": "pp-commands\\theme-pcc-14.py",  # new
        "install cool pin-15": "pp-commands\\theme-pcc-15.py",  # new
        "install cool pin-16": "pp-commands\\theme-pcc-16.py",  # new
        "install cool pin-17": "pp-commands\\theme-pcc-17.py",  # new
        "install cool pin-18": "pp-commands\\theme-pcc-18.py",  # new
        "install cool pin-19": "pp-commands\\theme-pcc-19.py",  # new
        "install cool pin-20": "pp-commands\\theme-pcc-20.py",  # new
        "install cool pin-21": "pp-commands\\theme-pcc-21.py",  # new
        "install cool pin-22": "pp-commands\\theme-pcc-22.py",  # new
        "install cool pin-23": "pp-commands\\theme-pcc-23.py",  # new
        "run githubdesktop": "pp-commands\\run-githubdesktop.py", # new
        "run dockerdesktop": "pp-commands\\run-dockerdesktop.py", # new
        "run pycharm": "pp-commands\\run-pycharm.py",  # new
        "run vs-code": "pp-commands\\run-vs-code.py",  # new
        "run vs": "pp-commands\\run-vs.py",  # new
        "p map": "pp-commands\\p-map.py", # new
        "p weather": "pp-commands\\p-weather.py", # new
        "p you": "pp-commands\\you.py",  # new
        "p qwen": "pp-commands\\qwen.py",  # new
        "p poe": "pp-commands\\poe.py",  # new
        "p perplexity": "pp-commands\\perplexity.py",  # new
        "p mistral": "pp-commands\\mistral.py",  # new
        "p jasper": "pp-commands\\jasper.py",  # new
        "p grok": "pp-commands\\grok.py",  # new
        "p gemini": "pp-commands\\gemini.py",  # new
        "p deepseek": "pp-commands\\deepseek.py",  # new
        "p copy": "pp-commands\\copy.py",  # new
        "p claude": "pp-commands\\claude.py",  # new
        "p chatgpt": "pp-commands\\chatgpt.py",  # new
        "run mavis main": "pp-commands\\run-mavis-main.py", # new
        "run mavis main fast": "pp-commands\\run-mavis-main-fast.py",  # new
        "htop": "pp-commands\\htop.py",  # new
        "bashtop": "pp-commands\\bashtop.py", # new
        "taskmanager": "pp-commands\\bashtop.py",  # new
        "btop": "pp-commands\\btop.py",  # new
        "atop": "pp-commands\\atop.py",  # new
        "emacs": "pp-commands\\emacs.py",  # new
        "vim": "pp-commands\\vim.py",  # new
        "nano": "pp-commands\\nano.py",  # new
        "dstat": "pp-commands\\dstat.py",  # new
        "nmon": "pp-commands\\nmon.py",  # new
        "glances": "pp-commands\\glances.py",  # new
        "iftop": "pp-commands\\iftop.py",  # new
        "nethogs": "pp-commands\\nethogs.py",  # new
        "bmon": "pp-commands\\bmon.py",  # new
        "tcpdump": "pp-commands\\tcpdump.py",  # new
        "speedtest-cli": "pp-commands\\speedtest-cli.py",  # new
        "ncdu": "pp-commands\\ncdu.py",  # new
        "duf": "pp-commands\\duf.py",  # new
        "lsblk": "pp-commands\\lsblk.py",  # new
        "iotop": "pp-commands\\iotop.py",  # new
        "fzf": "pp-commands\\fzf.py",  # new
        "fd": "pp-commands\\fd.py",  # new
        "ripgrep": "pp-commands\\ripgrep.py",  # new
        "tmux": "pp-commands\\tmux.py",  # new
        "bat": "pp-commands\\bat.py",  # new
        "exa": "pp-commands\\exa.py",  # new
        "tldr": "pp-commands\\tldr.py",  # new
        "gitui": "pp-commands\\gitui.py",  # new
        "lazygit": "pp-commands\\lazygit.py",  # new
        "zoxide": "pp-commands\\zoxide.py",  # new
        "starship": "pp-commands\\starship.py",  # new
        "nala": "pp-commands\\nala.py",  # new
        "bpytop": "pp-commands\\bpytop.py", # new
        "belnder": "pp-commands\\belnder.py", # new
        "clion": "pp-commands\\clion.py", # new
        "community": "pp-commands\\community.py", # new
        "intellij": "pp-commands\\intellij.py", # new
        "pycharm": "pp-commands\\pycharm.py", # new
        "rider": "pp-commands\\rider.py", # new
        "vs-code": "pp-commands\\vs-code.py", # new
        "webstorm": "pp-commands\\webstorm.py", # new
        "golab": "pp-commands\\golab.py",  # new
        "phpstorm": "pp-commands\\phpstorm.py",  # new
        "githubdesktop": "pp-commands\\githubdesktop.py",  # new
        "nvim": "pp-commands\\nvim.py", # new
        "code": "pp-commands\\code.py", # new
        "micro": "pp-commands\\micro.py", # new
        "gedit": "pp-commands\\gedit.py", # new
        "update": "pp-commands\\update.py", # new
        "update pp-term": "pp-commands\\updade.py",  # new
        "kakoune": "pp-commands\\kakoune.py",  # new
        "helix": "pp-commands\\helix.py",  # new
        "jed": "pp-commands\\jed.py",  # new
        "joe": "pp-commands\\joe.py",  # new
        "mg": "pp-commands\\mg.py",  # new
        "acme": "pp-commands\\acme.py",  # new
        "geany": "pp-commands\\geany.py",  # new
        "kate": "pp-commands\\kate.py",  # new
        "mousepad": "pp-commands\\mousepad.py",  # new
        "xed": "pp-commands\\xed.py",  # new
        "entr": "pp-commands\\entr.py",  # new
        "asdf": "pp-commands\\asdf.py",  # new
        "direnv": "pp-commands\\direnv.py",  # new
        "nmap": "pp-commands\\nmap.py",  # new
        "iperf3": "pp-commands\\iperf3.py",  # new
        "glow": "pp-commands\\glow.py",  # new
        "ranger": "pp-commands\\ranger.py",  # new
        "espanso": "pp-commands\\espanso.py",  # new
        "plasma-workspace": "pp-commands\\plasma-workspace.py",  # new
        "syncthing": "pp-commands\\syncthing.py",  # new
        "flatpak": "pp-commands\\flatpak.py",  # new
        "atom": "pp-commands\\atom.py",  # new
        "lite-xl": "pp-commands\\lite-xl.py",  # new
        "weather": "pp-commands\\weather.py"  # new
    }

    # Custom command launcher
    if user_input in commands:
        script_path = f"C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\{commands[user_input]}"

        # Maximale CPU-Priorität setzen (Windows-spezifisch)
        if platform.system() == "Windows":
            script_priority = psutil.BELOW_NORMAL_PRIORITY_CLASS  # Höhere Priorität einstellen
        else:
            script_priority = psutil.NORMAL_PRIORITY_CLASS

        # Wenn der Benutzer keine Batch-Datei hat, den Python-Skript ausführen
        if not user_input.endswith(".bat"):
            process = multiprocessing.Process(target=run_script, args=(python_path, script_path))
            process.start()
            process.join()
        else:
            # Batch-Datei ausführen
            process = multiprocessing.Process(target=run_script, args=(script_path,))
            process.start()
            process.join()

        return True

    # Built-in Commands Erweiterung
    if user_input.lower() in ["cls", "clear"]:
        os.system("cls" if os.name == "nt" else "clear")
        return True

    if user_input.startswith("cd "):
        path = user_input[3:].strip()
        change_directory(path)
        return True

    if user_input.lower() == "cd":
        path = os.path.expanduser("~")
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
            print(f"[{timestamp()}] [ERROR] {str(e)}", file=sys.stderr)
        return True

    if user_input.startswith("del "):
        target = user_input[4:].strip()
        delete_target(target)
        return True

    if user_input.startswith("rm "):
        target = user_input[3:].strip()
        delete_target(target)
        return True

    if user_input.startswith("echo "):
        print(user_input[5:].strip())
        return True

    """
    if "=" in user_input:
        var, value = map(str.strip, user_input.split("=", 1))
        os.environ[var] = value
        print(f"{blue}Environment variable set{reset}: {var}={value}")
        return True
    """

    if user_input.startswith(("type ", "cat ")):
        try:
            with open(user_input.split(maxsplit=1)[1].strip(), "r", encoding="utf-8") as f:
                print(f.read())
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] {str(e)}", file=sys.stderr)
        return True

    if user_input.lower() == "exit":
        print(f"{yellow}Exiting PP-Terminal... Goodbye {user_name}!{reset}")
        sys.exit(0)

    if user_input.lower() == "git ls":

        command = f"git log --oneline --graph --color --all --decorate"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True
    
    if user_input.lower() == "git ls all":

        command = f"git log --graph --all --color --decorate --pretty=format:'%C(yellow)%h%Creset - %Cgreen%ad%Creset - %s %C(red)[%an]%Creset' --date=short"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git pretty":

        command = f"git log --pretty=format:'%Cred%h%Creset - %Cgreen%cd%Creset - %s %C(bold blue)<%an>%Creset' --date=short"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git tig":

        command = f"tig"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True


    if user_input.lower() == "git lazy":

        command = f"lazygit"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git ls hole":

        command = "gitk --all"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git status":

        command = "git status -sb"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git diff":

        command = "git diff --color-word"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git branches":

        command = "git branch -vv -a"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git stash":

        command = "git stash list --pretty=format:'%C(yellow)%gd%Creset %Cgreen%cr%Creset %s %C(red)[%an]'"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True, text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "cloc .":

        command = f"wsl cloc ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count":

        command = f"wsl cloc ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "disk usage":

        command = f"wsl du -sh ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "tree2":

        command = f"wsl tree -L 2"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "find py":

        command = f"wsl find . -name '*.py'"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "grep ":

        user_input = user_input[5:]
        command = f"wsl grep -rnw . -e '{user_input}'"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "lint":

        command = f"wsl pylint ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "make":

        command = f"wsl make"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "format":

        command = f"wsl black ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "top":

        command = f"wsl top"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "disk":

        command = f"wsl df -h"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("nano "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("emacs "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("vim "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("nvim "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("micro "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("code "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("gedit "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("kakoune "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("helix "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("jed "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("joe "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("mg "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("acme "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("geany "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("kate "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("ncdu "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("tldr "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("bat "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("exa "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("fzf "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("fd "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("tmux "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("entr "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("asdf "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("direnv "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("nmap "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("iperf3 "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("speedtest-cli "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("glow "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("ranger "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("zoxide "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("nala "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("espanso "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("plasma-workspace "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("syncthing "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("flatpak "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("mousepad "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("xed "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("atom "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("lite-xl "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

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
            print(f"[{timestamp()}] [ERROR] Could not retrieve IP address")
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

    if user_input.lower() == "weather easy":
        get_weather()
        return True

    if user_input.startswith("open "):
        path = user_input[5:].strip()

        # Check if file exists
        if not os.path.exists(path):
            print(f"[{timestamp()}] [ERROR] File not found: {path}")
            return False

        try:
            if sys.platform.startswith("win"):
                os.startfile(path)  # Windows
            elif sys.platform.startswith("darwin"):
                subprocess.Popen(["open", path])  # macOS
            else:
                subprocess.Popen(["xdg-open", path])  # Linux
            print(f"[{timestamp()}] [PASS] Opened: {path}")
            return True
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Error while opening: {e}")
            return False

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
        handle_history_command()
        return True

    if user_input.startswith("search "):
        try:
            # Teilen Sie die Eingabe in Befehl, Dateiname und Schlüsselwort auf
            parts = user_input.split(maxsplit=2)
            if len(parts) < 3:
                print(f"[{timestamp()}] [INFO] Usage: search <filename> <keyword>")
                return True

            _, filename, keyword = parts

            # Öffnen Sie die Datei mit UTF-8-Kodierung
            with open(filename, "r", encoding="utf-8") as file:
                lines = file.readlines()

            # Suchen Sie in jeder Zeile nach dem Schlüsselwort, ohne Berücksichtigung der Groß- und Kleinschreibung
            matches = []
            for i, line in enumerate(lines, start=1):
                if keyword.lower() in line.lower():
                    matches.append(f"Line {i}: {line.rstrip()}")

            # Ausgabe der Ergebnisse oder einer entsprechenden Meldung, wenn keine Übereinstimmungen gefunden werden
            if matches:
                print("\n".join(matches))
            else:
                print(f"[{timestamp()}] [ERROR] No matches found.")

        except FileNotFoundError:
            print(f"[{timestamp()}] [ERROR] File not found: {filename}")
        except PermissionError:
            print(f"[{timestamp()}] [ERROR] No permission to read: {filename}")
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Error during search: {str(e)}")
        return True

    # Erstellen Sie einen Zip-Ordner (optimiert für Windows)
    if user_input.startswith("zip "):
        try:
            # Befehl und Ordner aus der Eingabe extrahieren
            parts = user_input.split(maxsplit=1)
            if len(parts) < 2:
                print("Usage: zip <folder>")
                return True

            _, folder = parts
            # Normalisieren Sie den Pfad, besonders nützlich unter Windows
            folder_path = os.path.normpath(folder)

            # Überprüfen Sie, ob der Ordner vorhanden ist
            if not os.path.isdir(folder_path):
                print(f"{red}Error: Folder does not exist{reset}: {folder_path}")
                return True

            # Erstellen Sie das Archiv. Der Archivname entspricht dem Ordnernamen ohne Erweiterung.
            shutil.make_archive(folder_path, 'zip', folder_path)
            print(f"{green}Folder successfully zipped!{reset}")

        except FileNotFoundError:
            print(f"[{timestamp()}] [ERROR] Folder not found: {folder_path}")
        except PermissionError:
            print(f"[{timestamp()}] [ERROR] No permission to access the folder: {folder_path}")
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] while zipping the folder: {str(e)}")
        return True

    # Entpacken Sie ein Archiv (optimiert für Windows mit erweiterten Prüfungen)
    if user_input.startswith("unzip "):
        try:
            # Extrahieren Sie den Befehl und die ZIP-Datei aus der Eingabe
            parts = user_input.split(maxsplit=1)
            if len(parts) < 2:
                print(f"[{timestamp()}] [INFO] Usage: unzip <zip_file_path>")
                return True

            _, zip_path = parts
            # Normalisieren Sie den Pfad, besonders nützlich unter Windows
            zip_path = os.path.normpath(zip_path)

            # Überprüfen Sie, ob die Zip-Datei vorhanden ist und eine Datei ist
            if not os.path.isfile(zip_path):
                print(f"[{timestamp()}] [ERROR] File does not exist: {zip_path}")
                return True

            # Zielverzeichnis anhand des Dateinamens ohne Erweiterung ermitteln
            extract_dir = os.path.splitext(zip_path)[0]

            # Öffnen und entpacken Sie das Zip-Archiv
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)

            print(f"{green}Archive successfully extracted to:{reset} {extract_dir}")

        except zipfile.BadZipFile:
            print(f"[{timestamp()}] [ERROR] Invalid zip archive: {zip_path}")
        except PermissionError:
            print(f"[{timestamp()}] [ERROR] No permission to access the file: {zip_path}")
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Error while extracting:{reset} {str(e)}")
        return True

    # RAM- und CPU-Status
    if user_input.lower() == "sysinfo":
        print(f"{blue}CPU Usage{reset}: {psutil.cpu_percent()}%")
        print(f"{blue}RAM Usage{reset}: {psutil.virtual_memory().percent}%")
        return True

    # Inhalt der Zwischenablage festlegen (verbessert durch erweiterte Validierung und Fehlerbehandlung)
    if user_input.startswith("clip set "):
        try:
            # Extrahieren Sie den zu kopierenden Text und entfernen Sie führende und nachfolgende Leerzeichen
            text = user_input[len("clip set "):].strip()
            if not text:
                print(f"[{timestamp()}] [INFO] Usage: clip set <text>")
                return True

            # Text in die Zwischenablage kopieren
            pyperclip.copy(text)
            print(f"{green}Text successfully copied to clipboard!{reset}")
        except ImportError:
            print(
                f"[{timestamp()}] [ERROR] pyperclip module is not installed. Please install it with 'pip install pyperclip'")
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Error while copying to clipboard{reset}: {str(e)}")
        return True

    # Zwischenablage lesen
    if user_input.lower() == "clip get":
        print(pyperclip.paste())
        return True

    if user_input.lower().startswith("ping "):
        import re
        # Ziel extrahieren und validieren
        target = user_input.split(maxsplit=1)[1].strip()
        if not re.fullmatch(r"[A-Za-z0-9\.-]+", target):
            logging.error("Invalid destination: %r", target)
            return True

        # OS-gerechte Anzahl-Flag
        count_flag = "-n" if subprocess.os.name == "nt" else "-c"
        cmd = ["ping", count_flag, "4", target]

        try:
            # Konsolen-Codepage ermitteln (nur unter Windows relevant)
            if subprocess.os.name == "nt":
                cp = ctypes.windll.kernel32.GetConsoleOutputCP()
                encoding = f"cp{cp}"
            else:
                encoding = "utf-8"

            # Subprozess starten, Ausgabe als Bytes
            proc = subprocess.run(
                cmd,
                capture_output=True,
                timeout=10
            )

            # Jetzt selbst decodieren mit der passenden Codepage
            stdout = proc.stdout.decode(encoding, errors="replace")
            stderr = proc.stderr.decode(encoding, errors="replace")
        except subprocess.TimeoutExpired:
            logging.error("The ping command took too long and was aborted.")
        except Exception as e:
            logging.error("Error when running ping: %s", e)
        else:
            # Ausgabe und Exit-Code loggen
            if stdout:
                logging.info("Ping output:\n%s", stdout.strip())
            if stderr:
                logging.warning("Ping stderr:\n%s", stderr.strip())
            if proc.returncode != 0:
                logging.warning("Ping failed (Exit-Code %d).", proc.returncode)
        return True

    # Papierkorb leeren
    if user_input.lower() == "emptytrash":
        try:
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000001)
            print(f"[{timestamp()}] [PASS] Recycle Bin emptied!")
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Error emptying trash: {str(e)}")
        return True

    if user_input.lower() == "themes":
        print("dark, light, main, hackerman, glass, aurelia, alternative, aptscience, cyberlife, ubuntu, nord, dracula, solarized_dark, gruvbox_dark, monokai, one_dark, material_dark, tokyo_night, arc_dark, ayu_mirage", "spiderman", "p_term", "mavis_1", "mavis_3", "mavis_4", "green", "red", "blue", "fallout_pipboy")
        return True

    if user_input.lower() == "pin":
        print("main", "main-3", "main-4", "evil", "cool", "cool-3", "cool-4", "cool-5", "cool-6", "cool-8", "cool-9", "cool-10", "cool-11", "cool-12", "cool-13", "cool-14", "cool-15", "cool-16", "cool-18", "cool-19", "cool-20", "cool-21", "cool-23")
        return True

    if user_input.startswith("launch "):
        command_str = user_input[len("launch "):].strip()

        # Leere Eingabe abfangen
        if not command_str:
            logging.error("[ERROR] No program specified after 'launch'.")
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

            logging.info("[INFO] Program launched: %s", command_str)
            return True  # Erfolgreiche Ausführung, Rückgabe True

        except FileNotFoundError:
            logging.error("[ERROR] Program not found: %s", command_str)
        except Exception as e:
            logging.exception("[ERROR] Error launching %s: %s", command_str, str(e))

        return False

    # Speedtest
    if user_input.lower() == "speedtest":
        try:
            # Ladebalken während der Speedtest läuft
            loading_bar("Running speedtest", 5)

            # Speedtest-Instanz
            st = speedtest.Speedtest()

            # Download- und Upload-Geschwindigkeiten in Mbit/s
            download = st.download() / 1_000_000  # Konvertieren von Bits in Mbit/s
            upload = st.upload() / 1_000_000  # Konvertieren von Bits in Mbit/s

            # Ping abrufen (Latenz)
            ping = st.results.ping

            # Drucken Sie die Ergebnisse in einem coolen Format aus
            print(f"{blue}Download{reset}: {download:.2f} Mbps")
            print(f"{blue}Upload{reset}: {upload:.2f} Mbps")
            print(f"{blue}Ping{reset}: {ping} ms")

            return True

        except Exception as e:
            # Wenn etwas schief geht, zeigen Sie den Fehler
            print(f"[{timestamp()}] [ERROR] Whoops, something went wrong with the speedtest: {e}")
            return False

    if user_input == "setting":
        subprocess.run("start ms-settings:", shell=True, check=False)

    if user_input == "workplace":
        subprocess.run("start ms-settings:workplace", shell=True, check=False)

    if user_input == "emailandaccounts":
        subprocess.run("start ms-settings:emailandaccounts", shell=True, check=False)

    if user_input == "otherusers":
        subprocess.run("start ms-settings:otherusers", shell=True, check=False)

    if user_input == "assignedaccess":
        subprocess.run("start ms-settings:assignedaccess", shell=True, check=False)

    if user_input == "signinoptions":
        subprocess.run("start ms-settings:signinoptions", shell=True, check=False)

    if user_input == "sync":
        subprocess.run("start ms-settings:sync", shell=True, check=False)

    if user_input == "yourinfo":
        subprocess.run("start ms-settings:yourinfo", shell=True, check=False)

    if user_input == "hello-face":
        subprocess.run("start ms-settings:signinoptions-launchfaceenrollment", shell=True, check=False)

    if user_input == "hello-fingerprint":
        subprocess.run("start ms-settings:signinoptions-launchfingerprintenrollment", shell=True, check=False)

    if user_input == "appsfeatures":
        subprocess.run("start ms-settings:appsfeatures", shell=True, check=False)

    if user_input == "appsfeatures-app":
        subprocess.run("start ms-settings:appsfeatures-app", shell=True, check=False)

    if user_input == "appsforwebsites":
        subprocess.run("start ms-settings:appsforwebsites", shell=True, check=False)

    if user_input == "defaultapps":
        subprocess.run("start ms-settings:defaultapps", shell=True, check=False)

    if user_input == "optionalfeatures":
        subprocess.run("start ms-settings:optionalfeatures", shell=True, check=False)

    if user_input == "maps":
        subprocess.run("start ms-settings:maps", shell=True, check=False)

    if user_input == "startupapps":
        subprocess.run("start ms-settings:startupapps", shell=True, check=False)

    if user_input == "videoplayback":
        subprocess.run("start ms-settings:videoplayback", shell=True, check=False)

    if user_input == "autoplay":
        subprocess.run("start ms-settings:autoplay", shell=True, check=False)

    if user_input == "bluetooth":
        subprocess.run("start ms-settings:bluetooth", shell=True, check=False)

    if user_input == "camera":
        subprocess.run("start ms-settings:camera", shell=True, check=False)

    if user_input == "mousetouchpad":
        subprocess.run("start ms-settings:mousetouchpad", shell=True, check=False)

    if user_input == "pen":
        subprocess.run("start ms-settings:pen", shell=True, check=False)

    if user_input == "printers":
        subprocess.run("start ms-settings:printers", shell=True, check=False)

    if user_input == "usb":
        subprocess.run("start ms-settings:usb", shell=True, check=False)

    if user_input == "display":
        subprocess.run("start ms-settings:display", shell=True, check=False)

    if user_input == "sound":
        subprocess.run("start ms-settings:sound", shell=True, check=False)

    if user_input == "notifications":
        subprocess.run("start ms-settings:notifications", shell=True, check=False)

    if user_input == "power":
        subprocess.run("start ms-settings:powersleep", shell=True, check=False)

    if user_input == "storage":
        subprocess.run("start ms-settings:storage", shell=True, check=False)

    if user_input == "multitasking":
        subprocess.run("start ms-settings:multitasking", shell=True, check=False)

    if user_input == "network-status":
        subprocess.run("start ms-settings:network-status", shell=True, check=False)

    if user_input == "wifi":
        subprocess.run("start ms-settings:network-wifi", shell=True, check=False)

    if user_input == "ethernet":
        subprocess.run("start ms-settings:network-ethernet", shell=True, check=False)

    if user_input == "vpn":
        subprocess.run("start ms-settings:network-vpn", shell=True, check=False)

    if user_input == "datausage":
        subprocess.run("start ms-settings:datausage", shell=True, check=False)

    if user_input == "privacy-microphone":
        subprocess.run("start ms-settings:privacy-microphone", shell=True, check=False)

    if user_input == "privacy-webcam":
        subprocess.run("start ms-settings:privacy-webcam", shell=True, check=False)

    if user_input == "privacy-location":
        subprocess.run("start ms-settings:privacy-location", shell=True, check=False)

    if user_input == "privacy-notifications":
        subprocess.run("start ms-settings:privacy-notifications", shell=True, check=False)

    if user_input == "windowsupdate":
        subprocess.run("start ms-settings:windowsupdate", shell=True, check=False)

    if user_input == "backup":
        subprocess.run("start ms-settings:backup", shell=True, check=False)

    if user_input == "recovery":
        subprocess.run("start ms-settings:recovery", shell=True, check=False)

    if user_input == "activation":
        subprocess.run("start ms-settings:activation", shell=True, check=False)

    if user_input == "fordevelopers":
        subprocess.run("start ms-settings:developers", shell=True, check=False)

    if user_input == "airplanemode":
        subprocess.run("start ms-settings:airplanemode", shell=True, check=False)

    if user_input == "cellular":
        subprocess.run("start ms-settings:cellular", shell=True, check=False)

    if user_input == "cloudstorage":
        subprocess.run("start ms-settings:cloudstorage", shell=True, check=False)

    if user_input == "language":
        subprocess.run("start ms-settings:language", shell=True, check=False)

    if user_input == "location":
        subprocess.run("start ms-settings:location", shell=True, check=False)

    if user_input == "lock":
        subprocess.run("start ms-settings:lock", shell=True, check=False)

    if user_input == "nfctransactions":
        subprocess.run("start ms-settings:nfctransactions", shell=True, check=False)

    if user_input == "proximity":
        subprocess.run("start ms-settings:privacy-proximity", shell=True, check=False)

    if user_input == "mobilehotspot":
        subprocess.run("start ms-settings:network-mobilehotspot", shell=True, check=False)

    if user_input == "proxy":
        subprocess.run("start ms-settings:network-proxy", shell=True, check=False)

    if user_input == "defender":
        subprocess.run("start ms-settings:windowsdefender", shell=True, check=False)

    if user_input == "privacy-contacts":
        subprocess.run("start ms-settings:privacy-contacts", shell=True, check=False)

    if user_input == "privacy-calendar":
        subprocess.run("start ms-settings:privacy-calendar", shell=True, check=False)

    if user_input == "privacy-callhistory":
        subprocess.run("start ms-settings:privacy-callhistory", shell=True, check=True)

    if user_input == "family":
        subprocess.run("start ms-settings:family", shell=True, check=False)

    if user_input == "gaming-gamebar":
        subprocess.run("start ms-settings:gaming-gamebar", shell=True, check=False)

    if user_input == "mixedreality-portal":
        subprocess.run("start ms-settings:mixedreality-portal", shell=True, check=False)

    if user_input == "easeofaccess":
        subprocess.run("start ms-settings:easeofaccess", shell=True, check=False)

    if user_input == "easeofaccess-narrator":
        subprocess.run("start ms-settings:easeofaccess-narrator", shell=True, check=False)

    if user_input == "easeofaccess-magnifier":
        subprocess.run("start ms-settings:easeofaccess-magnifier", shell=True, check=False)

    if user_input == "easeofaccess-closedcaptioning":
        subprocess.run("start ms-settings:easeofaccess-closedcaptioning", shell=True, check=False)

    if user_input == "easeofaccess-highcontrast":
        subprocess.run("start ms-settings:easeofaccess-highcontrast", shell=True, check=False)

    if user_input == "easeofaccess-speechrecognition":
        subprocess.run("start ms-settings:easeofaccess-speechrecognition", shell=True, check=False)

    if user_input == "easeofaccess-keyboard":
        subprocess.run("start ms-settings:easeofaccess-keyboard", shell=True, check=False)

    if user_input == "easeofaccess-mousepointer":
        subprocess.run("start ms-settings:easeofaccess-mousepointer", shell=True, check=False)

    if user_input == "easeofaccess-touch":
        subprocess.run("start ms-settings:easeofaccess-touch", shell=True, check=False)

    if user_input == "wirelessdisplay":
        subprocess.run("start ms-settings-connectabledevices:devicediscovery", shell=True, check=False)

    if user_input == "project":
        subprocess.run("start ms-settings:project", shell=True, check=False)

    if user_input == "tethering":
        subprocess.run("start ms-settings:network-tethering", shell=True, check=False)

    if user_input == "storagesense":
        subprocess.run("start ms-settings:storagesense", shell=True, check=False)

    if user_input == "batterysaver":
        subprocess.run("start ms-settings:batterysaver-settings", shell=True, check=False)

    if user_input == "autorotate":
        subprocess.run("start ms-settings:screenrotation", shell=True, check=False)

    if user_input == "dateandtime":
        subprocess.run("start ms-settings:dateandtime", shell=True, check=False)

    if user_input == "region":
        subprocess.run("start ms-settings:region", shell=True, check=False)

    if user_input == "speech":
        subprocess.run("start ms-settings:regionlanguage-speech", shell=True, check=False)

    if user_input == "typing":
        subprocess.run("start ms-settings:typing", shell=True, check=False)

    if user_input == "troubleshoot":
        subprocess.run("start ms-settings:troubleshoot", shell=True, check=False)

    if user_input == "recommendedtroubleshoot":
        subprocess.run("start ms-settings:troubleshoot-recommended", shell=True, check=False)

    if user_input == "windowsinsider":
        subprocess.run("start ms-settings:windowsinsider", shell=True, check=False)

    if user_input == "gaming-broadcasting":
        subprocess.run("start ms-settings:gaming-broadcasting", shell=True, check=False)

    if user_input == "gaming-gamedvr":
        subprocess.run("start ms-settings:gaming-gamedvr", shell=True, check=False)

    if user_input == "gaming-xboxnetworking":
        subprocess.run("start ms-settings:gaming-xboxnetworking", shell=True, check=False)

    if user_input == "mixedreality-settings":
        subprocess.run("start ms-settings:mixedreality-portal", shell=True, check=False)

    if user_input == "display-advanced":
        subprocess.run("start ms-settings:display-advanced", shell=True, check=False)

    if user_input == "defaultbrowsersettings":
        subprocess.run("start ms-settings:defaultbrowsersettings", shell=True, check=False)

    if user_input == "maps-downloadmaps":
        subprocess.run("start ms-settings:maps-downloadmaps", shell=True, check=False)

    if user_input == "sound-devices":
        subprocess.run("start ms-settings:sound-devices", shell=True, check=False)

    if user_input == "devices-touch":
        subprocess.run("start ms-settings:devices-touch", shell=True, check=False)

    if user_input == "devices-touchpad":
        subprocess.run("start ms-settings:devices-touchpad", shell=True, check=False)

    if user_input == "devicestyping-hwkbtextsuggestions":
        subprocess.run("start ms-settings:devicestyping-hwkbtextsuggestions", shell=True, check=False)

    if user_input == "privacy-feedback":
        subprocess.run("start ms-settings:privacy-feedback", shell=True, check=False)

    if user_input == "privacy-diagnostics":
        subprocess.run("start ms-settings:privacy-diagnostics", shell=True, check=False)

    if user_input == "cortana":
        subprocess.run("start ms-settings:cortana", shell=True, check=False)

    if user_input == "cortana-permissions":
        subprocess.run("start ms-settings:cortana-permissions", shell=True, check=False)

    if user_input == "cortana-windowssearch":
        subprocess.run("start ms-settings:cortana-windowssearch", shell=True, check=False)

    if user_input == "cortana-moredetails":
        subprocess.run("start ms-settings:cortana-moredetails", shell=True, check=False)

    if user_input == "controlcenter":
        subprocess.run("start ms-settings:controlcenter", shell=True, check=False)

    if user_input == "mobile-devices":
        subprocess.run("start ms-settings:mobile-devices", shell=True, check=False)

    if user_input == "fonts":
        subprocess.run("start ms-settings:fonts", shell=True, check=False)

    if user_input == "wheel":
        subprocess.run("start ms-settings:wheel", shell=True, check=False)

    if user_input == "appsfeatures-app?PFN=<YourAppPFN>":
        subprocess.run("start ms-settings:appsfeatures-app?PFN=YourAppPFN", shell=True, check=False)

    if user_input == "backup-deprecated":
        subprocess.run("start ms-settings:backup", shell=True, check=False)

    if user_input == "provisioning":
        subprocess.run("start ms-settings:provisioning", shell=True, check=False)

    if user_input == "about":
        subprocess.run("start ms-settings:about", shell=True, check=False)

    if user_input == "uninstallupdates":
        subprocess.run("start ms-settings:uninstallupdates", shell=True, check=False)

    if user_input == "manage-restartapps":
        subprocess.run("start ms-settings:appsforwebsites", shell=True, check=False)

    if user_input == "startsettings":
        subprocess.run("start ms-settings:personalization-start", shell=True, check=False)

    if user_input == "taskbar":
        subprocess.run("start ms-settings:personalization-taskbar", shell=True, check=False)

    if user_input == "themes":
        subprocess.run("start ms-settings:themes", shell=True, check=False)

    if user_input == "colors":
        subprocess.run("start ms-settings:colors", shell=True, check=False)

    if user_input == "lockscreen":
        subprocess.run("start ms-settings:personalization-lockscreen", shell=True, check=False)

    if user_input == "background":
        subprocess.run("start ms-settings:personalization-background", shell=True, check=False)

    if user_input == "volume":
        subprocess.run("start ms-settings:apps-volume", shell=True, check=False)

    if user_input == "defaultbrowsersettings":
        subprocess.run("start ms-settings:defaultbrowsersettings", shell=True, check=False)

    if user_input == "firewall":
        subprocess.run("start ms-settings:windowsdefender-firewall", shell=True, check=False)

    if user_input == "securitycenter":
        subprocess.run("start ms-settings:windowsdefender-securitycenter", shell=True, check=False)

    if user_input == "surfacehub":
        subprocess.run("start ms-settings:surfacehub", shell=True, check=False)

    if user_input == "windowsanywhere":
        subprocess.run("start ms-settings:windowsanywhere", shell=True, check=False)

    if user_input == "privacy-accountinfo":
        subprocess.run("start ms-settings:privacy-accountinfo", shell=True, check=False)

    if user_input == "privacy-calendars":
        subprocess.run("start ms-settings:privacy-calendar", shell=True, check=False)

    if user_input == "privacy-radios":
        subprocess.run("start ms-settings:privacy-radios", shell=True, check=False)

    if user_input == "privacy-multimedia":
        subprocess.run("start ms-settings:privacy-media", shell=True, check=False)

    if user_input == "privacy-feedback":
        subprocess.run("start ms-settings:privacy-feedback", shell=True, check=False)

    if user_input == "regionlanguage":
        subprocess.run("start ms-settings:regionlanguage", shell=True, check=False)

    if user_input == "speechtyping":
        subprocess.run("start ms-settings:privacy-speechtyping", shell=True, check=False)

    # Prozessliste
    if user_input.lower() == "ps":
        for proc in psutil.process_iter(['pid', 'name']):
            print(f"PID {proc.info['pid']}: {proc.info['name']}")
        return True

    if user_input.startswith("kill "):
        try:
            _, pid_str = user_input.split(maxsplit=1)
            pid = int(pid_str)
            process = psutil.Process(pid)
            process.terminate()
            print(f"[{timestamp()}] [INFO] Process {pid} has been terminated.")
        except ValueError:
            print(f"[{timestamp()}] [ERROR] Invalid PID: '{pid_str}' is not a valid number.")
        except psutil.NoSuchProcess:
            print(f"[{timestamp()}] [ERROR] No process with PID {pid} found.")
        except psutil.AccessDenied:
            print(f"[{timestamp()}] [ERROR] Permission denied: Unable to terminate process {pid}.")
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Terminating process: {str(e)}")
        return True

    # Datei herunterladen
    if user_input.startswith("download "):

        try:
            # URL aus Eingabe extrahieren
            _, url = user_input.split(maxsplit=1)
            file_name = Path(url).name

            # Download mit Fortschrittsfeedback
            loading_bar(f"Downloading {file_name}", 4)
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()

            # Write content in chunks
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)

            print(f"[{timestamp()}] [INFO] Downloaded {file_name}")
        except requests.HTTPError as http_err:
            print(f"[{timestamp()}] [ERROR] HTTP error during download: {http_err}")
        except requests.RequestException as req_err:
            print(f"[{timestamp()}] [ERROR] Request error during download: {req_err}")
        except Exception as err:
            print(f"[{timestamp()}] [ERROR] Unexpected error: {err}")
        return True

    # CPU Temperatur
    if user_input.lower() == "cputemp":
        """
        Returns the current CPU temperature in °C, or None if it cannot be determined.
        """
        try:
            # PowerShell command to query CPU temperature
            command = [
                "powershell.exe",
                "-Command",
                "(Get-WmiObject MSAcpi_ThermalZoneTemperature -Namespace 'root/wmi').CurrentTemperature / 10 - 273.15"
            ]

            # Execute the PowerShell command and capture the output
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()

            # Error handling
            if process.returncode != 0:
                print(f"[{timestamp()}] [ERROR] Error retrieving CPU temperature: {stderr}")
                return None

            # Process the output and return the temperature in °C
            try:
                temperature = float(stdout.strip())
                return temperature
            except ValueError:
                print(f"[{timestamp()}] [ERROR] Invalid output when retrieving CPU temperature.")
                return None

        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Error: {e}")
            return None

    # Chuck Norris Joke
    if user_input.lower() == "chucknorris":
        try:
            joke = requests.get("https://api.chucknorris.io/jokes/random").json()['value']
            print(f"{blue}Chuck Norris says{reset}: {joke}")
        except:
            print(f"[{timestamp()}] [ERROR] Couldn't fetch Chuck Norris joke!")
        return True

    # Theme Wechsel
    if user_input.startswith("theme "):
        switch_theme(user_input)
        return True

    # Temp Dateien löschen
    if user_input.lower() == "cleantemp":
        temp = os.getenv('TEMP')
        shutil.rmtree(temp, ignore_errors=True)
        print(f"[{timestamp()}] [INFO] Temporary files cleaned!")
        return True

    # Selbst Update - soon
    if user_input.lower() == "selfupdate":
        print(f"[{timestamp()}] [INFO] Checking for updates...")
        loading_bar("Updating", 4)
        print(f"[{timestamp()}] [PASS] PP-Terminal updated! (demo mode)")
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
        print(f"[{timestamp()}] [INFO] Starting Python REPL. Type 'exit()' to quit.")
        code.interact(local=dict(globals(), **locals()))
        return True

    if user_input.startswith("pb "):
        # Remove "pb " and strip any surrounding whitespace
        user_input = user_input[3:].strip()

        # Check if the input is not empty
        if not user_input:
            print(f"[{timestamp()}] [INFO] Please provide a valid URL after 'pb '.")
            return

        # Create the full URL
        url = f"https://{user_input}"

        # Try to open the URL in the browser
        try:
            webbrowser.open(url)
            print(f"[{timestamp()}] [INFO] The page is now opening: {url}")
            return True

        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Error opening the URL: {e}")
            return True

    languages = {
        "afrikaans": "af",
        "albanian": "sq",
        "amharic": "am",
        "arabic": "ar",
        "armenian": "hy",
        "assamese": "as",
        "aymara": "ay",
        "azerbaijani": "az",
        "bambara": "bm",
        "basque": "eu",
        "belarusian": "be",
        "bengali": "bn",
        "bhojpuri": "bho",
        "bosnian": "bs",
        "bulgarian": "bg",
        "catalan": "ca",
        "cebuano": "ceb",
        "chichewa": "ny",
        "chinese (simplified)": "zh-CN",
        "chinese (traditional)": "zh-TW",
        "corsican": "co",
        "croatian": "hr",
        "czech": "cs",
        "danish": "da",
        "dhivehi": "dv",
        "dogri": "doi",
        "dutch": "nl",
        "english": "en",
        "esperanto": "eo",
        "estonian": "et",
        "ewe": "ee",
        "filipino": "tl",
        "finnish": "fi",
        "french": "fr",
        "frisian": "fy",
        "galician": "gl",
        "georgian": "ka",
        "german": "de",
        "greek": "el",
        "guarani": "gn",
        "gujarati": "gu",
        "haitian creole": "ht",
        "hausa": "ha",
        "hawaiian": "haw",
        "hebrew": "iw",
        "hindi": "hi",
        "hmong": "hmn",
        "hungarian": "hu",
        "icelandic": "is",
        "igbo": "ig",
        "ilocano": "ilo",
        "indonesian": "id",
        "irish": "ga",
        "italian": "it",
        "japanese": "ja",
        "javanese": "jw",
        "kannada": "kn",
        "kazakh": "kk",
        "khmer": "km",
        "kinyarwanda": "rw",
        "konkani": "gom",
        "korean": "ko",
        "krio": "kri",
        "kurdish (kurmanji)": "ku",
        "kurdish (sorani)": "ckb",
        "kyrgyz": "ky",
        "lao": "lo",
        "latin": "la",
        "latvian": "lv",
        "lingala": "ln",
        "lithuanian": "lt",
        "luganda": "lg",
        "luxembourgish": "lb",
        "macedonian": "mk",
        "maithili": "mai",
        "malagasy": "mg",
        "malay": "ms",
        "malayalam": "ml",
        "maltese": "mt",
        "maori": "mi",
        "marathi": "mr",
        "meiteilon (manipuri)": "mni-Mtei",
        "mizo": "lus",
        "mongolian": "mn",
        "myanmar": "my",
        "nepali": "ne",
        "norwegian": "no",
        "odia (oriya)": "or",
        "oromo": "om",
        "pashto": "ps",
        "persian": "fa",
        "polish": "pl",
        "portuguese": "pt",
        "punjabi": "pa",
        "quechua": "qu",
        "romanian": "ro",
        "russian": "ru",
        "samoan": "sm",
        "sanskrit": "sa",
        "scots gaelic": "gd",
        "sepedi": "nso",
        "serbian": "sr",
        "sesotho": "st",
        "shona": "sn",
        "sindhi": "sd",
        "sinhala": "si",
        "slovak": "sk",
        "slovenian": "sl",
        "somali": "so",
        "spanish": "es",
        "sundanese": "su",
        "swahili": "sw",
        "swedish": "sv",
        "tajik": "tg",
        "tamil": "ta",
        "tatar": "tt",
        "telugu": "te",
        "thai": "th",
        "tigrinya": "ti",
        "tsonga": "ts",
        "turkish": "tr",
        "turkmen": "tk",
        "twi": "ak",
        "ukrainian": "uk",
        "urdu": "ur",
        "uyghur": "ug",
        "uzbek": "uz",
        "vietnamese": "vi",
        "welsh": "cy",
        "xhosa": "xh",
        "yiddish": "yi",
        "yoruba": "yo",
        "zulu": "zu"
    }

    if user_input.startswith("pt "):
        payload = user_input[3:].strip()  # Entfernt das Präfix 'pb ' -> "german->english hallo"

        if ' ' in payload and '->' in payload:
            lang_part, text = payload.split(' ', 1)  # Split "german->english" und den Text
            if '->' in lang_part:
                source_str, target_str = lang_part.split('->')  # Split "german" und "english"
                source = source_str.lower()
                target = target_str.lower()

                # Überprüfen, ob die angegebenen Sprachen in der Liste enthalten sind
                if source in languages and target in languages:
                    try:
                        # Übersetzung durchführen
                        result = GoogleTranslator(
                            source=languages[source],
                            target=languages[target]
                        ).translate(text)

                        print(f"Translation ({source} -> {target}): {result}")
                    except Exception as e:
                        print(f"[{timestamp()}] [ERROR] Error during translation: {e}")
                else:
                    print(f"[{timestamp()}] [ERROR] Language not supported.")
            else:
                print(f"[{timestamp()}] [ERROR] Invalid language format (e.g., german->english).")
        else:
            print(f"[{timestamp()}] [ERROR] Invalid command. Correct format: pb <source>-><target> <text>")

        return True

    if user_input.startswith("pa "):
        user_input = user_input[3:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa qwen3:0.6b "):
        user_input = user_input[14:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_qwen0_6(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa qwen3:1.7b "):
        user_input = user_input[14:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_qwen1_7(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa qwen3:4b "):
        user_input = user_input[12:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_qwen4(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa qwen3:8b "):
        user_input = user_input[12:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_qwen8(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa qwen3:14b "):
        user_input = user_input[13:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa qwen3:32b "):
        user_input = user_input[13:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_qwen32(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa qwen3:30b "):
        user_input = user_input[13:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_qwen30(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa qwen3:235b "):
        user_input = user_input[14:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_qwen235(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa llama4:scout "):
        user_input = user_input[16:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_llama4_scout(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa llama4:maverick "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_llama4_maverick(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    return False


# Konstanten
SETTINGS_PATH = os.path.expandvars(
    r"%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
)
BACKUP_SUFFIX = ".bak"
THEMES_PATH = f'C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\themes.json'

# C:\Users\julia\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\RoamingState für Bilder

# Vordefinierte Farbschemata
COLOR_SCHEMES = {
    "dark": {
        "name": "Dark",
        "background": "#0F0F1A",
        "foreground": "#ffffff",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "cursorColor": "#E10600",
        "selectionBackground": "#0047AB",
    },
    "light": {
        "name": "Light",
        "background": "#FFFFFF",
        "foreground": "#000000",
        "black": "#FFFFFF",
        "red": "#C50F1F",
        "green": "#13A10E",
        "yellow": "#C19C00",
        "blue": "#0037DA",
        "purple": "#881798",
        "cyan": "#3A96DD",
        "white": "#000000",
        "brightBlack": "#0047AB",
        "brightRed": "#E74856",
        "brightGreen": "#16C60C",
        "brightYellow": "#F9F1A5",
        "brightBlue": "#3B78FF",
        "brightPurple": "#B4009E",
        "brightCyan": "#61D6D6",
        "brightWhite": "#FAFAFA",
        "cursorColor": "#E10600",
        "selectionBackground": "#2C2C3A",
    },
    "main": {
        "name": "Dark",
        "background": "#333333",
        "foreground": "#ffffff",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "cursorColor": "#E10600",
        "selectionBackground": "#0047AB",
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
    "glass": {
        "name": "glass",
        "background": "#333333",
        "foreground": "#ffffff",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "cursorColor": "#E10600",
        "selectionBackground": "#0047AB",
    },
    "glass-main": {
        "name": "glass-main",
        "background": "#333333",
        "foreground": "#ffffff",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "cursorColor": "#E10600",
        "selectionBackground": "#0047AB",
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
        "foreground": "#ffffff",
        "background": "#333333",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "cursorColor": "#E10600",
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
    },
    "spiderman": {
        "name": "spiderman",
        "background": "#0F0F1A",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "selectionBackground": "#0047AB",
        "foreground": "#FFFFFF"
    },
    "p_term": {
        "name": "p_term",
        "background": "#0F0F1A",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "foreground": "#FFFFFF"
    },
    "mavis_1": {
        "name": "mavis_1",
        "background": "#0F0F1A",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "foreground": "#FFFFFF"
    },
    "mavis_3": {
        "name": "mavis_3",
        "background": "#0F0F1A",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "foreground": "#FFFFFF"
    },
    "mavis_4": {
        "name": "mavis_4",
        "background": "#0F0F1A",
        "black": "#1B1B2F",
        "red": "#E10600",
        "green": "#00FF9F",
        "yellow": "#FFD000",
        "blue": "#1E90FF",
        "purple": "#A200FF",
        "cyan": "#00CFFF",
        "white": "#FFFFFF",
        "brightBlack": "#2C2C3A",
        "brightRed": "#FF2C1F",
        "brightGreen": "#4CFFB0",
        "brightYellow": "#FFE94D",
        "brightBlue": "#1fb1ff",
        "brightPurple": "#E87CFF",
        "brightCyan": "#4DE9FF",
        "brightWhite": "#FAFAFA",
        "foreground": "#FFFFFF"
    },
    "green": {
        "name": "green",
        "background": "#000000",
        "foreground": "#00FF00",
        "black": "#00FF00",
        "red": "#00FF00",
        "green": "#00FF00",
        "yellow": "#00FF00",
        "blue": "#00FF00",
        "purple": "#00FF00",
        "cyan": "#00FF00",
        "white": "#00FF00",
        "brightBlack": "#00FF00",
        "brightRed": "#00FF00",
        "brightGreen": "#00FF00",
        "brightYellow": "#00FF00",
        "brightBlue": "#00FF00",
        "brightPurple": "#00FF00",
        "brightCyan": "#00FF00",
        "brightWhite": "#00FF00",
        "cursorColor": "#00FF00"
    },
    "red": {
        "name": "red",
        "background": "#000000",
        "foreground": "#FF0000",
        "black": "#FF0000",
        "red": "#FF0000",
        "green": "#FF0000",
        "yellow": "#FF0000",
        "blue": "#FF0000",
        "purple": "#FF0000",
        "cyan": "#FF0000",
        "white": "#FF0000",
        "brightBlack": "#FF0000",
        "brightRed": "#FF0000",
        "brightGreen": "#FF0000",
        "brightYellow": "#FF0000",
        "brightBlue": "#FF0000",
        "brightPurple": "#FF0000",
        "brightCyan": "#FF0000",
        "brightWhite": "#FF0000",
        "cursorColor": "#FF0000"
    },
    "blue": {
        "name": "blue",
        "background": "#000000",
        "foreground": "#00BFFF",
        "black": "#00BFFF",
        "red": "#00BFFF",
        "green": "#00BFFF",
        "yellow": "#00BFFF",
        "blue": "#00BFFF",
        "purple": "#00BFFF",
        "cyan": "#00BFFF",
        "white": "#00BFFF",
        "brightBlack": "#00BFFF",
        "brightRed": "#00BFFF",
        "brightGreen": "#00BFFF",
        "brightYellow": "#00BFFF",
        "brightBlue": "#00BFFF",
        "brightPurple": "#00BFFF",
        "brightCyan": "#00BFFF",
        "brightWhite": "#00BFFF",
        "cursorColor": "#00BFFF"
    },
    "fallout_pipboy": {
        "name": "Fallout PipBoy",
        "background": "#000000",
        "black": "#000000",
        "blue": "#2C83FF",
        "brightBlack": "#003300",
        "brightBlue": "#1D55A6",
        "brightCyan": "#4DFFB8",
        "brightGreen": "#32CD32",
        "brightPurple": "#20755E",
        "brightRed": "#5BFF00",
        "brightWhite": "#99FF99",
        "brightYellow": "#8F7C48",
        "cursorColor": "#00FF00",
        "cyan": "#009151",
        "foreground": "#4D9154",
        "green": "#09A600",
        "purple": "#701D43",
        "red": "#3B3A23",
        "selectionBackground": "#415441",
        "white": "#59FF59",
        "yellow": "#8F7500"
    },
    "aurelia": {
        "name": "aurelia",
        "background": "#1a1a1a",
        "black": "#000000",
        "blue": "#579BD5",
        "brightBlack": "#797979",
        "brightBlue": "#9CDCFE",
        "brightCyan": "#2BC4E2",
        "brightGreen": "#1AD69C",
        "brightPurple": "#975EAB",
        "brightRed": "#EB2A88",
        "brightWhite": "#EAEAEA",
        "brightYellow": "#e9ad95",
        "cyan": "#00B6D6",
        "foreground": "#EA549F",
        "green": "#4EC9B0",
        "purple": "#714896",
        "red": "#E92888",
        "white": "#EAEAEA",
        "yellow": "#CE9178"
    },
    "alternative": {
        "name": "alternative",
        "black": "#101116",
        "red": "#ff5680",
        "green": "#00ff9c",
        "yellow": "#fffc58",
        "blue": "#00b0ff",
        "purple": "#d57bff",
        "cyan": "#76c1ff",
        "white": "#c7c7c7",
        "brightBlack": "#686868",
        "brightRed": "#ff6e67",
        "brightGreen": "#5ffa68",
        "brightYellow": "#fffc67",
        "brightBlue": "#6871ff",
        "brightPurple": "#d682ec",
        "brightCyan": "#60fdff",
        "brightWhite": "#ffffff",
        "background": "#1d2342",
        "foreground": "#b8ffe1"
    }
}

# Laden themenspezifischer Standardeinstellungen
try:
    with open(THEMES_PATH, 'r', encoding='utf-8') as f:
        THEME_DEFAULTS = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"[{timestamp()}] [ERROR] Error loading themes.json: {e}")
    THEME_DEFAULTS = {}


def run_script(*args):
    try:
        run(args, shell=True)
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error executing the script: {e}")


def create_backup(file_path: str) -> str:
    backup_path = file_path + BACKUP_SUFFIX
    shutil.copy2(file_path, backup_path)
    print(f"[{timestamp()}] [INFO] Backup created at: {backup_path}")
    return backup_path


def load_settings(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_settings(file_path: str, settings: dict) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)
    print(f"[{timestamp()}] [INFO] Settings saved to {file_path}")


def apply_color_scheme(settings: dict, scheme_name: str) -> None:
    scheme = COLOR_SCHEMES.get(scheme_name)
    if scheme:
        settings.setdefault('schemes', [])
        settings['schemes'] = [s for s in settings['schemes'] if s.get('name') != scheme.get('name')]
        settings['schemes'].append(scheme)
        for profile in settings.get('profiles', {}).get('list', []):
            profile['colorScheme'] = scheme.get('name')
        settings['theme'] = 'light' if 'light' in scheme_name else 'dark'
        print(f"[{timestamp()}] [INFO] Applied color scheme: {scheme.get('name')}")


def apply_theme_defaults(settings: dict, theme_name: str) -> None:
    defaults = THEME_DEFAULTS.get(theme_name, {}).get('defaults')
    if defaults:
        settings.setdefault('profiles', {})
        settings['profiles']['defaults'] = defaults
        print(f"[{timestamp()}] [INFO] Applied theme defaults for: {theme_name}")


def restart_terminal() -> None:
    subprocess.run(["wt.exe", "new-tab"], check=False)
    print(f"[{timestamp()}] [INFO] Terminal restarted with new tab.")


def switch_theme(user_input: str) -> bool:
    if not user_input.lower().startswith("theme "):
        return False

    _, choice = user_input.split(maxsplit=1)
    key = choice.lower().replace('-', '_')

    if key not in COLOR_SCHEMES and key not in THEME_DEFAULTS:
        print(f"[{timestamp()}] [ERROR] Unknown theme '{choice}'. Available: {', '.join(sorted(set(COLOR_SCHEMES) | set(THEME_DEFAULTS)))}")
        return True

    try:
        create_backup(SETTINGS_PATH)
        settings = load_settings(SETTINGS_PATH)

        if key in COLOR_SCHEMES:
            apply_color_scheme(settings, key)

        if key in THEME_DEFAULTS:
            apply_theme_defaults(settings, key)

        save_settings(SETTINGS_PATH, settings)
        print(f"[{timestamp()}] [PASS] Theme '{choice}' applied successfully.")

        restart_terminal()

    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Failed to apply theme '{choice}': {e}")

    return True


def get_weather():
    print(f"[{timestamp()}] [INFO] Fetching detailed weather for Berlin... (Demo)\n")
    time.sleep(1)

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
            print(f"[{timestamp()}] [ERROR] Failed to retrieve weather data. Status code: {response.status_code}")
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error fetching weather: {str(e)}")


def type_out_text(text, delay=0.05):
    """Tippt den Text langsam aus."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def ensure_admin():
    """
    Startet das Skript mit Administrator- bzw. Root-Rechten neu, falls nötig.
    - Unter Linux/macOS: sudo
    - Unter Windows: über ctypes (ShellExecute)
    """
    if os.name == 'posix':
        if os.geteuid() != 0:
            print(f"[{timestamp()}] [INFO] Restarting with root privileges...", file=sys.stderr)
            args = ['sudo', sys.executable] + sys.argv
            os.execvp('sudo', args)
    elif os.name == 'nt':
        try:
            import ctypes
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print(f"[{timestamp()}] [INFO] Restarting with administrator privileges...", file=sys.stderr)
                params = ' '.join(shlex.quote(arg) for arg in sys.argv)
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
                sys.exit(0)
        except Exception as e:
            logging.error(f"[{timestamp()}] [ERROR] Admin check failed: {e}")
    else:
        logging.warning(f"[{timestamp()}] [WARN] Unsupported OS for admin elevation: {os.name}")


def delete_target(path: str):
    """
    Entfernt eine Datei oder ein Verzeichnis (rekursiv).
    Bei Fehlern wird die Ausnahme protokolliert.
    """
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"[{timestamp()}] [INFO] Directory deleted: {path}")
        else:
            os.remove(path)
            print(f"[{timestamp()}] [INFO] File deleted: {path}")
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] {e}", file=sys.stderr)


def get_response_from_ollama(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="qwen3:14b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_qwen0_6(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="qwen3:0.6b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_qwen1_7(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="qwen3:1.7b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_qwen4(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="qwen3:4b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_qwen8(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="qwen3:8b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_qwen32(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="qwen3:32b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_qwen30(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="qwen3:30b-a3b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_qwen235(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="qwen3:235b-a22b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_llama4_scout(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="llama4:scout",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_llama4_maverick(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="llama4:maverick",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


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
                print(f"[{timestamp()}] [INFO] New Ollama version available: {remote_version} (Current: {local_version})")
                while True:
                    user_input = input("Do you want to update Ollama? [y/n]:").strip().lower()
                    if user_input in ["y", "yes"]:
                        subprocess.run(["ollama", "update"], check=True)
                        print(f"[{timestamp()}] [PASS] Ollama updated successfully! Please restart the script.")
                        exit()
                    elif user_input in ["n", "no"]:
                        print(f"[{timestamp()}] [INFO] Skipping update.")
                        break
                    else:
                        print(f"[{timestamp()}] [INFO] Invalid input. Please enter 'y' for yes or 'n' for no.")

    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error checking for updates: {e}{reset}")


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
            raise EnvironmentError(f"[{timestamp()}] [INFO] Unsupported Operating System. Ollama is not supported on this platform.")
    except Exception as e:
        raise FileNotFoundError(f"[{timestamp()}] [ERROR] Error finding Ollama path: {e}")


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
            print(f"[{timestamp()}] [INFO] Ollama is not running. Starting Ollama...")

            # Pfad zu Ollama finden
            ollama_path = find_ollama_path()

            if not os.path.exists(ollama_path):
                raise FileNotFoundError(f"[{timestamp()}] [ERROR] Ollama executable not found at: {ollama_path}")

            # Ollama starten
            subprocess.Popen([ollama_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True if platform.system() != "Windows" else False)
            time.sleep(5)  # Warten, bis Ollama gestartet ist
            print(f"[{timestamp()}] [PASS] Ollama started successfully.{reset}\n")
        else:
            print(f"[{timestamp()}] [INFO] Ollama is already running.{reset}\n")
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error starting Ollama: {e}{reset}")


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
        print(f"[{timestamp()}] [ERROR] Error checking command {command}: {e}")
        return False

def is_tool_installed(tool_name):
    """Prüfen Sie, ob ein Tool installiert ist."""
    result = subprocess.run(["which", tool_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0

def search_websites(command):
    """Sucht mit DuckDuckGo nach Websites, die mit dem Keyword in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': command}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_websites_all(command, num_results=50, results_per_page=10):
    """Sucht mit DuckDuckGo nach Websites, die mit dem Keyword in Zusammenhang stehen, und gibt Links zurück"""
    base_url = "https://html.duckduckgo.com/html/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    collected = []

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")

    for offset in range(0, num_results, results_per_page):
        params = {'q': command, 's': str(offset)}
        try:
            response = requests.post(base_url, data=params, headers=headers, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Request failed at offset {offset}: {e}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='result')
        if not results:
            print(f"[{timestamp()}] [WARN] Keine weiteren Ergebnisse bei Offset {offset}.")
            break

        for result in results:
            link_tag = result.find('a', class_='result__a', href=True)
            desc_tag = result.find('a', class_='result__snippet') or result.find('div', class_='result__snippet')
            url = link_tag['href'] if link_tag else None
            snippet = desc_tag.get_text(strip=True) if desc_tag else 'Keine Beschreibung verfügbar.'

            if url and (url, snippet) not in collected:
                collected.append((url, snippet))
                idx = len(collected)
                print(f"{blue}[{idx}]{reset} {url}\n{snippet}\n")

            if len(collected) >= num_results:
                break
        if len(collected) >= num_results:
            break

    total = len(collected)
    if total == 0:
        print(f"[{timestamp()}] [ERROR] Keine Ergebnisse gefunden.")
    else:
        print(f"\n[{timestamp()}] [INFO] {total} Ergebnisse gesammelt.\n")

    return collected


def search_and_show_first_image(query):
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=1)
        for result in results:
            image_url = result.get("image")
            if not image_url:
                print(f"[{timestamp()}] [ERROR] Kein Bild gefunden.")
                return

            try:
                print(f"[{timestamp()}] [INFO] Lade Bild von: {image_url}")
                response = requests.get(image_url, timeout=10)
                image = Image.open(BytesIO(response.content))
                temp_path = "temp_duck_image.jpg"
                image.convert("RGB").save(temp_path)
                print(f"[{timestamp()}] [INFO] Zeige Bild ...")
                os.startfile(temp_path)  # Nur für Windows
                return
            except Exception as e:
                print(f"[{timestamp()}] [ERROR] Fehler beim Laden oder Anzeigen des Bildes: {e}")
                return


def search_github(command):
    """Durchsucht GitHub mit DuckDuckGo nach Repositories oder Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:github.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_huggingface(command):
    """Durchsucht Hugging Face mithilfe von DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:huggingface.co {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_ollama(command):
    """Durchsucht Ollama mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:ollama.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_stackoverflow(command):
    """Durchsucht Stackoverflow mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:stackoverflow.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_stackexchange(command):
    """Durchsucht Stackexchange mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:stackexchange.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_pypi(command):
    """Durchsucht pypi mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:pypi.org {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_arxiv(command):
    """Durchsucht arxiv mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:arxiv.org {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_paperswithcode(command):
    """Durchsucht paperswithcode mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:paperswithcode.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_kaggle(command):
    """Durchsucht Kaggle mithilfe von DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:kaggle.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }


    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_geeksforgeeks(command):
    """Durchsucht geeksforgeeks mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:geeksforgeeks.org {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }


    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_realpython(command):
    """Durchsucht realpython mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:realpython.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_w3schools(command):
    """Durchsucht w3schools mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:w3schools.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def search_developer_mozilla(command):
    """Durchsucht developer.mozilla.org mit DuckDuckGo nach Seiten, die mit dem Schlüsselwort in Zusammenhang stehen, und gibt Links zurück"""
    url = "https://html.duckduckgo.com/html/"
    params = {'q': f"site:developer.mozilla.org.com {command}"}
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    print(f"\n[{timestamp()}] [INFO] Searching for: '{command}' ...\n")
    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during request: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for i, a in enumerate(soup.find_all('a', class_='result__a', href=True), start=1):
        links.append(a['href'])
        print(f"{blue}[{i}]{reset} {a['href']}")

    if not links:
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {len(links)} results found.\n")


def find_vcvarsall():
    """
    Sucht nach der Visual Studio-Initialisierungsdatei (vcvarsall.bat).
    """
    path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat"
    if os.path.isfile(path):
        return path
    raise FileNotFoundError(f"[{timestamp()}] [ERROR] vcvarsall.bat not found. Please make sure Visual Studio is installed.")


def find_vcvarsall_c():
    """
    Sucht nach der Visual Studio Entwicklungsumgebung (vcvarsall.bat).
    """
    # Visual Studio Installationspfad (Standardort für VS 2022)
    vs_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat"
    if not os.path.isfile(vs_path):
        logging.error("[ERROR] Visual Studio vcvarsall.bat file not found.")
        raise FileNotFoundError(f"[{timestamp()}] [ERROR] vcvarsall.bat not found. Please ensure Visual Studio is installed.")
    return vs_path


# --- pp command---

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
    Kompiliert run_pp_command.cpp mit cl.exe über die Visual Studio-Umgebung.
    Die Ausgabe wird im UTF-8 Format eingelesen – ungültige Zeichen werden ersetzt.
    """
    logging.info("[INFO] Compile run_pp_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


# --- pp-c command---

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
    Kompiliert run_pp_command.c mit cl.exe über die Visual Studio-Umgebung.
    """
    logging.info("[INFO] Compiling run_mp_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


# --- pp-p command---

def run_command_with_admin_python_privileges(command: str):
    """
    Führt einen Shell-Befehl im aktuellen Arbeitsverzeichnis mit Admin-Rechten aus.
    - Windows: erhöhte PowerShell bleibt nach Ausführung geöffnet.
    - Unix: sudo mit Eingabeaufforderung zum Schließen.
    """
    working_dir = os.getcwd()

    # Windows-Plattform
    if sys.platform == "win32":
        if ctypes.windll.shell32.IsUserAnAdmin():
            # Bereits erhöht
            subprocess.run(command, shell=True, cwd=working_dir)

            print("Completed!")
        else:
            # Skript zusammenbauen
            # 1) Wechsel in das Arbeitsverzeichnis, 2) Befehl, 3) Read-Host, damit es offen bleibt
            script = f"Set-Location -LiteralPath '{working_dir}'; {command}; Read-Host 'Press Enter to exit…'"

            # ArgumentList-Array literal: PowerShell versteht das als echtes Array
            # Wir verwenden doppelte Anführungszeichen und escapen sie in Python
            args = [
                "-NoProfile",
                "-NoExit",
                "-Command",
                script.replace('"', '`"')
            ]
            # Jetzt das Array-Literal für PowerShell bauen:
            arg_list_literal = "@(" + ",".join(f'"{a}"' for a in args) + ")"

            # Finaler Start-Process-Aufruf:
            ps_cmd = [
                "powershell",
                "-NoProfile",
                "-Command",
                "Start-Process",
                "-FilePath", "powershell",
                "-ArgumentList", arg_list_literal,
                "-Verb", "RunAs"
            ]

            # Kein shell=True – wir übergeben schon das fertige List-Objekt
            subprocess.run(ps_cmd, shell=False)

            print("Completed!")

    # Unix-Variante
    else:
        safe_cmd = command.replace("'", "'\"'\"'")
        sudo_script = f"cd '{working_dir}' && {safe_cmd}; echo; read -p '[Press Enter to close]' _"
        try:
            subprocess.run(
                ["sudo", "bash", "-c", sudo_script],
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Execution error: {e}")


def is_wsl_installed():
    """Überprüfen Sie, ob WSL installiert ist, indem Sie versuchen, einen grundlegenden WSL-Befehl auszuführen."""
    try:
        # Versuchen Sie, „wsl --list“ auszuführen, das die installierten WSL-Distributionen auflistet
        subprocess.check_call(["wsl", "--list"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        # Ausführbare WSL-Datei nicht gefunden, d. h. WSL ist nicht installiert
        print("Error: WSL is not installed or not found on the system.")
        return False
    except subprocess.CalledProcessError:
        # WSL wurde gefunden, aber beim Ausführen des Befehls ist ein Fehler aufgetreten
        print("Error: WSL is installed, but an error occurred while executing the command.")
        return False
    except Exception as e:
        # Fangen Sie alle unerwarteten Ausnahmen ab
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
    logging.info("[INFO] Compile run_lx_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARING] Cancellation by user.")

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
    logging.info("[INFO] Compile run_lx_c_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_lx_c_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")

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
    logging.info("[INFO] Compiling run_lx_c_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_ubuntu_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_ubuntu_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_debian_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_debian_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_kali_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_kali_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_arch_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_arch_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_opensuse_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_opensuse_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_mint_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_mint_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_fedora_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_fedora_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_redhat_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_redhat_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_sles_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_sles_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_pengwin_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_pengwin_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_oracle_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_oracle_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_alpine_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_alpine_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compile run_clear_command.cpp with Visual Studio C++...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C++ compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C++-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    logging.info("[INFO] Compiling run_clear_command.c with Visual Studio...")
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
        logging.error("[ERROR] Compilation failed.")
        logging.error(result.stdout)
        logging.error(result.stderr)
        return False

    logging.info("[INFO] Compilation successful.")
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
            logging.error("[ERROR] Abort: C compilation was unsuccessful.")
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
        logging.info(f"[INFO] Execute: {' '.join(cmd)}")
        # Der C-Wrapper startet ein neues Terminalfenster, in dem der Befehl interaktiv ausgeführt wird.
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"[ERROR] Command failed: {e}")
    except KeyboardInterrupt:
        logging.warning("[WARNING] Cancellation by user.")


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
    Führt einen Scoop-Befehl aus – superschnell, stabil und mit robustem Logger-Fallback.

    Argumente:
    Befehl: Scoop-Befehl als String oder Liste.
    Timeout: Maximale Laufzeit in Sekunden.
    Capture_Output: Gibt stdout/stderr zurück, wenn True.
    Retrys: Anzahl der Wiederholungsversuche bei Exit-Fehlern.
    Retry_Delay: Basisverzögerung (Sekunden) für exponentielles Backoff.
    Logger: Optionaler Logger; falls keiner, wird ein Standard-Logger konfiguriert.

    Rückgabewert:
    subprocess.CompletedProcess mit .stdout/.stderr, wenn capture_output.

    Löst aus:
    RuntimeError: Wenn scoop.exe nicht gefunden wird.
    subprocess.CalledProcessError: Bei Exit-Code ≠ 0 (nach Wiederholungsversuchen).
    subprocess.TimeoutExpired: Bei Timeout.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    # Logger-Fallback und -Konfiguration
    if logger is None:
        logger = logging.getLogger("run_scoop_command")
    if not logger.handlers:
        # Wenn kein Handler vorhanden ist: Standard-Stream-Handler hinzufügen
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Zwischenspeichern des Scoop-Pfads
    if not hasattr(run_scoop_command, "_scoop_path"):
        path = shutil.which("scoop")
        if not path:
            msg = "Scoop not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_scoop_command._scoop_path = path
    scoop_path = run_scoop_command._scoop_path

    # Tokenisierung
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [scoop_path] + args

    logger.debug(f"Starting Scoop: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

    # Ausführung mit Wiederholungsversuchen
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
            raise  # Nach Wiederholungsversuchen den CalledProcessError weitergeben

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
    Führt einen Chocolatey-Befehl aus – superschnell, stabil und mit robustem Logger-Fallback.

    Argumente:
    command: Chocolatey-Befehl als String oder Liste.
    timeout: Maximale Laufzeit in Sekunden.
    capture_output: Gibt stdout und stderr zurück, wenn True.
    retries: Anzahl der Wiederholungsversuche bei Exit-Fehlern.
    retry_delay: Basisverzögerung (in Sekunden) für exponentielles Backoff.
    logger: Optionaler Logger; falls keiner, wird ein Standard-Logger konfiguriert.

    Rückgabewert:
    subprocess.CompletedProcess mit .stdout und .stderr (wenn capture_output True ist).

    Löst aus:
    RuntimeError: Wenn choco.exe nicht gefunden wird.
    subprocess.CalledProcessError: Bei Exit-Code ≠ 0 (nach Wiederholungsversuchen).
    subprocess.TimeoutExpired: Bei Timeout.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    # Logger-Fallback und -Konfiguration
    if logger is None:
        logger = logging.getLogger("run_choco_command")
    if not logger.handlers:
        # Standard-Stream-Handler hinzufügen, falls keiner vorhanden ist
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Zwischenspeichern des Choco-Pfads
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

    # Ausführung mit Wiederholungsversuchen
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
            raise  # Fehler nach Wiederholungsversuchen weitergeben

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
    Führt einen Winget-Befehl aus – superschnell, stabil und mit robustem Logger-Fallback.

    Argumente:
    command: Winget-Befehl als String oder Liste.
    timeout: Maximale Laufzeit in Sekunden.
    capture_output: Gibt stdout und stderr zurück, wenn True.
    retries: Anzahl der Wiederholungsversuche bei Exit-Fehlern.
    retry_delay: Basisverzögerung (in Sekunden) für exponentielles Backoff.
    logger: Optionaler Logger; falls keiner, wird ein Standard-Logger konfiguriert.

    Rückgabewert:
    subprocess.CompletedProcess mit .stdout und .stderr (wenn capture_output True ist).

    Löst aus:
    RuntimeError: Wenn Winget nicht gefunden wird.
    subprocess.CalledProcessError: Bei Exit-Code ≠ 0 (nach Wiederholungsversuchen).
    subprocess.TimeoutExpired: Bei Timeout.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    # Logger-Fallback und -Konfiguration
    if logger is None:
        logger = logging.getLogger("run_winget_command")
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Zwischenspeichern des Winget-Pfads
    if not hasattr(run_winget_command, "_winget_path"):
        path = shutil.which("winget")
        if not path:
            msg = "winget not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_winget_command._winget_path = path
    winget_path = run_winget_command._winget_path

    # Tokenisieren des Befehls
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [winget_path] + args

    logger.debug(f"Starting winget: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

    # Ausführung mit Wiederholungsversuchen
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
            raise  # Fehler nach Wiederholungsversuchen weitergeben

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
        f"\n{white}┌──({reset}{blue}{getpass.getuser()}"
        + colored("㋐", attrs=["bold"])
        + f"{blue}Peharge{reset}{white})-[{reset}{current_dir}{white}]-{reset}{env_indicator}"
        f"\n{white}└─{reset}{blue}${reset} "
    )

def get_main_2_pin(current_dir, env_indicator_9):
    return (
        f"\n{blue}┌──({reset}{getpass.getuser()}"
        + colored("㋐", attrs=["bold"])
        + f"Peharge{blue})-[{reset}{current_dir}{blue}]-{reset}{env_indicator_9}"
        f"\n{blue}└─{reset}{blue}${reset} "
    )


def get_main_3_pin(current_dir, env_indicator_5):
    return (
        f"\n{green}┌──({reset}{blue}{getpass.getuser()}"
        + colored("㋐", attrs=["bold"])
        + f"{blue}Peharge{reset}{green})-[{reset}{current_dir}{green}]-{reset}{env_indicator_5}"
        f"\n{green}└─{reset}{blue}${reset} "
    )


def get_main_4_pin(current_dir, env_indicator_3):
    print("")

    return (
        f"{env_indicator_3} {blue}PP{reset} {current_dir}:~{blue}${reset} "
    )


def get_main_5_pin(current_dir, env_indicator_3):
    print("")

    return (
        f"{env_indicator_3} {blue}{getpass.getuser()}" + colored("㋐", attrs=["bold"]) + f"{blue}Peharge{reset} {current_dir}:~{blue}${reset} "
    )


def get_evil_pin(current_dir, env_indicator):
    return (
        f"\n{white}┌──({reset}{red}root"
        + colored("㋐", attrs=["bold"])
        + f"{red}Peharge{reset}{white})-[{reset}{current_dir}{white}]-{reset}{env_indicator}"
        f"\n{white}└─{reset}{red}#{reset} "
    )


def get_evil_2_pin(current_dir, env_indicator_4):
    return (
        f"\n{red}┌──({reset}{getpass.getuser()}"
        + colored("㋐", attrs=["bold"])
        + f"Peharge{red})-[{reset}{current_dir}{red}]-{reset}{env_indicator_4}"
        f"\n{red}└─{reset}{red}#{reset} "
    )


def get_evil_3_pin(current_dir, env_indicator_9):
    return (
        f"\n{blue}┌──({reset}{red}root"
        + colored("㋐", attrs=["bold"])
        + f"{red}Peharge{reset}{blue})-[{reset}{current_dir}{blue}]-{reset}{env_indicator_9}"
        f"\n{blue}└─{reset}{red}#{reset} "
    )


def get_evil_4_pin(current_dir, env_indicator_3):
    print("")

    return (
        f"{env_indicator_3} {red}PP{reset} {current_dir}:~{red}#{reset} "
    )


def get_evil_5_pin(current_dir, env_indicator_3):
    print("")

    return (
        f"{env_indicator_3} {red}root" + colored("㋐", attrs=["bold"]) + f"{red}Peharge{reset} {current_dir}:~{red}#{reset} "
    )


def get_stable_pin(current_dir, env_indicator_6):
    return (
        f"\n┌──(root"
        + colored("㋐", attrs=["bold"])
        + f"Peharge)-[{current_dir}]-{env_indicator_6}"
        f"\n└─$ "
    )


def get_stable_2_pin(current_dir, env_indicator_8):
    print("")

    return (
        f"{env_indicator_8} PP {current_dir}:~$ "
    )


def get_stable_3_pin(current_dir, env_indicator_3):
    print("")

    return (
        f"{env_indicator_3} {getpass.getuser()}" + colored("㋐", attrs=["bold"]) + f"Peharge{reset} {current_dir}:~$ "
    )


def get_cool_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """

    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\powerlevel10k_rainbow.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"
    
    
def get_cool_2_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\atomicBit.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True         # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_3_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\jandedobbeleer.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True         # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_4_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """

    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\p10k_classic.omp.jso"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_5_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\amro.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True         # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_6_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\M365Princess.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True         # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_7_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\blue-owl.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True         # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_8_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\aliens.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_9_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\agnoster.minimal.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_10_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\agnosterplus.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_11_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\atomic.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_12_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\free-ukraine.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_13_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\easy-term.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_14_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\grandpa-style.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_15_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\lambdageneration.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_16_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\lightgreen.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_17_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\bubbles.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_18_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\negligible.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_19_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\slimfat.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_20_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\stelbent.minimal.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_21_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\tonybaloney.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_22_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\emodipt.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


def get_cool_23_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\tokyo.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julia"

    try:
        result = subprocess.run(
            [
                "oh-my-posh",
                "print",
                "primary",
                "--config", config_path,
                "--pwd", working_dir,
                "--shell", "pwsh"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # wichtig für korrekte Grafikzeichen
            shell=True  # in Windows häufig nötig für PATH-Auflösung
        )
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] oh-my-posh was not found. Is it in the PATH?"
    except Exception as e:
        return f"[{timestamp()}] [ERROR] Unexpected error: {e}"

    if result.returncode == 0:
        return result.stdout
    else:
        return f"[{timestamp()}] [ERROR] Error running oh-my-posh:\n{result.stderr}"


COMMANDS = [
    "p", "p git", "p git mavis", "p git mavis-web", "p git simon", "p htop", "p ls", "p ls mavis",
    "ps ls mavis-web", "p ls simon", "p simon", "p wsl", "p pip", "p models", "p ubuntu", "gitk", "git ls all", "git ls hole",
    "pp", "pp-cpp", "pp-c", "pp-p", "ps", "ps-github", "ps-huggingface", "ps-ollama", "ps-stackoverflow", "nano",
    "htop", "btop", "atop", "glances", "ncdu", "fzf", "bat", "gitui", "lazygit", "starship",
    "emacs", "vim", "nvim", "nano", "kate", "gedit", "geany", "code",
    "vscodium", "eclipse", "idea", "pycharm", "atom", "sublime_text", "kakoune", "lite-xl",
    "ps-arxiv", "pa", "run mavis main", "lx", "lx-c", "lx-p", "lx-cpp-c", "lx-c-c", "lx-p-c", "ubuntu", "ubuntu-c",
    "ubuntu-p", "debian", "debian-c", "debian-p", "kali", "kali-c", "kali-p", "hack", "arch", "arch-c",
    "arch-p", "opensuse", "opensuse-c", "opensuse-p", "mint", "mint-c", "mint-p", "fedora", "fedora-c",
    "fedora-p", "redhat", "redhat-c", "redhat-p", "sles", "sles-c", "sles-p", "pengwin", "pengwin-c",
    "pengwin-p", "oracle", "oracle-c", "oracle-p", "cd", "cls", "clear", "dir", "ls", "mkdir", "rmdir",
    "del", "rm", "echo", "type", "cat", "exit", "alpine", "scoop", "choco", "winget", "speedtest", "kill",
    "download", "cputemp", "chucknorris", "theme", "cleantemp", "selfupdate", "tree", "py", "ask", "pa", "pa google.com"
    "weather", "whoami", "hostname", "ip", "os", "time", "date", "open", "fortune", "history", "search",
    "zip", "unzip", "sysinfo", "clip set", "clip get", "ping", "emptytrash", "launch", "doctor", "hole doctor",
    "mavis env install", "install mavis env", "install mavis3", "install mavis3.3", "install mavis4",
    "install mavis4.3", "mavis env update", "update mavis env", "mavis update", "update mavis",
    "security", "p-terminal security", "securitycheck", "info", "mavis info", "info mavis", "p-term info",
    "info p-term", "neofetch", "fastfetch", "screenfetch", "jupyter", "run jupyter", "run ju",
    "run mavis-4", "run mavis-4-3", "run mavis-4-fast", "run mavis-4-3-fast", "run mavis-launcher-4",
    "run ollama mavis-4", "install ollama mavis-4", "change models mavis-4", "change models", "grafana",
    "run grafana", "install grafana", "account", "run qwen3:0.6b", "run qwen3:1.7b", "run qwen3:4b",
    "run qwen3:8b", "run qwen3:14b", "run qwen3:32b", "run qwen3:30b", "run qwen3:235b", "run deepseek-r1:1.5b",
    "run deepseek-r1:7b", "run deepseek-r1:8b", "run deepseek-r1:14b", "run deepseek-r1:32b", "run deepseek-r1:70b",
    "run deepseek-r1:671b", "run deepscaler", "run llama3.1:8b", "run llama3.1:70b", "run llama3.1:405",
    "run llama3.2:1b", "run llama3.2:3b", "run llama3.3", "run llama3:8b", "run llama3:70b", "run mistral",
    "run mistral-large", "run mistral-nemo", "run mistral-openorca", "run mistral-small:22b",
    "run mistral-small:24b", "run phi4", "run qwen2.5:0.5b", "run qwen2.5:1.5b", "run qwen2.5:3b", "run qwen2.5:7b",
    "run qwen2.5:14b", "run qwen2.5:32b", "run qwen2.5:72b", "run qwen2.5-coder:0.5b", "run qwen2.5-coder:1.5b",
    "run qwen2.5-coder:3b", "run qwen2.5-coder:7b", "run qwen2.5-coder:14b", "run qwen2.5-coder:32b", "run gemma3:1b", "run gemma3:4b",
    "run gemma3:12b", "run gemma3:27b", "run qwq", "run command-a", "run phi4-mini", "run granite3.2:8b",
    "run granite3.2:2b", "run granite3.2-vision:2b", "run qwen-2-5-omni:7b", "run qvq:72b", "run qwen-2-5-vl:32b",
    "run qwen-2-5-vl:72b", "run llama-4-maverick:17b", "run llama-4-scout:17b", "run deepcoder:1.5b",
    "run deepcoder:14b", "run mistral-small3.1", "help", "image generation", "video generation", "models",
    "models ls", "install 3d-slicer", "run 3d-slicer", "install simon", "run simon", "jupyter --version",
    "grafana --version", "3d-slicer --version", "pin-evil", "pin-main", "pin-cool", "pin-cool-3", "pin-cool-4",
    "p install", "p uninstall", "p upgrade", "p list", "p show", "p freeze", "p search", "install cool pin", "install cool pin-3", "install cool pin-4"
    "p check", "p config", "p debug", "p cache", "p download", "p verify", "p wheel",
    "p completion", "pip install", "pip uninstall", "pip list", "pip show", "pip freeze",
    "pip search", "pip check", "pip config", "pip debug", "pip cache", "pip download",
    "pip verify", "pip wheel", "pip completion", "ollama install", "ollama uninstall",
    "ollama upgrade", "ollama list", "ollama show", "ollama search", "ollama config",
    "ollama debug", "ollama models", "ollama generate", "ollama tune", "ollama chat",
    "ollama train", "ollama predict", "ollama eval", "ollama deploy", "ps-ollama models",
    "ps-ollama install", "ps-ollama uninstall", "ps-ollama upgrade", "powershell help",
    "powershell run", "powershell execute", "powershell script", "powershell install-module",
    "powershell update-module", "powershell remove-module", "powershell get-command",
    "powershell get-help", "powershell get-module", "powershell get-process",
    "powershell get-service", "powershell get-eventlog", "powershell start-process",
    "powershell stop-process", "powershell start-service", "powershell stop-service",
    "powershell restart-service", "powershell invoke-command", "powershell set-executionpolicy",
    "powershell test-connection", "powershell export-csv", "powershell import-csv",
    "powershell convertto-json", "powershell convertfrom-json", "powershell get-content",
    "powershell set-content", "powershell add-content", "powershell select-string",
    "powershell new-item", "powershell remove-item", "powershell copy-item",
    "powershell move-item", "powershell rename-item", "powershell get-childitem",
    "powershell get-item", "powershell set-location", "powershell get-location",
    "powershell resolve-path", "powershell test-path", "powershell get-acl",
    "powershell set-acl", "powershell get-event", "powershell register-event",
    "powershell unregister-event", "powershell wait-event", "powershell clear-eventlog",
    "powershell show-eventlog", "powershell new-eventlog", "powershell remove-eventlog",
    "powershell write-eventlog", "powershell get-wmiobject", "powershell invoke-wmimethod",
    "powershell set-wmiinstance", "powershell remove-wmiobject", "powershell get-counter",
    "powershell start-job", "powershell get-job", "powershell stop-job",
    "powershell receive-job", "powershell remove-job", "powershell wait-job",
    "powershell get-variable", "powershell set-variable", "powershell remove-variable",
    "powershell new-variable", "powershell get-credential", "powershell get-history",
    "powershell add-history", "powershell clear-history", "powershell get-alias",
    "powershell set-alias", "powershell remove-alias", "powershell new-alias",
    "powershell get-host", "powershell get-command", "powershell get-member",
    "powershell get-help", "powershell show-command", "powershell start-transcript",
    "powershell stop-transcript", "powershell out-file", "powershell out-string",
    "powershell out-host", "powershell out-null", "powershell out-printer",
    "powershell out-gridview", "powershell format-list", "powershell format-table",
    "powershell format-custom", "powershell format-wide", "powershell measure-object",
    "powershell group-object", "powershell sort-object", "powershell select-object",
    "powershell where-object", "powershell foreach-object", "powershell new-object",
    "powershell compare-object", "powershell test-connection", "powershell foreach",
    "ubuntu neofetch", "ubuntu install git", "ubuntu install htop","ubuntu ls", "ubuntu list files",
    "ubuntu install python", "ubuntu install pip", "ubuntu check system info", "ubuntu update system",
    "ubuntu install models", "ubuntu clear terminal", "ubuntu show processes", "ubuntu search files",
    "ubuntu create directory", "ubuntu remove directory", "ubuntu install wget", "ubuntu find text in files",
    "ubuntu compress files", "ubuntu extract files", "ubuntu setup firewall", "ubuntu restart network",
    "ubuntu check disk usage", "ubuntu monitor network traffic", "ubuntu install curl", "ubuntu install snap",
    "ubuntu install docker", "arch neofetch", "arch install git", "arch install htop","arch list files",
    "arch install python","arch install pip","arch check system info","arch update system","arch install models",
    "arch clear terminal","arch show processes","arch search files","arch create directory","arch remove directory",
    "arch install wget", "arch find text in files", "arch compress files", "arch extract files", "arch setup firewall",
    "arch restart network", "arch check disk usage", "arch monitor network traffic", "arch install curl", "arch install snap",
    "arch install docker", "arch sudo pacman -S", "arch sudo pacman -R", "arch sudo pacman -Syu", "arch ls"
    "kali neofetch", "kali install git", "kali install htop", "kali list files", "kali install python",
    "kali install pip", "kali check system info", "kali update system", "kali install models", "kali clear terminal",
    "kali show processes", "kali search files", "kali create directory", "kali remove directory", "kali install wget",
    "kali find text in files", "kali compress files", "kali extract files", "kali setup firewall", "kali restart network",
    "kali check disk usage", "kali monitor network traffic", "kali install curl", "kali install snap", "kali install docker", "kali ls",
    "mint install docker", "mint install nmap", "mint install metasploit", "mint install wireshark",
    "mint install burpsuite", "mint install sqlmap", "mint install git", "mint install python3-pip", "mint install curl",
    "mint install vim", "mint install htop", "mint install gparted", "mint install vlc", "mint install thunderbird",
    "mint update", "mint upgrade", "mint autoremove", "mint clean", "mint ls", "mint cd /etc", "mint cd ~",
    "mint mkdir test", "mint mkdir -p ~/Projekte/python", "mint rm file.txt", "mint rm -rf testordner", "mint cp a.txt b.txt",
    "mint mv a.txt ~/Dokumente/", "mint touch neu.txt", "mint cat /etc/os-release", "mint nano ~/.bashrc", "mint sudo reboot",
    "mint sudo shutdown now", "mint ping 8.8.8.8", "mint ifconfig", "mint ip a", "mint netstat -tuln", "mint ss -tulpn",
    "mint systemctl status", "mint systemctl restart NetworkManager", "mint ps aux", "mint top", "mint whoami", "mint uname -a",
    "mint df -h", "mint free -m", "mint history", "mint clear", "mint echo 'Hallo Mint!'", "mint chmod +x script.sh",
    "mint chown user:user file.txt", "mint find / -name '*.conf'", "mint grep 'password' /etc/passwd", "mint wget https://example.com/datei.zip",
    "mint unzip datei.zip", "mint tar -xvf archiv.tar", "mint curl -I https://example.com", "debian install docker",
    "debian install nmap", "debian install metasploit", "debian install wireshark", "debian install burpsuite", "debian install sqlmap",
    "debian install git", "debian install python3-pip", "debian install curl", "debian install vim", "debian install htop",
    "debian install gparted", "debian install vlc", "debian install thunderbird", "debian update", "debian upgrade", "debian autoremove",
    "debian clean", "debian ls", "debian cd /etc", "debian cd ~", "debian mkdir test", "debian mkdir -p ~/Projekte/python",
    "debian rm file.txt", "debian rm -rf testordner", "debian cp a.txt b.txt", "debian mv a.txt ~/Dokumente/", "debian touch neu.txt",
    "debian cat /etc/os-release", "debian nano ~/.bashrc", "debian sudo reboot", "debian sudo shutdown now", "debian ping 8.8.8.8",
    "debian ifconfig", "debian ip a", "debian netstat -tuln", "debian ss -tulpn", "debian systemctl status", "debian systemctl restart NetworkManager",
    "debian ps aux", "debian top", "debian whoami", "debian uname -a", "debian df -h", "debian free -m", "debian history", "debian clear",
    "debian echo 'Hallo Debian!'", "debian chmod +x script.sh", "debian chown user:user file.txt", "debian find / -name '*.conf'",
    "debian grep 'password' /etc/passwd", "debian wget https://example.com/datei.zip", "debian unzip datei.zip",
    "debian tar -xvf archiv.tar", "debian curl -I https://example.com", "opensuse install docker", "opensuse install nmap",
    "opensuse install metasploit", "opensuse install wireshark", "opensuse install burpsuite", "opensuse install sqlmap", "opensuse install git",
    "opensuse install python3-pip", "opensuse install curl", "opensuse install vim", "opensuse install htop", "opensuse install gparted",
    "opensuse install vlc", "opensuse install thunderbird", "opensuse update", "opensuse upgrade", "opensuse autoremove",
    "opensuse clean", "opensuse ls", "opensuse cd /etc", "opensuse cd ~", "opensuse mkdir test", "opensuse mkdir -p ~/Projekte/python",
    "opensuse rm file.txt", "opensuse rm -rf testordner", "opensuse cp a.txt b.txt", "opensuse mv a.txt ~/Dokumente/",
    "opensuse touch neu.txt",  "opensuse cat /etc/os-release", "opensuse nano ~/.bashrc", "opensuse sudo reboot", "opensuse sudo shutdown now",
    "opensuse ping 8.8.8.8", "opensuse ifconfig", "opensuse ip a", "opensuse netstat -tuln", "opensuse ss -tulpn",
    "opensuse systemctl status", "opensuse systemctl restart NetworkManager", "opensuse ps aux", "opensuse top", "opensuse whoami",
    "opensuse uname -a", "opensuse df -h", "opensuse free -m", "opensuse history", "opensuse clear", "opensuse echo 'Hallo openSUSE!'",
    "opensuse chmod +x script.sh", "opensuse chown user:user file.txt", "opensuse find / -name '*.conf'", "opensuse grep 'password' /etc/passwd",
    "opensuse wget https://example.com/datei.zip", "opensuse unzip datei.zip", "opensuse tar -xvf archiv.tar", "opensuse curl -I https://example.com",
    "fedora install docker", "fedora install nmap", "fedora install metasploit", "fedora install wireshark", "fedora install burpsuite",
    "fedora install sqlmap", "fedora install git", "fedora install python3-pip", "fedora install curl", "fedora install vim", "fedora install htop",
    "fedora install gparted", "fedora install vlc", "fedora install thunderbird", "fedora update", "fedora upgrade", "fedora autoremove", "fedora clean",
    "fedora ls", "fedora cd /etc", "fedora cd ~", "fedora mkdir test", "fedora mkdir -p ~/Projekte/python", "fedora rm file.txt",
    "fedora rm -rf testordner", "fedora cp a.txt b.txt", "fedora mv a.txt ~/Dokumente/", "fedora touch neu.txt", "fedora cat /etc/os-release",
    "fedora nano ~/.bashrc""fedora sudo reboot", "fedora sudo shutdown now", "fedora ping 8.8.8.8", "fedora ifconfig", "fedora ip a",
    "fedora netstat -tuln", "fedora ss -tulpn", "fedora systemctl status", "fedora systemctl restart NetworkManager", "fedora ps aux", "fedora top",
    "fedora whoami", "fedora uname -a", "fedora df -h", "fedora free -m", "fedora history", "fedora clear", "fedora echo 'Hallo Fedora!'",
    "fedora chmod +x script.sh", "fedora chown user:user file.txt", "fedora find / -name '*.conf'", "fedora grep 'password' /etc/passwd",
    "fedora wget https://example.com/datei.zip", "fedora unzip datei.zip", "fedora tar -xvf archiv.tar", "fedora curl -I https://example.com",
    "Get-Process", "Get-Service", "Get-ChildItem", "Get-Help", "Get-Command",
    "Set-ExecutionPolicy", "Start-Service", "Stop-Service", "Restart-Computer", "Get-EventLog",
    "Get-Content", "Set-Content", "Out-File", "Get-Location", "Set-Location",
    "New-Item", "Remove-Item", "Copy-Item", "Move-Item", "Rename-Item",
    "Get-Item", "Get-Date", "Clear-Host", "Get-History", "Get-Alias",
    "Test-Connection", "Get-NetIPConfiguration", "Get-NetAdapter", "Resolve-DnsName", "Test-NetConnection",
    "Import-Module", "Export-ModuleMember", "Get-Module", "Install-Module", "Update-Module",
    "New-LocalUser", "Get-LocalUser", "Add-LocalGroupMember", "Get-LocalGroup", "Remove-LocalUser",
    "Start-Process notepad.exe", "Stop-Process -Name notepad", "Sort-Object CPU",
    "Where-Object {$_.Status -eq 'Running'}", "Measure-Object",
    "Get-Help Get-Process -Online", "New-Item -Path . -Name 'test.txt' -ItemType File", "Set-ItemProperty",
    "Remove-ItemProperty", "Get-ItemProperty",
    "ConvertTo-Json", "ConvertFrom-Json", "Select-Object", "Where-Object", "ForEach-Object",
    "Group-Object", "Sort-Object", "Format-Table", "Write-Host 'Hello'", "Write-Output 'World'",
    "Read-Host 'Enter value'", "Start-Sleep -Seconds 5", "New-ScheduledTask", "Get-ScheduledTask",
    "Unregister-ScheduledTask", "Enable-ScheduledTask", "Disable-ScheduledTask", "Get-WmiObject Win32_BIOS",
    "Get-WmiObject Win32_OperatingSystem",
    "Get-WmiObject Win32_Processor", "Get-WmiObject Win32_LogicalDisk", "Get-WmiObject Win32_NetworkAdapter",
    "Get-CimInstance", "Invoke-Command",
    "Enter-PSSession", "New-PSSession", "Remove-PSSession", "Get-EventLog -LogName System",
    "Clear-EventLog -LogName System",
    "Write-EventLog", "Limit-EventLog", "$env:PATH", "$PSVersionTable", "$HOME",
    "$PWD", "$Error", "Test-Path C:\\Windows", "New-Variable -Name Test -Value 123", "Remove-Variable Test",
    "Get-Variable", "Set-Variable Test 456", "New-Alias ll Get-ChildItem", "Get-Alias ll", "Remove-Alias ll",
    "Export-Clixml", "Import-Clixml", "Split-Path", "Join-Path", "Compare-Object",
    "Out-Null", "Out-GridView", "Show-Command", "Start-Transcript", "Stop-Transcript",
    "Invoke-RestMethod", "Invoke-WebRequest", "Send-MailMessage", "Compress-Archive", "Expand-Archive",
    "New-Guid", "Get-Random", "New-Object", "Get-Credential", "Register-ScheduledTask",
    "pip install requests", "pip install numpy", "pip install pandas", "pip install flask", "pip install django",
    "pip uninstall requests", "pip uninstall numpy", "pip list", "pip show flask", "pip freeze",
    "pip install -r requirements.txt", "pip check", "pip cache purge", "pip search fastapi", "pip install --upgrade pip",
    "pip install matplotlib", "pip install scikit-learn", "pip install beautifulsoup4", "pip install selenium", "pip install jupyter",
    "pip install pytest", "pip install ipython", "pip install virtualenv", "pip install wheel", "pip install pipenv",
    "pip download requests", "pip install --user numpy", "pip install --no-cache-dir flask", "pip show numpy", "pip uninstall -y pandas",
    "pip install -e .", "pip install git+https://github.com/psf/requests.git", "pip install 'requests<3.0'", "pip install torch", "pip install transformers",
    "pip config list", "pip config get global.index-url", "pip config set global.index-url https://pypi.org/simple", "pip install --pre pandas", "pip install fastapi[all]",
    "pip install openpyxl", "pip install pydantic", "pip install uvicorn", "pip install rich", "pip install tqdm", "python"
    "ollama run qwen3", "ollama run gemma3", "ollama run deepseek-r1", "ollama run llama3", "ollama run mistral:7b",
    "ollama run codellama:13b", "ollama run gemma:2b", "ollama run phi:1.5",
    "ollama pull llama3", "ollama pull mistral:7b", "ollama pull codellama:13b", "ollama pull gemma:2b", "ollama pull phi:1.5",
    "ollama list", "ollama show llama3", "ollama show mistral:7b", "ollama show codellama:13b", "ollama show gemma:2b",
    "ollama delete llama3", "ollama delete mistral:7b", "ollama delete codellama:13b", "ollama delete gemma:2b", "ollama delete phi:1.5",
    "ollama create mymodel -f Modelfile", "ollama push mymodel", "ollama run mymodel", "ollama run mymodel --verbose", "ollama run mymodel --mirostat 1",
    "ollama run llama3 --temperature 0.7", "ollama run llama3 --top-k 50", "ollama run llama3 --top-p 0.95", "ollama run llama3 --repeat-penalty 1.2", "ollama run llama3 --num-predict 100",
    "ollama run llama3 --prompt 'Erkläre Quantencomputing.'", "ollama run mistral:7b --format markdown", "ollama run codellama:13b --verbose", "ollama run gemma:2b --mirostat 1", "ollama run phi:1.5 --temperature 0.5",
    "ollama serve", "ollama version", "ollama help", "ollama help run", "ollama help create",
    "ollama list --format json", "ollama pull llama3:13b", "ollama run --system 'Du bist ein hilfreicher Assistent.'", "ollama run llama3 --verbose", "ollama run llama3 --mirostat 1"
]

# Verlauf und Index
history = []
history_index = -1

def setup_autocomplete(commands=None):
    """
    Aktiviert Tab-Autocomplete für eine gegebene Befehlsliste.
    Nur Befehle, die mit dem bereits getippten Text beginnen, werden vorgeschlagen.
    """
    if commands is None:
        commands = COMMANDS.copy()

    # Definiere, welche Zeichen als Worttrenner gelten (hier nur Leerzeichen)
    readline.set_completer_delims(' \t\n')

    def completer(text, state):
        # Bei jedem Aufruf filtern wir die Befehle anhand des Präfixes 'text'
        matches = [cmd for cmd in commands if cmd.startswith(text)]
        try:
            return matches[state]
        except IndexError:
            return None

    # Setze den Completer und die Key-Bindings
    readline.set_completer(completer)
    readline.parse_and_bind('tab: complete')
    # show-all-if-ambiguous = bei mehreren Treffern sofort alle anzeigen
    readline.parse_and_bind('set show-all-if-ambiguous on')
    # completion-ignore-case = Groß-/Kleinschreibung ignorieren
    readline.parse_and_bind('set completion-ignore-case on')


def get_completions(prefix):
    """Gibt alle COMMANDS zurück, die mit prefix anfangen (für tab-Vervollständigung)."""
    return [cmd for cmd in COMMANDS if cmd.startswith(prefix)]


def input_line(prompt):
    """Lesen einer Zeile mit History (Up/Down) und Tab-Completion."""
    sys.stdout.write(prompt)
    sys.stdout.flush()

    buf = ''
    global history_index
    history_index = len(history)

    while True:
        ch = msvcrt.getwch()

        # Enter
        if ch in ('\r', '\n'):
            print()
            if buf:
                history.append(buf)
            return buf

        # Backspace
        if ch == '\b':
            if buf:
                buf = buf[:-1]
                sys.stdout.write('\b \b')
                sys.stdout.flush()
            continue

        # Tab = Completion
        if ch == '\t':
            comps = get_completions(buf)
            if comps:
                # Spaltenorientierte Ausgabe
                sys.stdout.write('\n')
                cols, _ = shutil.get_terminal_size((80, 20))
                maxlen = max(len(c) for c in comps) + 2  # +2 für Abstand
                per_line = cols // maxlen

                for i, c in enumerate(comps):
                    sys.stdout.write(c.ljust(maxlen))
                    if (i + 1) % per_line == 0:
                        sys.stdout.write('\n')
                sys.stdout.write('\n')

                # Prompt und bisherigen Puffer neu ausgeben
                sys.stdout.write(prompt + buf)
                sys.stdout.flush()
            continue

        # Pfeiltasten: Spezialcode '\xe0'
        if ch == '\xe0':
            arrow = msvcrt.getwch()
            # Up arrow
            if arrow == 'H' and history and history_index > 0:
                history_index -= 1
                new_buf = history[history_index]
            # Down arrow
            elif arrow == 'P':
                if history_index < len(history) - 1:
                    history_index += 1
                    new_buf = history[history_index]
                else:
                    history_index = len(history)
                    new_buf = ''
            else:
                continue
            # Lösche bisherigen Buffer vom Bildschirm
            sys.stdout.write('\b' * len(buf))
            sys.stdout.write(' ' * len(buf))
            sys.stdout.write('\b' * len(buf))
            buf = new_buf
            sys.stdout.write(buf)
            sys.stdout.flush()
            continue

        # Normale Zeichen
        if ch.isprintable():
            buf += ch
            sys.stdout.write(ch)
            sys.stdout.flush()


def handle_history_command():
    """
    Gibt alle Einträge in history aus.
    Rückgabe True signalisiert, dass das Kommando history verarbeitet wurde.
    """
    if not history:
        print(f"[{timestamp()}] [ERROR] No commands in the history.")
    else:
        print(f"[{timestamp()}] [INFO] Previous commands:")
        for idx, cmd in enumerate(history, start=1):
            print(f"  {idx}: {cmd}")
    return True


def main():
    state = "main"

    print_banner()
    set_python_path()
    # setup_autocomplete()

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
                f"{white}[{reset}{display_env_path}{white}]{reset}"
                if env_active else
                f"{white}[{reset}{red}no venv recorded{reset}{white}]{reset}"
            )

            env_indicator_3 = (
                f"({display_env_path})"
                if env_active else
                f"({red}venv{reset})"
            )

            env_indicator_4 = (
                f"{red}[{reset}{display_env_path}{red}]{reset}"
                if env_active else
                f"{red}[no venv recorded]{reset}"
            )

            env_indicator_5 = (
                f"{green}[{reset}{display_env_path}{green}]{reset}"
                if env_active else
                f"{green}[{reset}{red}no venv recorded{reset}{green}]{reset}"
            )

            env_indicator_6 = (
                f"[{display_env_path}]"
                if env_active else
                f"[no venv recorded]"
            )

            env_indicator_8 = (
                f"({display_env_path})"
                if env_active else
                f"(no venv)"
            )

            env_indicator_9 = (
                f"{blue}[{reset}{display_env_path}{blue}]{reset}"
                if env_active else
                f"{blue}[{reset}{red}no venv recorded{reset}{blue}]{reset}"
            )

            # PIN-Design je nach state
            if state == "main":
                setup_autocomplete()
                pin = get_main_pin(current_dir, env_indicator)
                print(pin, end='')
                # print(pin, end='', flush=True)
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-2":
                setup_autocomplete()
                pin = get_main_2_pin(current_dir, env_indicator_9)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-3":
                setup_autocomplete()
                pin = get_main_3_pin(current_dir, env_indicator_5)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-4":
                setup_autocomplete()
                pin = get_main_4_pin(current_dir, env_indicator_3)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-5":
                setup_autocomplete()
                pin = get_main_5_pin(current_dir, env_indicator_3)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "evil":
                setup_autocomplete()
                pin = get_evil_pin(current_dir, env_indicator)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "evil-2":
                setup_autocomplete()
                pin = get_evil_2_pin(current_dir, env_indicator_4)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "evil-3":
                setup_autocomplete()
                pin = get_evil_3_pin(current_dir, env_indicator_9)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "evil-4":
                setup_autocomplete()
                pin = get_evil_4_pin(current_dir, env_indicator_3)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "evil-5":
                setup_autocomplete()
                pin = get_evil_5_pin(current_dir, env_indicator_3)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "stable":
                setup_autocomplete()
                pin = get_stable_pin(current_dir, env_indicator_6)
                user_input = input(pin).strip()
                history.append(user_input)

            elif state == "stable-2":
                setup_autocomplete()
                pin = get_stable_2_pin(current_dir, env_indicator_6)
                user_input = input(pin).strip()
                history.append(user_input)

            elif state == "stable-3":
                setup_autocomplete()
                pin = get_stable_3_pin(current_dir, env_indicator_8)
                user_input = input(pin).strip()
                history.append(user_input)

            elif state == "cool":
                pin = get_cool_pin()
                user_input = input_line(pin)

            elif state == "cool-2":
                pin = get_cool_2_pin()
                user_input = input_line(pin)

            elif state == "cool-3":
                pin = get_cool_3_pin()
                user_input = input_line(pin)

            elif state == "cool-4":
                pin = get_cool_4_pin()
                user_input = input_line(pin)

            elif state == "cool-5":
                pin = get_cool_5_pin()
                user_input = input_line(pin)

            elif state == "cool-6":
                pin = get_cool_6_pin()
                user_input = input_line(pin)

            elif state == "cool-7":
                pin = get_cool_7_pin()
                user_input = input_line(pin)

            elif state == "cool-8":
                pin = get_cool_8_pin()
                user_input = input_line(pin)

            elif state == "cool-9":
                pin = get_cool_9_pin()
                user_input = input_line(pin)

            elif state == "cool-10":
                pin = get_cool_10_pin()
                user_input = input_line(pin)

            elif state == "cool-11":
                pin = get_cool_11_pin()
                user_input = input_line(pin)

            elif state == "cool-12":
                pin = get_cool_12_pin()
                user_input = input_line(pin)

            elif state == "cool-13":
                pin = get_cool_13_pin()
                user_input = input_line(pin)

            elif state == "cool-14":
                pin = get_cool_14_pin()
                user_input = input_line(pin)

            elif state == "cool-15":
                pin = get_cool_15_pin()
                user_input = input_line(pin)

            elif state == "cool-16":
                pin = get_cool_16_pin()
                user_input = input_line(pin)

            elif state == "cool-17":
                pin = get_cool_17_pin()
                user_input = input_line(pin)

            elif state == "cool-18":
                pin = get_cool_18_pin()
                user_input = input_line(pin)

            elif state == "cool-19":
                pin = get_cool_19_pin()
                user_input = input_line(pin)

            elif state == "cool-20":
                pin = get_cool_20_pin()
                user_input = input_line(pin)

            elif state == "cool-21":
                pin = get_cool_21_pin()
                user_input = input_line(pin)

            elif state == "cool-22":
                pin = get_cool_22_pin()
                user_input = input_line(pin)

            elif state == "cool-23":
                pin = get_cool_23_pin()
                user_input = input_line(pin)

            else:
                pin = get_main_pin(current_dir, env_indicator)
                user_input = input_line(pin)

            if handle_special_commands(user_input):
                continue

            elif user_input.lower() == "pin main":
                state = "main"
                continue

            elif user_input.lower() == "pin main-2":
                state = "main-2"
                continue

            elif user_input.lower() == "pin main-3":
                state = "main-3"
                continue

            elif user_input.lower() == "pin main-4":
                state = "main-4"
                continue

            elif user_input.lower() == "pin main-5":
                state = "main-5"
                continue

            elif user_input.lower() == "pin evil":
                state = "evil"
                continue

            elif user_input.lower() == "pin evil-2":
                state = "evil-2"
                continue

            elif user_input.lower() == "pin evil-3":
                state = "evil-3"
                continue

            elif user_input.lower() == "pin evil-4":
                state = "evil-4"
                continue

            elif user_input.lower() == "pin evil-5":
                state = "evil-5"
                continue

            elif user_input.lower() == "pin stable":
                state = "stable"
                continue

            elif user_input.lower() == "pin stable-2":
                state = "stable-2"
                continue

            elif user_input.lower() == "pin stable-3":
                state = "stable-3"
                continue

            elif user_input.lower() == "pin cool":
                state = "cool"
                continue

            elif user_input.lower() == "pin cool-2":
                state = "cool-2"
                continue

            elif user_input.lower() == "pin cool-3":
                state = "cool-3"
                continue

            elif user_input.lower() == "pin cool-4":
                state = "cool-4"
                continue

            elif user_input.lower() == "pin cool-5":
                state = "cool-5"
                continue

            elif user_input.lower() == "pin cool-6":
                state = "cool-6"
                continue

            elif user_input.lower() == "pin cool-7":
                state = "cool-7"
                continue

            elif user_input.lower() == "pin cool-8":
                state = "cool-8"
                continue

            elif user_input.lower() == "pin cool-9":
                state = "cool-9"
                continue

            elif user_input.lower() == "pin cool-10":
                state = "cool-10"
                continue

            elif user_input.lower() == "pin cool-11":
                state = "cool_11"
                continue

            elif user_input.lower() == "pin cool-12":
                state = "cool-12"
                continue

            elif user_input.lower() == "pin cool-13":
                state = "cool-13"
                continue

            elif user_input.lower() == "pin cool-14":
                state = "cool-14"
                continue

            elif user_input.lower() == "pin cool-15":
                state = "cool-15"
                continue

            elif user_input.lower() == "pin cool-16":
                state = "cool-16"
                continue

            elif user_input.lower() == "pin cool-17":
                state = "cool-17"
                continue

            elif user_input.lower() == "pin cool-18":
                state = "cool-18"
                continue

            elif user_input.lower() == "pin cool-19":
                state = "cool-19"
                continue

            elif user_input.lower() == "pin cool-20":
                state = "cool-20"
                continue

            elif user_input.lower() == "pin cool-21":
                state = "cool-21"
                continue

            elif user_input.lower() == "pin cool-22":
                state = "cool-22"
                continue

            elif user_input.lower() == "pin cool-23":
                state = "cool-23"
                continue

            elif user_input.startswith("pp "):
                user_input = user_input[3:]
                run_command_with_admin_python_privileges(user_input)

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

            elif user_input.startswith("pps "):
                user_input = user_input[4:].strip()
                run_command("powershell " + user_input, shell=True)

            elif user_input.startswith("cmd "):
                user_input = user_input[4:].strip()
                run_command(user_input, shell=True)

            elif user_input.startswith("ps "):
                user_input = user_input[3:].strip()
                search_websites(user_input)

            elif user_input.startswith("ps-all "):
                user_input = user_input[7:].strip()
                search_websites_all(user_input)

            elif user_input.startswith("ps-img "):
                user_input = user_input[7:].strip()
                search_and_show_first_image(user_input)

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
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("lx-cpp "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("lx-cpp-c "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_cpp_c_command(user_input)

            elif user_input.startswith("lx-c "):
                user_input = user_input[5:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_c_command(user_input)

            elif user_input.startswith("lx-c-c "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_c_c_command(user_input)

            elif user_input.startswith("lx-p "):
                user_input = user_input[5:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_python_command(user_input)

            elif user_input.startswith("lx-p-c "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_p_c_command(user_input)

            elif user_input.startswith("linux "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("ubuntu "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_command(user_input)

            elif user_input.startswith("ubuntu-c "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_c_command(user_input)

            elif user_input.startswith("ubuntu-p "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_python_command(user_input)

            elif user_input.startswith("debian "):
                user_input = user_input[7:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Debian: {user_input}")
                    run_debian_command(user_input)

            elif user_input.startswith("debian-c "):
                user_input = user_input[9:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Debian: {user_input}")
                    run_debian_c_command(user_input)

            elif user_input.startswith("debian-p "):
                user_input = user_input[9:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Debian: {user_input}")
                    run_debian_python_command(user_input)

            elif user_input.startswith("kali "):
                user_input = user_input[5:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Kali: {user_input}")
                    run_kali_command(user_input)

            elif user_input.startswith("kali-c "):
                user_input = user_input[7:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Kali: {user_input}")
                    run_kali_c_command(user_input)

            elif user_input.startswith("kali-p "):
                user_input = user_input[7:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Kali: {user_input}")
                    run_kali_python_command(user_input)

            elif user_input.startswith("hack "):
                user_input = user_input[5:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Kali: {user_input}")
                    run_kali_command(user_input)

            elif user_input.startswith("arch "):
                user_input = user_input[5:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Arch: {user_input}")
                    run_arch_command(user_input)

            elif user_input.startswith("arch-c "):
                user_input = user_input[7:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Arch: {user_input}")
                    run_arch_c_command(user_input)

            elif user_input.startswith("arch-p "):
                user_input = user_input[7:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Arch: {user_input}")
                    run_arch_python_command(user_input)

            elif user_input.startswith("openSUSE "):
                user_input = user_input[9:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_opensuse_command(user_input)

            elif user_input.startswith("openSUSE-c "):
                user_input = user_input[11:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_opensuse_c_command(user_input)

            elif user_input.startswith("openSUSE-p "):
                user_input = user_input[11:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_opensuse_python_command(user_input)

            elif user_input.startswith("mint "):
                user_input = user_input[5:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_mint_command(user_input)

            elif user_input.startswith("mint-c "):
                user_input = user_input[7:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_mint_c_command(user_input)

            elif user_input.startswith("mint-p "):
                user_input = user_input[7:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_mint_python_command(user_input)

            elif user_input.startswith("fedora "):
                user_input = user_input[7:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Fedora: {user_input}")
                    run_fedora_command(user_input)

            elif user_input.startswith("fedora-c "):
                user_input = user_input[9:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Fedora: {user_input}")
                    run_fedora_c_command(user_input)

            elif user_input.startswith("fedora-p "):
                user_input = user_input[9:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Fedora: {user_input}")
                    run_fedora_python_command(user_input)

            elif user_input.startswith("redhat "):
                user_input = user_input[7:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on RedHat: {user_input}")
                    run_redhat_command(user_input)

            elif user_input.startswith("redhat-c "):
                user_input = user_input[9:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on RedHat: {user_input}")
                    run_redhat_c_command(user_input)

            elif user_input.startswith("redhat-p "):
                user_input = user_input[9:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on RedHat: {user_input}")
                    run_redhat_python_command(user_input)

            elif user_input.startswith("sles "):
                user_input = user_input[7:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on SLES: {user_input}")
                    run_sles_command(user_input)

            elif user_input.startswith("sles-c "):
                user_input = user_input[9:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on SLES: {user_input}")
                    run_sles_c_command(user_input)

            elif user_input.startswith("sles-p "):
                user_input = user_input[9:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on SLES: {user_input}")
                    run_sles_python_command(user_input)

            elif user_input.startswith("pengwin "):
                user_input = user_input[7:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Pengwin: {user_input}")
                    run_pengwin_command(user_input)

            elif user_input.startswith("pengwin-c "):
                user_input = user_input[9:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Pengwin: {user_input}")
                    run_pengwin_c_command(user_input)

            elif user_input.startswith("pengwin-p "):
                user_input = user_input[9:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Pengwin: {user_input}")
                    run_pengwin_python_command(user_input)

            elif user_input.startswith("oracle "):
                user_input = user_input[7:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Oracle: {user_input}")
                    run_oracle_command(user_input)

            elif user_input.startswith("oracle-c "):
                user_input = user_input[9:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Oracle: {user_input}")
                    run_oracle_c_command(user_input)

            elif user_input.startswith("oracle-p "):
                user_input = user_input[9:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Oracle: {user_input}")
                    run_oracle_python_command(user_input)

            elif user_input.startswith("alpine "):
                user_input = user_input[7:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Alpine: {user_input}")
                    run_alpine_command(user_input)

            elif user_input.startswith("alpine-c "):
                user_input = user_input[9:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Alpine: {user_input}")
                    run_alpine_c_command(user_input)

            elif user_input.startswith("alpine-p "):
                user_input = user_input[9:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Alpine: {user_input}")
                    run_alpine_python_command(user_input)

            elif user_input.startswith("clear "):
                user_input = user_input[7:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Clear: {user_input}")
                    run_clear_command(user_input)

            elif user_input.startswith("clear-c "):
                user_input = user_input[9:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Clear: {user_input}")
                    run_clear_c_command(user_input)

            elif user_input.startswith("clear-p "):
                user_input = user_input[9:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print(f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Clear: {user_input}")
                    run_clear_python_command(user_input)

            elif user_input.startswith("sc "):
                user_input = user_input[3:].strip()
                print(f"[{timestamp()}] [INFO] Executing the following command with scoop: {user_input}")
                run_scoop_command(user_input)

            elif user_input.startswith("scoop "):
                user_input = user_input[6:].strip()
                print(f"[{timestamp()}] [INFO] Executing the following command with scoop: {user_input}")
                run_scoop_command(user_input)

            elif user_input.startswith("cho "):
                user_input = user_input[4:].strip()
                print(f"[{timestamp()}] [INFO] Executing the following command with choco: {user_input}")
                run_choco_command(user_input)

            elif user_input.startswith("choco "):
                user_input = user_input[6:].strip()
                print(f"[{timestamp()}] [INFO] Executing the following command with choco: {user_input}")
                run_choco_command(user_input)

            elif user_input.startswith("winget "):
                user_input = user_input[6:].strip()
                print(f"[{timestamp()}] [INFO] Executing the following command with winget : {user_input}")
                run_winget_command(user_input)

            else:
                run_command(user_input, shell=True)

            sys.stdout.flush()
            sys.stderr.flush()

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] {str(e)}", file=sys.stderr)


if __name__ == "__main__":
    main()