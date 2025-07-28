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
WARNING: It is recommended to install Clojure only from the official source:
https://clojure.org/guides/install_clojure

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the Clojure installation? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Clojure folgen
print(f"[{timestamp()}] [INFO] Proceeding with Clojure installation...")

import os
import sys
import shutil
import subprocess
import logging
import tempfile
import json
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# --- Logging konfigurieren ---
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

# --- Konstanten ---
GITHUB_RELEASES_API = "https://api.github.com/repos/clojure/brew-install/releases/latest"  # CLI releases publiziert hier :contentReference[oaicite:0]{index=0}
CLI_CMD             = "clojure"
JAVA_CMD            = "java"

def is_tool_installed(cmd: str) -> bool:
    """Prüft, ob ein Befehl im PATH verfügbar ist."""
    return shutil.which(cmd) is not None

def fetch_latest_installer_info() -> dict:
    """
    Holt über die GitHub-API das neueste Release aus clojure/brew-install und
    sucht nach dem Asset 'win-install.ps1'.
    """
    logging.info("Ermittle neueste Clojure-CLI-Version über GitHub API...")
    req = Request(GITHUB_RELEASES_API, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req) as resp:
            data = json.load(resp)
    except (HTTPError, URLError) as e:
        logging.error(f"Fehler bei der API-Abfrage: {e}")
        sys.exit(1)

    version = data.get("tag_name", "").lstrip("v")
    asset_url = None
    for asset in data.get("assets", []):
        if asset.get("name", "") == "win-install.ps1":
            asset_url = asset.get("browser_download_url")
            break

    if not version or not asset_url:
        logging.error("Konnte 'win-install.ps1' im neuesten Release nicht finden.")
        sys.exit(1)

    logging.info(f"Gefundene Version: {version}")
    return {"version": version, "url": asset_url}

def download_file(url: str, dest: Path):
    """Lädt eine Datei herunter und zeigt Fortschritt im Log."""
    logging.info(f"Download: {url}")
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp, open(dest, "wb") as out:
            total = int(resp.getheader("Content-Length", 0) or 0)
            downloaded = 0
            chunk_size = 8192
            while True:
                chunk = resp.read(chunk_size)
                if not chunk:
                    break
                out.write(chunk)
                downloaded += len(chunk)
                if total:
                    pct = downloaded * 100 / total
                    logging.info(f"Fortschritt: {pct:.1f}%")
        logging.info(f"Gespeichert unter: {dest}")
    except (HTTPError, URLError) as e:
        logging.error(f"Download-Fehler: {e}")
        sys.exit(1)

def run_powershell_installer(ps1_path: Path):
    """Führt das heruntergeladene PowerShell-Skript zur Installation aus."""
    logging.info(f"Starte PowerShell-Installer: {ps1_path}")
    cmd = [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", str(ps1_path)
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info("Clojure-CLI wurde erfolgreich installiert.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation fehlgeschlagen (Exit-Code {e.returncode}):\n{e.stderr}")
        sys.exit(e.returncode)

def verify_installation():
    """Prüft die Installation via 'clojure --version'."""
    try:
        out = subprocess.check_output([CLI_CMD, "--version"], text=True).strip()
        logging.info(f"Clojure-CLI Version: {out}")
    except Exception as e:
        logging.error(f"Verifikation fehlgeschlagen: {e}")
        sys.exit(1)

def main():
    logging.info("=== Clojure-CLI Installer gestartet ===")

    if os.name != "nt":
        logging.error("Dieses Skript läuft nur unter Windows.")
        sys.exit(1)

    if not is_tool_installed(JAVA_CMD):
        logging.error("Java nicht gefunden. Bitte installiere eine JDK-Version und setze JAVA_HOME.")
        sys.exit(1)
    else:
        logging.info("Java ist installiert.")

    if is_tool_installed(CLI_CMD):
        logging.info("Clojure-CLI ist bereits installiert. Abbruch.")
        return

    info = fetch_latest_installer_info()
    with tempfile.TemporaryDirectory() as td:
        ps1_file = Path(td) / "win-install.ps1"
        download_file(info["url"], ps1_file)
        run_powershell_installer(ps1_file)

    verify_installation()
    logging.info("=== Clojure-CLI Installation abgeschlossen ===")

if __name__ == "__main__":
    main()