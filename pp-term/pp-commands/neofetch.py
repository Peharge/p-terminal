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
import json

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
import subprocess
import winreg
import re
from typing import Tuple

# Farb- und Formatierungs-Codes
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

def state_info():
    with open(f"C:/Users/{getpass.getuser()}/p-terminal/pp-term/state-info.json", "r") as file:
        data = json.load(file)
    return data["state"]

if "adv" in state_info():
    main_color = "\033[92m"
elif "evil" in state_info():
    main_color = "\033[91m"
else:
    main_color = "\033[94m"

def format_bytes(byte_value: int) -> float:
    """Bytes in GB umwandeln und auf 2 Nachkommastellen runden."""
    return round(byte_value / (1024 ** 3), 2)

def timestamp() -> str:
    """Gibt einen Zeitstempel im Format [YYYY-MM-DD HH:MM:SS] zurück."""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# Allgemeiner Helfer für Version-Abfragen
def safe_version(callable_fn, default: str = "unknown") -> str:
    try:
        result = callable_fn()
        return result.strip() if isinstance(result, str) else result
    except Exception:
        return default

# Systeminformationen sammeln
def get_system_info() -> dict:
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
        pip_out = subprocess.check_output(['pip', '--version'], text=True)
        system_info['pip_version'] = pip_out.split()[1]
    except Exception:
        system_info['pip_version'] = "unknown"
    # Netzwerk-Schnittstellen
    network_interfaces = psutil.net_if_addrs()
    interfaces_info = {}
    for iface, addrs in network_interfaces.items():
        details = {}
        for addr in addrs:
            if addr.family == socket.AF_INET:
                details['IPv4'] = addr.address
            elif addr.family == socket.AF_INET6:
                details['IPv6'] = addr.address
            elif addr.family == psutil.AF_LINK:
                details['MAC'] = addr.address
        interfaces_info[iface] = details
    system_info['network_interfaces'] = interfaces_info
    # Load Average / CPU-Auslastung
    if system_info['os_name'] == "Windows":
        system_info['load_avg'] = f"CPU Usage: {psutil.cpu_percent(interval=1)}%"
    else:
        try:
            la1, la5, la15 = os.getloadavg()
            system_info['load_avg'] = {"1m": la1, "5m": la5, "15m": la15}
        except OSError:
            system_info['load_avg'] = "Not available"
    # Uptime
    uptime_seconds = time.time() - psutil.boot_time()
    system_info['uptime'] = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    # Aktive Benutzer
    users = psutil.users()
    system_info['user_info'] = [
        {'user': u.name, 'terminal': u.terminal or 'N/A', 'started': time.ctime(u.started)}
        for u in users
    ]
    return system_info

# Versions-Getter

def get_powershell_version() -> str:
    return safe_version(lambda: subprocess.check_output(
        ["powershell", "-Command", "$PSVersionTable.PSVersion.ToString()"], text=True, check=True
    ), default="0")

def get_wsl_version() -> str:
    return safe_version(lambda: subprocess.check_output([
        "wsl", "--version"], text=True, check=True
    ).splitlines()[0], default="0")

def get_kernel_version() -> str:
    return safe_version(lambda: subprocess.check_output(
        ["wsl", "uname", "-r"], text=True, check=True
    ), default="0")

def get_wslg_version() -> str:
    return safe_version(lambda: subprocess.check_output([
        "wsl", "--version"], text=True, check=True
    ).splitlines()[4] if len(subprocess.check_output(["wsl", "--version"], text=True).splitlines())>4 else "unknown", default="unknown")

def get_msrpc_version() -> str:
    return safe_version(lambda: subprocess.check_output([
        "wsl", "--version"], text=True, check=True
    ).splitlines()[6] if len(subprocess.check_output(["wsl", "--version"], text=True).splitlines())>6 else "unknown", default="unknown")

def get_direct3d_version() -> str:
    return safe_version(lambda: subprocess.check_output([
        "wsl", "--version"], text=True, check=True
    ).splitlines()[8] if len(subprocess.check_output(["wsl", "--version"], text=True).splitlines())>8 else "unknown", default="unknown")

def get_dxcore_version() -> str:
    return safe_version(lambda: subprocess.check_output([
        "wsl", "--version"], text=True, check=True
    ).splitlines()[10] if len(subprocess.check_output(["wsl", "--version"], text=True).splitlines())>10 else "unknown", default="unknown")

def get_visual_studio_version() -> str:
    def _vs():
        registry_path = r"SOFTWARE\Microsoft\VisualStudio\14.0\Setup\VisualStudio"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
            version, _ = winreg.QueryValueEx(key, "Version")
            return version
    return safe_version(_vs, default="0")

def get_ollama_version() -> str:
    def _ollama():
        return subprocess.check_output(["ollama", "--version"], text=True, check=True)
    ver = safe_version(_ollama, default="0")
    if ver == "0":
        try:
            subprocess.check_output(['ollama', 'start'], text=True, check=True)
            ver2 = safe_version(_ollama, default="0")
            return ver2
        except Exception:
            return "0"
    return ver

# BBCode → ANSI-ASCII-Art

def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def ansi_color(r: int, g: int, b: int) -> str:
    return f'\033[38;2;{r};{g};{b}m'

def parse_bbcode(text: str) -> str:
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

# Farbpaletten-Anzeige

def show_color_palette_1() -> str:
    return ''.join(f"\033[48;5;{i}m  \033[0m" for i in range(8))

def show_color_palette_3() -> str:
    return ''.join(f"\033[48;5;{i}m  \033[0m" for i in range(8,16))

# Versionsdatei laden
def load_versions_json() -> dict:
    json_path = rf'C:\Users\{os.getlogin()}\p-terminal\pp-term\pp-term-versions.json'
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except Exception:
        return {}


# ASCII-Art-Block (BBCode)

