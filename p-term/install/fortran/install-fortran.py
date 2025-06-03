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
import subprocess
import logging
import tempfile
import shutil
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
GITHUB_API_LATEST = "https://api.github.com/repos/LKedward/quickstart-fortran/releases/latest"

def is_gfortran_installed() -> bool:
    """Prüft, ob 'gfortran' bereits im PATH verfügbar ist."""
    return shutil.which("gfortran") is not None

def fetch_latest_release() -> dict:
    """Holt über die GitHub-API das neueste Release und die Windows-Installer-URL."""
    logging.info("Ermittle neueste Quickstart-Fortran-Version über GitHub API…")
    req = Request(GITHUB_API_LATEST, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req) as resp:
            data = json.load(resp)
    except (HTTPError, URLError) as e:
        logging.error(f"Fehler beim Abruf der Release-API: {e}")
        sys.exit(1)

    version = data.get("tag_name", "").lstrip("v")
    asset_url = None
    asset_name = None
    for asset in data.get("assets", []):
        name = asset.get("name", "").lower()
        if name.endswith(".exe"):
            asset_url = asset["browser_download_url"]
            asset_name = asset.get("name")
            break

    if not version or not asset_url:
        logging.error("Konnte keinen Windows-Installer für Quickstart-Fortran finden.")
        sys.exit(1)

    logging.info(f"Gefundene Version: {version}, Installer: {asset_name}")
    return {"version": version, "url": asset_url, "filename": asset_name}

def download_installer(url: str, dest: Path):
    """Lädt den Installer herunter und protokolliert den Fortschritt."""
    logging.info(f"Starte Download von {url}")
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
                    logging.info(f"Download-Fortschritt: {pct:.1f}%")
        logging.info(f"Download abgeschlossen: {dest}")
    except (HTTPError, URLError) as e:
        logging.error(f"Download-Fehler: {e}")
        sys.exit(1)

def run_installer(installer_path: Path):
    """Führt den Installer aus."""
    logging.info(f"Starte Quickstart-Fortran-Installer: {installer_path}")
    try:
        subprocess.run([str(installer_path)], check=True)
        logging.info("Installation abgeschlossen.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation fehlgeschlagen: {e}")
        sys.exit(1)

def verify_installation():
    """Prüft die Installation via 'gfortran --version'."""
    try:
        out = subprocess.check_output(["gfortran", "--version"], text=True).strip()
        logging.info(f"GFortran erfolgreich installiert: {out}")
    except Exception as e:
        logging.error(f"Verifikation von GFortran fehlgeschlagen: {e}")
        sys.exit(1)

def main():
    logging.info("=== GFortran-Installer gestartet ===")
    if os.name != "nt":
        logging.error("Dieses Skript funktioniert nur unter Windows.")
        sys.exit(1)

    if is_gfortran_installed():
        logging.info("GFortran ist bereits installiert. Abbruch.")
        return

    info = fetch_latest_release()
    version = info["version"]
    url = info["url"]
    filename = info["filename"]

    with tempfile.TemporaryDirectory() as tmpdir:
        installer_path = Path(tmpdir) / filename
        download_installer(url, installer_path)
        run_installer(installer_path)

    verify_installation()
    logging.info("=== GFortran-Installation abgeschlossen ===")

if __name__ == "__main__":
    main()
