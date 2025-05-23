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
import shutil
import subprocess
import logging
import tempfile
import zipfile
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

# --- Konstanten für die Installation ---
LUA_VERSION    = "5.4.6"  # Aktuelle stabile Version
BASE_URL       = "https://downloads.sourceforge.net/project/luabinaries"
FILENAME       = f"lua-{LUA_VERSION}_Win64_bin.zip"
DOWNLOAD_URL   = f"{BASE_URL}/{LUA_VERSION}/Windows%20Libraries/{FILENAME}"
INSTALL_ROOT   = Path("C:/Program Files/Lua")
INSTALL_DIR    = INSTALL_ROOT / f"Lua-{LUA_VERSION}"
BIN_DIR        = INSTALL_DIR  # die ZIP enthält direkt die .exe im Wurzelverzeichnis

def is_lua_installed() -> bool:
    """Prüft, ob 'lua' bereits im PATH aufrufbar ist."""
    return shutil.which("lua") is not None

def download_lua(dest: Path):
    """Lädt das Lua-Binary-ZIP herunter."""
    logging.info(f"Starte Download von Lua {LUA_VERSION} von {DOWNLOAD_URL}")
    try:
        req = Request(DOWNLOAD_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp, open(dest, "wb") as out:
            total = int(resp.getheader("Content-Length", 0))
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
                    logging.info(f"Download-Fortschritt: {pct:.1f}%")
        logging.info(f"Download abgeschlossen: {dest}")
    except (HTTPError, URLError) as e:
        logging.error(f"Fehler beim Download: {e}")
        sys.exit(1)

def extract_lua(zip_path: Path):
    """
    Entpackt das ZIP-Archiv nach INSTALL_DIR
    und löscht ggf. alte Installation.
    """
    if INSTALL_DIR.exists():
        logging.info("Alte Lua-Installation gefunden, wird gelöscht...")
        shutil.rmtree(INSTALL_DIR)
    logging.info(f"Entpacke {zip_path} nach {INSTALL_DIR}")
    INSTALL_DIR.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(INSTALL_DIR)
    logging.info("Entpackung abgeschlossen.")

def update_path():
    """Fügt Lua-Installationsverzeichnis dem System-PATH hinzu (für neue Terminals)."""
    lua_dir = str(BIN_DIR)
    current = os.environ.get("PATH", "")
    if lua_dir.lower() in current.lower():
        logging.info("Lua ist bereits im PATH.")
        return
    new_path = f"{current};{lua_dir}"
    logging.info(f"Füge Lua dem PATH hinzu: {lua_dir}")
    # setx schreibt den neuen PATH in die Registry
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation():
    """Prüft die Installation via 'lua -v'."""
    try:
        result = subprocess.run(["lua", "-v"], capture_output=True, text=True, check=True)
        logging.info(f"Lua erfolgreich installiert: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Fehler bei der Verifikation von Lua: {e}")
        sys.exit(1)

def main():
    logging.info("=== Lua-Installer gestartet ===")
    if os.name != "nt":
        logging.error("Dieses Skript funktioniert nur unter Windows.")
        sys.exit(1)

    if is_lua_installed():
        logging.info("Lua ist bereits installiert. Abbruch.")
        return

    # Temporäres Verzeichnis für den Download
    with tempfile.TemporaryDirectory() as td:
        tmp_zip = Path(td) / FILENAME
        download_lua(tmp_zip)
        extract_lua(tmp_zip)

    update_path()
    verify_installation()
    logging.info("=== Lua-Installation abgeschlossen ===")

if __name__ == "__main__":
    main()