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

NODE_INDEX_JSON = "https://nodejs.org/dist/index.json"

def is_npm_installed() -> bool:
    """Prüft, ob 'npm' im PATH aufrufbar ist."""
    return shutil.which("npm") is not None

def get_latest_lts_node() -> dict:
    """
    Liest die Node.js-Dist-Index.json aus und findet die
    neueste LTS-Version für Windows x64 (MSI).
    """
    logging.info("Frage Node.js-Versionen ab: %s", NODE_INDEX_JSON)
    try:
        req = Request(NODE_INDEX_JSON, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req) as resp:
            versions = json.load(resp)
    except (HTTPError, URLError) as e:
        logging.error("Fehler beim Abruf der Node.js-Versionsliste: %s", e)
        sys.exit(1)

    for v in versions:
        # v["lts"] ist False oder ein String mit Codename, z.B. "Gallium"
        if v.get("lts"):
            version = v["version"]          # z.B. "v20.3.1"
            msi_name = f"node-{version}-x64.msi"
            url = f"https://nodejs.org/dist/{version}/{msi_name}"
            logging.info("Gefundene LTS-Version: %s", version)
            return {"version": version, "msi": msi_name, "url": url}

    logging.error("Keine LTS-Version in index.json gefunden.")
    sys.exit(1)

def download_file(url: str, dest: Path):
    """Lädt eine Datei von url nach dest mit Fortschritts-Log."""
    logging.info("Starte Download: %s", url)
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
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
                    logging.info("Download-Fortschritt: %.1f%%", pct)
        logging.info("Download abgeschlossen: %s", dest)
    except (HTTPError, URLError) as e:
        logging.error("Download-Fehler: %s", e)
        sys.exit(1)

def run_node_installer(msi_path: Path):
    """Installiert Node.js per MSI-Silent-Mode."""
    logging.info("Starte Node.js-Installer: %s", msi_path)
    # /qn = no UI, /norestart = kein automatischer Reboot
    cmd = ["msiexec", "/i", str(msi_path), "/qn", "/norestart"]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Node.js erfolgreich installiert.")
    except subprocess.CalledProcessError as e:
        logging.error("Node.js-Installation fehlgeschlagen (Exit-Code %d)", e.returncode)
        sys.exit(e.returncode)

def install_typescript():
    """Installiert TypeScript global via npm."""
    logging.info("Installiere TypeScript global via npm")
    cmd = ["npm", "install", "-g", "typescript"]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        logging.info("TypeScript global installiert.")
        logging.debug("npm-Ausgabe:\n%s", result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("TypeScript-Installation fehlgeschlagen (Exit-Code %d):\n%s", e.returncode, e.stderr)
        sys.exit(e.returncode)

def verify_tsc():
    """Validiert, dass 'tsc' (TypeScript-Compiler) verfügbar ist."""
    try:
        result = subprocess.run(["tsc", "--version"], check=True, capture_output=True, text=True)
        logging.info("tsc gefunden: %s", result.stdout.strip())
    except Exception as e:
        logging.error("tsc nicht gefunden oder Fehler: %s", e)
        sys.exit(1)

def main():
    logging.info("=== TypeScript-Installer gestartet ===")
    if os.name != "nt":
        logging.error("Dieses Skript läuft nur unter Windows.")
        sys.exit(1)

    # Schritt 1: npm prüfen
    if not is_npm_installed():
        logging.info("npm nicht gefunden. Installiere Node.js LTS...")
        info = get_latest_lts_node()
        with tempfile.TemporaryDirectory() as td:
            msi_path = Path(td) / info["msi"]
            download_file(info["url"], msi_path)
            run_node_installer(msi_path)
    else:
        logging.info("npm ist bereits installiert.")

    # Schritt 2: TypeScript installieren
    install_typescript()

    # Schritt 3: Verifikation
    verify_tsc()
    logging.info("=== TypeScript-Installation abgeschlossen ===")

if __name__ == "__main__":
    main()