bbcode_text = """
[color=#808080]       [/color][color=#717171],[/color][color=#626262]╓[/color][color=#565656]▄[/color][color=#4f4f4f]▄[/color][color=#494949]▄[/color][color=#494949]▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄[/color][color=#464646]▄[/color][color=#454545]▄▄▄▄▄▄[/color][color=#424342]▄[/color][color=#424242]▄▄▄▄▄▄[/color][color=#3f3f3f]▄[/color][color=#3e3e3e]▄▄▄▄▄▄▄▄▄[/color][color=#4b4b4b]▄[/color][color=#595959]▄[/color][color=#6c6c6c],[/color]
[color=#808080]    [/color][color=#666666]╓[/color][color=#464646]▓[/color][color=#313131]▓[/color][color=#303130]▓▓▓▓▓▓▓▓[/color][color=#353535]▓[/color][color=#353535]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#313131]▓[/color][color=#313131]▓▓▓▓▓[/color][color=#2d2d2d]▓[/color][color=#2c2d2d]▓▓▓▓[/color][color=#2a2a2a]▓[/color][color=#292929]▓▓▓▓[/color][color=#262626]▓[/color][color=#252525]▓███[/color][color=#222222]█[/color][color=#222222]█████[/color][color=#1f1f1f]█[/color][color=#1e1e1e]████[/color][color=#373737]█[/color][color=#5f5f5f],[/color]
[color=#808080]  [/color][color=#686868]╓[/color][color=#363636]█[/color][color=#2f2f2f]▓[/color][color=#303030]▓▓▓▓[/color][color=#333333]▓▓[/color][color=#343434]▓▓▓▓▓[/color][color=#363636]▓▓▓▓[/color][color=#373737]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#323232]▓[/color][color=#313131]▓▓▓▓▓[/color][color=#2e2e2e]▓[/color][color=#2d2d2d]▓▓▓▓[/color][color=#2a2a2a]▓[/color][color=#292929]▓▓▓▓[/color][color=#262626]▓[/color][color=#262626]▓███[/color][color=#232323]█[/color][color=#222222]█████[/color][color=#1f1f1f]█[/color][color=#1e1e1e]█████[/color][color=#1b1b1b]█[/color][color=#252525]█[/color][color=#656565],[/color]
[color=#808080] [/color][color=#575757]▄[/color][color=#2e2e2e]▓[/color][color=#2f2f2f]▓▓▓▓[/color][color=#323232]▓[/color][color=#323332]▓▓▓▓▓[/color][color=#353535]▓▓[/color][color=#363636]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[/color][color=#313131]▓[/color][color=#313131]▓▓▓▓[/color][color=#2e2e2e]▓[/color][color=#2d2d2d]▓▓▓▓[/color][color=#2a2a2a]▓[/color][color=#292929]▓▓▓▓[/color][color=#262626]▓[/color][color=#252525]▓███[/color][color=#222222]█[/color][color=#222222]█████[/color][color=#1f1f1f]█[/color][color=#1e1e1e]█████[/color][color=#1b1b1b]██[/color][color=#555555]▄[/color]
[color=#707070] [/color][color=#2e2e2e]▓[/color][color=#2f2f2f]▓▓▓▓[/color][color=#323232]▓[/color][color=#323232]▓▓▓▓▓[/color][color=#353535]▓[/color][color=#363636]▓▓▓▓▓▓▓▓▓[/color][color=#393939]▓▓▓▓▓▓▓▓▓[/color][color=#3f3f3f]▓[/color][color=#494949]▀▓[/color][color=#373737]▓[/color][color=#373737]▓▓▓▓▓▓[/color][color=#343434]▓[/color][color=#333333]▓▓▓▓[/color][color=#303030]▓[/color][color=#303030]▓▓▓▓[/color][color=#2d2d2d]▓[/color][color=#2c2c2c]▓▓▓▓[/color][color=#292929]▓[/color][color=#282828]▓▓▓▓[/color][color=#252525]█[/color][color=#242424]████[/color][color=#212121]█[/color][color=#212121]█████[/color][color=#1d1e1d]█[/color][color=#1d1d1d]██████[/color]
[color=#525252]▐[/color][color=#2e2e2e]▓[/color][color=#2f2f2f]▓▓▓▓[/color][color=#323232]▓[/color][color=#333333]▓▓▓▓▓[/color][color=#363636]▓[/color][color=#363636]▓▓▓▓▓▓▓▓▓[/color][color=#393939]▓▓▓▓▓[/color][color=#3d3e3e]▓[/color][color=#4a4a4a]▀[/color][color=#575757]░[/color][color=#626262]░[/color][color=#646464]░░░░[/color][color=#525252]░[/color][color=#444444]▀[/color][color=#373737]▓[/color][color=#363636]▓▓▓▓[/color][color=#333433]▓▓[/color][color=#323232]▓▓▓[/color][color=#303030]▓▓[/color][color=#2e2e2e]▓▓▓[/color][color=#2c2c2c]▓▓[/color][color=#2b2b2b]▓▓▓[/color][color=#282828]▓[/color][color=#272727]▓▓▓▓[/color][color=#242424]█[/color][color=#242424]████[/color][color=#212121]█[/color][color=#202020]█████[/color][color=#1d1d1d]█[/color][color=#1c1c1c]█████[/color][color=#5c5c5c]C[/color]
[color=#515151]▐[/color][color=#2e2e2e]▓[/color][color=#2f2f2f]▓▓▓▓[/color][color=#323232]▓[/color][color=#333333]▓▓▓▓▓[/color][color=#363636]▓[/color][color=#363636]▓▓▓▓▓▓▓▓▓[/color][color=#393939]▓[/color][color=#3b3c3b]▓[/color][color=#484848]▀[/color][color=#545454]░[/color][color=#616161]░[/color][color=#656565]░[/color][color=#656565]░░░░░░░░░[/color][color=#616261]░[/color][color=#575757]░[/color][color=#494949]▀[/color][color=#3a3a3a]▓[/color][color=#343434]▓[/color][color=#343434]▓▓▓▓[/color][color=#313131]▓[/color][color=#303030]▓▓▓▓[/color][color=#2d2d2d]▓[/color][color=#2c2c2c]▓▓▓▓[/color][color=#292929]▓[/color][color=#282828]▓▓▓▓[/color][color=#252525]▓[/color][color=#242424]████[/color][color=#212221]█[/color][color=#212121]█████[/color][color=#1e1e1e]█[/color][color=#1d1d1d]██████[/color][color=#595959]C[/color]
[color=#515151]▐[/color][color=#2e2e2e]▓[/color][color=#2f2f2f]▓▓▓▓[/color][color=#323232]▓[/color][color=#333333]▓▓▓▓▓[/color][color=#363636]▓[/color][color=#363636]▓▓▓▓▓▓▓[/color][color=#393939]▓[/color][color=#515151]▀[/color][color=#5e5e5e]░[/color][color=#656565]░[/color][color=#656565]░░░░░░░░░░░░░[/color][color=#616161]░[/color][color=#616161]░░░[/color][color=#5b5b5b]░[/color][color=#4d4d4d]▀[/color][color=#3f3f3f]▓[/color][color=#333333]▓[/color][color=#313231]▓▓▓[/color][color=#2f2f2f]▓▓[/color][color=#2e2e2e]▓▓▓[/color][color=#2b2c2b]▓▓[/color][color=#2a2a2a]▓▓▓[/color][color=#272727]▓▓[/color][color=#262626]▓▓█[/color][color=#242424]██[/color][color=#222222]███[/color][color=#202020]███[/color][color=#1e1e1e]███[/color][color=#1c1c1c]███[/color][color=#1b1b1b]██[/color][color=#595959]C[/color]
[color=#515151]▐[/color][color=#2e2e2e]▓[/color][color=#2f2f2f]▓▓▓▓[/color][color=#323232]▓[/color][color=#333333]▓▓▓▓▓[/color][color=#363636]▓[/color][color=#363636]▓▓▓▓▓▓▓[/color][color=#3a3a3a]▓[/color][color=#646564]░[/color][color=#656565]░░░░░░░░░░░░░░░[/color][color=#616161]░[/color][color=#606060]░░░░[/color][color=#5d5d5d]▒[/color][color=#5d5d5c]▒▒[/color][color=#505050]░[/color][color=#424242]▀[/color][color=#343434]▓[/color][color=#2f2f2f]▓[/color][color=#2e2e2e]▓▓▓▓[/color][color=#2b2b2b]▓[/color][color=#2a2b2a]▓▓▓▓[/color][color=#272727]▓[/color][color=#272727]▓▓██[/color][color=#232423]█[/color][color=#232323]████[/color][color=#202020]█[/color][color=#1f1f1f]█████[/color][color=#1c1c1c]█[/color][color=#1c1c1c]████[/color][color=#595959]C[/color]
[color=#515151]▐[/color][color=#2e2e2e]▓[/color][color=#2e2e2e]▓▓▓▓[/color][color=#313231]▓[/color][color=#323232]▓▓▓▓▓[/color][color=#353535]▓[/color][color=#363636]▓▓▓▓▓▓▓[/color][color=#393939]▓[/color][color=#646464]░[/color][color=#646464]░░░░░░░░░░░░░░░[/color][color=#616160]░[/color][color=#606060]░░░▒[/color][color=#5d5d5d]▒[/color][color=#5c5c5c]▒▒▒[/color][color=#595959]▒[/color][color=#585858]▒[/color][color=#525252]▒[/color][color=#444544]▒[/color][color=#373737]▓[/color][color=#2d2d2d]▓[/color][color=#2c2c2c]▓▓▓[/color][color=#292929]▓▓[/color][color=#282828]▓▓▓[/color][color=#262626]▓█[/color][color=#242424]███[/color][color=#222222]██[/color][color=#202020]████[/color][color=#1e1e1e]██[/color][color=#1d1d1d]████[/color][color=#1b1b1b]██[/color][color=#595959]C[/color]
[color=#505050]▐[/color][color=#2d2d2d]▓[/color][color=#2e2e2e]▓▓▓▓[/color][color=#313131]▓[/color][color=#323232]▓▓▓▓▓[/color][color=#353535]▓[/color][color=#353535]▓▓▓▓▓▓▓[/color][color=#383938]▓[/color][color=#636363]░[/color][color=#636363]░░░░░░░░[/color][color=#5f5f5f]░[/color][color=#474747]▄[/color][color=#313131]▄▄[/color][color=#5f605f]░[/color][color=#616161]░░░░▒▒▒[/color][color=#5c5c5c]▒[/color][color=#5b5b5b]▒▒▒[/color][color=#585858]▒[/color][color=#575757]▒▒[/color][color=#545454]▒[/color][color=#535353]▒▒[/color][color=#464646]▒[/color][color=#393939]▓[/color][color=#2d2d2d]▓[/color][color=#292929]▓[/color][color=#282828]▓▓▓▓[/color][color=#252525]▓[/color][color=#242424]████[/color][color=#222222]█[/color][color=#212121]█████[/color][color=#1e1e1e]█[/color][color=#1d1d1d]██████[/color][color=#1a1a1a]█[/color][color=#595959]C[/color]
[color=#505050]▐[/color][color=#2d2d2d]▓[/color][color=#2d2d2d]▓▓▓▓[/color][color=#303030]▓[/color][color=#313131]▓▓▓▓▓[/color][color=#343434]▓[/color][color=#343434]▓▓▓▓▓▓▓[/color][color=#383838]▓[/color][color=#626262]░[/color][color=#626262]░░░░░[/color][color=#505050]▄[/color][color=#353535]▄[/color][color=#1a1a1a]█[/color][color=#090909]█[/color][color=#090909]██[/color][color=#0d0d0d]█[/color][color=#0e0e0e]█[/color][color=#222222]█[/color][color=#3c3c3c]▄[/color][color=#565656]░[/color][color=#5e5e5e]▒[/color][color=#5d5d5d]▒▒▒▒[/color][color=#5a5a5a]▒[/color][color=#595959]▒▒▒[/color][color=#565656]▒[/color][color=#545454]▒▒[/color][color=#525252]▒[/color][color=#505050]▒▒[/color][color=#4e4e4d]▒[/color][color=#4c4c4c]╢[/color][color=#464646]▒[/color][color=#3a3a3a]▓[/color][color=#2e2e2e]▓[/color][color=#262626]▓[/color][color=#252525]▓███[/color][color=#232323]█[/color][color=#222222]█████[/color][color=#1f1f1f]█[/color][color=#1e1e1e]█████[/color][color=#1b1b1b]██[/color][color=#1a1a1a]██[/color][color=#595959]C[/color]
[color=#505050]▐[/color][color=#2c2c2c]▓[/color][color=#2d2d2d]▓▓▓▓[/color][color=#2f2f2f]▓[/color][color=#303030]▓▓▓▓▓[/color][color=#333333]▓[/color][color=#333433]▓▓▓▓▓▓▓[/color][color=#373737]▓[/color][color=#616161]░[/color][color=#616161]░[/color][color=#575757]░[/color][color=#424242]▄[/color][color=#272727]█[/color][color=#0d0d0d]█[/color][color=#0a0a0a]███[/color][color=#121212]█[/color][color=#171717]█[/color][color=#1c1c1c]█[/color][color=#202020]█[/color][color=#212121]███[/color][color=#191919]█[/color][color=#1d1d1d]█[/color][color=#313231]█[/color][color=#484848]▄[/color][color=#5a5a5a]▒[/color][color=#5a5a5a]▒▒▒▒[/color][color=#555555]▒[/color][color=#545454]▒▒[/color][color=#525252]▒[/color][color=#515151]▒▒[/color][color=#4e4e4e]▒[/color][color=#4c4c4c]▒╢[/color][color=#494949]╢[/color][color=#484848]╢╢[/color][color=#444444]▒[/color][color=#3a3a3a]▓[/color][color=#2f302f]▓[/color][color=#252525]█[/color][color=#232323]██[/color][color=#212121]████[/color][color=#1f1f1f]██[/color][color=#1e1e1e]████[/color][color=#1b1b1b]███[/color][color=#1a1a1a]██[/color][color=#595959]C[/color]
[color=#4f4f4f]▐[/color][color=#2b2b2b]▓[/color][color=#2c2c2c]▓▓▓▓▓[/color][color=#2f2f2f]▓[/color][color=#303030]▓▓▓▓▓[/color][color=#323232]▓▓[/color][color=#333333]▓▓▓▓▓▓[/color][color=#3e3e3e]▓[/color][color=#2d2e2d]▓[/color][color=#272727]▓[/color][color=#1e1e1e]█[/color][color=#141414]█[/color][color=#121212]██[/color][color=#1b1b1b]█[/color][color=#202020]█[/color][color=#262626]█[/color][color=#383838]▀[/color][color=#494949]▀[/color][color=#595958]░[/color][color=#4e4e4e]░[/color][color=#3d3d3d]▀[/color][color=#2d2d2d]▓[/color][color=#282828]▓[/color][color=#242424]▓[/color][color=#202020]▓[/color][color=#1b1b1b]█[/color][color=#171717]█[/color][color=#262626]█[/color][color=#3b3b3b]▄[/color][color=#505050]░[/color][color=#555555]▒[/color][color=#545454]▒▒[/color][color=#515151]▒[/color][color=#505050]▒▒[/color][color=#4e4e4d]▒[/color][color=#4c4c4c]╢╢[/color][color=#494949]╢[/color][color=#484848]╢╢[/color][color=#454545]╢[/color][color=#434343]╢╢[/color][color=#404040]╣[/color][color=#3f3f3f]▓[/color][color=#393939]╢[/color][color=#212121]█[/color][color=#212121]██████[/color][color=#1d1d1d]█[/color][color=#1d1d1d]██████[/color][color=#1a1a1a]█[/color][color=#191919]█[/color][color=#595959]C[/color]
[color=#4f4f4f]▐[/color][color=#2a2a2a]▓[/color][color=#2b2b2b]▓▓▓▓▓[/color][color=#2e2e2e]▓[/color][color=#2e2f2e]▓▓▓▓▓▓[/color][color=#313131]▓[/color][color=#323232]▓▓▓▓▓▓▓▓[/color][color=#2a2a2a]▓[/color][color=#252525]▓[/color][color=#222222]▓▓[/color][color=#313131]▓[/color][color=#434343]▀[/color][color=#535353]░[/color][color=#5d5d5d]▒[/color][color=#5d5d5d]▒▒▒▒▒▒[/color][color=#505050]░[/color][color=#3f3f3f]▀[/color][color=#2e2e2e]▓[/color][color=#272727]▓[/color][color=#242424]▓[/color][color=#202020]▓[/color][color=#1c1c1c]█[/color][color=#161616]██[/color][color=#2f2f2f]█[/color][color=#434343]▒[/color][color=#505050]▒[/color][color=#4e4f4e]▒▒[/color][color=#4c4c4c]╣[/color][color=#4a4b4a]╢╢[/color][color=#484848]╢[/color][color=#464646]╢╢[/color][color=#434343]╢[/color][color=#424242]╢╣[/color][color=#3f3f3f]▓[/color][color=#3d3e3d]▓[/color][color=#3c3c3c]▓[/color][color=#1c1c1c]█[/color][color=#1e1e1e]███████████████[/color][color=#595859]C[/color]
[color=#4e4e4e]▐[/color][color=#292929]▓[/color][color=#2a2a2a]▓▓▓▓▓[/color][color=#2d2d2d]▓[/color][color=#2d2d2d]▓▓▓▓▓▓▓[/color][color=#303030]▓[/color][color=#313131]▓▓▓▓▓▓▓▓[/color][color=#3f403f]▀[/color][color=#4d4d4d]▒[/color][color=#5a5a5a]░[/color][color=#5c5c5c]▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#575757]▒[/color][color=#4f4f4f]▒[/color][color=#3f3f3f]▀[/color][color=#2f2f2f]▓[/color][color=#262626]▓[/color][color=#232323]▓[/color][color=#202020]█[/color][color=#1c1c1c]█[/color][color=#171717]█[/color][color=#151515]█[/color][color=#242424]█[/color][color=#363636]▄[/color][color=#474747]▒[/color][color=#494949]╢╢╢╢[/color][color=#434343]╢[/color][color=#424242]╢╣[/color][color=#3f3f3f]▓[/color][color=#3d3d3d]▓▓[/color][color=#3a3b3b]▓[/color][color=#171717]█[/color][color=#1a1a1a]█[/color][color=#1c1c1c]██[/color][color=#1e1e1e]███████████[/color][color=#191919]█[/color][color=#585858]C[/color]
[color=#4d4d4d]▐[/color][color=#282828]▓[/color][color=#282928]▓▓▓▓▓[/color][color=#2b2b2b]▓[/color][color=#2c2c2c]▓▓▓▓▓▓▓[/color][color=#2f2f2f]▓[/color][color=#2f2f2f]▓▓▓▓▓[/color][color=#494949]▒[/color][color=#555555]░[/color][color=#595959]▒[/color][color=#595a59]▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#565656]▒[/color][color=#555555]▒▒▒[/color][color=#4f4f4f]▒[/color][color=#3f3f3f]▄[/color][color=#2f2f2f]█[/color][color=#272727]▓[/color][color=#272727]▓▓[/color][color=#222222]█[/color][color=#1f1f1f]█[/color][color=#1b1b1b]██[/color][color=#292929]▀[/color][color=#414141]▒[/color][color=#454545]╢╢╢╢╣▓[/color][color=#3d3d3d]▓[/color][color=#3c3c3c]▓▓[/color][color=#393939]▓[/color][color=#141414]█[/color][color=#181818]█[/color][color=#1b1b1b]█[/color][color=#1c1c1c]█████████████[/color][color=#585858]C[/color]
[color=#4d4d4d]▐[/color][color=#272727]▓[/color][color=#272727]▓▓▓▓▓▓[/color][color=#2a2a2a]▓[/color][color=#2b2b2b]▓▓▓▓▓▓▓▓[/color][color=#2e2e2e]▓▓[/color][color=#2e2e2e]▓[/color][color=#333332]▓[/color][color=#565656]▒[/color][color=#575757]▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#535353]▒[/color][color=#414141]▄[/color][color=#2b2b2b]█[/color][color=#171717]█[/color][color=#121212]██[/color][color=#1c1c1c]█[/color][color=#212121]█[/color][color=#242424]█[/color][color=#2a2a2a]█[/color][color=#343434]▓[/color][color=#3d3d3d]▒[/color][color=#464646]▒[/color][color=#474747]╢╢╢[/color][color=#434343]╢[/color][color=#424242]╢╣[/color][color=#3f3f3f]▓[/color][color=#3e3e3e]▓▓[/color][color=#3b3b3b]▓[/color][color=#3a3a3a]▓▓[/color][color=#373837]▓[/color][color=#131313]█[/color][color=#171717]█[/color][color=#1a1a1a]█[/color][color=#1b1b1b]█████████████[/color][color=#585858]C[/color]
[color=#4c4c4c]▐[/color][color=#252625]▓[/color][color=#262626]▓▓▓▓▓▓[/color][color=#292929]▓[/color][color=#292929]▓▓▓▓▓▓▓▓[/color][color=#2c2c2c]▓▓▓[/color][color=#303030]▓[/color][color=#535353]▒[/color][color=#545454]▒▒▒▒▒▒▒▒▒▒▒▒[/color][color=#494949]▒[/color][color=#333332]▄[/color][color=#1d1d1d]█[/color][color=#0c0c0c]█[/color][color=#0c0d0d]██[/color][color=#111111]█[/color][color=#141414]█[/color][color=#1c1c1c]█[/color][color=#2c2c2c]█[/color][color=#3b3b3b]▒[/color][color=#474747]▒[/color][color=#494949]╢╢╢╢╢[/color][color=#434343]╢[/color][color=#424242]╢╣[/color][color=#3f403f]╣[/color][color=#3e3e3e]▓▓[/color][color=#3c3c3c]▓[/color][color=#3a3b3a]▓▓[/color][color=#383838]▓[/color][color=#373737]▓▓[/color][color=#131313]█[/color][color=#171717]█[/color][color=#191919]█[/color][color=#1b1b1b]█████████████[/color][color=#585858]C[/color]
[color=#4b4b4b]▐[/color][color=#242424]█[/color][color=#252525]█▓▓▓▓▓▓[/color][color=#282828]▓[/color][color=#282828]▓▓▓▓▓▓▓▓▓▓[/color][color=#2d2d2d]▓[/color][color=#505050]▒[/color][color=#505050]▒▒▒▒▒▒▒▒▒[/color][color=#4c4c4c]▒[/color][color=#232323]█[/color][color=#0e0e0e]█[/color][color=#090909]███[/color][color=#131313]█[/color][color=#181818]█[/color][color=#282828]█[/color][color=#373737]▒[/color][color=#454545]▒[/color][color=#4a4a4a]╢[/color][color=#494949]╢╢╢[/color][color=#464646]╢[/color][color=#454545]╢╢╢[/color][color=#424242]╢[/color][color=#414141]╣╣[/color][color=#3e3e3e]▓[/color][color=#3d3d3d]▓▓[/color][color=#3b3b3b]▓[/color][color=#3a3a3a]▓▓[/color][color=#373737]▓[/color][color=#353535]╢[/color][color=#282828]█[/color][color=#1d1d1d]█[/color][color=#121212]█[/color][color=#161616]█[/color][color=#191919]█[/color][color=#1a1a1a]█████████████[/color][color=#585858]C[/color]
[color=#4b4b4b]▐[/color][color=#232323]█[/color][color=#232323]████▓▓▓[/color][color=#262626]▓▓[/color][color=#272727]▓▓▓▓▓▓▓▓▓[/color][color=#2b2b2b]▓[/color][color=#4d4d4d]╣[/color][color=#4d4d4d]▒▒▒▒▒▒▒▒▒[/color][color=#434343]▒[/color][color=#080808]█[/color][color=#0e0e0e]█[/color][color=#131313]█[/color][color=#171717]█[/color][color=#323232]█[/color][color=#424342]▒[/color][color=#494949]╢[/color][color=#494949]╢╢╢╢[/color][color=#464646]╢[/color][color=#454545]╢╢╢[/color][color=#424242]╢[/color][color=#414141]╣╣▓[/color][color=#3e3e3e]▓[/color][color=#3d3d3d]▓▓▓[/color][color=#3a3a3a]▓[/color][color=#383838]▓[/color][color=#2d2d2d]█[/color][color=#1f1f1f]█[/color][color=#121212]█[/color][color=#0b0b0b]█[/color][color=#0c0c0c]█[/color][color=#101010]█[/color][color=#141414]█[/color][color=#171717]█[/color][color=#181818]██[/color][color=#1a1a1a]████████████[/color][color=#585858]C[/color]
[color=#4a4a4a]▐[/color][color=#222222]█[/color][color=#222222]████████[/color][color=#252525]▓[/color][color=#262626]▓▓▓▓▓▓▓▓▓▓[/color][color=#494949]╢[/color][color=#4a4a4a]╢╢╢╢╣╣╢╢╢[/color][color=#3f3f3f]▒[/color][color=#0c0c0c]█[/color][color=#141414]█[/color][color=#191919]█[/color][color=#1d1d1d]█[/color][color=#444444]╣[/color][color=#474747]╢╢╢╢╢╢╢╢╣[/color][color=#404040]╣[/color][color=#3f3f3f]▓▓▓[/color][color=#3c3c3c]▓[/color][color=#3b3b3b]▓▓[/color][color=#323232]╣[/color][color=#242424]█[/color][color=#161616]█[/color][color=#0b0b0b]█[/color][color=#0c0c0c]██[/color][color=#0f0f0f]█[/color][color=#111111]█[/color][color=#131313]█[/color][color=#151515]█[/color][color=#171717]██[/color][color=#191919]██████████████[/color][color=#585858]C[/color]
[color=#494949]▐[/color][color=#202020]█[/color][color=#212121]█████████[/color][color=#242424]█[/color][color=#242424]███▓▓▓▓▓▓[/color][color=#464646]╢[/color][color=#464646]╢╢╢╢╢╢╢╢╢[/color][color=#3c3c3c]▒[/color][color=#0e0e0e]█[/color][color=#151515]█[/color][color=#1b1b1b]█[/color][color=#1f1f1f]█[/color][color=#404140]╣[/color][color=#434343]╢╢╢╢╣╣╣▓▓[/color][color=#3d3d3d]▓[/color][color=#3c3c3c]▓▓[/color][color=#373737]╣[/color][color=#282828]█[/color][color=#1a1a1a]█[/color][color=#0d0d0d]█[/color][color=#0b0b0b]███[/color][color=#111111]█[/color][color=#131313]█[/color][color=#151515]██[/color][color=#181818]█[/color][color=#191919]██████████████████[/color][color=#575757]C[/color]
[color=#494949]▐[/color][color=#1f1f1f]█[/color][color=#1f2020]██████████[/color][color=#232323]█[/color][color=#232323]████████[/color][color=#424242]╢[/color][color=#424242]╢╢╢╢╢╢╢╢╢[/color][color=#393939]▓[/color][color=#0e0e0e]█[/color][color=#151515]█[/color][color=#1a1a1a]█[/color][color=#1e1e1e]█[/color][color=#3d3d3d]╣[/color][color=#404040]╣╣▓▓▓▓▓▓[/color][color=#3a3a3a]╢[/color][color=#2d2d2d]█[/color][color=#1e1e1e]█[/color][color=#101010]█[/color][color=#0b0b0b]█[/color][color=#0d0d0d]█[/color][color=#0f0f0f]█[/color][color=#111111]█[/color][color=#131313]█[/color][color=#151515]█[/color][color=#161616]██[/color][color=#191919]██[/color][color=#1a1a1a]████████████████████[/color][color=#575757]C[/color]
[color=#484848]▐[/color][color=#1e1e1e]█[/color][color=#1e1e1e]███████████[/color][color=#212121]██[/color][color=#222222]██████[/color][color=#3e3f3e]▓[/color][color=#3f3f3f]▓▓▓▓▓▓▓▓▓[/color][color=#353535]▓[/color][color=#0e0e0e]█[/color][color=#141414]█[/color][color=#191919]█[/color][color=#1d1d1d]█[/color][color=#3a3a3a]▓[/color][color=#3c3c3c]▓▓▓▓▓[/color][color=#313130]▓[/color][color=#222222]█[/color][color=#141414]█[/color][color=#0b0b0b]█[/color][color=#0c0c0c]██[/color][color=#101010]█[/color][color=#121212]█[/color][color=#141414]█[/color][color=#161616]█[/color][color=#181818]██[/color][color=#1a1a1a]█████████████████████████[/color][color=#575757]C[/color]
[color=#474747]▐[/color][color=#1d1d1d]█[/color][color=#1d1d1d]█████████████[/color][color=#202020]██[/color][color=#202020]████[/color][color=#3b3b3b]▓[/color][color=#3b3b3b]▓▓▓▓▓▓▓▓▓[/color][color=#313131]▓[/color][color=#0d0d0d]█[/color][color=#141414]█[/color][color=#181818]█[/color][color=#1c1c1c]█[/color][color=#373737]▓[/color][color=#393939]▓╢[/color][color=#282828]█[/color][color=#191919]█[/color][color=#0c0c0c]█[/color][color=#0c0c0c]██[/color][color=#101010]█[/color][color=#121212]█[/color][color=#141414]█[/color][color=#161616]█[/color][color=#171717]██[/color][color=#1a1a1a]██[/color][color=#1b1b1b]████████████████████[/color][color=#161616]█[/color][color=#161616]██████[/color][color=#575757]C[/color]
[color=#474747]▐[/color][color=#1c1c1c]█[/color][color=#1c1c1c]██████████████[/color][color=#1f1f1f]█████[/color][color=#383838]▓[/color][color=#383838]▓▓▓▓▓▓▓▓▓[/color][color=#2e2e2e]▓[/color][color=#0d0d0d]█[/color][color=#131313]█[/color][color=#171717]█[/color][color=#1b1b1b]█[/color][color=#252525]██[/color][color=#151515]█[/color][color=#121212]█[/color][color=#101010]████[/color][color=#171717]█[/color][color=#181818]██[/color][color=#1a1a1a]██████████████████████████████[/color][color=#151515]█[/color][color=#141414]█[/color][color=#575757]C[/color]
[color=#464646]▐[/color][color=#1b1b1b]█[/color][color=#1b1b1b]███████████████████[/color][color=#353535]▓[/color][color=#353535]▓▓▓▓▓▓▓▓▓[/color][color=#2f2f2f]╢[/color][color=#181818]█[/color][color=#141414]██████████████████████████████████████████[/color][color=#151515]████[/color][color=#575757]C[/color]
[color=#464646]▐[/color][color=#1a1a1a]█[/color][color=#1a1a1a]███████████████████[/color][color=#323232]▓[/color][color=#323232]▓▓▓▓▓▓▓▓▓▓╢[/color][color=#262626]█[/color][color=#171717]█[/color][color=#171717]██[/color][color=#1b1b1b]█[/color][color=#1b1b1b]███████████████████████[/color][color=#171717]█[/color][color=#171717]███████████████[/color][color=#141414]█[/color][color=#141414]█[/color][color=#575756]C[/color]
[color=#454545]▐[/color][color=#191919]█[/color][color=#191919]███████████████████[/color][color=#2f302f]▓[/color][color=#303030]▓▓▓▓▓▓▓[/color][color=#262626]█[/color][color=#1b1b1b]█[/color][color=#111111]█[/color][color=#0c0c0c]████[/color][color=#171717]█[/color][color=#191919]██[/color][color=#1a1a1a]█████████████████████████████[/color][color=#151515]█[/color][color=#151515]██████████[/color][color=#565656]C[/color]
[color=#454545]▐[/color][color=#181818]█[/color][color=#181818]███████████████████[/color][color=#2d2d2d]▓[/color][color=#2d2d2d]▓▓▓[/color][color=#272727]█[/color][color=#1d1d1d]█[/color][color=#121212]█[/color][color=#0b0b0b]█[/color][color=#0c0c0c]██[/color][color=#0f0f0f]█[/color][color=#101010]██[/color][color=#141414]█[/color][color=#161616]█[/color][color=#171717]██[/color][color=#191919]██████████████████████████████████[/color][color=#141414]█[/color][color=#141414]██████[/color][color=#565656]C[/color]
[color=#4c4c4c]▐[/color][color=#171717]█[/color][color=#171717]███████████████████[/color][color=#282928]▓[/color][color=#222222]█[/color][color=#1a1a1a]█[/color][color=#111111]█[/color][color=#0e0e0e]█[/color][color=#0d0d0d]███[/color][color=#111111]█[/color][color=#131313]██[/color][color=#151515]█[/color][color=#161616]██████[/color][color=#191919]████████████████████████████████████[/color][color=#131313]█[/color][color=#131313]███[/color]
[color=#797979] [/color][color=#1a1a1a]█[/color][color=#161616]█[/color][color=#171717]██████████████████████[/color][color=#121212]█[/color][color=#121212]███[/color][color=#151515]█[/color][color=#161616]████████████████████████████████████████████████[/color][color=#202020]█[/color]
[color=#808080]  █[/color][color=#161616]█[/color][color=#161616]█████████████████████████████████████████████████████████████████████[/color][color=#121212]█[/color][color=#121212]███[/color][color=#252525]█[/color]
[color=#808080]   [/color][color=#494949]▀[/color][color=#1a1a1a]█[/color][color=#151515]█[/color][color=#151515]████████████████████████████████████████████████████████████████████[/color][color=#121212]█[/color][color=#1d1d1d]█[/color][color=#535353]▀[/color]
[color=#808080]     [/color][color=#626262]`[/color][color=#414141]▀[/color][color=#272727]█[/color][color=#161616]█[/color][color=#151515]███████████████████████████████████████████████████████[/color][color=#131313]████████[/color][color=#2a2a2a]▀[/color][color=#464646]▀[/color]
"""

