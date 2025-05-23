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
DOTNET_INSTALL_SCRIPT = "https://dot.net/v1/dotnet-install.ps1"
INSTALL_DIR           = Path("C:/Program Files/dotnet")
FSI_CMD               = "fsi"          # F# Interactive
DOTNET_CMD            = "dotnet"

def is_dotnet_installed() -> bool:
    """Prüft, ob 'dotnet' bereits im PATH verfügbar ist."""
    return shutil.which(DOTNET_CMD) is not None

def is_fsharp_available() -> bool:
    """Prüft, ob 'fsi' (F# Interactive) verfügbar ist."""
    return shutil.which(FSI_CMD) is not None

def download_install_script(dest: Path) -> None:
    """Lädt das offizielle dotnet-install PowerShell-Skript herunter."""
    logging.info(f"Starte Download des dotnet-install-Skripts von {DOTNET_INSTALL_SCRIPT}")
    try:
        req = Request(DOTNET_INSTALL_SCRIPT, headers={"User-Agent": "Mozilla/5.0"})
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
                    logging.info(f"Download-Fortschritt: {pct:.1f}%")
        logging.info(f"dotnet-install-Skript gespeichert: {dest}")
    except (HTTPError, URLError) as e:
        logging.error(f"Fehler beim Herunterladen: {e}")
        sys.exit(1)

def run_install_script(script_path: Path) -> None:
    """
    Führt das PowerShell-Skript aus, um das .NET SDK (LTS) zu installieren.
    """
    logging.info(f"Starte Installation des .NET SDK (LTS) in {INSTALL_DIR}")
    ps_command = [
        "powershell",
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", str(script_path),
        "-Channel", "LTS",
        "-InstallDir", str(INSTALL_DIR),
        "-NoPath"
    ]
    try:
        subprocess.run(ps_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info(".NET SDK erfolgreich installiert.")
    except subprocess.CalledProcessError as e:
        logging.error(f".NET-Installation fehlgeschlagen (Exit-Code {e.returncode}):\n{e.stderr}")
        sys.exit(e.returncode)

def update_path() -> None:
    """Fügt das dotnet-Install-Verzeichnis dem System-PATH hinzu (für neue Terminals)."""
    dotnet_bin = str(INSTALL_DIR)
    current = os.environ.get("PATH", "")
    if dotnet_bin.lower() in current.lower():
        logging.info("dotnet ist bereits im PATH.")
        return
    new_path = f"{current};{dotnet_bin}"
    logging.info(f"Füge dotnet-InstallDir dem PATH hinzu: {dotnet_bin}")
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation() -> None:
    """
    Prüft die Installation via 'dotnet --list-sdks' und 'fsi --version'.
    """
    try:
        sdks = subprocess.check_output([DOTNET_CMD, "--list-sdks"], text=True).strip()
        logging.info(f"Installierte .NET SDKs:\n{sdks}")
    except Exception as e:
        logging.error(f"Fehler bei '.NET SDK'-Prüfung: {e}")
        sys.exit(1)

    try:
        out = subprocess.check_output([FSI_CMD, "--version"], text=True).strip()
        logging.info(f"F# Interactive (fsi) Version: {out}")
    except Exception as e:
        logging.error(f"Fehler bei 'fsi'-Prüfung: {e}")
        sys.exit(1)

def main():
    logging.info("=== F# Installer (.NET SDK) gestartet ===")
    if os.name != "nt":
        logging.error("Dieses Skript funktioniert nur unter Windows.")
        sys.exit(1)

    # .NET SDK installieren, falls nicht vorhanden
    if not is_dotnet_installed():
        with tempfile.TemporaryDirectory() as td:
            script = Path(td) / "dotnet-install.ps1"
            download_install_script(script)
            run_install_script(script)
        update_path()
    else:
        logging.info(".NET SDK ist bereits installiert.")

    # F# Interactive prüfen
    if is_fsharp_available():
        logging.info("F# Interactive ist bereits verfügbar.")
    else:
        logging.error("F# Interactive (fsi) wurde nicht gefunden.")
        sys.exit(1)

    verify_installation()
    logging.info("=== F# Installation abgeschlossen ===")

if __name__ == "__main__":
    main()