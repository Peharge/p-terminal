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
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import ujson as _json  # ultraschnelles JSON
except ImportError:
    _json = json

colorama.init()

DEFAULT_ENV_DIR = os.path.join("p-terminal", "pp-term", ".env")
DEFAULT_PYTHON_EXECUTABLE = os.path.join(DEFAULT_ENV_DIR, "Scripts", "python.exe")

# Globales Thema
current_theme = "dark"

"""
log_path = Path(__file__).parent / "pp-term-compiler.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_path, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
"""

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

user_name = getpass.getuser()

sys.stdout.reconfigure(encoding='utf-8')

# Constants
APP_NAME = "p-terminal"
STATE_FILE = Path.home() / f".{APP_NAME}" / "current_env.json"

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
purple = "\033[95m"
dim = "\033[2m"
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
        print(f"[{timestamp()}] [INFO] Version file not found under{json_path}")
    except json.JSONDecodeError:
        print(f"[{timestamp()}] [ERROR] JSON format error in {json_path}")

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


def ensure_state_dir_exists() -> None:
    """Stellt sicher, dass das Verzeichnis für den Statusfile existiert."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)


def save_current_env(env_path: str) -> None:
    """Speichert den angegebenen Virtualenv-Pfad als String im Statusfile."""
    try:
        ensure_state_dir_exists()
        payload = {"active_env": env_path}
        # atomar schreiben: erst in temp, dann umbenennen
        tmp = STATE_FILE.with_suffix(".tmp")
        tmp.write_text(_json.dumps(payload), encoding="utf-8")
        tmp.replace(STATE_FILE)
    except Exception as e:
        logging.error(f"Error saving status file: {e}")


def load_saved_env() -> Optional[str]:
    """Lädt den zuletzt gespeicherten Virtualenv-Pfad (als String)."""
    try:
        if STATE_FILE.is_file():
            raw = STATE_FILE.read_text(encoding="utf-8")
            data = _json.loads(raw)
            val = data.get("active_env", "")
            if val and Path(val).is_dir():
                return val
    except Exception as e:
        logging.warning(f"Error loading status file: {e}")
    return None


def _check_env_dir(path: Path) -> Optional[Path]:
    """Hilfsfunktion: gibt den Pfad zurück, wenn es ein Env ist."""
    activate = path / "Scripts" / "activate"
    return path if activate.is_file() else None


def find_env_in_current_dir(max_workers: int = None) -> Optional[str]:
    """
    Durchsucht das aktuelle Arbeitsverzeichnis nach Virtualenvs.
    Nutzt Multithreading, um Verzeichnisse parallel zu prüfen.
    Gibt den ersten gefundenen Pfad zurück.
    """
    cwd = Path.cwd()
    # os.scandir liefert DirEntry-Objekte, sehr effizient
    dirs = [Path(entry.path) for entry in os.scandir(cwd) if entry.is_dir()]
    if not dirs:
        return None

    # max_workers default: Anzahl CPUs * 2
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_path = {executor.submit(_check_env_dir, d): d for d in dirs}
        for future in as_completed(future_to_path):
            result = future.result()
            if result:
                return str(result.resolve())
    return None


def find_active_env() -> str:
    """
    Bestimmt den aktiven Virtualenv:
    1. Suche parallel nach Env im CWD.
    2. Wenn anders als gespeichertes, dann speichern.
    3. Wenn keins gefunden, dann gespeichertes verwenden.
    4. Wenn nichts gespeichert: Fallback-Env.
    """
    found = find_env_in_current_dir()
    saved = load_saved_env()

    if found:
        if found != saved:
            save_current_env(found)
        return found

    if saved:
        return saved

    return str(DEFAULT_ENV_DIR.resolve())


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
        "install mavis3": "mavis-install\\install-info-mavis-4.py",  # new
        "install mavis3.3": "mavis-install\\install-info-mavis-4.py",  # new
        "install mavis4": "mavis-install\\install-info-mavis-4.py",  # new
        "install mavis4.3": "mavis-install\\install-info-mavis-4.py",  # new
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
        "fastfetch": "pp-commands\\neofetch.py",  # new
        "screenfetch": "pp-commands\\neofetch.py",  # new
        "jupyter": "mavis-run-jup\\run-jup.py",
        "run jupyter": "mavis-run-jup\\run-jup.py",
        "run ju": "mavis-run-jup\\run-jup.py",  # new
        "run mavis-4": "pp-commands\\run-mavis-4.py",  # new
        "run mavis-4-3": "pp-commands\\run-mavis-4-3.py",  # new
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
        "run mistral-large": "pp-commands\\mistral-large.py",  # new
        "run mistral-nemo": "pp-commands\\mistral-nemo.py",  # new
        "run mistral-openorca": "pp-commands\\mistral-openorca.py",  # new
        "run mistral-small:22b": "pp-commands\\mistral-small-22b.py",  # new
        "run mistral-small:24b": "pp-commands\\mistral-small-24b.py",  # new
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
        "run qwen3:0.6b": "pp-commands\\qwen-3-0-6b.py",  # new
        "run qwen3:1.7b": "pp-commands\\qwen-3-1-7b.py",  # new
        "run qwen3:4b": "pp-commands\\qwen-3-4b.py",  # new
        "run qwen3:8b": "pp-commands\\qwen-3-8b.py",  # new
        "run qwen3:14b": "pp-commands\\qwen-3-14b.py",  # new
        "run qwen3:32b": "pp-commands\\qwen-3-32.py",  # new
        "run qwen3:30b": "pp-commands\\qwen-3-30.py",  # new
        "run qwen3:235b": "pp-commands\\qwen-3-235.py",  # new
        "run gemma3:1b": "pp-commands\\gemma-3-1b.py",  # new
        "run gemma3:4b": "pp-commands\\gemma-3-4b.py",  # new
        "run gemma3:12b": "pp-commands\\gemma-3-12b.py",  # new
        "run gemma3:27b": "pp-commands\\gemma-3-27b.py",  # new
        "run qwq": "pp-commands\\qwq.py",  # new
        "run command-a": "pp-commands\\command-a.py",  # new
        "run phi4-mini": "pp-commands\\phi-4-mini.py",  # new
        "run granite3.2:8b": "pp-commands\\granite-3-2-8b.py",  # new
        "run granite3.2:2b": "pp-commands\\granite-3-2-2b.py",  # new
        "run granite3.2-vision:2b": "pp-commands\\granite-3-2-2b-vision.py",  # new
        "run qwen2.5-omni:7b": "pp-commands\\qwen-2-5-omni-7b.py",  # new
        "run qvq:72b": "pp-commands\\qvq-72b.py",  # new
        "run qwen2.5-vl:32b": "pp-commands\\qwen-2-5-vl-32b.py",  # new
        "run qwen2.5-vl:72b": "pp-commands\\qwen-2-5-vl-72b.py",  # new
        "run llama4-maverick:17b": "pp-commands\\llama-4-maverick-17b-ollama.py",  # new
        "run llama4-scout:17b": "pp-commands\\llama-4-scout-17b-ollama.py",  # new
        "run llama4-maverick:17b hg": "pp-commands\\llama-4-maverick-17b.py",  # new
        "run llama4-scout:17b hg": "pp-commands\\llama-4-scout-17b.py",  # new
        "run deepcoder:1.5b": "pp-commands\\deepcoder-1-5b.py",  # new
        "run deepcoder:14b": "pp-commands\\deepcoder-14b.py",  # new
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
        "install mistral-large": "pp-commands\\mistral-large.py",  # new
        "install mistral-nemo": "pp-commands\\mistral-nemo.py",  # new
        "install mistral-openorca": "pp-commands\\mistral-openorca.py",  # new
        "install mistral-small:22b": "pp-commands\\mistral-small-22b.py",  # new
        "install mistral-small:24b": "pp-commands\\mistral-small-24b.py",  # new
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
        "install gemma3:1b": "pp-commands\\gemma-3-1b.py",  # new
        "install gemma3:4b": "pp-commands\\gemma-3-4b.py",  # new
        "install gemma3:12b": "pp-commands\\gemma-3-12b.py",  # new
        "install gemma3:27b": "pp-commands\\gemma-3-27b.py",  # new
        "install qwq": "pp-commands\\qwq.py",  # new
        "install command-a": "pp-commands\\command-a.py",  # new
        "install phi4-mini": "pp-commands\\phi-4-mini.py",  # new
        "install granite3.2:8b": "pp-commands\\granite-3-2-8b.py",  # new
        "install granite3.2:2b": "pp-commands\\granite-3-2-2b.py",  # new
        "install granite3.2-vision:2b": "pp-commands\\granite-3-2-2b-vision.py",  # new
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
        "p run all": "pp-commands\\p-run-all.py",  # new
        "p htop": "pp-commands\\p-htop.py",  # new
        "p run gemma3": "pp-commands\\p-gemma-3.py",  # new
        "p run deepseek-r1": "pp-commands\\p-deepseek-r1.py",  # new
        "p run qwen2.5": "pp-commands\\p-qwen-2-5.py",  # new
        "p run qwen2.5-coder": "pp-commands\\p-qwen-2-5-coder.py",  # new
        "p python frameworks": "pp-commands\\p-python-frameworks.py",  # new
        "p pip list": "pp-commands\\p-python-frameworks.py",  # new
        "p pip ls": "pp-commands\\p-python-frameworks.py",  # new
        "p git ls": "pp-commands\\p-git.py",  # new
        "p git": "pp-commands\\p-git.py",  # new
        "p git p-terminal-old": "pp-commands\\p-git-p-terminal-old.py",  # new
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
        "p git linux": "pp-commands\\p-git-linux.py",  # new
        "p ls": "pp-commands\\p-ls.py",  # new
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
        "p simon.com": "pp-commands\\p-simon-git.py",  # new
        "wsl info": "pp-commands\\wsl-info.py",  # new
        "p wsl": "pp-commands\\p-wsl.py",  # new
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
        "install 3d-slicer": "run\\simon\\3d-slicer\\install-3d-slicer.py",  # new
        "run 3d-slicer": "run\\simon\\3d-slicer\\run-3d-slicer.py",  # new
        "install simon": "run\\simon\\install-simon-1.py",  # new
        "run simon": "mavis-run-jup\\run-jup.py",  # new
        "jupyter --version": "pp-commands\\jupyter-version.py",  # new
        "grafana --version": "pp-commands\\grafana-version.py",  # new
        "3d-slicer --version": "pp-commands\\3d-slicer-version.py",  # new
        "doctor": "pp-commands\\doctor.py",  # new
        "hole doctor": "pp-commands\\doctor-hole.py",  # new
        "fun": "pp-commands\\fun-matrix.py",  # new
        "fun sl": "pp-commands\\fun-sl.py",  # new
        "fun aafire": "pp-commands\\fun-aafire.py",  # new
        "fun cmatrix": "pp-commands\\fun-cmatrix.py",  # new
        "fun cow": "pp-commands\\fun-cow.py",  # new
        "fun dragon": "pp-commands\\fun-dragon.py",  # new
        "fun figlet": "pp-commands\\fun-figlet.py",  # new
        "fun fortune": "pp-commands\\fun-fortune.py",  # new
        "install fun main": "pp-commands\\fun-install.py",  # new
        "install fun games main": "pp-commands\\fun-install.py",  # new
        "install fun calc main": "pp-commands\\fun-install.py",  # new
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
        "install fun": "pp-commands\\fun-matrix.py",  # new
        "finstall un sl": "pp-commands\\fun-sl.py",  # new
        "install fun aafire": "pp-commands\\fun-aafire.py",  # new
        "install fun cmatrix": "pp-commands\\fun-cmatrix.py",  # new
        "install fun cow": "pp-commands\\fun-cow.py",  # new
        "install fun dragon": "pp-commands\\fun-dragon.py",  # new
        "install fun figlet": "pp-commands\\fun-figlet.py",  # new
        "install fun fortune": "pp-commands\\fun-fortune.py",  # new
        "install fun ponysay": "pp-commands\\fun-ponysay.py",  # new
        "install fun telnet": "pp-commands\\fun-telnet.py",  # new
        "install fun train": "pp-commands\\fun-train.py",  # new
        "install fun install games": "pp-commands\\fun-install-games.py",  # new
        "install fun bastet": "pp-commands\\fun-bashtet.py",  # new
        "install fun chess": "pp-commands\\fun-gnuchess.py",  # new
        "install fun moon-buggy": "pp-commands\\fun-moon-buggy.py",  # new
        "install fun nethack": "pp-commands\\fun-nethack-console.py",  # new
        "install fun nsnake": "pp-commands\\fun-nsnake.py",  # new
        "install fun pacman": "pp-commands\\fun-pacman4console.py",  # new
        "install fun tictactoe": "pp-commands\\fun-tictactoe-ng.py",  # new
        "install fun tint": "pp-commands\\fun-tint.py",  # new
        "install fun tetris": "pp-commands\\fun-vitetris.py",  # new
        "install fun calculator": "pp-commands\\fun-calc.py",  # new
        "install fun calc": "pp-commands\\fun-calc.py",  # new
        "install fun install calculator": "pp-commands\\fun-install-calc.py",  # new
        "install fun matrix": "pp-commands\\fun-matrix.py",  # new
        "install fun matrix green": "pp-commands\\fun-matrix-green.py",  # new
        "install fun aquarium": "pp-commands\\fun-asciiquarium.py",  # new
        "install fun aqua": "pp-commands\\fun-asciiquarium.py",  # new
        "install fun bb": "pp-commands\\fun-bb.py",  # new
        "install cool pin": "pp-commands\\theme-pcc.py",  # new
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
        "run githubdesktop": "pp-commands\\run-githubdesktop.py",  # new
        "run dockerdesktop": "pp-commands\\run-dockerdesktop.py",  # new
        "run pycharm": "pp-commands\\run-pycharm.py",  # new
        "run vs-code": "pp-commands\\run-vs-code.py",  # new
        "run vs": "pp-commands\\run-vs.py",  # new
        "p map": "pp-commands\\p-map.py",  # new
        "p weather": "pp-commands\\p-weather.py",  # new
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
        "p savannah gnu": "pp-commands\\p-savannah-gnu.py",  # new
        "p gnu": "pp-commands\\p-gnu.py",  # new
        "p gnu software": "pp-commands\\p-gnu-software.py",  # new
        "p git.com": "pp-commands\\p-git-com.py",  # new
        "run mavis main": "pp-commands\\run-mavis-main.py",  # new
        "run mavis main fast": "pp-commands\\run-mavis-main-fast.py",  # new
        "htop": "pp-commands\\htop.py",  # new
        "bashtop": "pp-commands\\bashtop.py",  # new
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
        "bpytop": "pp-commands\\bpytop.py",  # new
        "belnder": "pp-commands\\belnder.py",  # new
        "clion": "pp-commands\\clion.py",  # new
        "community": "pp-commands\\community.py",  # new
        "intellij": "pp-commands\\intellij.py",  # new
        "pycharm": "pp-commands\\pycharm.py",  # new
        "rider": "pp-commands\\rider.py",  # new
        "vs-code": "pp-commands\\vs-code.py",  # new
        "webstorm": "pp-commands\\webstorm.py",  # new
        "golab": "pp-commands\\golab.py",  # new
        "phpstorm": "pp-commands\\phpstorm.py",  # new
        "githubdesktop": "pp-commands\\githubdesktop.py",  # new
        "nvim": "pp-commands\\nvim.py",  # new
        "code": "pp-commands\\code.py",  # new
        "micro": "pp-commands\\micro.py",  # new
        "gedit": "pp-commands\\gedit.py",  # new
        "update": "pp-commands\\update.py",  # new
        "selfupdate": "pp-commands\\update.py",  # new
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
        "weather": "pp-commands\\weather.py",  # new
        "g++": "pp-commands\\gpp.py",  # new
        "gcc": "pp-commands\\gcc.py",  # new
        "install alpine-wsl": "run\\wsl\\install-alpine-wsl.py",  # new
        "install arch-wsl": "run\\wsl\\install-arch-wsl.py",  # new
        "install clear-wsl": "run\\wsl\\install-clear-wsl.py",  # new
        "install debian-wsl": "run\\wsl\\install-debian-wsl.py",  # new
        "install fedora-wsl": "run\\wsl\\install-fedora-wsl.py",  # new
        "install kali-wsl": "run\\wsl\\install-kali-wsl.py",  # new
        "install mint-wsl": "run\\wsl\\install-mint-wsl.py",  # new
        "install opensuse-wsl": "run\\wsl\\install-opensuse-wsl.py",  # new
        "install oracle-wsl": "run\\wsl\\install-oracle-wsl.py",  # new
        "install pengwin-wsl": "run\\wsl\\install-pengwin-wsl.py",  # new
        "install redhat-wsl": "run\\wsl\\install-redhat-wsl.py",  # new
        "install suse-wsl": "run\\wsl\\install-suse-wsl.py",  # new
        "install ubuntu-wsl": "run\\wsl\\install-ubuntu-wsl.py",  # new
        "install wsl": "run\\wsl\\install-wsl.py",  # new
        "install vs-code": "run\vs\\install-vs-code.py",  # new
        "install rustup": "run\\rust\\rustup\\install-rustup.py",  # new
        "install ruby": "run\\ruby\\install-ruby.py",  # new
        "install rscript": "run\\ruby\\install-rscript.py",
        "install pycharm": "run\\pycharm\\install-pycharm.py",  # new
        "install nodejs": "run\\java\\javac\\install-nodejs.py",  # new
        "install githubdesktop": "run\\github\\install-githubdesktop.py",  # new
        "install docker": "run\\docker\\install-dockerdesktop.py",  # new
        "install vs-cpp": "run\\cpp\\install-vs-cpp.py",  # new
        "install vs-c": "run\\c\\install-vs-c.py",  # new
        "install vs-cs": "run\\cs\\install-vs.py",  # new
        "install go": "run\\go\\install-go.py",  # new
        "install julia": "run\\julia\\install-julia.py",  # new
        "install ffmpeg": "run\\ffmpeg\\install-ffmpeg.py",  # new
        "install clojure": "run\\clojure\\install-clojure.py",  # new
        "install dart": "run\\dart\\install-dart.py",  # new
        "install elixir": "run\\elixir\\install-elixir.py",  # new
        "install elm": "run\\elm\\install-elm.py",  # new
        "install fs": "run\\fs\\install-fs.py",  # new
        "install haskell": "run\\haskell\\install-haskell.py",  # new
        "install kotlin": "run\\haskell\\install-kotlin.py",  # new
        "install lua": "run\\lua\\install-lua.py",  # new
        "install php": "run\\php\\install-php.py",  # new
        "install scala": "run\\scala\\install-scala.py",  # new
        "install swift": "run\\swift\\install-swift.py",  # new
        "install typescript": "run\\typescript\\install-typescript.py",  # new
        "install zig": "run\\zig\\install-zig.py",  # new
        "install v": "run\\v\\install-v.py",  # new
        "install solidity": "run\\solidity\\install-solidity.py",  # new
        "install nim": "run\\nim\\install-nim.py",  # new
        "install haxe": "run\\haxe\\install-haxe.py",  # new
        "install hack": "run\\hack\\install-hack.py",  # new
        "install fortran": "run\\fortran\\install-fortran.py",  # new
        "install lisp": "run\\lisp\\install-lisp.py",  # new
        "install racket": "run\\racket\\install-racket.py",  # new
        "install g++": "pp-commands\\gpp.py",  # new
        "install gcc": "pp-commands\\gcc.py",  # new
        "install algol": "pp-commands\\gcc.py",  # new
        "install htop": "pp-commands\\htop.py",  # new
        "install bashtop": "pp-commands\\bashtop.py",  # new
        "install taskmanager": "pp-commands\\bashtop.py",  # new
        "install btop": "pp-commands\\btop.py",  # new
        "install atop": "pp-commands\\atop.py",  # new
        "install emacs": "pp-commands\\emacs.py",  # new
        "install vim": "pp-commands\\vim.py",  # new
        "install nano": "pp-commands\\nano.py",  # new
        "install dstat": "pp-commands\\dstat.py",  # new
        "install nmon": "pp-commands\\nmon.py",  # new
        "install glances": "pp-commands\\glances.py",  # new
        "install iftop": "pp-commands\\iftop.py",  # new
        "install nethogs": "pp-commands\\nethogs.py",  # new
        "install bmon": "pp-commands\\bmon.py",  # new
        "install tcpdump": "pp-commands\\tcpdump.py",  # new
        "install speedtest-cli": "pp-commands\\speedtest-cli.py",  # new
        "install ncdu": "pp-commands\\ncdu.py",  # new
        "install duf": "pp-commands\\duf.py",  # new
        "install lsblk": "pp-commands\\lsblk.py",  # new
        "install iotop": "pp-commands\\iotop.py",  # new
        "install fzf": "pp-commands\\fzf.py",  # new
        "install fd": "pp-commands\\fd.py",  # new
        "install ripgrep": "pp-commands\\ripgrep.py",  # new
        "install tmux": "pp-commands\\tmux.py",  # new
        "install bat": "pp-commands\\bat.py",  # new
        "install exa": "pp-commands\\exa.py",  # new
        "install tldr": "pp-commands\\tldr.py",  # new
        "install gitui": "pp-commands\\gitui.py",  # new
        "install lazygit": "pp-commands\\lazygit.py",  # new
        "install zoxide": "pp-commands\\zoxide.py",  # new
        "install starship": "pp-commands\\starship.py",  # new
        "install nala": "pp-commands\\nala.py",  # new
        "install bpytop": "pp-commands\\bpytop.py",  # new
        "install belnder": "pp-commands\\belnder.py",  # new
        "install clion": "pp-commands\\clion.py",  # new
        "install community": "pp-commands\\community.py",  # new
        "install intellij": "pp-commands\\intellij.py",  # new
        "install rider": "pp-commands\\rider.py",  # new
        "install webstorm": "pp-commands\\webstorm.py",  # new
        "install golab": "pp-commands\\golab.py",  # new
        "install phpstorm": "pp-commands\\phpstorm.py",  # new
        "install nvim": "pp-commands\\nvim.py",  # new
        "install code": "pp-commands\\code.py",  # new
        "install micro": "pp-commands\\micro.py",  # new
        "install gedit": "pp-commands\\gedit.py",  # new
        "install update": "pp-commands\\update.py",  # new
        "install selfupdate": "pp-commands\\update.py",  # new
        "install update pp-term": "pp-commands\\updade.py",  # new
        "install kakoune": "pp-commands\\kakoune.py",  # new
        "install helix": "pp-commands\\helix.py",  # new
        "install jed": "pp-commands\\jed.py",  # new
        "install joe": "pp-commands\\joe.py",  # new
        "install mg": "pp-commands\\mg.py",  # new
        "install acme": "pp-commands\\acme.py",  # new
        "install geany": "pp-commands\\geany.py",  # new
        "install kate": "pp-commands\\kate.py",  # new
        "install mousepad": "pp-commands\\mousepad.py",  # new
        "install xed": "pp-commands\\xed.py",  # new
        "install entr": "pp-commands\\entr.py",  # new
        "install asdf": "pp-commands\\asdf.py",  # new
        "install direnv": "pp-commands\\direnv.py",  # new
        "install nmap": "pp-commands\\nmap.py",  # new
        "install iperf3": "pp-commands\\iperf3.py",  # new
        "install glow": "pp-commands\\glow.py",  # new
        "install ranger": "pp-commands\\ranger.py",  # new
        "install espanso": "pp-commands\\espanso.py",  # new
        "install plasma-workspace": "pp-commands\\plasma-workspace.py",  # new
        "install syncthing": "pp-commands\\syncthing.py",  # new
        "install flatpak": "pp-commands\\flatpak.py",  # new
        "install atom": "pp-commands\\atom.py",  # new
        "install lite-xl": "pp-commands\\lite-xl.py",  # new
        "install weather": "pp-commands\\weather.py",  # new
        "update ollama": "pp-commands\\update-ollama.py",  # new
        "update git": "pp-commands\\update-git.py",  # new
        "update visual studio build tools": "pp-commands\\update-vsb.py",  # new
        "update vsb": "pp-commands\\update-vsb.py",  # new
        "update rustup": "pp-commands\\update-rustup.py",  # new
        "update docker": "pp-commands\\update-docker.py",  # new
        "update wsl": "pp-commands\\update-wsl.py",  # new
        "update powershell": "pp-commands\\update-powershell.py"  # new
    }

    # Hier alles in der if-Schleife:
    if user_input in commands:
        # 1) Skript-Pfad ermitteln
        base = Path.home() / "p-terminal" / "pp-term"
        script_path = base / commands[user_input]
        if not script_path.exists():
            logging.error(f"[ERROR] Script not found:{script_path}")
            sys.exit(1)

        # 2) Maximale Priorität und CPU-Affinität vorbereiten
        if platform.system() == "Windows":
            # direkt beim Popen über creationflags setzen
            creationflags = psutil.REALTIME_PRIORITY_CLASS
            logging.info("[INFO] Windows REALTIME_PRIORITY_CLASS selected")
        else:
            # Unix: nice -20 ergibt höchste Priorität (evtl. Root-Rechte nötig)
            # Wir setzen hier nur den Wert und übergeben ihn später ans Popen
            nice_value = -20
            creationflags = 0  # kein Windows-Flag
            logging.info(f"[INFO] Unix nice value {nice_value} selected")

        # Volle CPU-Affinität auf alle physischen Kerne (oder alle logischen)
        all_cores = list(range(psutil.cpu_count(logical=True)))
        logging.info(f"[INFO] CPU affinity to cores {all_cores}")

        # 3) Kommandozeile zusammenbauen
        if script_path.suffix.lower() == ".bat":
            command = [str(script_path)]
            logging.info("[INFO] Start batch file")
        else:
            command = [python_path, str(script_path)]
            logging.info(f"[INFO] Start Python script with {python_path}")

        # 4) Prozess schnell starten
        try:
            # Unter Windows mit REALTIME, sonst normal
            proc = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=creationflags
            )
            p = psutil.Process(proc.pid)

            # Unix: nice setzen
            if platform.system() != "Windows":
                try:
                    p.nice(nice_value)
                    logging.info(f"[INFO] Unix nice set: {nice_value}")
                except Exception as e:
                    logging.warning(f"[INFO] CPU affinity set to all cores{e}")

            # CPU-Affinität
            try:
                p.cpu_affinity(all_cores)
                logging.info("[INFO] CPU affinity set to all cores")
            except Exception as e:
                logging.warning(f"[WARING] Could not set CPU affinity:{e}")

            # 5) Auf Beendigung warten
            stdout, stderr = proc.communicate()
            if proc.returncode != 0:
                logging.error(f"[ERROR] Script error {proc.returncode}:\n{stderr.decode().strip()}")
                return True
            else:
                logging.info(f"[PASS] Script completed successfully: \n{stdout.decode().strip()}")
                return True
        except Exception as e:
            logging.exception(f"[ERROR] Error starting the script: {e}")
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

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git pretty":

        command = f"git log --pretty=format:'%Cred%h%Creset - %Cgreen%cd%Creset - %s %C(bold blue)<%an>%Creset' --date=short"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git tig":

        command = f"tig"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git lazy":

        command = f"lazygit"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git ls hole":

        command = "gitk --all"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git status":

        command = "git status -sb"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git diff":

        command = "git diff --color-word"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git branches":

        command = "git branch -vv -a"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "git stash":

        command = "git stash list --pretty=format:'%C(yellow)%gd%Creset %Cgreen%cr%Creset %s %C(red)[%an]'"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing Git command: {e}")
        return True

    if user_input.lower() == "cloc .":

        command = f"wsl cloc ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count":

        command = f"wsl cloc ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count1":

        command = f"wsl cloc ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "cloc *":

        command = f"wsl cloc *"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count2":

        command = f"wsl cloc *"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("cloc --exclude-dir="):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("ls count-dir="):
        user_input = user_input[13:].strip()
        command = f"wsl cloc --exclude-dir={user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("cloc --include-lang="):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("ls count-lang="):
        user_input = user_input[14:].strip()
        command = f"wsl cloc --include-lang={user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "cloc --by-file":

        command = f"wsl cloc --by-file"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count3":

        command = f"wsl cloc --by-file"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "cloc --csv":

        command = f"wsl cloc --csv"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count4":

        command = f"wsl cloc --csv"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "cloc --json":

        command = f"wsl cloc --json"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count5":

        command = f"wsl cloc --json"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "cloc --quiet":

        command = f"wsl cloc --quiet"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count --quiet":

        command = f"wsl cloc --quiet"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "cloc --help":

        command = f"wsl cloc --help"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count --help":

        command = f"wsl cloc --help"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "cloc --versions":

        command = f"wsl cloc --versions"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "ls count --versions":

        command = f"wsl cloc --versions"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "disk usage":

        command = f"wsl du -sh ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "tree2":

        command = f"wsl tree -L 2"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "find py":

        command = f"wsl find . -name '*.py'"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

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

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

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

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "format":

        command = f"wsl black ."

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "top":

        command = f"wsl top"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.lower() == "disk":

        command = f"wsl df -h"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("nano "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("emacs "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("vim "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("nvim "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("micro "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("code "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("gedit "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("kakoune "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("helix "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("jed "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("joe "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("mg "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("acme "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("geany "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("kate "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("ncdu "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("tldr "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("bat "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("exa "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("fzf "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("fd "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("tmux "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("entr "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("asdf "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("direnv "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("nmap "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("iperf3 "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("speedtest-cli "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("glow "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("ranger "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("zoxide "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("nala "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("espanso "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("plasma-workspace "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("syncthing "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("flatpak "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("mousepad "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("xed "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("atom "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("lite-xl "):

        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] Error executing WSL command: {e}")
        return True

    if user_input.startswith("g++ "):
        user_input = user_input[4:].strip()

        command = f"wsl g++ -o {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with g++")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("g++ -o "):
        user_input = user_input[7:].strip()

        command = f"wsl g++ -o {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with g++")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.lower() == "g++-version":

        command = f"wsl g++ --version"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("gcc "):
        user_input = user_input[4:].strip()

        command = f"wsl gcc++ -o {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with gcc")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("gcc -o "):
        user_input = user_input[7:].strip()

        command = f"wsl gcc -o {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with gcc")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.lower() == "gcc-version":
        command = f"wsl {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    elif user_input.startswith("vs-cpp "):
        user_input = user_input[7:].strip()
        print(f"[{timestamp()}] [INFO] Compile {user_input} with Visual Wtudio Building Tools 20222")
        handle_vs_cpp_command(user_input)
        return True

    elif user_input.startswith("cppc "):
        user_input = user_input[5:].strip()
        print(f"[{timestamp()}] [INFO] Compile {user_input} with Visual Wtudio Building Tools 20222")
        handle_vs_cpp_command(user_input)
        return True

    elif user_input.startswith("pc-cpp "):
        user_input = user_input[7:].strip()
        print(f"[{timestamp()}] [INFO] Compile {user_input} with Visual Wtudio Building Tools 20222")
        handle_vs_cpp_command(user_input)
        return True

    elif user_input.startswith("vs-c "):
        user_input = user_input[5:].strip()
        print(f"[{timestamp()}] [INFO] Compile {user_input} with Visual Wtudio Building Tools 20222")
        handle_vs_c_command(user_input)
        return True

    elif user_input.startswith("cc "):
        user_input = user_input[3:].strip()
        print(f"[{timestamp()}] [INFO] Compile {user_input} with Visual Wtudio Building Tools 20222")
        handle_vs_c_command(user_input)
        return True

    elif user_input.startswith("pc-c "):
        user_input = user_input[5:].strip()
        print(f"[{timestamp()}] [INFO] Compile {user_input} with Visual Wtudio Building Tools 20222")
        handle_vs_c_command(user_input)
        return True

    elif user_input.startswith("vs-cs "):
        user_input = user_input[6:].strip()
        print(f"[{timestamp()}] [INFO] Compile {user_input} with Visual Wtudio Building Tools 20222")
        handle_vs_cs_command(user_input)
        return True

    elif user_input.startswith("csc "):
        user_input = user_input[4:].strip()
        print(f"[{timestamp()}] [INFO] Compile {user_input} with Visual Wtudio Building Tools 20222")
        handle_vs_cs_command(user_input)
        return True

    elif user_input.startswith("pc-cs "):
        user_input = user_input[6:].strip()
        print(f"[{timestamp()}] [INFO] Compile {user_input} with Visual Wtudio Building Tools 20222")
        handle_vs_cs_command(user_input)
        return True

    if user_input.startswith("rustc "):
        user_input = user_input[6:].strip()

        command = f"rustc {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with rustup")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-rust "):
        user_input = user_input[8:].strip()

        command = f"rustc {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with rustup")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("node "):
        user_input = user_input[5:].strip()

        command = f"node {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with nodejs")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("jsc "):
        user_input = user_input[4:].strip()

        command = f"node {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with NodeJs")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-js "):
        user_input = user_input[6:].strip()

        command = f"node {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with NodeJs")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("javac "):
        user_input = user_input[6:].strip()

        command = f"javac {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Java - JDK")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-java "):
        user_input = user_input[8:].strip()

        command = f"javac {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Java - JDK")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("ruby "):
        user_input = user_input[5:].strip()

        command = f"ruby {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Ruby")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("rubyc "):
        user_input = user_input[6:].strip()

        command = f"ruby {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Ruby")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-ruby "):
        user_input = user_input[8:].strip()

        command = f"ruby {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Ruby")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("Rscript "):
        user_input = user_input[8:].strip()

        command = f"Rscript {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Rscript")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("Rscriptc "):
        user_input = user_input[9:].strip()

        command = f"Rscript {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Rscript")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-r "):
        user_input = user_input[5:].strip()

        command = f"Rscript {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Rscript")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pyinstaller --onefile "):
        user_input = user_input[22:].strip()

        command = f"pyinstaller --onefile {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with PyInstaller")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pythonc "):
        user_input = user_input[8:].strip()

        command = f"pyinstaller --onefile {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with PyInstaller")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-python "):
        user_input = user_input[10:].strip()

        command = f"pyinstaller --onefile {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with PyInstaller")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-python-all "):
        user_input = user_input[14:].strip()

        command = f"pyinstaller --onefile --noconsole --icon={user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with PyInstaller")
            print(f"[{timestamp()}] [INFO] Note the systkas: pc-python-all mein_icon.ico meine_app.py")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("go run "):
        user_input = user_input[7:].strip()

        command = f"go run {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with GO")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("go build "):
        user_input = user_input[9:].strip()

        command = f"go build {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with GO")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("goc "):
        user_input = user_input[4:].strip()

        command = f"go build {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with GO Build")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-go "):
        user_input = user_input[6:].strip()

        command = f"go build {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with GO Build")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("julia "):
        user_input = user_input[6:].strip()

        command = f"julia {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Julia")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("juliac "):
        user_input = user_input[7:].strip()

        command = f"julia {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Julia")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-julia "):
        user_input = user_input[9:].strip()

        command = f"julia {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Julia")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("php "):
        user_input = user_input[4:].strip()

        command = f"php {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with PHP")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("phpc "):
        user_input = user_input[5:].strip()

        command = f"php {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with PHP")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-php "):
        user_input = user_input[7:].strip()

        command = f"php {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with PHP")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("lua "):
        user_input = user_input[4:].strip()

        command = f"lua {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Lua")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("glue srlua.exe "):
        user_input = user_input[15:].strip()

        command = f"glue srlua.exe {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with PyInstaller")
            print(f"[{timestamp()}] [INFO] Note the systkas: glue srlua.exe script.luac myprogram.exe")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("luac "):
        user_input = user_input[5:].strip()

        command = f"glue srlua.exe {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Glue")
            print(f"[{timestamp()}] [INFO] Note the systkas: luac script.luac myprogram.exe")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-lua "):
        user_input = user_input[7:].strip()

        command = f"lua {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Lua")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pce-lua "):
        user_input = user_input[7:].strip()

        command = f"glue srlua.exe {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Glue")
            print(f"[{timestamp()}] [INFO] Note the systkas: pce-lua script.luac myprogram.exe")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("tsc "):
        user_input = user_input[4:].strip()

        command = f"tsc {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Tsc")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-tsc "):
        user_input = user_input[7:].strip()

        command = f"tsc {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Tsc")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("ts-node "):
        user_input = user_input[9:].strip()

        command = f"ts-node {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with TypeScript NodeJs")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("tsc "):
        user_input = user_input[4:].strip()

        command = f"ts-node {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with TypeScript NodeJs")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-ts "):
        user_input = user_input[6:].strip()

        command = f"ts-node {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with TypeScript NodeJs")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("kotlinc "):
        user_input = user_input[8:].strip()

        command = f"kotlinc hello.kt -include-runtime -d {user_input}"  # .jar

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Kotlinc hello.kt")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("kotlinc1 "):
        user_input = user_input[9:].strip()

        command = f"kotlinc hello.kt -include-runtime -d {user_input}"  # .jar

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Kotlinc hello.kt")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("kotlinc2 "):
        user_input = user_input[9:].strip()

        command = f"java -jar {user_input}"  # .jar

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Java")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("kotlinc3 "):
        user_input = user_input[9:].strip()

        command = f"kotlinc -script {user_input}"  # .kts

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Kotlinc")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-kotlin "):
        user_input = user_input[10:].strip()

        command = f"kotlinc -script {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Kotlinc")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("swift "):
        user_input = user_input[6:].strip()

        command = f"swift {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Swift")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("swiftc "):
        user_input = user_input[7:].strip()

        command = f"swift {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Swift")
            print(f"[{timestamp()}] [INFO] Note the systkas: swiftc hello.swift -o hello.exe")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-swift "):
        user_input = user_input[9:].strip()

        command = f"swift {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Swift")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("dart run "):
        user_input = user_input[9:].strip()

        command = f"dart run {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Dart")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("dartc "):
        user_input = user_input[6:].strip()

        command = f"dart run {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Dart")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-dart "):
        user_input = user_input[8:].strip()

        command = f"dart run {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Dart")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("ghc "):
        user_input = user_input[4:].strip()

        command = f"ghc {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Ghc")
            print(f"[{timestamp()}] [INFO] Note the systkas: ghc hello.hs -o hello.exe")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("ghci "):
        user_input = user_input[5:].strip()

        command = f"ghci {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Ghci")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-haskell "):
        user_input = user_input[11:].strip()

        command = f"ghci {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Ghci")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("dotnet fsi "):
        user_input = user_input[11:].strip()

        command = f"dotnet fsi {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Dotnet Fsi")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-fs "):
        user_input = user_input[6:].strip()

        command = f"dotnet fsi {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Dotnet Fsi")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("scalac "):
        user_input = user_input[7:].strip()

        command = f"scalac {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Scalac")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-scala "):
        user_input = user_input[9:].strip()

        command = f"scalac {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Scalac")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("clj "):
        user_input = user_input[4:].strip()

        command = f"clj {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Clj")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-clj "):
        user_input = user_input[7:].strip()

        command = f"clj {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Clj")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("ocamlc "):
        user_input = user_input[7:].strip()

        command = f"ocamlc {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with ocamlc")
            print(f"[{timestamp()}] [INFO] Note the systkas: ocamlc hello.ml -o hello.exe")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-ocaml "):
        user_input = user_input[9:].strip()

        command = f"ocamlc {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with ocamlc")
            print(f"[{timestamp()}] [INFO] Note the systkas: pc-ocaml hello.ml -o hello.exe")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("elixir "):
        user_input = user_input[7:].strip()

        command = f"elixir {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Elixir")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-elixir "):
        user_input = user_input[10:].strip()

        command = f"elixir {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Elixir")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("elm make "):
        user_input = user_input[9:].strip()

        command = f"elm make {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Elm Make ")
            print(f"[{timestamp()}] [INFO] Note the systkas: elm make src/Main.elm --output=main.js")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-elm "):
        user_input = user_input[7:].strip()

        command = f"elm make {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Elm Make ")
            print(f"[{timestamp()}] [INFO] Note the systkas: pc-elm src/Main.elm --output=main.js")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("v run "):
        user_input = user_input[7:].strip()

        command = f"v run {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with V")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-v "):
        user_input = user_input[5:].strip()

        command = f"v run {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with V")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("zig build-exe "):
        user_input = user_input[14:].strip()

        command = f"zig build-exe {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Zig")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("zigc "):
        user_input = user_input[5:].strip()

        command = f"zig build-exe {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Zig")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-zig "):
        user_input = user_input[7:].strip()

        command = f"zig build-exe {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Zig")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("nim compile "):
        user_input = user_input[12:].strip()

        command = f"nim compile {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Nim")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("nimc "):
        user_input = user_input[5:].strip()

        command = f"nim compile {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Nim")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-nim "):
        user_input = user_input[7:].strip()

        command = f"nim compile {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Nim")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("bazel run //explorer -- ./"):
        user_input = user_input[26:].strip()

        command = f"bazel run //explorer -- ./{user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Bazel")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("carbanc "):
        user_input = user_input[8:].strip()

        command = f"bazel run //explorer -- ./{user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Bazel")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-carban "):
        user_input = user_input[10:].strip()

        command = f"bazel run //explorer -- ./{user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Bazel")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("solc --bin --abi "):
        user_input = user_input[17:].strip()

        command = f"solc --bin --abi {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Solc -> solc --bin --abi")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("solidityc "):
        user_input = user_input[10:].strip()

        command = f"solc --bin --abi {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Solc -> solc --bin --abi")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-solidity "):
        user_input = user_input[12:].strip()

        command = f"solc --bin --abi {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Solc -> solc --bin --abi")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("hhvm "):
        user_input = user_input[5:].strip()

        command = f"hhvm {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Hhvm")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("hackc "):
        user_input = user_input[6:].strip()

        command = f"hhvm {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Hhvm")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-hack "):
        user_input = user_input[8:].strip()

        command = f"hhvm {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Hhvm")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("crystal run "):
        user_input = user_input[12:].strip()

        command = f"crystal run {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Crystal")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("crystalc "):
        user_input = user_input[9:].strip()

        command = f"crystal run {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Crystal")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-crystal "):
        user_input = user_input[11:].strip()

        command = f"crystal run {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Crystal")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("haxe -main "):
        user_input = user_input[11:].strip()

        command = f"haxe -main {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Haxe")
            print(f"[{timestamp()}] [INFO] Note the systkas: haxe -main Hello -js hello.js")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("haxec "):
        user_input = user_input[6:].strip()

        command = f"haxe -main {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Haxe")
            print(f"[{timestamp()}] [INFO] Note the systkas: haxec Hello -js hello.js")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-haxe "):
        user_input = user_input[8:].strip()

        command = f"haxe -main {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Haxe")
            print(f"[{timestamp()}] [INFO] Note the systkas: pc-haxe Hello -js hello.js")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("gfortran -o "):
        user_input = user_input[12:].strip()

        command = f"gfortran -o {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Gfortran")
            print(f"[{timestamp()}] [INFO] Note the systkas: gfortran -o hello hello.f90")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("ifort -o "):
        user_input = user_input[9:].strip()

        command = f"ifort -o {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Ifort")
            print(f"[{timestamp()}] [INFO] Note the systkas: ifort -o hello hello.f90")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-fortran "):
        user_input = user_input[11:].strip()

        command = f"gfortran -o {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile your code with Gfortran")
            print(f"[{timestamp()}] [INFO] Note the systkas: pc-fortran hello hello.f90")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("sbcl --script "):
        user_input = user_input[14:].strip()

        command = f"sbcl --script {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Sbcl")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-lisp "):
        user_input = user_input[8:].strip()

        command = f"sbcl --script {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Sbcl")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("racket "):
        user_input = user_input[7:].strip()

        command = f"racket {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Racket")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("racketc "):
        user_input = user_input[8:].strip()

        command = f"racket {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Racket")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-racket "):
        user_input = user_input[10:].strip()

        command = f"racket {user_input}"

        process = subprocess.Popen(command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                   text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Racket")
            process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing pc command: {e}")
        return True

    if user_input.startswith("pc-algol "):
        user_input = user_input[9:].strip()

        # Compile the Algol60 source code
        compile_command = "wsl gcc algol60.c -o algol60"
        compile_process = subprocess.Popen(compile_command, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr,
                                           shell=True, text=True)

        # Execute the compiled program with arguments
        command_3 = f"./algol60 {user_input}"
        run_process = subprocess.Popen(command_3, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=True,
                                       text=True)

        try:
            print(f"[{timestamp()}] [INFO] Compile {user_input} with Gcc")
            compile_process.wait()
            run_process.wait()
        except KeyboardInterrupt:
            print(f"[{timestamp()}] [INFO] Cancellation by user.")
        except subprocess.CalledProcessError as e:
            print(f"[{timestamp()}] [ERROR] executing command: {e}")

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
        print(f"{timestamp()}")
        return True

    if user_input.lower() == "date":
        print(f"{timestamp()}")
        return True

    if user_input.lower() == "weather easy":
        get_weather()
        return True

    if user_input.startswith("open "):
        # Extrahiere und parse den Zielpfad / die URL
        try:
            parts = shlex.split(user_input, posix=not sys.platform.startswith("win"))
            if len(parts) < 2:
                print(f"[{timestamp()}] [ERROR] No destination specified.")
                return False
            else:
                target = parts[1]
                target_expanded = os.path.expandvars(os.path.expanduser(target))

                # URL erkennen
                if target_expanded.startswith(('http://', 'https://', 'ftp://')):
                    try:
                        webbrowser.open(target_expanded)
                        print(f"[{timestamp()}] [PASS] URL opened: {target_expanded}")
                        return True
                    except Exception as e:
                        print(f"[{timestamp()}] [ERROR] URL could not be opened: {e}")
                        return False
                else:
                    # Prüfe Existenz im Dateisystem
                    if not os.path.exists(target_expanded):
                        print(f"[{timestamp()}] [ERROR] Not found: {target_expanded}")
                        return False
                    else:
                        try:
                            if sys.platform.startswith("win"):
                                os.startfile(target_expanded)
                            elif sys.platform.startswith("darwin"):
                                subprocess.Popen(["open", target_expanded])
                            else:
                                subprocess.Popen(["xdg-open", target_expanded])

                            print(f"[{timestamp()}] [PASS] Open: {target_expanded}")
                            return True
                        except Exception as e:
                            print(f"[{timestamp()}] [ERROR] Open failed: {e}")
                            return False
        except ValueError as e:
            print(f"[{timestamp()}] [ERROR] Parse error: {e}")
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

    if user_input.lower() == "theme":
        print("alternative", "aptscience", "arc_dark", "aurelia", "ayu_mirage", "blue", "blueglass", "cyberlife",
              "dark", "dracula",
              "fallout_pipboy", "glass", "glassmain", "green", "greenglass", "gruvbox_dark", "hackerman", "light",
              "main", "material_dark",
              "mavis_1", "mavis_3", "mavis_4", "mint", "monokai", "nord", "one_dark", "p_term", "red", "redglass",
              "solarized_dark", "spiderman",
              "tokyo_night", "ubuntu", "ubuntuglass", "violetglass", "yellowglass")
        return True

    if user_input.lower() == "pin":
        print("main/main-1", "main-3", "main-4", "main-5", "main-6", "main-7", "main-8", "main-9", "main-10", "main-11",
              "main-12", "main-13", "main-14",
              "main-15", "main-16", "main-17", "main-18", "main-19", "main-20", "main-21", "main-22", "main-23",
              "main-24", "main-25", "main-26", "main-27",
              "main-28", "main-29", "main-30", "main-31", "main-32", "main-33", "main-34", "main-35", "evil/evil-1",
              "evil-2", "evil-3", "evil-4", "evil-5",
              "stable/stable-1", "stable-2", "stable-3", "stable-4", "stable-5", "cool/cool-1", "cool-2", "cool-3",
              "cool-4", "cool-5", "cool-6", "cool-7",
              "cool-8", "cool-9", "cool-10", "cool-11", "cool-12", "cool-13", "cool-14", "cool-15", "cool-16",
              "cool-17", "cool-18", "cool-19", "cool-20",
              "cool-21", "cool-22", "cool-23")
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

            process.terminate()  # Graceful termination
            gone, alive = psutil.wait_procs([process], timeout=3)

            if alive:
                # Falls Prozess nicht terminiert hat, sofort killen
                for p in alive:
                    p.kill()
                gone, alive = psutil.wait_procs(alive, timeout=3)

            if not alive:
                print(f"[{timestamp()}] [INFO] Process {pid} has been terminated.")
            else:
                print(f"[{timestamp()}] [WARNING] Process {pid} could not be killed.")

        except ValueError:
            print(f"[{timestamp()}] [ERROR] Invalid PID: '{pid_str}' is not a valid number.")
        except psutil.NoSuchProcess:
            print(f"[{timestamp()}] [ERROR] No process with PID {pid} found.")
        except psutil.AccessDenied:
            print(f"[{timestamp()}] [ERROR] Permission denied: Unable to terminate process {pid}.")
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Unexpected error while terminating process: {str(e)}")
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
        temp = os.getenv('TEMP') or os.getenv('TMP')  # Falls TEMP nicht gesetzt ist
        if not temp or not os.path.isdir(temp):
            print(f"[{timestamp()}] [ERROR] Temporary directory not found.")
            return True

        # Sicherheitscheck: nur löschen, wenn Pfad eindeutig TEMP-Verzeichnis ist
        # z.B. Vermeide versehentliches Löschen von Wurzelverzeichnissen
        if temp in ("C:\\", "C:\\Windows", "C:\\Windows\\System32", "/"):
            print(f"[{timestamp()}] [ERROR] Unsafe temporary directory path: {temp}. Abgebrochen.")
            return True

        try:
            # Alle Dateien und Ordner im TEMP löschen
            for entry in os.listdir(temp):
                path = os.path.join(temp, entry)
                try:
                    if os.path.isfile(path) or os.path.islink(path):
                        os.unlink(path)
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                except Exception as e:
                    print(f"[{timestamp()}] [WARNING] Fehler beim Löschen von {path}: {e}")

            print(f"[{timestamp()}] [INFO] Temporary files cleaned!")
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Fehler beim Bereinigen des TEMP-Ordners: {e}")
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
    if user_input.strip().lower() == "py":
        import code
        import traceback

        print(f"[{timestamp()}] [INFO] Initializing Python REPL startup sequence...")

        try:
            active = find_active_env()
            if active is None:
                raise ValueError("Active environment is None")
            print(f"[{timestamp()}] [INFO] Active environment successfully located.")
        except Exception as e:
            print(f"[{timestamp()}] [ERROR] Failed to find active environment: {e}")
            traceback.print_exc()
        else:
            print(f"[{timestamp()}] [INFO] Launching interactive Python REPL.")
            print(f"[{timestamp()}] [INFO] Type 'exit()' or press Ctrl-D to quit.")

            try:
                if isinstance(active, dict):
                    local_ns = active
                else:
                    try:
                        local_ns = vars(active)
                    except TypeError:
                        print(
                            f"[{timestamp()}] [WARNING] Could not extract vars() from active object. Using empty namespace.")
                        local_ns = {}

                code.interact(local=local_ns)

            except SystemExit:
                print(f"[{timestamp()}] [INFO] Exiting REPL via SystemExit.")
            except Exception as e:
                print(f"[{timestamp()}] [ERROR] Unhandled exception during REPL session: {e}")
                traceback.print_exc()
            finally:
                print(f"[{timestamp()}] [INFO] Python REPL session terminated.")

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

    if user_input.startswith("pa-qwen3:0.6b "):
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

    if user_input.startswith("pa-qwen3:1.7b "):
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

    if user_input.startswith("pa-qwen3:4b "):
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

    if user_input.startswith("pa-qwen3:8b "):
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

    if user_input.startswith("pa-qwen3:14b "):
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

    if user_input.startswith("pa-qwen3:32b "):
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

    if user_input.startswith("pa-qwen3:30b "):
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

    if user_input.startswith("pa-qwen3:235b "):
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

    if user_input.startswith("pa-llama4:scout "):
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

    if user_input.startswith("pa-llama4:maverick "):
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

    if user_input.startswith("pa-deepseek-r1:1.5b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_deepseek_r1_1_5(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-deepseek-r1:7b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_deepseek_r1_7(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-deepseek-r1:8b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_deepseek_r1_8(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-deepseek-r1:14b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_deepseek_r1_14(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-deepseek-r1:32b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_deepseek_r1_32(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-deepseek-r1:70b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_deepseek_r1_70(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-deepseek-r1:671b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_deepseek_r1_671(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-gemma3:1b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_gemma3_1(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-gemma3:4b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_gemma3_4(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-gemma3:12b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_gemma3_12(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-gemma3:27b "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_gemma3_27(user_input, ollama)

        print(f"{blue}🤖 AI says{reset}:", end=" ")
        type_out_text(response)

        return True

    if user_input.startswith("pa-devstral "):
        user_input = user_input[19:].strip()
        ollama_installed = check_command_installed("ollama")
        if ollama_installed:
            print(f"[{timestamp()}] [INFO] Ollama is installed.")
        else:
            print(f"[{timestamp()}] [ERROR] Ollama is not installed. Please install it to proceed.")

        start_ollama()
        check_ollama_update()

        response = get_response_from_ollama_devstral(user_input, ollama)

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

# C:\Users\julian\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\RoamingState für Bilder

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
    "glassmain": {
        "name": "glassmain",
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
    "ubuntuglass": {
        "name": "ubuntuglass",
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
    "violetglass": {
        "name": "violetglass",
        "background": "#300A24",
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
    "yellowglass": {
        "name": "yellowglass",
        "background": "#FFD54F",
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
    "blueglass": {
        "name": "blueglass",
        "background": "#003366",
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
    "greenglass": {
        "name": "greenglass",
        "background": "#004d26",
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
    "redglass": {
        "name": "redglass",
        "background": "#660000",
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
    "mint": {
        "name": "mint",
        "background": "#202020",
        "foreground": "#DADADA",
        "black": "#1D1F21",
        "red": "#CC6666",
        "green": "#B5BD68",
        "yellow": "#F0C674",
        "blue": "#81A2BE",
        "purple": "#B294BB",
        "cyan": "#8ABEB7",
        "white": "#C5C8C6",
        "brightBlack": "#666666",
        "brightRed": "#FF6C6B",
        "brightGreen": "#C8E688",
        "brightYellow": "#FFD700",
        "brightBlue": "#9FC6FF",
        "brightPurple": "#E6A8FF",
        "brightCyan": "#A1EFE4",
        "brightWhite": "#FFFFFF",
        "cursorColor": "#A3E97B"
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
        print(
            f"[{timestamp()}] [ERROR] Unknown theme '{choice}'. Available: {', '.join(sorted(set(COLOR_SCHEMES) | set(THEME_DEFAULTS)))}")
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


def handle_vs_cpp_command(user_input: str) -> bool:
    """
    Verarbeitet den Befehl 'vs-cpp <datei>.cpp' oder direkt '<datei>.cpp' und kompiliert die angegebene C++-Datei
    mit den Visual Studio Build-Tools im aktuellen Arbeitsverzeichnis.

    Gibt True zurück, um die Schleife fortzusetzen.
    """
    parts = user_input.strip().split()

    # Erlaube Eingabe mit oder ohne 'vs-cpp'
    if len(parts) == 1 and parts[0].lower().endswith('.cpp'):
        filename = parts[0]
    elif len(parts) == 2 and parts[0].lower() == 'vs-cpp' and parts[1].lower().endswith('.cpp'):
        filename = parts[1]
    else:
        print(f"[{timestamp()}] [ERROR] Usage: vs-cpp <filename>.cpp or simply <filename>.cpp")
        return True

    # Prüfe Datei im aktuellen Verzeichnis
    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(filepath):
        print(f"[{timestamp()}] [ERROR] File not found:{filename}")
        return True

    try:
        vcvarsall = find_vcvarsall()
    except FileNotFoundError as e:
        print(e)
        return True

    # Initialisiere VS-Umgebung und kompiliere
    bat_command = f'"{vcvarsall}" x64 && cl /EHsc "{filename}"'
    # '/c' sorgt dafür, dass cmd nach Ausführung schließt
    full_command = f'cmd.exe /c "{bat_command}"'

    logging.info(f"[INFO] Execute:{bat_command}")
    try:
        # check=True wirft bei Fehler eine CalledProcessError
        subprocess.run(full_command, shell=True, check=True)
    except KeyboardInterrupt:
        print(f"[{timestamp()}] [INFO] Cancellation by user.")
    except subprocess.CalledProcessError as e:
        print(f"[{timestamp()}] [ERROR] Compilation failed (Exit {e.returncode}).")
    return True


def handle_vs_c_command(user_input: str) -> bool:
    """
    Verarbeitet C-Befehle 'vs-c <datei>.c' oder '<datei>.c'.
    Gibt True zurück, um die Schleife fortzusetzen.
    """
    parts = user_input.strip().split()
    if len(parts) == 1 and parts[0].lower().endswith('.c'):
        filename = parts[0]
    elif len(parts) == 2 and parts[0].lower() == 'vs-c' and parts[1].lower().endswith('.c'):
        filename = parts[1]
    else:
        return False

    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(filepath):
        print(f"[{timestamp()}] [ERROR] File not found:{filename}")
        return True

    try:
        vcvarsall = find_vcvarsall_c()
    except FileNotFoundError as e:
        print(e)
        return True

    bat_command = f'"{vcvarsall}" x64 && cl "{filename}"'
    full_command = f'cmd.exe /c "{bat_command}"'

    logging.info(f"[INFO] Run C-Build: {bat_command}")
    try:
        subprocess.run(full_command, shell=True, check=True)
    except KeyboardInterrupt:
        print(f"[{timestamp()}] [INFO] Cancellation by user.")
    except subprocess.CalledProcessError as e:
        print(f"[{timestamp()}] [ERROR] Compilation failed (Exit {e.returncode}).")
    return True


def handle_vs_cs_command(user_input: str) -> bool:
    """
    Verarbeitet den Befehl 'vs-cs <datei>.cs' oder direkt '<datei>.cs' und kompiliert die angegebene C#-Datei.
    """
    parts = user_input.strip().split()

    if len(parts) == 1 and parts[0].lower().endswith('.cs'):
        filename = parts[0]
    elif len(parts) == 2 and parts[0].lower() == 'vs-cs' and parts[1].lower().endswith('.cs'):
        filename = parts[1]
    else:
        print(f"[{timestamp()}] [ERROR] Usage: vs-cs <filename>.cs or simply <filename>.cs")
        return True

    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.isfile(filepath):
        print(f"[{timestamp()}] [ERROR] File not found: {filename}")
        return True

    try:
        csc_path = find_csc_path()
    except FileNotFoundError as e:
        print(e)
        return True

    output_exe = os.path.splitext(filename)[0] + '.exe'
    compile_cmd = f'"{csc_path}" /nologo /out:"{output_exe}" "{filename}"'

    logging.info(f"[INFO] Execute: {compile_cmd}")
    try:
        subprocess.run(compile_cmd, shell=True, check=True)
        print(f"[{timestamp()}] [INFO] Compilation successful: {output_exe}")
    except KeyboardInterrupt:
        print(f"[{timestamp()}] [INFO] Compilation cancelled by user.")
    except subprocess.CalledProcessError as e:
        print(f"[{timestamp()}] [ERROR] Compilation failed (Exit {e.returncode}).")
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


def get_response_from_ollama_deepseek_r1_1_5(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="deepseek-r1:1.5b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_deepseek_r1_7(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="deepseek-r1:7b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_deepseek_r1_8(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="deepseek-r1:8b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_deepseek_r1_14(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="deepseek-r1:14b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_deepseek_r1_32(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="deepseek-r1:32b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_deepseek_r1_70(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="deepseek-r1:70b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_deepseek_r1_671(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="deepseek-r1:671b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_gemma3_1(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="gemma3:1b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_gemma3_4(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="gemma3:4b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_gemma3_12(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="gemma3:12b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_gemma3_27(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="gemma3:27b",  # Modellname
            messages=[{"role": "user", "content": user_message}]
        )
        return response['message']['content']
    except Exception as e:
        return f"[{timestamp()}] [ERROR] {e}"


def get_response_from_ollama_devstral(user_message, ollama):
    """Fragt Ollama nach einer Antwort auf die Benutzereingabe."""
    try:
        response = ollama.chat(
            model="devstral",  # Modellname
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
                print(
                    f"[{timestamp()}] [INFO] New Ollama version available: {remote_version} (Current: {local_version})")
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
            raise EnvironmentError(
                f"[{timestamp()}] [INFO] Unsupported Operating System. Ollama is not supported on this platform.")
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
            subprocess.Popen([ollama_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                             close_fds=True if platform.system() != "Windows" else False)
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
            print(f"[{timestamp()}] [WARN] No further results at Offset {offset}.")
            break

        for result in results:
            link_tag = result.find('a', class_='result__a', href=True)
            desc_tag = result.find('a', class_='result__snippet') or result.find('div', class_='result__snippet')
            url = link_tag['href'] if link_tag else None
            snippet = desc_tag.get_text(strip=True) if desc_tag else 'No description available.'

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
        print(f"[{timestamp()}] [ERROR] No results found.")
    else:
        print(f"\n[{timestamp()}] [INFO] {total} Results collected.\n")

    return collected


def search_and_show_first_image(query):
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=1)
        for result in results:
            image_url = result.get("image")
            if not image_url:
                print(f"[{timestamp()}] [ERROR] No picture found.")
                return

            try:
                print(f"[{timestamp()}] [INFO] Charge picture of: {image_url}")
                response = requests.get(image_url, timeout=10)
                image = Image.open(BytesIO(response.content))
                temp_path = "temp_duck_image.jpg"
                image.convert("RGB").save(temp_path)
                print(f"[{timestamp()}] [INFO] Show picture ...")
                os.startfile(temp_path)  # Nur für Windows
                return
            except Exception as e:
                print(f"[{timestamp()}] [ERROR] Error loading or displaying the image: {e}")
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
    raise FileNotFoundError(
        f"[{timestamp()}] [ERROR] vcvarsall.bat not found. Please make sure Visual Studio is installed.")


def find_vcvarsall_c():
    """
    Sucht nach der Visual Studio Entwicklungsumgebung (vcvarsall.bat).
    """
    # Visual Studio Installationspfad (Standardort für VS 2022)
    vs_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat"
    if not os.path.isfile(vs_path):
        logging.error("[ERROR] Visual Studio vcvarsall.bat file not found.")
        raise FileNotFoundError(
            f"[{timestamp()}] [ERROR] vcvarsall.bat not found. Please ensure Visual Studio is installed.")
    return vs_path


def find_csc_path() -> str:
    """
    Searches for the C# compiler csc.exe in the .NET SDK or Visual Studio directory.
    """
    possible_paths = [
        r"C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe",
        r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe",
        r"C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Current\Bin\Roslyn\csc.exe",
    ]
    for path in possible_paths:
        if os.path.isfile(path):
            logging.info(f"[{timestamp()}] [INFO] Found csc at {path}")
            return path

    logging.error(f"[{timestamp()}] [ERROR] csc.exe not found in known locations.")
    raise FileNotFoundError(f"[{timestamp()}] [ERROR] csc.exe not found. Please install .NET SDK or Visual Studio.")


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

import os
import re
import sys
import subprocess
import ctypes

# Kritische Befehle – nur mit Warnung
FORBIDDEN_COMMANDS = [
    r"\brm\b",
    r"\bRemove-Item\b",
    r"\bdel\b",
    r"\bFormat-Volume\b",
    r"\bShutdown\b",
    r"\bStop-Computer\b",
    r"\bClear-Content\b",
    r"\bSet-Content\b",
    r"\bRemove-ItemProperty\b",
    r"\bRemove-Module\b",
    r"\bsudo\s+rm\b",
    r"\bmkfs\b",
    r"\bdiskpart\b",
    r"\breg delete\b"
]


def is_dangerous_command(command: str) -> bool:
    """
    Prüft, ob der Befehl als gefährlich eingestuft wird.
    """
    for pattern in FORBIDDEN_COMMANDS:
        if re.search(pattern, command, re.IGNORECASE):
            return True
    return False


# Interaktive Sicherheitsabfrage
def confirm_execution(command: str, dangerous: bool) -> bool:
    """
    Fragt den Benutzer, ob der Befehl ausgeführt werden darf.
    Bei gefährlichen Befehlen erfolgt eine deutliche Warnung.
    """
    logging.warning(f"[INFO] You are about to run the following command with admin privileges: {command}\n")
    if dangerous:
        logging.warning("[WARING] This command is considered potentially - critical - or - system-threatening - !")

    answer = input("Continue? [y/n]: ").strip().lower()
    return answer in ['y', 'yes']


# Admin-Befehl ausführen (plattformsicher)
def run_command_with_admin_python_privileges(command: str):
    """
    Führt einen Shell-/PowerShell-Befehl mit Adminrechten aus,
    erlaubt auch gefährliche Befehle nach ausdrücklicher Zustimmung.
    """
    import platform

    working_dir = os.getcwd()
    dangerous = is_dangerous_command(command)

    if not confirm_execution(command, dangerous):
        logging.warning("Aborted.")
        return

    if sys.platform == "win32":
        try:
            if ctypes.windll.shell32.IsUserAnAdmin():
                subprocess.run(command, shell=True, cwd=working_dir, check=True)
            else:
                ps_script = (
                    f"Set-Location -LiteralPath '{working_dir}'; "
                    f"{command}; "
                    "Read-Host 'Press Enter to exit…'"
                )

                args = [
                    "-NoProfile",
                    "-NoExit",
                    "-Command",
                    ps_script.replace('"', '`"')
                ]

                arg_list_literal = "@(" + ",".join(f'"{a}"' for a in args) + ")"

                ps_cmd = [
                    "powershell",
                    "-NoProfile",
                    "-Command",
                    "Start-Process",
                    "-FilePath", "powershell",
                    "-ArgumentList", arg_list_literal,
                    "-Verb", "RunAs"
                ]

                subprocess.run(ps_cmd, check=True)
            logging.warning("[PASS] Execution completed.")
        except subprocess.CalledProcessError as e:
            logging.warning(f"[ERROR] {e}")
        except Exception as e:
            logging.warning(f"[ERROR] Unexpected error: {e}")

    else:
        safe_cmd = command.replace("'", "'\"'\"'")
        full_script = f"cd '{working_dir}' && {safe_cmd}; echo; read -p '[Drücke Enter zum Schließen]' _"
        try:
            subprocess.run(
                ["sudo", "bash", "-c", full_script],
                check=True
            )
            logging.warning("[PASS] Execution completed.")
        except subprocess.CalledProcessError as e:
            logging.warning(f"[ERROR] Execution error: {e}")
        except Exception as e:
            logging.warning(f"[ERROR] Unexpected error: {e}")


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


def run_ninite_command(
        command: Union[str, List[str]],
        timeout: Optional[int] = None,
        capture_output: bool = False,
        retries: int = 2,
        retry_delay: float = 1.0,
        logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Führt einen Ninite-Befehl aus – superschnell, stabil und mit robustem Logger-Fallback.

    Argumente:
    command: Ninite-Befehl als String oder Liste.
    timeout: Maximale Laufzeit in Sekunden.
    capture_output: Gibt stdout/stderr zurück, wenn True.
    retries: Anzahl der Wiederholungsversuche bei Exit-Fehlern.
    retry_delay: Basisverzögerung (Sekunden) für exponentielles Backoff.
    logger: Optionaler Logger; falls keiner, wird ein Standard-Logger konfiguriert.

    Rückgabewert:
    subprocess.CompletedProcess mit .stdout/.stderr, wenn capture_output.

    Löst aus:
    RuntimeError: Wenn ninite.exe nicht gefunden wird.
    subprocess.CalledProcessError: Bei Exit-Code ≠ 0 (nach Wiederholungsversuchen).
    subprocess.TimeoutExpired: Bei Timeout.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    # Logger-Fallback und -Konfiguration
    if logger is None:
        logger = logging.getLogger("run_ninite_command")
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Zwischenspeichern des Ninite-Pfads
    if not hasattr(run_ninite_command, "_ninite_path"):
        path = shutil.which("ninite")
        if not path:
            msg = "Ninite not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_ninite_command._ninite_path = path
    ninite_path = run_ninite_command._ninite_path

    # Tokenisierung
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [ninite_path] + args

    logger.debug(f"Starting Ninite: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

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
            logger.info(f"Ninite succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise

        except subprocess.TimeoutExpired as e:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise


def run_justinstall_command(
        command: Union[str, List[str]],
        timeout: Optional[int] = None,
        capture_output: bool = False,
        retries: int = 2,
        retry_delay: float = 1.0,
        logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Führt einen Just-Install-Befehl aus – superschnell, stabil und mit robustem Logger-Fallback.

    Argumente:
    command: Just-Install-Befehl als String oder Liste.
    timeout: Maximale Laufzeit in Sekunden.
    capture_output: Gibt stdout/stderr zurück, wenn True.
    retries: Anzahl der Wiederholungsversuche bei Exit-Fehlern.
    retry_delay: Basisverzögerung (Sekunden) für exponentielles Backoff.
    logger: Optionaler Logger; falls keiner, wird ein Standard-Logger konfiguriert.

    Rückgabewert:
    subprocess.CompletedProcess mit .stdout/.stderr, wenn capture_output.

    Löst aus:
    RuntimeError: Wenn just-install.exe nicht gefunden wird.
    subprocess.CalledProcessError: Bei Exit-Code ≠ 0 (nach Wiederholungsversuchen).
    subprocess.TimeoutExpired: Bei Timeout.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    # Logger-Fallback und -Konfiguration
    if logger is None:
        logger = logging.getLogger("run_justinstall_command")
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Zwischenspeichern des Just-Install-Pfads
    if not hasattr(run_justinstall_command, "_justinstall_path"):
        path = shutil.which("just-install")
        if not path:
            msg = "Just-Install not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_justinstall_command._justinstall_path = path
    justinstall_path = run_justinstall_command._justinstall_path

    # Tokenisierung
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [justinstall_path] + args

    logger.debug(f"Starting Just-Install: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

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
            logger.info(f"Just-Install succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise

        except subprocess.TimeoutExpired as e:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise


def run_oneget_command(
        command: Union[str, List[str]],
        timeout: Optional[int] = None,
        capture_output: bool = False,
        retries: int = 2,
        retry_delay: float = 1.0,
        logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Führt einen OneGet-Befehl aus – superschnell, stabil und mit robustem Logger-Fallback.

    Argumente:
    command: OneGet/PackageManagement-Befehl als String oder Liste.
    timeout: Maximale Laufzeit in Sekunden.
    capture_output: Gibt stdout/stderr zurück, wenn True.
    retries: Anzahl der Wiederholungsversuche bei Exit-Fehlern.
    retry_delay: Basisverzögerung (Sekunden) für exponentielles Backoff.
    logger: Optionaler Logger; falls keiner, wird ein Standard-Logger konfiguriert.

    Rückgabewert:
    subprocess.CompletedProcess mit .stdout/.stderr, wenn capture_output.

    Löst aus:
    RuntimeError: Wenn oneget/PackageManagement nicht gefunden wird.
    subprocess.CalledProcessError: Bei Exit-Code ≠ 0 (nach Wiederholungsversuchen).
    subprocess.TimeoutExpired: Bei Timeout.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    # Logger-Fallback und -Konfiguration
    if logger is None:
        logger = logging.getLogger("run_oneget_command")
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Zwischenspeichern des OneGet-Pfads (PowerShell erforderlich)
    if not hasattr(run_oneget_command, "_powershell_path"):
        path = shutil.which("powershell")
        if not path:
            msg = "PowerShell not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_oneget_command._powershell_path = path
    powershell_path = run_oneget_command._powershell_path

    # Tokenisierung und Befehlszusammenbau
    # OneGet läuft als PowerShell-Modul, daher wird das Kommando als PowerShell-Argument übergeben
    ps_command = command if isinstance(command, str) else " ".join(command)
    # Sicherstellen, dass das Kommando in Anführungszeichen ist, falls nötig
    ps_args = [
        powershell_path,
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        ps_command
    ]

    logger.debug(f"Starting OneGet: {' '.join(ps_args)} (timeout={timeout}, retries={retries})")

    # Ausführung mit Wiederholungsversuchen
    attempt = 0
    while True:
        attempt += 1
        try:
            start = time.perf_counter()
            result = subprocess.run(
                ps_args,
                shell=False,
                stdout=subprocess.PIPE if capture_output else None,
                stderr=subprocess.PIPE if capture_output else None,
                text=True,
                timeout=timeout,
                check=True
            )
            duration = time.perf_counter() - start
            logger.info(f"OneGet succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise

        except subprocess.TimeoutExpired as e:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise


def run_boxstarter_command(
        command: Union[str, List[str]],
        timeout: Optional[int] = None,
        capture_output: bool = False,
        retries: int = 2,
        retry_delay: float = 1.0,
        logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Führt einen Boxstarter-Befehl aus – superschnell, stabil und mit robustem Logger-Fallback.

    Argumente:
    command: Boxstarter-Befehl als String oder Liste.
    timeout: Maximale Laufzeit in Sekunden.
    capture_output: Gibt stdout/stderr zurück, wenn True.
    retries: Anzahl der Wiederholungsversuche bei Exit-Fehlern.
    retry_delay: Basisverzögerung (Sekunden) für exponentielles Backoff.
    logger: Optionaler Logger; falls keiner, wird ein Standard-Logger konfiguriert.

    Rückgabewert:
    subprocess.CompletedProcess mit .stdout/.stderr, wenn capture_output.

    Löst aus:
    RuntimeError: Wenn Boxstarter (BoxstarterShell) nicht gefunden wird.
    subprocess.CalledProcessError: Bei Exit-Code ≠ 0 (nach Wiederholungsversuchen).
    subprocess.TimeoutExpired: Bei Timeout.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    # Logger-Fallback und -Konfiguration
    if logger is None:
        logger = logging.getLogger("run_boxstarter_command")
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Zwischenspeichern des PowerShell-Pfads (Boxstarter ist ein PowerShell-Modul)
    if not hasattr(run_boxstarter_command, "_powershell_path"):
        path = shutil.which("powershell")
        if not path:
            msg = "PowerShell not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_boxstarter_command._powershell_path = path
    powershell_path = run_boxstarter_command._powershell_path

    # Tokenisierung und Befehlskonstruktion
    # Boxstarter läuft als PowerShell-Modul, daher: Import-Module und dann Befehl ausführen
    box_command = command if isinstance(command, str) else " ".join(command)
    ps_command = f"Import-Module -Name Boxstarter; {box_command}"

    ps_args = [
        powershell_path,
        "-NoProfile",
        "-NonInteractive",
        "-Command",
        ps_command
    ]

    logger.debug(f"Starting Boxstarter: {' '.join(ps_args)} (timeout={timeout}, retries={retries})")

    # Ausführung mit Wiederholungsversuchen
    attempt = 0
    while True:
        attempt += 1
        try:
            start = time.perf_counter()
            result = subprocess.run(
                ps_args,
                shell=False,
                stdout=subprocess.PIPE if capture_output else None,
                stderr=subprocess.PIPE if capture_output else None,
                text=True,
                timeout=timeout,
                check=True
            )
            duration = time.perf_counter() - start
            logger.info(f"Boxstarter succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise

        except subprocess.TimeoutExpired as e:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise


def run_npackd_command(
        command: Union[str, List[str]],
        timeout: Optional[int] = None,
        capture_output: bool = False,
        retries: int = 2,
        retry_delay: float = 1.0,
        logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Führt einen Npackd-Befehl aus – superschnell, stabil und mit robustem Logger-Fallback.

    Argumente:
    command: NpackdCL-Befehl als String oder Liste.
    timeout: Maximale Laufzeit in Sekunden.
    capture_output: Gibt stdout/stderr zurück, wenn True.
    retries: Anzahl der Wiederholungsversuche bei Exit-Fehlern.
    retry_delay: Basisverzögerung (Sekunden) für exponentielles Backoff.
    logger: Optionaler Logger; falls keiner, wird ein Standard-Logger konfiguriert.

    Rückgabewert:
    subprocess.CompletedProcess mit .stdout/.stderr, wenn capture_output.

    Löst aus:
    RuntimeError: Wenn NpackdCL.exe nicht gefunden wird.
    subprocess.CalledProcessError: Bei Exit-Code ≠ 0 (nach Wiederholungsversuchen).
    subprocess.TimeoutExpired: Bei Timeout.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    # Logger-Fallback und -Konfiguration
    if logger is None:
        logger = logging.getLogger("run_npackd_command")
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Zwischenspeichern des NpackdCL-Pfads
    if not hasattr(run_npackd_command, "_npackdcl_path"):
        path = shutil.which("NpackdCL") or shutil.which("npackdcl")
        if not path:
            msg = "NpackdCL.exe not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_npackd_command._npackdcl_path = path
    npackdcl_path = run_npackd_command._npackdcl_path

    # Tokenisierung
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [npackdcl_path] + args

    logger.debug(f"Starting Npackd: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

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
            logger.info(f"Npackd succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise

        except subprocess.TimeoutExpired as e:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise


def run_zero_install_command(
        command: Union[str, List[str]],
        timeout: Optional[int] = None,
        capture_output: bool = False,
        retries: int = 2,
        retry_delay: float = 1.0,
        logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Führt einen Zero Install (0install)-Befehl aus – stabil, performant, mit Wiederholungslogik und Logging.

    Argumente:
    Befehl: 0install-Befehl als String oder Liste.
    Timeout: Maximale Ausführungszeit in Sekunden.
    Capture_Output: Wenn True, werden stdout/stderr erfasst.
    Retrys: Anzahl der Wiederholungen bei Fehlern.
    Retry_Delay: Anfangsverzögerung für Backoff (Sekunden).
    Logger: Optionaler Logger; bei None wird ein Standardlogger genutzt.

    Rückgabewert:
    subprocess.CompletedProcess – enthält stdout/stderr bei Bedarf.

    Löst aus:
    RuntimeError: Wenn 0install nicht gefunden wird.
    subprocess.CalledProcessError: Wenn der Befehl mit Fehlercode endet.
    subprocess.TimeoutExpired: Wenn ein Timeout erreicht wird.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    if logger is None:
        logger = logging.getLogger("run_zero_install_command")
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Suche und Cache von 0install
    if not hasattr(run_zero_install_command, "_zinst_path"):
        path = shutil.which("0install")
        if not path:
            msg = "Zero Install (0install) not found – please install and ensure it's in PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_zero_install_command._zinst_path = path
    zinst_path = run_zero_install_command._zinst_path

    # Kommando parsen
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [zinst_path] + args

    logger.debug(f"Running Zero Install: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

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
            logger.info(f"Zero Install succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise

        except subprocess.TimeoutExpired:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise


def run_appget_command(
        command: Union[str, List[str]],
        timeout: Optional[int] = None,
        capture_output: bool = False,
        retries: int = 2,
        retry_delay: float = 1.0,
        logger: Optional[logging.Logger] = None
) -> subprocess.CompletedProcess:
    """
    Führt einen AppGet-Befehl aus – superschnell, stabil und mit robustem Logger-Fallback.

    Argumente:
    command: AppGet-Befehl als String oder Liste.
    timeout: Maximale Laufzeit in Sekunden.
    capture_output: Gibt stdout/stderr zurück, wenn True.
    retries: Anzahl der Wiederholungsversuche bei Exit-Fehlern.
    retry_delay: Basisverzögerung (Sekunden) für exponentielles Backoff.
    logger: Optionaler Logger; falls keiner, wird ein Standard-Logger konfiguriert.

    Rückgabewert:
    subprocess.CompletedProcess mit .stdout/.stderr, wenn capture_output.

    Löst aus:
    RuntimeError: Wenn appget.exe nicht gefunden wird.
    subprocess.CalledProcessError: Bei Exit-Code ≠ 0 (nach Wiederholungsversuchen).
    subprocess.TimeoutExpired: Bei Timeout.
    KeyboardInterrupt: Bei Benutzerunterbrechung.
    """
    # Logger-Fallback und -Konfiguration
    if logger is None:
        logger = logging.getLogger("run_appget_command")
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # Zwischenspeichern des AppGet-Pfads
    if not hasattr(run_appget_command, "_appget_path"):
        path = shutil.which("appget")
        if not path:
            msg = "AppGet not found – please install and check PATH."
            logger.error(msg)
            raise RuntimeError(msg)
        run_appget_command._appget_path = path
    appget_path = run_appget_command._appget_path

    # Tokenisierung
    args = command if isinstance(command, list) else shlex.split(command)
    cmd = [appget_path] + args

    logger.debug(f"Starting AppGet: {' '.join(cmd)} (timeout={timeout}, retries={retries})")

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
            logger.info(f"AppGet succeeded in {duration:.2f}s (attempt {attempt})")
            return result

        except subprocess.CalledProcessError as e:
            stderr = (e.stderr or "").strip() or "<no stderr>"
            logger.error(f"Exit code {e.returncode} (attempt {attempt}): {stderr}")
            if attempt <= retries:
                wait = retry_delay * (2 ** (attempt - 1))
                logger.warning(f"Retrying in {wait:.1f}s…")
                time.sleep(wait)
                continue
            raise

        except subprocess.TimeoutExpired as e:
            logger.error(f"Timeout after {timeout}s (attempt {attempt})")
            raise

        except KeyboardInterrupt:
            logger.warning("Aborted by user")
            raise


def get_main_pin(current_dir, env_indicator_10):
    return (
            f"\n{white}┌──({reset}{blue}{getpass.getuser()}"
            + colored("㋐", attrs=["bold"])
            + f"{blue}Peharge{reset}{white})-[{reset}{blue}{current_dir}{reset}{white}]-{reset}{env_indicator_10}"
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
            f"{env_indicator_3} {blue}{getpass.getuser()}" + colored("㋐", attrs=[
        "bold"]) + f"{blue}Peharge{reset} {current_dir}:~{blue}${reset} "
    )


def get_main_6_pin(current_dir, env_indicator_main):
    return (
            f"\n{blue}🌌 [{white}{bold}{getpass.getuser()}" + colored("㋐", attrs=["bold"]) + f"Peharge{reset}{blue}]"
                                                                                            f" {dim}{timestamp()}{reset} "
                                                                                            f"{white}[{current_dir}]{reset} {env_indicator_main}"
                                                                                            f"\n{blue}➤{reset} "
    )


def get_main_7_pin(current_dir, env_indicator_main):
    return (
            f"\n{blue}╭─ {white}{bold}{getpass.getuser()}" + colored("㋐", attrs=["bold"]) + f"Peharge{reset}{blue}"
                                                                                            f"\n├─ 📁 {white}{current_dir}{blue}"
                                                                                            f"\n╰─ 🌐 {env_indicator_main}{reset}"
                                                                                            f"\n{blue}λ{reset} "
    )


def get_main_8_pin(current_dir, env_indicator_main):
    return (
            f"\n{blue}[{white}{getpass.getuser()}" + colored("㋐", attrs=[
        "bold"]) + f"Peharge{blue}]{reset}:{white}{current_dir}{reset} {blue}{env_indicator_main}{reset} ➤ "
    )


def get_main_9_pin(current_dir, env_indicator_main):
    brain = "🧠"
    return (
            f"\n{blue}{brain} {bold}AI{reset} {white}| {getpass.getuser()}" + colored("㋐", attrs=["bold"]) + "Peharge"
                                                                                                             f" | {current_dir} | {env_indicator_main}"
                                                                                                             f"\n{blue}└─▶{reset} "
    )


def get_main_10_pin(current_dir, env_indicator_main):
    chip = "🧬"
    bolt = "⚡"
    return (
            f"\n{blue}{chip} SYSTEM {white}| {bold}{getpass.getuser()}" + colored("㋐", attrs=[
        "bold"]) + f"Peharge{reset} {blue}| {current_dir}{reset}"
                   f"\n{white}{bolt} ENV: {env_indicator_main}{reset}"
                   f"\n{blue}⟩{reset} "
    )


def get_main_11_pin(current_dir, env_indicator_main):
    circuit = colored('❖❖', 'blue')
    return (
        f"\n{circuit} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + f'Peharge', 'white', attrs=['bold'])}"
        f" {colored('⟿', 'blue')} {colored(current_dir, 'white')}"
        f" {colored('⟿', 'blue')} {env_indicator_main}"
        f"\n{circuit} {colored(timestamp(), 'white')} {colored('❯', 'blue')} "
    )


def get_main_12_pin(current_dir, env_indicator_main):
    wave = colored('〰️', 'blue')
    return (
            f"\n{wave}{wave}{colored('╼', 'white')} {colored(getpass.getuser(), 'white')}" + colored("㋐", attrs=[
        "bold"]) + f"{colored('Peharge', 'white')}"
                   f" {wave}{wave}{colored('╾', 'white')} {colored(current_dir, 'white')}"
                   f" {wave}{wave}{colored('╼', 'white')} {env_indicator_main}"
                   f"\n{colored('▶', 'blue')} "
    )


def get_main_13_pin(current_dir, env_indicator_main):
    diamond = colored('◆', 'blue')
    return (
        f"\n{diamond * 3} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white', attrs=['bold'])} {diamond * 3}"
        f"\n {colored(current_dir, 'blue')} {colored('|', 'white')} {env_indicator_main}"
        f"\n{colored('⇨', 'blue')} "
    )


def get_main_14_pin(current_dir, env_indicator_main):
    pulse = colored('•', 'blue')
    return (
            f"\n{pulse} {colored('GRID>', 'white', attrs=['bold'])} {colored(getpass.getuser(), 'blue')}" + colored("㋐",
                                                                                                                    attrs=[
                                                                                                                        "bold"]) + f"{colored('Peharge', 'white')}"
                                                                                                                                   f" {pulse}\n{pulse} {colored(current_dir, 'blue')} {pulse} {env_indicator_main}"
                                                                                                                                   f"\n{pulse} {colored('»', 'blue')} "
    )


def get_main_15_pin(current_dir, env_indicator_main):
    sl = colored('⧸', 'blue')
    return (
        f"\n{sl}{sl}{sl} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white', attrs=['bold'])} {sl}{sl}{sl}"
        f"\n {colored(current_dir, 'blue')} {sl} {env_indicator_main}"
        f"\n{colored('❯', 'blue')} "
    )


def get_main_16_pin(current_dir, env_indicator_main):
    return (
        f"\n{colored('▯▯▯▯', 'blue')} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white', attrs=['bold'])}"
        f" {colored('⇢', 'blue')} {colored(current_dir, 'white')}"
        f" {colored('⇢', 'blue')} {env_indicator_main}"
        f"\n{colored('▯▯▯▯', 'blue')} {colored(timestamp(), 'white')} {colored('›', 'blue')} "
    )


def get_main_17_pin(current_dir, env_indicator_main):
    bar = colored('▮', 'blue')
    return (
        f"\n{bar * 3} {colored('DATAPULSE', 'white', attrs=['bold'])} {bar * 3}"
        f"\n{bar} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'blue')} {bar}"
        f"\n{bar} {colored(current_dir, 'white')} {bar} {env_indicator_main}"
        f"\n{bar * 3} {colored('▶', 'white')} "
    )


def get_main_18_pin(current_dir, env_indicator_main):
    node = colored('◉', 'blue')
    return (
            f"\n{node} {colored(getpass.getuser(), 'white')}" + colored("㋐",
                                                                        attrs=["bold"]) + "{colored('Peharge', 'blue')}"
                                                                                          f" {node} {colored(current_dir, 'white')} {node} {env_indicator_main}"
                                                                                          f"\n{node} {colored('❯', 'white')} "
    )


def get_main_19_pin(current_dir, env_indicator_main):
    grid = colored('⊡', 'blue')
    return (
        f"\n{grid}{grid}{grid} {colored('QUANTUM', 'white', attrs=['bold'])} {grid}{grid}{grid}"
        f"\n{colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'blue')} | {colored(current_dir, 'white')} | {env_indicator_main}"
        f"\n{colored('▸▸', 'blue')} "
    )


def get_main_20_pin(current_dir, env_indicator_main):
    return (
        f"\n{colored('~', 'blue')} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white')} {colored('~', 'blue')}"
        f" {colored(current_dir, 'blue')} {colored('/', 'white')} {env_indicator_main}"
        f"\n{colored('❯', 'blue')} "
    )


def get_main_21_pin(current_dir, env_indicator_main):
    flow = colored('»', 'blue')
    return (
        f"\n{flow * 2} {colored('BYTEFLOW', 'white', attrs=['bold'])} {flow * 2}"
        f"\n{flow} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'blue')} {flow}"
        f"\n{flow} {colored(current_dir, 'white')} {flow} {env_indicator_main}"
        f"\n{flow * 2} {colored('›', 'white')} "
    )


def get_main_22_pin(current_dir, env_indicator_main):
    prism = colored('◇', 'blue')
    return (
        f"\n{prism * 2} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white')} {prism * 2}"
        f"\n{colored(current_dir, 'blue')} {colored('⇄', 'white')} {env_indicator_main}"
        f"\n{colored('❯❯', 'blue')} "
    )


def get_main_23_pin(current_dir, env_indicator_main):
    return (
        f"\n{colored('[', 'blue')}{colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white')}{colored(']', 'blue')}"
        f"{colored('<', 'white')}{colored(current_dir, 'blue')}{colored('>', 'white')}"
        f"{colored('[', 'blue')}{env_indicator_main}{colored(']', 'white')}"
        f"\n{colored('›', 'blue')} "
    )


def get_main_24_pin(current_dir, env_indicator_main):
    slash = colored('╱', 'blue')
    return (
        f"\n{slash * 3} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white')} {slash * 3}"
        f"\n{slash} {colored(current_dir, 'blue')} {slash} {env_indicator_main}"
        f"\n{colored('❯', 'blue')} "
    )


def get_main_25_pin(current_dir, env_indicator_main):
    ring = colored('◯', 'blue')
    return (
        f"\n{ring} {colored('PEHARGE', 'white', attrs=['bold'])} {ring}"
        f"\n{colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'blue')} · {colored(current_dir, 'white')} · {env_indicator_main}"
        f"\n{colored('➤', 'blue')} "
    )


def get_main_26_pin(current_dir, env_indicator_main):
    aurora = colored('≈≈≈', 'blue')
    return (
        f"\n{aurora} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white', attrs=['bold'])} {aurora}"
        f"\n{colored(current_dir, 'blue')} {colored('~', 'white')} {env_indicator_main}"
        f"\n{colored('➤', 'blue')} "
    )


def get_main_27_pin(current_dir, env_indicator_main):
    hexg = colored('⬡', 'blue')
    return (
        f"\n{hexg * 2} {colored('HEXGRID', 'white', attrs=['bold'])} {hexg * 2}"
        f"\n{colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'blue')} {hexg} {colored(current_dir, 'white')} {hexg} {env_indicator_main}"
        f"\n{colored('›', 'blue')} "
    )


def get_main_28_pin(current_dir, env_indicator_main):
    beacon = colored('✦', 'blue')
    return (
            f"\n{beacon} {colored(getpass.getuser(), 'white')}" + colored("㋐", attrs=[
        "bold"]) + f"{colored('Peharge', 'blue')} {beacon}"
                   f"\n{colored('Dir:', 'white')} {colored(current_dir, 'blue')} {beacon} {env_indicator_main}"
                   f"\n{colored('❯', 'blue')} "
    )


def get_main_29_pin(current_dir, env_indicator_main):
    binf = colored('1010', 'blue')
    return (
        f"\n{binf} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white', attrs=['bold'])} {binf}"
        f"\n{colored(current_dir, 'blue')} | {env_indicator_main}"
        f"\n{colored('►', 'blue')} "
    )


def get_main_30_pin(current_dir, env_indicator_main):
    mesh = colored('╳', 'blue')
    return (
            f"\n{mesh}{mesh}{mesh} {colored(getpass.getuser(), 'white')}" + colored("㋐", attrs=[
        "bold"]) + f"{colored('Peharge', 'blue')} {mesh}{mesh}{mesh}"
                   f"\n{colored(current_dir, 'blue')} {mesh} {env_indicator_main}"
                   f"\n{colored('❯', 'blue')} "
    )


def get_main_31_pin(current_dir, env_indicator_main):
    star = colored('✺', 'blue')
    return (
        f"\n{star * 2} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white', attrs=['bold'])} {star * 2}"
        f"\n{colored('📂', 'white')} {colored(current_dir, 'blue')}   {env_indicator_main}"
        f"\n{colored('➤', 'blue')} "
    )


def get_main_32_pin(current_dir, env_indicator_main):
    # Sicherstellen, dass current_dir ein String ist
    if isinstance(current_dir, Path):
        current_dir = str(current_dir)

    lf = colored('╔═', 'blue')
    rt = colored('═╗', 'blue')
    lb = colored('╚═', 'blue')
    rb = colored('═╝', 'blue')

    user = getpass.getuser()
    user_display = colored(user + colored("㋐", attrs=["bold"]) + 'Peharge', 'white')
    header = f"{lf}{user_display}{rt}"
    footer = f"{lb}{colored(current_dir + ' | ' + env_indicator_main, 'blue')}{rb}"

    return f"\n{header}\n{footer}\n{colored('►', 'blue')} "


def get_main_33_pin(current_dir, env_indicator_main):
    q = colored('⟐', 'blue')
    return (
        f"\n{q} {colored('Q-PULSE', 'white', attrs=['bold'])} {q}"
        f"\n{colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'blue')} • {colored(current_dir, 'white')} • {env_indicator_main}"
        f"\n{colored('❯', 'blue')} "
    )


def get_main_34_pin(current_dir, env_indicator_main):
    arc = colored('◥◣', 'blue')
    return (
            f"\n{arc} {colored(getpass.getuser(), 'white')}" + colored("㋐", attrs=[
        "bold"]) + f"{colored('Peharge', 'blue')} {arc}"
                   f"\n{colored(current_dir, 'blue')} [{env_indicator_main}]"
                   f"\n{colored('➤', 'blue')} "
    )


def get_main_35_pin(current_dir, env_indicator_main):
    bar = colored('━', 'blue')
    return (
        f"\n{bar * 4} {colored(getpass.getuser() + colored("㋐", attrs=["bold"]) + 'Peharge', 'white', attrs=['bold'])} {bar * 4}"
        f"\n{colored(current_dir, 'blue')} {bar} {env_indicator_main}"
        f"\n{colored('›', 'blue')} "
    )


def get_evil_pin(current_dir, env_indicator_11):
    return (
            f"\n{white}┌──({reset}{red}root"
            + colored("㋐", attrs=["bold"])
            + f"{red}Peharge{reset}{white})-[{reset}{red}{current_dir}{reset}{white}]-{reset}{env_indicator_11}"
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
            f"{env_indicator_3} {red}root" + colored("㋐", attrs=[
        "bold"]) + f"{red}Peharge{reset} {current_dir}:~{red}#{reset} "
    )


def get_stable_pin(current_dir, env_indicator_6):
    return (
            f"\n┌──({getpass.getuser()}"
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
            f"{env_indicator_3} {getpass.getuser()}" + colored("㋐",
                                                               attrs=["bold"]) + f"Peharge{reset} {current_dir}:~$ "
    )


def get_stable_4_pin(current_dir, env_indicator_6):
    return (
            f"\n┌──(root"
            + colored("㋐", attrs=["bold"])
            + f"Peharge)-[{current_dir}]-{env_indicator_6}"
              f"\n└─# "
    )


def get_stable_5_pin(current_dir, env_indicator_8):
    print("")

    return (
        f"{env_indicator_8} PP {current_dir}:~# "
    )


def get_stable_6_pin(current_dir, env_indicator_8):
    print("")

    return (
            f"{env_indicator_8} root" + colored("㋐", attrs=["bold"]) + f"Peharge{reset} {current_dir}:~# "
    )


def get_cool_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """

    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\powerlevel10k_rainbow.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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


