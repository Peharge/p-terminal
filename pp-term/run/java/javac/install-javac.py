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

#!/usr/bin/env python3
# install_javac.py

import sys
import os
import shutil
import subprocess
import logging
import tempfile
import json
import zipfile
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

# Logging konfigurieren
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

# Adoptium API für Temurin JDK 17 LTS
API_URL = (
    "https://api.adoptium.net/v3/assets/latest/17/ga"
    "?architecture=x64&image_type=jdk&jvm_impl=hotspot&os=windows&vendor=eclipse"
)
INSTALL_DIR = Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Java"


def is_javac_installed() -> bool:
    """Prüft, ob javac über den PATH aufgerufen werden kann."""
    return shutil.which("javac") is not None


def fetch_asset_info() -> dict:
    """
    Ruft JSON von Adoptium API ab und liefert das erste Asset-Objekt.
    """
    logging.info(f"Rufe Asset-Daten ab von {API_URL}")
    try:
        req = Request(API_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp:
            data = json.load(resp)
            if not data:
                raise ValueError("Leere Antwort von Adoptium API")
            asset = data[0]
            pkg = asset["binary"]["package"]
            logging.info(f"Gefundene Version: {asset['release_name']}")
            return {"version": asset["release_name"], "link": pkg["link"], "type": pkg["name"].split('.')[-1]}
    except (HTTPError, URLError, ValueError) as e:
        logging.error(f"Fehler beim Abruf der Asset-Info: {e}")
        sys.exit(1)


def download_package(link: str, dest_path: Path) -> None:
    logging.info(f"Downloade Paket von {link}")
    try:
        req = Request(link, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as response, open(dest_path, "wb") as out_file:
            total = int(response.getheader('Content-Length', 0))
            downloaded = 0
            chunk_size = 8192
            while chunk := response.read(chunk_size):
                out_file.write(chunk)
                downloaded += len(chunk)
                if total:
                    percent = downloaded * 100 / total
                    logging.info(f"Download: {percent:.1f}%")
        logging.info(f"Download abgeschlossen: {dest_path}")
    except (HTTPError, URLError) as e:
        logging.error(f"Download-Fehler: {e}")
        sys.exit(1)


def install_from_zip(zip_path: Path, version: str) -> None:
    target = INSTALL_DIR / version
    logging.info(f"Entpacke JDK nach {target}")
    with zipfile.ZipFile(zip_path, 'r') as zin:
        zin.extractall(target)
    bin_dir = next(target.glob('*/bin'), None)
    if bin_dir:
        path_update = str(bin_dir)
        logging.info(f"Füge {path_update} zur PATH-Variable hinzu")
        subprocess.run(["setx", "PATH", f"%PATH%;{path_update}"], check=False)
        logging.info("Bitte starten Sie ein neues Terminal, damit PATH wirksam wird.")
    else:
        logging.warning("bin-Verzeichnis nicht gefunden, PATH nicht aktualisiert.")


def main():
    logging.info("=== Java JDK Installer gestartet ===")
    if is_javac_installed():
        logging.info("javac ist bereits installiert. Abbruch.")
        return

    asset = fetch_asset_info()
    with tempfile.TemporaryDirectory() as tmpdir:
        file_name = f"jdk-{asset['version']}.{asset['type']}"
        pkg_path = Path(tmpdir) / file_name
        download_package(asset['link'], pkg_path)
        if pkg_path.suffix.lower() == ".msi":
            logging.info("Führe MSI-Installer aus")
            subprocess.run(["msiexec", "/i", str(pkg_path), "/quiet", "/norestart"], check=True)
        elif pkg_path.suffix.lower() in ['.zip', '.gz']:
            install_from_zip(pkg_path, asset['version'])
        else:
            logging.error(f"Unbekannter Pakettyp: {pkg_path.suffix}")
            sys.exit(1)

    if is_javac_installed():
        logging.info("javac steht jetzt zur Verfügung.")
    else:
        logging.warning("javac nicht gefunden. Bitte PATH prüfen.")
    logging.info("=== Prozess abgeschlossen ===")

if __name__ == "__main__":
    if os.name != "nt":
        logging.error("Dieses Skript läuft nur unter Windows.")
        sys.exit(1)
    main()
