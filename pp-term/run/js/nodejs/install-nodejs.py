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
import os
import shutil
import subprocess
import logging
import tempfile
import json
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

NODE_INDEX_URL = "https://nodejs.org/dist/index.json"


def is_node_installed() -> bool:
    """Prüft, ob Node.js (node) über den PATH aufgerufen werden kann."""
    return shutil.which("node") is not None


def fetch_latest_version() -> str:
    """
    Liest die Node.js Releases JSON und liefert die neueste stabile Version (erste Eintrag).
    Rückgabe im Format 'vX.Y.Z'.
    """
    logging.info(f"Hole Releases-Daten von {NODE_INDEX_URL}")
    try:
        req = Request(NODE_INDEX_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp:
            data = json.load(resp)
            if not data:
                raise ValueError("Leere Versionsliste erhalten.")
            latest = data[0]["version"]  # z.B. "v18.16.0"
            logging.info(f"Neueste Version ermittelt: {latest}")
            return latest
    except (HTTPError, URLError, ValueError) as e:
        logging.error(f"Fehler beim Abruf der Version: {e}")
        sys.exit(1)


def download_installer(version: str, dest_path: Path) -> None:
    """
    Lädt den Node.js Windows MSI-Installer für x64 herunter.
    URL: https://nodejs.org/dist/{version}/node-{version}-x64.msi
    """
    url = f"https://nodejs.org/dist/{version}/node-{version}-x64.msi"
    logging.info(f"Starte Download des Installers von {url}")
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as response, open(dest_path, "wb") as out_file:
            total = int(response.getheader('Content-Length', 0))
            downloaded = 0
            chunk_size = 8192
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
                downloaded += len(chunk)
                if total:
                    percent = downloaded * 100 / total
                    logging.info(f"Download-Fortschritt: {percent:.1f}%")
        logging.info(f"Download abgeschlossen: {dest_path}")
    except (HTTPError, URLError) as e:
        logging.error(f"Fehler beim Download: {e}")
        sys.exit(1)


def run_msi_installer(msi_path: Path) -> None:
    """
    Führt den MSI-Installer im Silent-Modus via msiexec aus.
    """
    logging.info(f"Starte Installation mit msiexec: {msi_path}")
    cmd = [
        "msiexec",
        "/i", str(msi_path),
        "/quiet",
        "/norestart"
    ]
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        logging.info("Node.js erfolgreich installiert.")
        logging.debug(f"msiexec stdout:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Installation fehlgeschlagen (Exit-Code {e.returncode}):\n{e.stderr}")
        sys.exit(e.returncode)


def ensure_node_available():
    """
    Prüft nach der Installation, ob 'node' im PATH ist.
    """
    if is_node_installed():
        logging.info("Node.js steht nun zur Verfügung.")
    else:
        logging.warning("Node.js nicht im PATH gefunden. Bitte Terminal neu starten oder PATH überprüfen.")


def main():
    logging.info("=== Node.js Installer gestartet ===")
    if is_node_installed():
        logging.info("Node.js ist bereits installiert. Beende Prozess.")
        return

    version = fetch_latest_version()
    with tempfile.TemporaryDirectory() as tmpdir:
        msi_file = Path(tmpdir) / f"node-{version}-x64.msi"
        download_installer(version, msi_file)
        run_msi_installer(msi_file)

    ensure_node_available()
    logging.info("=== Prozess abgeschlossen ===")


if __name__ == "__main__":
    if os.name != "nt":
        logging.error("Dieses Skript läuft nur unter Windows.")
        sys.exit(1)
    main()
