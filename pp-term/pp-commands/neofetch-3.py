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

# https://asciiart.club/

import sys
import getpass
import subprocess
import threading
import time
import importlib.util
import os
from datetime import datetime
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


required_packages = [
    "requests", "py-cpuinfo", "psutil"
]


def activate_virtualenv(venv_path):
    """Aktiviert eine bestehende virtuelle Umgebung."""
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path,
                                                                                                          "bin",
                                                                                                          "activate")

    if not os.path.exists(activate_script):
        print(f"[{timestamp()}] [ERROR] Virtual environment not found at {venv_path}.")
        sys.exit(1)

    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"[{timestamp()}] [PASS] Virtual environment {venv_path} activated.")


def ensure_packages_installed(packages):
    """Installiert fehlende Pakete effizient."""
    to_install = [pkg for pkg in packages if importlib.util.find_spec(pkg) is None]

    if to_install:
        print(f"[{timestamp()}] [INFO] Installing missing packages: {', '.join(to_install)}...")
        subprocess.run([sys.executable, "-m", "pip", "install"] + to_install, check=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        print(f"[{timestamp()}] [PASS] All missing packages installed.")
    else:
        print(f"[{timestamp()}] [INFO] All required packages are already installed.")


# Virtuelle Umgebung aktivieren und Pakete sicherstellen
venv_path = f"C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\.env"
activate_virtualenv(venv_path)
ensure_packages_installed(required_packages)

import os
import platform
import cpuinfo
import psutil
import shutil
import time
import socket
import pip
import subprocess
import winreg
import json
import re
from typing import Tuple

# -------------------- Farb- und Formatierungs-Codes --------------------
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


# -------------------- Hilfsfunktionen --------------------

def format_bytes(byte_value: int) -> float:
    """Bytes in GB umwandeln und auf 2 Nachkommastellen runden."""
    return round(byte_value / (1024 ** 3), 2)


def timestamp() -> str:
    """Gibt einen Zeitstempel im Format [YYYY-MM-DD HH:MM:SS] zurück."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# -------------------- Systeminformationen sammeln --------------------

def get_system_info() -> dict:
    """Sammelt umfangreiche Systeminformationen."""
    system_info = {}

    # Betriebssystem
    system_info['os_name'] = platform.system()
    system_info['os_version'] = platform.version()
    system_info['os_release'] = platform.release()
    system_info['os_arch'] = platform.architecture()[0]

    # CPU-Informationen
    cpu_info = cpuinfo.get_cpu_info()
    system_info['cpu_model'] = cpu_info.get("brand_raw", "N/A")
    system_info['cpu_arch'] = cpu_info.get("arch", "N/A")
    system_info['cpu_cores'] = psutil.cpu_count(logical=False)
    system_info['cpu_threads'] = psutil.cpu_count(logical=True)
    freq = psutil.cpu_freq()
    system_info['cpu_freq'] = round(freq.max, 2) if freq and freq.max else "N/A"

    # RAM
    ram = psutil.virtual_memory()
    system_info['ram_total'] = format_bytes(ram.total)
    system_info['ram_used'] = format_bytes(ram.used)
    system_info['ram_free'] = format_bytes(ram.available)
    system_info['ram_usage'] = ram.percent

    # Swap
    swap = psutil.swap_memory()
    system_info['swap_total'] = format_bytes(swap.total)
    system_info['swap_used'] = format_bytes(swap.used)
    system_info['swap_free'] = format_bytes(swap.free)

    # Festplattenplatz (Root-Laufwerk)
    total_storage, used_storage, free_storage = shutil.disk_usage("/")
    system_info['storage_total'] = format_bytes(total_storage)
    system_info['storage_used'] = format_bytes(used_storage)
    system_info['storage_free'] = format_bytes(free_storage)

    # Netzwerk
    system_info['hostname'] = socket.gethostname()
    try:
        system_info['ip_address'] = socket.gethostbyname(system_info['hostname'])
    except Exception:
        system_info['ip_address'] = "N/A"

    # Python und Pip
    system_info['python_version'] = platform.python_version()
    try:
        system_info['pip_version'] = subprocess.check_output(['pip', '--version'], text=True).split()[1]
    except Exception as e:
        system_info['pip_version'] = f"Error: {e}"

    # Netzwerk-Schnittstellen (MAC, IPv4, IPv6)
    network_interfaces = psutil.net_if_addrs()
    interfaces_info = {}
    for interface, addresses in network_interfaces.items():
        interface_details = {}
        for address in addresses:
            if address.family == socket.AF_INET:
                interface_details['IPv4'] = address.address
            elif address.family == socket.AF_INET6:
                interface_details['IPv6'] = address.address
            elif address.family == psutil.AF_LINK:
                interface_details['MAC'] = address.address
        interfaces_info[interface] = interface_details
    system_info['network_interfaces'] = interfaces_info

    # Load Average (unter Windows als CPU-Auslastung, ansonsten getloadavg)
    if system_info['os_name'] == "Windows":
        system_info['load_avg'] = f"CPU Usage: {psutil.cpu_percent(interval=1)}%"
    else:
        try:
            la1, la5, la15 = os.getloadavg()
            system_info['load_avg'] = {"1m": la1, "5m": la5, "15m": la15}
        except OSError:
            system_info['load_avg'] = "Not available"

    # Systemlaufzeit (Uptime)
    uptime_seconds = time.time() - psutil.boot_time()
    system_info['uptime'] = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

    # Aktive Benutzer
    users = psutil.users()
    system_info['user_info'] = []
    for u in users:
        system_info['user_info'].append({
            'user': u.name,
            'terminal': u.terminal or 'N/A',
            'started': time.ctime(u.started)
        })

    return system_info


# -------------------- Windows-spezifische Versions-Getter --------------------

def get_powershell_version():
    try:
        result = subprocess.run(
            ["powershell", "-Command", "$PSVersionTable.PSVersion.ToString()"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving PowerShell version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] PowerShell is not installed or not in the PATH."


def get_wsl_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        version = result.stdout.strip().split("\n")[0]
        return version
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving WSL version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installiert or not in the PATH."


def get_kernel_version():
    try:
        result = subprocess.run(
            ["wsl", "uname", "-r"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving kernel version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installiert or not in the PATH."


def get_wslg_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        lines = result.stdout.strip().split("\n")
        return lines[4] if len(lines) > 4 else "N/A"
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving WSLg version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installiert or not in the PATH."


def get_msrpc_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        lines = result.stdout.strip().split("\n")
        return lines[6] if len(lines) > 6 else "N/A"
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving MSRPC version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installiert or not in the PATH."


def get_direct3d_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        lines = result.stdout.strip().split("\n")
        return lines[8] if len(lines) > 8 else "N/A"
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving Direct3D version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installiert or not in the PATH."


def get_dxcore_version():
    try:
        result = subprocess.run(
            ["wsl", "--version"],
            capture_output=True, text=True, check=True
        )
        lines = result.stdout.strip().split("\n")
        return lines[10] if len(lines) > 10 else "N/A"
    except subprocess.CalledProcessError:
        return f"[{timestamp()}] [ERROR] Error retrieving DXCore version."
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] WSL is not installiert or not in the PATH."


def get_visual_studio_version():
    try:
        # Beispiel-Registry-Pfad für Visual Studio 2015:
        registry_path = r"SOFTWARE\Microsoft\VisualStudio\14.0\Setup\VisualStudio"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
            version, _ = winreg.QueryValueEx(key, "Version")
            return version
    except FileNotFoundError:
        return f"[{timestamp()}] [ERROR] Visual Studio not found"


def get_ollama_version():
    try:
        return subprocess.check_output(['ollama', '--version'], text=True).strip()
    except subprocess.CalledProcessError:
        # Versuche, Ollama zu starten und nochmal
        try:
            subprocess.check_output(['ollama', 'start'], text=True)
        except subprocess.CalledProcessError:
            return f"[{timestamp()}] [INFO] Warning: Could not start Ollama."
        try:
            return subprocess.check_output(['ollama', '--version'], text=True).strip()
        except subprocess.CalledProcessError:
            return f"[{timestamp()}] [INFO] Warning: Could not connect to a running Ollama instance."


# -------------------- BBCode → ANSI-ASCII-Art --------------------

def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def ansi_color(r: int, g: int, b: int) -> str:
    return f'\033[38;2;{r};{g};{b}m'


def parse_bbcode(text: str) -> str:
    """
    Wandelt BBCode-Farbangaben ([color=#RRGGBB]...[/color]) in ANSI-Farbcodes um.
    Gibt den kompletten ANSI-strukturierten String zurück.
    """
    output = ""
    color_stack = []
    pos = 0
    pattern = re.compile(r'\[color=#([0-9a-fA-F]{6})\]|\[/color\]')
    for match in pattern.finditer(text):
        start, end = match.span()
        output += text[pos:start]
        if match.group(0).startswith('[color='):
            r, g, b = hex_to_rgb(match.group(1))
            color_stack.append((r, g, b))
            output += ansi_color(r, g, b)
        else:
            # [/color]
            if color_stack:
                color_stack.pop()
            if color_stack:
                r, g, b = color_stack[-1]
                output += ansi_color(r, g, b)
            else:
                output += '\033[0m'
        pos = end
    output += text[pos:] + '\033[0m'
    return output


# -------------------- Farbpaletten-Anzeige --------------------

def show_color_palette_1() -> str:
    """Zeigt die ersten 8 ANSI-256 Farben (Hintergrund) ohne Zahlen."""
    palette = ""
    for i in range(8):
        palette += f"\033[48;5;{i}m  \033[0m"
    return palette


def show_color_palette_3() -> str:
    """Zeigt die Farben 8–15 der ANSI-256 Palette (Hintergrund)."""
    palette = ""
    for i in range(8, 16):
        palette += f"\033[48;5;{i}m  \033[0m"
    return palette


# -------------------- Versionsdatei laden --------------------

def load_versions_json():
    """Lädt die Versionsinformationen aus der JSON-Datei"""
    # Rohstring, damit \ als normaler Backslash gelesen wird
    json_path = rf'C:\Users\{os.getlogin()}\p-terminal\pp-term\pp-term-versions.json'
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[{timestamp()}] [INFO] Versionsdatei nicht gefunden unter {json_path}")
    except json.JSONDecodeError:
        print(f"[{timestamp()}] [INFO] JSON-Formatfehler in {json_path}")
    return {}


# -------------------- ASCII-Art-Block (BBCode) --------------------

bbcode_text = """
[color=#808080] [/color]
[color=#808080] [/color]
[color=#808080]               [/color][color=#767d75],[/color][color=#737c73],,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,[/color]
[color=#808080]          [/color][color=#677966]╓[/color][color=#487047]▄[/color][color=#316a30]▓[/color][color=#236621]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#2a6828]▓[/color][color=#3e6e3d]▓[/color][color=#5a7559]╖[/color]
[color=#808080]        g[/color][color=#296827]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#457044]▄[/color]
[color=#808080]       [/color][color=#3b6d39]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#286826]▓[/color]
[color=#808080]      [/color][color=#50734f]▐[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#346233]▓[/color][color=#456144]▀[/color][color=#3a6139]▀[/color][color=#266225]▓[/color][color=#1e631c]▓[/color][color=#1e631c]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#336b32]▓[/color]
[color=#808080]      ▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#2f622e]▓[/color][color=#426041]▀[/color][color=#555f54]▒[/color][color=#5e5e5e]▒[/color][color=#5f5f5f]▒▒▒▒[/color][color=#575f57]▒[/color][color=#436043]▀[/color][color=#2e612d]▓[/color][color=#1f621d]▓[/color][color=#1d621c]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#2c622a]▓[/color][color=#3e613d]▀[/color][color=#515f51]▒[/color][color=#5d5e5d]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#4d5f4c]▒[/color][color=#386037]▀[/color][color=#246123]▓[/color][color=#1d611b]▓[/color][color=#1d621c]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#346133]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#565e56]▒[/color][color=#415f41]▀[/color][color=#2c602b]▓[/color][color=#1e611c]▓[/color][color=#1d621c]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#346033]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#4c5f4b]▒[/color][color=#365f36]▀[/color][color=#236022]▓[/color][color=#1c611b]▓[/color][color=#1d621c]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#336032]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒[/color][color=#535a53]▒[/color][color=#3d543d]▄[/color][color=#475747]▄[/color][color=#5b5d5b]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#555f55]▒[/color][color=#405f40]▀[/color][color=#2b602a]▓[/color][color=#1d611c]▓[/color][color=#1d621c]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#335f32]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒[/color][color=#595c58]▒[/color][color=#445744]▄[/color][color=#2d522d]▓[/color][color=#174d19]█[/color][color=#104c11]▓[/color][color=#104c11]▓▓█[/color][color=#234f24]█[/color][color=#3c553d]▄[/color][color=#555b55]▒[/color][color=#5e5e5e]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#4a5f4a]▒[/color][color=#356035]▓[/color][color=#226121]▓[/color][color=#1d621c]▓[/color][color=#1e631c]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#336032]▌[/color][color=#5c5d5c]▒[/color][color=#4d5c4d]▒[/color][color=#375a37]▓[/color][color=#215622]▓[/color][color=#145416]▓[/color][color=#135214]▓▓▓▓▓[/color][color=#1f5320]▓█▓▓▓[/color][color=#194d1a]█[/color][color=#315232]▓[/color][color=#4a584b]▄[/color][color=#5d5e5d]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#545f54]▒[/color][color=#40603f]▀[/color][color=#2b622a]▓[/color][color=#1e631d]▓[/color][color=#1e641d]▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#1a5e19]▓[/color][color=#175c19]▓▓[/color][color=#155817]▓▓▓[/color][color=#305831]▀[/color][color=#465b47]▒[/color][color=#5a5e5a]▒[/color][color=#5f5e5f]▒▒[/color][color=#4b5b4b]▒[/color][color=#315531]▀[/color][color=#185019]█[/color][color=#114e13]▓[/color][color=#114d12]▓▓█[/color][color=#264f27]▓[/color][color=#405540]▄[/color][color=#575c57]▒[/color][color=#5e5e5e]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#20621f]▓[/color][color=#1e631d]▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#1b601a]▓[/color][color=#1a5e1a]▓▓[/color][color=#2b5b2b]▓[/color][color=#405c40]▀[/color][color=#555d55]▒[/color][color=#5e5e5e]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#505b50]▒[/color][color=#365637]▀[/color][color=#1d511e]▓[/color][color=#124f13]▓[/color][color=#114f13]▓▓█[/color][color=#1c4c1d]█[/color][color=#345235]▓[/color][color=#4d584e]▄[/color][color=#5d5e5d]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒[/color][color=#21621f]▓[/color][color=#1e631c]▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#3b5f3a]▀[/color][color=#4f5e4f]▒[/color][color=#5d5e5d]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#455a46]▒[/color][color=#1a521b]▓[/color][color=#125114]▓[/color][color=#114f13]▓▓[/color][color=#0f4a11]█[/color][color=#0e480f]█[/color][color=#18481a]█[/color][color=#445444]Ñ[/color][color=#5e5e5e]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#216120]▓[/color][color=#1e631c]▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#3a5f39]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#575c57]▒[/color][color=#405741]▄[/color][color=#285329]▓[/color][color=#155016]█[/color][color=#125013]▓▓▓█[/color][color=#285129]▓[/color][color=#3e563e]▀[/color][color=#545b54]▒[/color][color=#5e5e5e]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒[/color][color=#226120]▓[/color][color=#1e631c]▓▓▓▓▓▓▓▓▓▓▓▓▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#385f37]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒[/color][color=#495949]▄[/color][color=#315332]▓[/color][color=#1a4e1c]█[/color][color=#114d12]▓[/color][color=#114e12]▓▓█[/color][color=#245126]▓[/color][color=#3b563b]▀[/color][color=#515b51]░[/color][color=#5e5e5e]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#236222]▓[/color][color=#1e631c]▓[/color][color=#1e641d]▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#365f36]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#274e28]▓[/color][color=#114b13]█[/color][color=#104d12]▓▓█[/color][color=#215022]▓[/color][color=#375538]▀[/color][color=#4e5a4e]░[/color][color=#5d5e5d]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#545f54]▒[/color][color=#405f40]▄[/color][color=#2d612c]▓[/color][color=#1e631d]▓[/color][color=#1e641d]▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#355e35]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#184c19]▓[/color][color=#104d12]▓[/color][color=#114e13]▓[/color][color=#1a501a]▓[/color][color=#5c5e5c]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#455e44]▄[/color][color=#315f30]▓[/color][color=#20601f]▓[/color][color=#1c611b]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#345f33]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#174d19]▓[/color][color=#114e12]▓[/color][color=#124f13]▓[/color][color=#1b511c]▓[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#4a5e4a]▄[/color][color=#365e36]▓[/color][color=#235e22]▓[/color][color=#1b601a]▓[/color][color=#1c611b]▓▓▓▓▓▓▓▓▓[/color][color=#1f651d]▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#325f32]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#174e19]▓[/color][color=#114f13]▓[/color][color=#135114]▓[/color][color=#1c531d]▓[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#505e50]▒[/color][color=#3b5e3b]▓[/color][color=#285e27]▓[/color][color=#1b5f1b]▓[/color][color=#1b601a]▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#1f651e]▓[/color][color=#1f651e]▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#315f30]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#174f18]▓[/color][color=#125214]▓▓[/color][color=#1d571f]▓[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒[/color][color=#555e55]▒[/color][color=#415e41]▄[/color][color=#2d5e2d]▓[/color][color=#1d5e1c]▓[/color][color=#1b601a]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#305f2f]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#185119]▓[/color][color=#135515]▓▓[/color][color=#1f5a20]▓[/color][color=#5f5e5f]▒[/color][color=#5a5e59]▒[/color][color=#475e47]▄[/color][color=#335f33]▓[/color][color=#215f20]▓[/color][color=#1b601a]▓[/color][color=#1c601b]▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#1f651d]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#2f602e]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#19551a]▓[/color][color=#155817]▓▓[/color][color=#1b5d1b]▓[/color][color=#255f24]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#1f651e]▓[/color][color=#1f651e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#2e602d]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒▒[/color][color=#4b5b4b]▒[/color][color=#365a36]▀[/color][color=#215d21]▓[/color][color=#1b601a]▓[/color][color=#1c611b]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#1f651e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#2d612c]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒▒▒▒▒[/color][color=#525f52]▒[/color][color=#3f5f3f]▓[/color][color=#2c602b]▓[/color][color=#1e611d]▓[/color][color=#1d621c]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#356b33]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#2d622b]▌[/color][color=#5f5f5f]▒[/color][color=#5f5f5f]▒▒▒[/color][color=#565f56]▒[/color][color=#436043]▄[/color][color=#30602f]▓[/color][color=#20611f]▓[/color][color=#1d621c]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#256723]▓[/color]
[color=#808080]      [/color][color=#3b6d39]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#2c632a]▓[/color][color=#595f59]▒[/color][color=#486047]▄[/color][color=#356234]▓[/color][color=#246322]▓[/color][color=#1e641d]▓[/color][color=#1e641d]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#286826]▓[/color]
[color=#808080]      [/color][color=#687968]└[/color][color=#21661f]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#547453]╝[/color]
[color=#808080]       [/color][color=#647864]╙[/color][color=#276825]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#557454]╜[/color]
[color=#808080]         ╙[/color][color=#306a2e]▓[/color][color=#20661e]▓[/color][color=#20661e]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#2b6929]▓[/color][color=#4e724d]╜[/color]
[color=#808080]             [/color][color=#547453]╙[/color][color=#4a7149]▀[/color][color=#446f43]▀[/color][color=#436f41]▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀[/color][color=#497147]▀[/color][color=#527351]╙[/color][color=#627761]'[/color]
[color=#808080] [/color]
[color=#808080] [/color]
"""

ascii_art = parse_bbcode(bbcode_text)


# -------------------- ASCII- und Info-Zeilen nebeneinander ausgeben --------------------

def gather_info_lines(sys_info: dict, versions: dict) -> list:
    """
    Baut eine Liste von Strings auf, die alle Versions- und Systeminfos enthält.
    Farbige Überschriften (z.B. blau) werden hier eingefügt.
    """
    blue = "\033[34m"
    reset = "\033[0m"
    lines = []

    # Versionen aus der JSON-Datei (mit Fallback "Unbekannt")
    p_terminal_ver = versions.get("P-Terminal Version", "Unbekannt")
    pp_terminal_ver = versions.get("PP-Terminal Version", "Unbekannt")
    launcher_ver = versions.get("PP-Terminal Launcher Version", "Unbekannt")
    p_compiler_ver = versions.get("Peharge Compiler Version", "Unbekannt")
    p_iq_cernel_ver = versions.get("Peharge IQ Kernel Version", "Unbekannt")
    license_info = versions.get("P-Terminal License", "Unbekannt")

    title = f"PP-Terminal - {os.getlogin()}"
    line = "-" * len(title)

    # Zeilen hinzufügen
    lines.append("")
    lines.append("")
    lines.append(f"                                 {title}")
    lines.append(f"               {line}")
    lines.append(f"          {blue}P-Terminal Version{reset}: {p_terminal_ver}")
    lines.append(f"        {blue}PP-Terminal Version{reset}: {pp_terminal_ver}")
    lines.append(f"       {blue}PP-Terminal Launcher Version{reset}: {launcher_ver}")
    lines.append(f"      {blue}Peharge Compiler Version{reset}: {p_compiler_ver}")
    lines.append(f"      {blue}Peharge IQ Kernel Version{reset}: {p_iq_cernel_ver}")
    lines.append(f"      {blue}P-Terminal License{reset}: {license_info}")
    lines.append(f"      {blue}MAVIS Version{reset}: 4.3")
    lines.append(f"      {blue}MAVIS Launcher Version{reset}: 4")
    lines.append(f"      {blue}MAVIS Terminal Version{reset}: 5")
    lines.append(f"      {blue}MAVIS License{reset}: MIT")

    # Betriebssystem
    lines.append(f"      {blue}OS{reset}: {sys_info['os_name']} {sys_info['os_release']}")
    lines.append(f"      {blue}Version{reset}: {sys_info['os_version']}")
    lines.append(f"      {blue}Architecture{reset}: {sys_info['os_arch']}")
    # lines.append(f"      {blue}Hostname{reset}: {sys_info['hostname']}")
    lines.append(f"      {blue}IP Address{reset}: {sys_info['ip_address']}")

    # CPU
    lines.append(f"      {blue}CPU{reset}: {sys_info['cpu_model']}")
    # lines.append(f"      {blue}Architektur{reset}: {sys_info['cpu_arch']}")
    # lines.append(f"      {blue}Cores{reset}: {sys_info['cpu_cores']} (logical: {sys_info['cpu_threads']})")
    # lines.append(f"      {blue}Max Frequency{reset}: {sys_info['cpu_freq']} MHz")

    # RAM / Swap
    # lines.append(f"      {blue}RAM{reset}: {sys_info['ram_total']} GB")
    # lines.append(f"      {blue}RAM Total{reset}: {sys_info['ram_total']} GB")
    # lines.append(f"      {blue}RAM Used{reset}: {sys_info['ram_used']} GB ({sys_info['ram_usage']}%)")
    # lines.append(f"      {blue}RAM Free{reset}: {sys_info['ram_free']} GB")
    lines.append(f"      {blue}Swap{reset}: {sys_info['swap_total']} GB")
    # lines.append(f"      {blue}Swap Total{reset}: {sys_info['swap_total']} GB")
    # lines.append(f"      {blue}Swap Used{reset}: {sys_info['swap_used']} GB")
    # lines.append(f"      {blue}Swap Free{reset}: {sys_info['swap_free']} GB")

    # Storage
    lines.append(f"      {blue}Storage{reset}: {sys_info['storage_total']} GB")
    # lines.append(f"      {blue}Storage Total{reset}: {sys_info['storage_total']} GB")
    # lines.append(f"      {blue}Storage Used{reset}: {sys_info['storage_used']} GB")
    # lines.append(f"      {blue}Storage Free{reset}: {sys_info['storage_free']} GB")

    # Load Average oder CPU-Auslastung
    """
    if isinstance(sys_info['load_avg'], dict):
        la = sys_info['load_avg']
        lines.append(f"      {blue}Load Average{reset}: 1m={la['1m']}, 5m={la['5m']}, 15m={la['15m']}")
    else:
        lines.append(f"      {blue}Load Average{reset}: {sys_info['load_avg']}")

    # Uptime
    lines.append(f"      {blue}Uptime{reset}: {sys_info['uptime']}")
    """

    """
    # Netzwerkschnittstellen (nur IPv4 und MAC)
    for iface, details in sys_info['network_interfaces'].items():
        ipv4 = details.get('IPv4', 'N/A')
        mac  = details.get('MAC', 'N/A')
        lines.append(f"      {blue}Interface {iface}{reset}: IPv4={ipv4}, MAC={mac}")

    """

    # Benutzer
    for user in sys_info['user_info']:
        lines.append(
            f"      {blue}User{reset}: {user['user']} (terminal: {user['terminal']}, started: {user['started']})")

    # Python/Pip/Git
    lines.append(f"      {blue}Python Version{reset}: {sys_info['python_version']}")
    lines.append(f"      {blue}PIP Version{reset}: {sys_info['pip_version']}")
    try:
        git_ver = subprocess.check_output(['git', '--version'], text=True).strip()
    except Exception:
        git_ver = "unbekannt"
    lines.append(f"      {blue}Git Version{reset}: {git_ver}")

    # Windows-spezifische Utilities
    lines.append(f"      {blue}PowerShell Version{reset}: {get_powershell_version()}")
    lines.append(f"      {blue}WSL Version{reset}: {get_wsl_version()}")
    lines.append(f"      {blue}Kernelversion{reset}: {get_kernel_version()}")
    lines.append(f"      {blue}WSLg Version{reset}: {get_wslg_version()}")
    lines.append(f"      {blue}MSRDC Version{reset}: {get_msrpc_version()}")
    lines.append(f"      {blue}Direct3D Version{reset}: {get_direct3d_version()}")
    lines.append(f"      {blue}DXCore Version{reset}: {get_dxcore_version()}")
    lines.append(f"       {blue}Ollama Version{reset}: {get_ollama_version()}")
    lines.append(f"         {blue}Visual Studio Version{reset}: {get_visual_studio_version()}")

    # Rust
    try:
        rust_ver = subprocess.check_output(['rustc', '--version'], text=True).strip()
    except Exception:
        rust_ver = "unbekannt"
    lines.append(f"            {blue}Rust Version{reset}: {rust_ver}")

    # Farbpaletten
    lines.append("")
    lines.append("                                 " + show_color_palette_1())
    lines.append("              " + show_color_palette_3())
    lines.append("")
    lines.append("")
    lines.append("")

    return lines


def print_side_by_side(ascii_str: str, info_lines: list, ascii_width: int = 60):
    """
    Gibt die ANSI-ASCII-Art (ascii_str) links und die Liste info_lines rechts nebeneinander aus.
    ascii_width legt die Breite der linken Spalte fest (inkl. ANSI-Codes).
    """
    ascii_lines = ascii_str.splitlines()
    max_lines = max(len(ascii_lines), len(info_lines))

    for i in range(max_lines):
        left = ascii_lines[i] if i < len(ascii_lines) else ""
        right = info_lines[i] if i < len(info_lines) else ""
        print(f"{left.ljust(ascii_width)}  {right}")


# -------------------- Hauptprogramm --------------------

if __name__ == "__main__":
    print("\n")
    # 1) Systeminformationen ermitteln
    sys_info = get_system_info()

    # 2) Versions-JSON laden und zusammenführen
    versions = load_versions_json()
    # Wenn die JSON bereits Schlüssel wie "P-Terminal Version" enthält, werden diese übernommen.
    # Außerdem können weitere Keys aus sys_info oder anderen Quellen hinzugefügt werden.
    sys_info.update(versions)

    # 3) ASCII-Art vorbereiten (BBCode → ANSI)
    #    (Bereits oben über die Variable ascii_art geschehen)

    # 4) Info-Zeilen erstellen
    info_lines = gather_info_lines(sys_info, versions)

    # 5) Nebeneinander ausgeben (links ASCII, rechts Infos)
    #    Passe ascii_width nach Bedarf an (z.B. 60–80), damit nichts überlappt.
    print_side_by_side(ascii_art, info_lines, ascii_width=70)
    print("\n")