def get_cool_3_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\jandedobbeleer.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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


def get_cool_4_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """

    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\p10k_classic.omp.jso"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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


def get_cool_6_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\M365Princess.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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


def get_cool_7_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\blue-owl.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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


def get_cool_8_pin():
    """
    Ruft eine gerenderte Oh-My-Posh-Prompt basierend auf einer bestimmten Theme-Konfiguration ab.
    """
    print("")

    config_path = os.path.expanduser(
        r"~\AppData\Local\Programs\oh-my-posh\themes\aliens.omp.json"
    )
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    working_dir = os.getcwd()  # oder spezifisch: r"C:\Users\julian"

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
    "ps ls mavis-web", "p ls simon", "p simon", "p wsl", "p pip", "p models", "p ubuntu", "gitk", "git ls all",
    "git ls hole",
    "pp", "pp-cpp", "pp-c", "pp-p", "ps", "ps-github", "ps-huggingface", "ps-ollama", "ps-stackoverflow", "nano",
    "htop", "btop", "atop", "glances", "ncdu", "fzf", "bat", "gitui", "lazygit", "starship",
    "emacs", "vim", "nvim", "nano", "kate", "gedit", "geany", "code", "ps-all", "pps", "pb", "pt",
    "vscodium", "eclipse", "idea", "pycharm", "atom", "sublime_text", "kakoune", "lite-xl",
    "ps-arxiv", "pa", "run mavis main", "lx", "lx-c", "lx-p", "lx-cpp-c", "lx-c-c", "lx-p-c", "ubuntu", "ubuntu-c",
    "ubuntu-p", "debian", "debian-c", "debian-p", "kali", "kali-c", "kali-p", "hack", "arch", "arch-c",
    "arch-p", "opensuse", "opensuse-c", "opensuse-p", "mint", "mint-c", "mint-p", "fedora", "fedora-c",
    "fedora-p", "redhat", "redhat-c", "redhat-p", "sles", "sles-c", "sles-p", "pengwin", "pengwin-c",
    "pengwin-p", "oracle", "oracle-c", "oracle-p", "cd", "cls", "clear", "dir", "ls", "mkdir", "rmdir",
    "vc-cpp", "vc-c", "vc-cs", "g++", "gcc", "rustc", "node", "javac", "ruby", "Rscript", "pythonc", "go run", "julia",
    "del", "rm", "echo", "type", "cat", "exit", "alpine", "scoop", "choco", "winget", "speedtest", "kill",
    "download", "cputemp", "chucknorris", "theme", "cleantemp", "selfupdate", "tree", "py", "ask", "pb google.com"
                                                                                                   "weather", "whoami",
    "hostname", "ip", "os", "time", "date", "open", "fortune", "history", "search",
    "zip", "unzip", "sysinfo", "clip set", "clip get", "ping", "emptytrash", "launch", "doctor", "hole doctor",
    "mavis env install", "install mavis env", "install mavis3", "install mavis3.3", "install mavis4",
    "install mavis4.3", "mavis env update", "update mavis env", "mavis update", "update mavis",
    "security", "p-terminal security", "securitycheck", "info", "mavis info", "info mavis", "p-term info",
    "info p-term", "neofetch", "fastfetch", "screenfetch", "jupyter", "run jupyter", "run ju",
    "ninite", "just-install", "oneget", "boxstarter", "npackd", "zero-install", "appget",
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
    "run qwen2.5-coder:3b", "run qwen2.5-coder:7b", "run qwen2.5-coder:14b", "run qwen2.5-coder:32b", "run gemma3:1b",
    "run gemma3:4b",
    "run gemma3:12b", "run gemma3:27b", "run qwq", "run command-a", "run phi4-mini", "run granite3.2:8b",
    "run granite3.2:2b", "run granite3.2-vision:2b", "run qwen-2-5-omni:7b", "run qvq:72b", "run qwen-2-5-vl:32b",
    "run qwen-2-5-vl:72b", "run llama-4-maverick:17b", "run llama-4-scout:17b", "run deepcoder:1.5b",
    "run deepcoder:14b", "run mistral-small3.1", "help", "image generation", "video generation", "models",
    "models ls", "install 3d-slicer", "run 3d-slicer", "install simon", "run simon", "jupyter --version",
    "grafana --version", "3d-slicer --version", "pin-evil", "pin-main", "pin-cool", "pin-cool-3", "pin-cool-4",
    "p install", "p uninstall", "p upgrade", "p list", "p show", "p freeze", "p search", "install cool pin",
    "install cool pin-3", "install cool pin-4"
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
    "ubuntu neofetch", "ubuntu install git", "ubuntu install htop", "ubuntu ls", "ubuntu list files",
    "ubuntu install python", "ubuntu install pip", "ubuntu check system info", "ubuntu update system",
    "ubuntu install models", "ubuntu clear terminal", "ubuntu show processes", "ubuntu search files",
    "ubuntu create directory", "ubuntu remove directory", "ubuntu install wget", "ubuntu find text in files",
    "ubuntu compress files", "ubuntu extract files", "ubuntu setup firewall", "ubuntu restart network",
    "ubuntu check disk usage", "ubuntu monitor network traffic", "ubuntu install curl", "ubuntu install snap",
    "ubuntu install docker", "arch neofetch", "arch install git", "arch install htop", "arch list files",
    "arch install python", "arch install pip", "arch check system info", "arch update system", "arch install models",
    "arch clear terminal", "arch show processes", "arch search files", "arch create directory", "arch remove directory",
    "arch install wget", "arch find text in files", "arch compress files", "arch extract files", "arch setup firewall",
    "arch restart network", "arch check disk usage", "arch monitor network traffic", "arch install curl",
    "arch install snap",
    "arch install docker", "arch sudo pacman -S", "arch sudo pacman -R", "arch sudo pacman -Syu", "arch ls"
                                                                                                  "kali neofetch",
    "kali install git", "kali install htop", "kali list files", "kali install python",
    "kali install pip", "kali check system info", "kali update system", "kali install models", "kali clear terminal",
    "kali show processes", "kali search files", "kali create directory", "kali remove directory", "kali install wget",
    "kali find text in files", "kali compress files", "kali extract files", "kali setup firewall",
    "kali restart network",
    "kali check disk usage", "kali monitor network traffic", "kali install curl", "kali install snap",
    "kali install docker", "kali ls",
    "mint install docker", "mint install nmap", "mint install metasploit", "mint install wireshark",
    "mint install burpsuite", "mint install sqlmap", "mint install git", "mint install python3-pip",
    "mint install curl",
    "mint install vim", "mint install htop", "mint install gparted", "mint install vlc", "mint install thunderbird",
    "mint update", "mint upgrade", "mint autoremove", "mint clean", "mint ls", "mint cd /etc", "mint cd ~",
    "mint mkdir test", "mint mkdir -p ~/Projekte/python", "mint rm file.txt", "mint rm -rf testordner",
    "mint cp a.txt b.txt",
    "mint mv a.txt ~/Dokumente/", "mint touch neu.txt", "mint cat /etc/os-release", "mint nano ~/.bashrc",
    "mint sudo reboot",
    "mint sudo shutdown now", "mint ping 8.8.8.8", "mint ifconfig", "mint ip a", "mint netstat -tuln", "mint ss -tulpn",
    "mint systemctl status", "mint systemctl restart NetworkManager", "mint ps aux", "mint top", "mint whoami",
    "mint uname -a",
    "mint df -h", "mint free -m", "mint history", "mint clear", "mint echo 'Hallo Mint!'", "mint chmod +x script.sh",
    "mint chown user:user file.txt", "mint find / -name '*.conf'", "mint grep 'password' /etc/passwd",
    "mint wget https://example.com/datei.zip",
    "mint unzip datei.zip", "mint tar -xvf archiv.tar", "mint curl -I https://example.com", "debian install docker",
    "debian install nmap", "debian install metasploit", "debian install wireshark", "debian install burpsuite",
    "debian install sqlmap",
    "debian install git", "debian install python3-pip", "debian install curl", "debian install vim",
    "debian install htop",
    "debian install gparted", "debian install vlc", "debian install thunderbird", "debian update", "debian upgrade",
    "debian autoremove",
    "debian clean", "debian ls", "debian cd /etc", "debian cd ~", "debian mkdir test",
    "debian mkdir -p ~/Projekte/python",
    "debian rm file.txt", "debian rm -rf testordner", "debian cp a.txt b.txt", "debian mv a.txt ~/Dokumente/",
    "debian touch neu.txt",
    "debian cat /etc/os-release", "debian nano ~/.bashrc", "debian sudo reboot", "debian sudo shutdown now",
    "debian ping 8.8.8.8",
    "debian ifconfig", "debian ip a", "debian netstat -tuln", "debian ss -tulpn", "debian systemctl status",
    "debian systemctl restart NetworkManager",
    "debian ps aux", "debian top", "debian whoami", "debian uname -a", "debian df -h", "debian free -m",
    "debian history", "debian clear",
    "debian echo 'Hallo Debian!'", "debian chmod +x script.sh", "debian chown user:user file.txt",
    "debian find / -name '*.conf'",
    "debian grep 'password' /etc/passwd", "debian wget https://example.com/datei.zip", "debian unzip datei.zip",
    "debian tar -xvf archiv.tar", "debian curl -I https://example.com", "opensuse install docker",
    "opensuse install nmap",
    "opensuse install metasploit", "opensuse install wireshark", "opensuse install burpsuite",
    "opensuse install sqlmap", "opensuse install git",
    "opensuse install python3-pip", "opensuse install curl", "opensuse install vim", "opensuse install htop",
    "opensuse install gparted",
    "opensuse install vlc", "opensuse install thunderbird", "opensuse update", "opensuse upgrade",
    "opensuse autoremove",
    "opensuse clean", "opensuse ls", "opensuse cd /etc", "opensuse cd ~", "opensuse mkdir test",
    "opensuse mkdir -p ~/Projekte/python",
    "opensuse rm file.txt", "opensuse rm -rf testordner", "opensuse cp a.txt b.txt", "opensuse mv a.txt ~/Dokumente/",
    "opensuse touch neu.txt", "opensuse cat /etc/os-release", "opensuse nano ~/.bashrc", "opensuse sudo reboot",
    "opensuse sudo shutdown now",
    "opensuse ping 8.8.8.8", "opensuse ifconfig", "opensuse ip a", "opensuse netstat -tuln", "opensuse ss -tulpn",
    "opensuse systemctl status", "opensuse systemctl restart NetworkManager", "opensuse ps aux", "opensuse top",
    "opensuse whoami",
    "opensuse uname -a", "opensuse df -h", "opensuse free -m", "opensuse history", "opensuse clear",
    "opensuse echo 'Hallo openSUSE!'",
    "opensuse chmod +x script.sh", "opensuse chown user:user file.txt", "opensuse find / -name '*.conf'",
    "opensuse grep 'password' /etc/passwd",
    "opensuse wget https://example.com/datei.zip", "opensuse unzip datei.zip", "opensuse tar -xvf archiv.tar",
    "opensuse curl -I https://example.com",
    "fedora install docker", "fedora install nmap", "fedora install metasploit", "fedora install wireshark",
    "fedora install burpsuite",
    "fedora install sqlmap", "fedora install git", "fedora install python3-pip", "fedora install curl",
    "fedora install vim", "fedora install htop",
    "fedora install gparted", "fedora install vlc", "fedora install thunderbird", "fedora update", "fedora upgrade",
    "fedora autoremove", "fedora clean",
    "fedora ls", "fedora cd /etc", "fedora cd ~", "fedora mkdir test", "fedora mkdir -p ~/Projekte/python",
    "fedora rm file.txt",
    "fedora rm -rf testordner", "fedora cp a.txt b.txt", "fedora mv a.txt ~/Dokumente/", "fedora touch neu.txt",
    "fedora cat /etc/os-release",
    "fedora nano ~/.bashrc""fedora sudo reboot", "fedora sudo shutdown now", "fedora ping 8.8.8.8", "fedora ifconfig",
    "fedora ip a",
    "fedora netstat -tuln", "fedora ss -tulpn", "fedora systemctl status", "fedora systemctl restart NetworkManager",
    "fedora ps aux", "fedora top",
    "fedora whoami", "fedora uname -a", "fedora df -h", "fedora free -m", "fedora history", "fedora clear",
    "fedora echo 'Hallo Fedora!'",
    "fedora chmod +x script.sh", "fedora chown user:user file.txt", "fedora find / -name '*.conf'",
    "fedora grep 'password' /etc/passwd",
    "fedora wget https://example.com/datei.zip", "fedora unzip datei.zip", "fedora tar -xvf archiv.tar",
    "fedora curl -I https://example.com",
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
    "pip install -r requirements.txt", "pip check", "pip cache purge", "pip search fastapi",
    "pip install --upgrade pip",
    "pip install matplotlib", "pip install scikit-learn", "pip install beautifulsoup4", "pip install selenium",
    "pip install jupyter",
    "pip install pytest", "pip install ipython", "pip install virtualenv", "pip install wheel", "pip install pipenv",
    "pip download requests", "pip install --user numpy", "pip install --no-cache-dir flask", "pip show numpy",
    "pip uninstall -y pandas",
    "pip install -e .", "pip install git+https://github.com/psf/requests.git", "pip install 'requests<3.0'",
    "pip install torch", "pip install transformers",
    "pip config list", "pip config get global.index-url", "pip config set global.index-url https://pypi.org/simple",
    "pip install --pre pandas", "pip install fastapi[all]",
    "pip install openpyxl", "pip install pydantic", "pip install uvicorn", "pip install rich", "pip install tqdm",
    "python"
    "ollama run qwen3", "ollama run gemma3", "ollama run deepseek-r1", "ollama run llama3", "ollama run mistral:7b",
    "ollama run codellama:13b", "ollama run gemma:2b", "ollama run phi:1.5",
    "ollama pull llama3", "ollama pull mistral:7b", "ollama pull codellama:13b", "ollama pull gemma:2b",
    "ollama pull phi:1.5",
    "ollama list", "ollama show llama3", "ollama show mistral:7b", "ollama show codellama:13b", "ollama show gemma:2b",
    "ollama delete llama3", "ollama delete mistral:7b", "ollama delete codellama:13b", "ollama delete gemma:2b",
    "ollama delete phi:1.5",
    "ollama create mymodel -f Modelfile", "ollama push mymodel", "ollama run mymodel", "ollama run mymodel --verbose",
    "ollama run mymodel --mirostat 1",
    "ollama run llama3 --temperature 0.7", "ollama run llama3 --top-k 50", "ollama run llama3 --top-p 0.95",
    "ollama run llama3 --repeat-penalty 1.2", "ollama run llama3 --num-predict 100",
    "ollama run llama3 --prompt 'Erkläre Quantencomputing.'", "ollama run mistral:7b --format markdown",
    "ollama run codellama:13b --verbose", "ollama run gemma:2b --mirostat 1", "ollama run phi:1.5 --temperature 0.5",
    "ollama serve", "ollama version", "ollama help", "ollama help run", "ollama help create",
    "ollama list --format json", "ollama pull llama3:13b", "ollama run --system 'Du bist ein hilfreicher Assistent.'",
    "ollama run llama3 --verbose", "ollama run llama3 --mirostat 1"
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

            current_dir = Path.cwd().resolve()
            active_env_path = Path(find_active_env()).resolve()

            # Prüfe python.exe an typischen Stellen
            env_active = (
                # Windows-Pfade
                    (active_env_path / "Scripts/python.exe").exists() or
                    (active_env_path / "python.exe").exists() or
                    (active_env_path / "condabin/conda.bat").exists() or
                    (active_env_path / "conda.exe").exists() or

                    # (Unix/Linux-Pfade - eigetnlich unötig)
                    (active_env_path / "bin/python").exists() or
                    (active_env_path / "bin/python1.4").exists() or
                    (active_env_path / "bin/python1.5").exists() or
                    (active_env_path / "bin/python1.6").exists() or
                    (active_env_path / "bin/python2").exists() or
                    (active_env_path / "bin/python2.0").exists() or
                    (active_env_path / "bin/python2.1").exists() or
                    (active_env_path / "bin/python2.2").exists() or
                    (active_env_path / "bin/python2.3").exists() or
                    (active_env_path / "bin/python2.4").exists() or
                    (active_env_path / "bin/python2.5").exists() or
                    (active_env_path / "bin/python2.6").exists() or
                    (active_env_path / "bin/python2.7").exists() or
                    (active_env_path / "bin/python3").exists() or
                    (active_env_path / "bin/python3.0").exists() or
                    (active_env_path / "bin/python3.1").exists() or
                    (active_env_path / "bin/python3.2").exists() or
                    (active_env_path / "bin/python3.3").exists() or
                    (active_env_path / "bin/python3.4").exists() or
                    (active_env_path / "bin/python3.5").exists() or
                    (active_env_path / "bin/python3.6").exists() or
                    (active_env_path / "bin/python3.7").exists() or
                    (active_env_path / "bin/python3.8").exists() or
                    (active_env_path / "bin/python3.9").exists() or
                    (active_env_path / "bin/python3.10").exists() or
                    (active_env_path / "bin/python3.11").exists() or
                    (active_env_path / "bin/python3.12").exists() or
                    (active_env_path / "bin/python3.13").exists() or
                    (active_env_path / "bin/conda").exists()
            )

            try:
                if current_dir in active_env_path.parents or current_dir == active_env_path:
                    display_env_path_main = Path(".") / active_env_path.relative_to(current_dir)
                    display_env_path = ".\\" + str(display_env_path_main)
                else:
                    display_env_path = str(active_env_path)
            except Exception:
                display_env_path = str(active_env_path)

            env_indicator_main = (
                f"{display_env_path}"
                if env_active else
                f"{red}no venv{reset}"
            )

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

            env_indicator_10 = (
                f"{white}[{reset}{blue}{display_env_path}{reset}{white}]{reset}"
                if env_active else
                f"{red}no venv{reset}"
            )

            env_indicator_11 = (
                f"{white}[{reset}{red}{display_env_path}{reset}{white}]{reset}"
                if env_active else
                f"{red}no venv{reset}"
            )

            # PIN-Design je nach state
            if state == "main":
                setup_autocomplete()
                pin = get_main_pin(current_dir, env_indicator_10)
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

            elif state == "main-6":
                setup_autocomplete()
                pin = get_main_6_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)


            elif state == "main-7":
                setup_autocomplete()
                pin = get_main_7_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-8":
                setup_autocomplete()
                pin = get_main_8_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-9":
                setup_autocomplete()
                pin = get_main_9_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-10":
                setup_autocomplete()
                pin = get_main_10_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-11":
                setup_autocomplete()
                pin = get_main_11_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-12":
                setup_autocomplete()
                pin = get_main_12_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-13":
                setup_autocomplete()
                pin = get_main_13_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-14":
                setup_autocomplete()
                pin = get_main_14_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-15":
                setup_autocomplete()
                pin = get_main_15_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-16":
                setup_autocomplete()
                pin = get_main_16_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-17":
                setup_autocomplete()
                pin = get_main_17_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-18":
                setup_autocomplete()
                pin = get_main_18_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-19":
                setup_autocomplete()
                pin = get_main_19_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-20":
                setup_autocomplete()
                pin = get_main_20_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-21":
                setup_autocomplete()
                pin = get_main_21_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-22":
                setup_autocomplete()
                pin = get_main_22_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-23":
                setup_autocomplete()
                pin = get_main_23_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-24":
                setup_autocomplete()
                pin = get_main_24_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-25":
                setup_autocomplete()
                pin = get_main_25_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-26":
                setup_autocomplete()
                pin = get_main_26_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-27":
                setup_autocomplete()
                pin = get_main_27_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-28":
                setup_autocomplete()
                pin = get_main_28_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-29":
                setup_autocomplete()
                pin = get_main_29_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-30":
                setup_autocomplete()
                pin = get_main_30_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-31":
                setup_autocomplete()
                pin = get_main_31_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-32":
                setup_autocomplete()
                pin = get_main_32_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-33":
                setup_autocomplete()
                pin = get_main_33_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-34":
                setup_autocomplete()
                pin = get_main_34_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "main-35":
                setup_autocomplete()
                pin = get_main_35_pin(current_dir, env_indicator_main)
                print(pin, end='')
                user_input = input().strip()
                history.append(user_input)

            elif state == "evil":
                setup_autocomplete()
                pin = get_evil_pin(current_dir, env_indicator_11)
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

            elif state == "stable-4":
                setup_autocomplete()
                pin = get_stable_4_pin(current_dir, env_indicator_8)
                user_input = input(pin).strip()
                history.append(user_input)

            elif state == "stable-5":
                setup_autocomplete()
                pin = get_stable_5_pin(current_dir, env_indicator_8)
                user_input = input(pin).strip()
                history.append(user_input)

            elif state == "stable-6":
                setup_autocomplete()
                pin = get_stable_6_pin(current_dir, env_indicator_8)
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

            elif user_input.lower() == "pin main-1":
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

            elif user_input.lower() == "pin main-6":
                state = "main-6"
                continue

            elif user_input.lower() == "pin main-7":
                state = "main-7"
                continue

            elif user_input.lower() == "pin main-8":
                state = "main-8"
                continue

            elif user_input.lower() == "pin main-9":
                state = "main-9"
                continue

            elif user_input.lower() == "pin main-10":
                state = "main-10"
                continue

            elif user_input.lower() == "pin main-11":
                state = "main-11"
                continue

            elif user_input.lower() == "pin main-12":
                state = "main-12"
                continue

            elif user_input.lower() == "pin main-13":
                state = "main-13"
                continue

            elif user_input.lower() == "pin main-14":
                state = "main-14"
                continue

            elif user_input.lower() == "pin main-15":
                state = "main-15"
                continue

            elif user_input.lower() == "pin main-16":
                state = "main-16"
                continue

            elif user_input.lower() == "pin main-17":
                state = "main-17"
                continue

            elif user_input.lower() == "pin main-18":
                state = "main-18"
                continue

            elif user_input.lower() == "pin main-19":
                state = "main-19"
                continue

            elif user_input.lower() == "pin main-20":
                state = "main-20"
                continue

            elif user_input.lower() == "pin main-21":
                state = "main-21"
                continue

            elif user_input.lower() == "pin main-22":
                state = "main-22"
                continue

            elif user_input.lower() == "pin main-23":
                state = "main-23"
                continue

            elif user_input.lower() == "pin main-24":
                state = "main-24"
                continue

            elif user_input.lower() == "pin main-25":
                state = "main-25"
                continue

            elif user_input.lower() == "pin main-26":
                state = "main-26"
                continue

            elif user_input.lower() == "pin main-27":
                state = "main-27"
                continue

            elif user_input.lower() == "pin main-28":
                state = "main-28"
                continue

            elif user_input.lower() == "pin main-29":
                state = "main-29"
                continue

            elif user_input.lower() == "pin main-30":
                state = "main-30"
                continue

            elif user_input.lower() == "pin main-31":
                state = "main-31"
                continue

            elif user_input.lower() == "pin main-32":
                state = "main-32"
                continue

            elif user_input.lower() == "pin main-33":
                state = "main-33"
                continue

            elif user_input.lower() == "pin main-34":
                state = "main-34"
                continue

            elif user_input.lower() == "pin main-35":
                state = "main-35"
                continue

            elif user_input.lower() == "pin evil":
                state = "evil"
                continue

            elif user_input.lower() == "pin evil-1":
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

            elif user_input.lower() == "pin stable-1":
                state = "stable"
                continue

            elif user_input.lower() == "pin stable-2":
                state = "stable-2"
                continue

            elif user_input.lower() == "pin stable-3":
                state = "stable-3"
                continue

            elif user_input.lower() == "pin stable-4":
                state = "stable-4"
                continue

            elif user_input.lower() == "pin stable-5":
                state = "stable-5"
                continue

            elif user_input.lower() == "pin stable-6":
                state = "stable-6"
                continue

            elif user_input.lower() == "pin cool":
                state = "cool"
                continue

            elif user_input.lower() == "pin cool-1":
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

            elif user_input.startswith("pp-rm "):
                user_input_file = user_input[6:]
                user_input = f"Remove-Item -LiteralPath '{current_dir}\\{user_input_file}' -Recurse -Force"
                run_command_with_admin_python_privileges(user_input)

            elif user_input.startswith("pp-mkdir "):
                # Create new directory
                folder_name = user_input[9:].strip()
                folder_path = os.path.join(current_dir, folder_name)
                cmd = f"New-Item -ItemType Directory -Path '{folder_path}' -Force"
                run_command_with_admin_python_privileges(cmd)
                logging.info(f"[SUCCESS] Created folder: {folder_path}")

            elif user_input.startswith("pp-cp "):
                # Copy source to destination
                parts = user_input[6:].strip().split()
                if len(parts) < 2:
                    logging.info("[USAGE] pp-cp <source> <destination>")
                else:
                    source = os.path.join(current_dir, parts[0])
                    destination = os.path.join(current_dir, parts[1])
                    cmd = f"Copy-Item -Path '{source}' -Destination '{destination}' -Recurse -Force"
                    run_command_with_admin_python_privileges(cmd)
                    logging.info(f"[SUCCESS] Copied from '{source}' to '{destination}'")

            elif user_input.startswith("pp-mv "):
                # Move source to destination
                parts = user_input[6:].strip().split()
                if len(parts) < 2:
                    logging.info("[USAGE] pp-mv <source> <destination>")
                else:
                    source = os.path.join(current_dir, parts[0])
                    destination = os.path.join(current_dir, parts[1])
                    cmd = f"Move-Item -Path '{source}' -Destination '{destination}' -Force"
                    run_command_with_admin_python_privileges(cmd)
                    logging.info(f"[SUCCESS] Moved from '{source}' to '{destination}'")

            elif user_input.startswith("pp-touch "):
                # Create new empty file
                file_name = user_input[9:].strip()
                file_path = os.path.join(current_dir, file_name)
                cmd = f"New-Item -ItemType File -Path '{file_path}' -Force"
                run_command_with_admin_python_privileges(cmd)
                logging.info(f"[SUCCESS] Created file: {file_path}")

            elif user_input.startswith("pp-cat "):
                # Display content of file
                file_name = user_input[7:].strip()
                file_path = os.path.join(current_dir, file_name)
                if not os.path.isfile(file_path):
                    logging.info(f"[ERROR] File not found: {file_path}")
                else:
                    cmd = f"Get-Content -Path '{file_path}'"
                    run_command_with_admin_python_privileges(cmd)

            elif user_input.strip() == "pp-ls":
                # List directory contents
                cmd = f"Get-ChildItem -Path '{current_dir}'"
                run_command_with_admin_python_privileges(cmd)

            elif user_input.startswith("pp-open "):
                # Open file with default app
                file_name = user_input[8:].strip()
                file_path = os.path.join(current_dir, file_name)
                if not os.path.exists(file_path):
                    logging.info(f"[ERROR] File does not exist: {file_path}")
                else:
                    cmd = f"Start-Process '{file_path}'"
                    run_command_with_admin_python_privileges(cmd)
                    logging.info(f"[SUCCESS] Opened: {file_path}")

            elif user_input.startswith("pp-zip "):
                parts = user_input[7:].strip().split()
                if len(parts) < 2:
                    logging.info("[USAGE] pp-zip <source_folder> <zip_filename>")
                else:
                    source = os.path.join(current_dir, parts[0])
                    zipfile = os.path.join(current_dir, parts[1])
                    cmd = f"Compress-Archive -Path '{source}\\*' -DestinationPath '{zipfile}' -Force"
                    run_command_with_admin_python_privileges(cmd)
                    logging.info(f"[SUCCESS] Compressed '{source}' → '{zipfile}'")

            elif user_input.startswith("pp-unzip "):
                parts = user_input[9:].strip().split()
                if len(parts) < 2:
                    logging.info("[USAGE] pp-unzip <zip_file> <destination>")
                else:
                    zipfile = os.path.join(current_dir, parts[0])
                    destination = os.path.join(current_dir, parts[1])
                    cmd = f"Expand-Archive -Path '{zipfile}' -DestinationPath '{destination}' -Force"
                    run_command_with_admin_python_privileges(cmd)
                    logging.info(f"[SUCCESS] Extracted '{zipfile}' → '{destination}'")

            elif user_input.startswith("pp-search "):
                keyword = user_input[10:].strip()
                cmd = f"Select-String -Path '{current_dir}\\*' -Pattern '{keyword}' -CaseSensitive:$false -SimpleMatch"
                run_command_with_admin_python_privileges(cmd)

            elif user_input.strip() == "pp-netstat":
                cmd = "netstat -ano"
                run_command_with_admin_python_privileges(cmd)

            elif user_input.startswith("pp-ping "):
                host = user_input[8:].strip()
                cmd = f"Test-Connection -ComputerName '{host}' -Count 4"
                run_command_with_admin_python_privileges(cmd)

            elif user_input.strip() == "pp-ipconfig":
                cmd = "ipconfig /all"
                run_command_with_admin_python_privileges(cmd)

            elif user_input.strip() == "pp-users":
                cmd = "Get-LocalUser | Format-Table Name,Enabled,LastLogon"
                run_command_with_admin_python_privileges(cmd)

            elif user_input.strip() == "pp-services":
                cmd = "Get-Service | Where-Object {$_.Status -eq 'Running'} | Sort-Object Status,DisplayName"
                run_command_with_admin_python_privileges(cmd)

            elif user_input.startswith("pp-kill "):
                target = user_input[8:].strip()
                if target.isdigit():
                    cmd = f"Stop-Process -Id {target} -Force"
                else:
                    cmd = f"Stop-Process -Name '{target}' -Force"
                run_command_with_admin_python_privileges(cmd)
                logging.info(f"[SUCCESS] Process '{target}' terminated.")

            elif user_input.strip() == "pp-procs":
                cmd = "Get-Process | Sort-Object CPU -Descending | Select-Object -First 15 Name,Id,CPU,WorkingSet"
                run_command_with_admin_python_privileges(cmd)

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

            elif user_input.startswith("shell "):
                user_input = user_input[6:].strip()
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
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("lx-cpp "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("lx-cpp-c "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_cpp_c_command(user_input)

            elif user_input.startswith("lx-c "):
                user_input = user_input[5:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_c_command(user_input)

            elif user_input.startswith("lx-c-c "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_c_c_command(user_input)

            elif user_input.startswith("lx-p "):
                user_input = user_input[5:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_python_command(user_input)

            elif user_input.startswith("lx-p-c "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_p_c_command(user_input)

            elif user_input.startswith("linux "):
                user_input = user_input[6:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Linux: {user_input}")
                    run_linux_command(user_input)

            elif user_input.startswith("ubuntu "):
                user_input = user_input[7:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_command(user_input)

            elif user_input.startswith("ubuntu-c "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_c_command(user_input)

            elif user_input.startswith("ubuntu-p "):
                user_input = user_input[9:].strip()
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Ubuntu: {user_input}")
                    run_ubuntu_python_command(user_input)

            elif user_input.startswith("debian "):
                user_input = user_input[7:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Debian: {user_input}")
                    run_debian_command(user_input)

            elif user_input.startswith("debian-c "):
                user_input = user_input[9:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Debian: {user_input}")
                    run_debian_c_command(user_input)

            elif user_input.startswith("debian-p "):
                user_input = user_input[9:].strip()  # Remove the "debian " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Debian: {user_input}")
                    run_debian_python_command(user_input)

            elif user_input.startswith("kali "):
                user_input = user_input[5:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Kali: {user_input}")
                    run_kali_command(user_input)

            elif user_input.startswith("kali-c "):
                user_input = user_input[7:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Kali: {user_input}")
                    run_kali_c_command(user_input)

            elif user_input.startswith("kali-p "):
                user_input = user_input[7:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Kali: {user_input}")
                    run_kali_python_command(user_input)

            elif user_input.startswith("hack "):
                user_input = user_input[5:].strip()  # Remove the "kali " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Kali: {user_input}")
                    run_kali_command(user_input)

            elif user_input.startswith("arch "):
                user_input = user_input[5:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Arch: {user_input}")
                    run_arch_command(user_input)

            elif user_input.startswith("arch-c "):
                user_input = user_input[7:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Arch: {user_input}")
                    run_arch_c_command(user_input)

            elif user_input.startswith("arch-p "):
                user_input = user_input[7:].strip()  # Remove the "arch " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Arch: {user_input}")
                    run_arch_python_command(user_input)

            elif user_input.startswith("openSUSE "):
                user_input = user_input[9:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_opensuse_command(user_input)

            elif user_input.startswith("openSUSE-c "):
                user_input = user_input[11:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_opensuse_c_command(user_input)

            elif user_input.startswith("openSUSE-p "):
                user_input = user_input[11:].strip()  # Remove the "openSUSE " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_opensuse_python_command(user_input)

            elif user_input.startswith("mint "):
                user_input = user_input[5:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_mint_command(user_input)

            elif user_input.startswith("mint-c "):
                user_input = user_input[7:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_mint_c_command(user_input)

            elif user_input.startswith("mint-p "):
                user_input = user_input[7:].strip()  # Remove the "mint " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on openSUSE: {user_input}")
                    run_mint_python_command(user_input)

            elif user_input.startswith("fedora "):
                user_input = user_input[7:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Fedora: {user_input}")
                    run_fedora_command(user_input)

            elif user_input.startswith("fedora-c "):
                user_input = user_input[9:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Fedora: {user_input}")
                    run_fedora_c_command(user_input)

            elif user_input.startswith("fedora-p "):
                user_input = user_input[9:].strip()  # Remove the "fedora " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Fedora: {user_input}")
                    run_fedora_python_command(user_input)

            elif user_input.startswith("redhat "):
                user_input = user_input[7:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on RedHat: {user_input}")
                    run_redhat_command(user_input)

            elif user_input.startswith("redhat-c "):
                user_input = user_input[9:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on RedHat: {user_input}")
                    run_redhat_c_command(user_input)

            elif user_input.startswith("redhat-p "):
                user_input = user_input[9:].strip()  # Remove the "redhat " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on RedHat: {user_input}")
                    run_redhat_python_command(user_input)

            elif user_input.startswith("sles "):
                user_input = user_input[7:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on SLES: {user_input}")
                    run_sles_command(user_input)

            elif user_input.startswith("sles-c "):
                user_input = user_input[9:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on SLES: {user_input}")
                    run_sles_c_command(user_input)

            elif user_input.startswith("sles-p "):
                user_input = user_input[9:].strip()  # Remove the "sles " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on SLES: {user_input}")
                    run_sles_python_command(user_input)

            elif user_input.startswith("pengwin "):
                user_input = user_input[7:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Pengwin: {user_input}")
                    run_pengwin_command(user_input)

            elif user_input.startswith("pengwin-c "):
                user_input = user_input[9:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Pengwin: {user_input}")
                    run_pengwin_c_command(user_input)

            elif user_input.startswith("pengwin-p "):
                user_input = user_input[9:].strip()  # Remove the "pengwin " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Pengwin: {user_input}")
                    run_pengwin_python_command(user_input)

            elif user_input.startswith("oracle "):
                user_input = user_input[7:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Oracle: {user_input}")
                    run_oracle_command(user_input)

            elif user_input.startswith("oracle-c "):
                user_input = user_input[9:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Oracle: {user_input}")
                    run_oracle_c_command(user_input)

            elif user_input.startswith("oracle-p "):
                user_input = user_input[9:].strip()  # Remove the "oracle " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Oracle: {user_input}")
                    run_oracle_python_command(user_input)

            elif user_input.startswith("alpine "):
                user_input = user_input[7:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Alpine: {user_input}")
                    run_alpine_command(user_input)

            elif user_input.startswith("alpine-c "):
                user_input = user_input[9:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Alpine: {user_input}")
                    run_alpine_c_command(user_input)

            elif user_input.startswith("alpine-p "):
                user_input = user_input[9:].strip()  # Remove the "alpine " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Alpine: {user_input}")
                    run_alpine_python_command(user_input)

            elif user_input.startswith("clear "):
                user_input = user_input[7:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Clear: {user_input}")
                    run_clear_command(user_input)

            elif user_input.startswith("clear-c "):
                user_input = user_input[9:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
                else:
                    print(f"[{timestamp()}] [INFO] Executing the following command on Clear: {user_input}")
                    run_clear_c_command(user_input)

            elif user_input.startswith("clear-p "):
                user_input = user_input[9:].strip()  # Remove the "clear " prefix
                if not is_wsl_installed():
                    print(
                        f"[{timestamp()}] [ERROR] WSL is not installed or could not be found. Please install WSL to use this feature.")
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

            elif user_input.startswith("ninite "):
                user_input = user_input[7:].strip()
                print(
                    f"[{timestamp()}] [INFO] Ninite doesn't support individual CLI commands per app. Launching Ninite installer or providing guidance.")
                run_ninite_command(user_input)

            elif user_input.startswith("just-install "):
                user_input = user_input[13:].strip()
                print(f"[{timestamp()}] [INFO] Executing the following command with just-install: {user_input}")
                run_justinstall_command(user_input)

            elif user_input.startswith("oneget "):
                user_input = user_input[7:].strip()
                print(
                    f"[{timestamp()}] [INFO] Executing the following command with OneGet/PackageManagement: {user_input}")
                run_oneget_command(user_input)

            elif user_input.startswith("boxstarter "):
                user_input = user_input[11:].strip()
                print(f"[{timestamp()}] [INFO] Executing the following command with Boxstarter: {user_input}")
                run_boxstarter_command(user_input)

            elif user_input.startswith("npackd "):
                user_input = user_input[7:].strip()
                print(f"[{timestamp()}] [INFO] Executing the following command with Npackd: {user_input}")
                run_npackd_command(user_input)

            elif user_input.startswith("zero-install "):
                user_input = user_input[13:].strip()
                print(f"[{timestamp()}] [INFO] Executing the following command with Zero Install: {user_input}")
                run_zero_install_command(user_input)

            elif user_input.startswith("appget "):
                user_input = user_input[7:].strip()
                print(f"[{timestamp()}] [INFO] AppGet has been discontinued. You may want to use winget instead.")
                run_appget_command(user_input)

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