ascii_art = parse_bbcode(bbcode_text)

# ASCII- und Info-Zeilen nebeneinander ausgeben

def gather_info_lines(sys_info: dict, versions: dict) -> list:
    """
    Baut eine Liste von Strings auf, die alle Versions- und Systeminfos enthält.
    Farbige Überschriften (z.B. blau) werden hier eingefügt.
    """
    blue = "\033[34m"
    reset = "\033[0m"
    lines = []

    # Versionen aus der JSON-Datei (mit Fallback "Unbekannt")
    p_terminal_ver       = versions.get("P-Terminal Version",       "Unbekannt")
    pp_terminal_ver      = versions.get("PP-Terminal Version",      "Unbekannt")
    launcher_ver         = versions.get("PP-Terminal Launcher Version", "Unbekannt")
    p_compiler_ver       = versions.get("Peharge Compiler Version", "Unbekannt")
    p_cernel_ver    = versions.get("Peharge Kernel Version", "Unbekannt")
    iq_cernel_ver    = versions.get("IQ Kernel Version", "Unbekannt")
    simon_ver    = versions.get("SIMON Version", "Unbekannt")
    license_info         = versions.get("P-Terminal License",       "Unbekannt")

    title = f"PP-Terminal - {os.getlogin()}"
    line = "-" * len(title)

    # Zeilen hinzufügen
    lines.append("")
    lines.append(f"             {title}")
    lines.append(f"          {line}")
    lines.append(f"        {main_color}P-Terminal Version{reset}: {p_terminal_ver}")
    lines.append(f"       {main_color}PP-Terminal Version{reset}: {pp_terminal_ver}")
    lines.append(f"       {main_color}PP-Terminal Launcher Version{reset}: {launcher_ver}")
    lines.append(f"      {main_color}Peharge Compiler Version{reset}: {p_compiler_ver}")
    lines.append(f"      {main_color}Peharge Kernel Version{reset}: {p_cernel_ver}")
    lines.append(f"      {main_color}IQ Kernel Version{reset}: {iq_cernel_ver}")
    lines.append(f"      {main_color}SIMON Version{reset}: {simon_ver}")
    lines.append(f"      {main_color}P-Terminal License{reset}: {license_info}")
    lines.append(f"      {main_color}MAVIS Version{reset}: 4.3")
    lines.append(f"      {main_color}MAVIS Launcher Version{reset}: 4")
    lines.append(f"      {main_color}MAVIS Terminal Version{reset}: 5")
    lines.append(f"      {main_color}MAVIS License{reset}: MIT")

    # Betriebssystem
    lines.append(f"      {main_color}OS{reset}: {sys_info['os_name']} {sys_info['os_release']}")
    lines.append(f"      {main_color}Version{reset}: {sys_info['os_version']}")
    lines.append(f"      {main_color}Architecture{reset}: {sys_info['os_arch']}")
    # lines.append(f"      {main_color}Hostname{reset}: {sys_info['hostname']}")
    lines.append(f"      {main_color}IP Address{reset}: {sys_info['ip_address']}")

    # CPU
    lines.append(f"      {main_color}CPU{reset}: {sys_info['cpu_model']}")
    # lines.append(f"      {main_color}Architektur{reset}: {sys_info['cpu_arch']}")
    # lines.append(f"      {main_color}Cores{reset}: {sys_info['cpu_cores']} (logical: {sys_info['cpu_threads']})")
    # lines.append(f"      {main_color}Max Frequency{reset}: {sys_info['cpu_freq']} MHz")

    # RAM / Swap
    # lines.append(f"      {main_color}RAM{reset}: {sys_info['ram_total']} GB")
    # lines.append(f"      {main_color}RAM Total{reset}: {sys_info['ram_total']} GB")
    # lines.append(f"      {main_color}RAM Used{reset}: {sys_info['ram_used']} GB ({sys_info['ram_usage']}%)")
    # lines.append(f"      {main_color}RAM Free{reset}: {sys_info['ram_free']} GB")
    lines.append(f"      {main_color}Swap{reset}: {sys_info['swap_total']} GB")
    # lines.append(f"      {main_color}Swap Total{reset}: {sys_info['swap_total']} GB")
    # lines.append(f"      {main_color}Swap Used{reset}: {sys_info['swap_used']} GB")
    # lines.append(f"      {main_color}Swap Free{reset}: {sys_info['swap_free']} GB")

    # Storage
    lines.append(f"      {main_color}Storage{reset}: {sys_info['storage_total']} GB")
    # lines.append(f"      {main_color}Storage Total{reset}: {sys_info['storage_total']} GB")
    # lines.append(f"      {main_color}Storage Used{reset}: {sys_info['storage_used']} GB")
    # lines.append(f"      {main_color}Storage Free{reset}: {sys_info['storage_free']} GB")

    # Load Average oder CPU-Auslastung
    """
    if isinstance(sys_info['load_avg'], dict):
        la = sys_info['load_avg']
        lines.append(f"      {main_color}Load Average{reset}: 1m={la['1m']}, 5m={la['5m']}, 15m={la['15m']}")
    else:
        lines.append(f"      {main_color}Load Average{reset}: {sys_info['load_avg']}")

    # Uptime
    lines.append(f"      {main_color}Uptime{reset}: {sys_info['uptime']}")
    """

    """
    # Netzwerkschnittstellen (nur IPv4 und MAC)
    for iface, details in sys_info['network_interfaces'].items():
        ipv4 = details.get('IPv4', 'N/A')
        mac  = details.get('MAC', 'N/A')
        lines.append(f"      {main_color}Interface {iface}{reset}: IPv4={ipv4}, MAC={mac}")
        
    """

    # Benutzer
    for user in sys_info['user_info']:
        lines.append(f"      {main_color}User{reset}: {user['user']} (terminal: {user['terminal']}, started: {user['started']})")

    # Python/Pip/Git
    lines.append(f"      {main_color}Python Version{reset}: {sys_info['python_version']}")
    lines.append(f"      {main_color}PIP Version{reset}: {sys_info['pip_version']}")
    try:
        git_ver = subprocess.check_output(['git', '--version'], text=True).strip()
    except Exception:
        git_ver = "unbekannt"
    lines.append(f"      {main_color}Git Version{reset}: {git_ver}")

    # Windows-spezifische Utilities
    lines.append(f"      {main_color}PowerShell Version{reset}: {get_powershell_version()}")
    lines.append(f"      {main_color}WSL Version{reset}: {get_wsl_version()}")
    lines.append(f"      {main_color}Kernelversion{reset}: {get_kernel_version()}")
    lines.append(f"      {main_color}WSLg Version{reset}: {get_wslg_version()}")
    lines.append(f"      {main_color}MSRDC Version{reset}: {get_msrpc_version()}")
    lines.append(f"      {main_color}Direct3D Version{reset}: {get_direct3d_version()}")
    lines.append(f"       {main_color}DXCore Version{reset}: {get_dxcore_version()}")
    lines.append(f"       {main_color}Ollama Version{reset}: {get_ollama_version()}")
    lines.append(f"        {main_color}Visual Studio Version{reset}: {get_visual_studio_version()}")

    # Rust
    try:
        rust_ver = subprocess.check_output(['rustc', '--version'], text=True).strip()
    except Exception:
        rust_ver = "unbekannt"
    lines.append(f"         {main_color}Rust Version{reset}: {rust_ver}")

    # Farbpaletten
    lines.append("")
    lines.append("                    " + show_color_palette_1())
    lines.append("                " + show_color_palette_3())
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

# Hauptprogramm

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
