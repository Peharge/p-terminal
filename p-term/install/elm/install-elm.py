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
from pathlib import Path

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

def is_tool_installed(cmd: str) -> bool:
    """Prüft, ob ein CLI-Tool im PATH verfügbar ist."""
    return shutil.which(cmd) is not None

def install_elm_via_npm():
    """Installiert Elm global via npm."""
    logging.info("Installiere Elm global via npm...")
    try:
        subprocess.run(["npm", "install", "-g", "elm"], check=True)
        logging.info("Elm wurde erfolgreich installiert.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Fehler bei der Elm-Installation: {e}")
        sys.exit(1)

def get_npm_global_prefix() -> str:
    """Ermittelt das npm-Global-Prefix (Pfad zu globalen Binärdateien)."""
    try:
        prefix = subprocess.check_output(
            ["npm", "config", "get", "prefix"],
            text=True
        ).strip()
        return prefix
    except subprocess.CalledProcessError as e:
        logging.error(f"Konnte npm prefix nicht ermitteln: {e}")
        sys.exit(1)

def update_path(npm_prefix: str):
    """
    Fügt das Verzeichnis mit den globalen npm-Binärdateien dem System-PATH hinzu.
    Das ist typischerweise das npm_prefix-Verzeichnis selbst unter Windows.
    """
    bin_path = npm_prefix
    current = os.environ.get("PATH", "")
    if bin_path.lower() in current.lower():
        logging.info("npm global prefix ist bereits im PATH.")
        return
    new_path = f"{current};{bin_path}"
    logging.info(f"Füge npm global prefix dem PATH hinzu: {bin_path}")
    # setx schreibt den neuen PATH in die Registry (für neue Terminals)
    subprocess.run(f'setx PATH "{new_path}"', shell=True, check=False)

def verify_installation():
    """Prüft die Elm-Installation via 'elm --version'."""
    try:
        out = subprocess.check_output(["elm", "--version"], text=True).strip()
        logging.info(f"Elm erfolgreich installiert, Version: {out}")
    except Exception as e:
        logging.error(f"Verifikation von Elm fehlgeschlagen: {e}")
        sys.exit(1)

def main():
    logging.info("=== Elm-Installer gestartet ===")
    if os.name != "nt":
        logging.error("Dieses Skript funktioniert nur unter Windows.")
        sys.exit(1)

    # Prüfe Node.js/npm
    if not is_tool_installed("node") or not is_tool_installed("npm"):
        logging.error("Node.js und npm werden benötigt. Bitte vorher installieren.")
        sys.exit(1)
    else:
        logging.info("Node.js und npm sind installiert.")

    # Elm installieren, falls nicht vorhanden
    if is_tool_installed("elm"):
        logging.info("Elm ist bereits installiert. Abbruch.")
    else:
        install_elm_via_npm()

    # npm global prefix ermitteln und in PATH aufnehmen
    npm_prefix = get_npm_global_prefix()
    update_path(npm_prefix)

    # Verifikation
    verify_installation()
    logging.info("=== Elm-Installation abgeschlossen ===")

if __name__ == "__main__":
    main()