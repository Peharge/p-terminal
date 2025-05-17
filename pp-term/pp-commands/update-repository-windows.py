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
import json
import subprocess
from datetime import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

# === Constants ===
BASE_DIR = os.path.join(os.path.expanduser("~"), "p-terminal", "pp-term", "update")
DATA_FILE = os.path.join(BASE_DIR, "last_update.json")
BATCH_FILE = os.path.join(BASE_DIR, "update-p-terminal-repository.bat")


def timestamp() -> str:
    """Returns the current time formatted with milliseconds"""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def read_last_update():
    """Reads the last saved date from the JSON file."""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("last_update")
    except (json.JSONDecodeError, IOError) as e:
        print(f"[{timestamp()}] [ERROR] Error reading update file: {e}")
    return None


def write_last_update():
    """Saves the current date into the JSON file."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        current_date = datetime.now().strftime("%d.%m.%Y")
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump({"last_update": current_date}, file)
        return current_date
    except IOError as e:
        print(f"[{timestamp()}] [ERROR] Error writing update file: {e}")
        return None


def prompt_for_update():
    """Asks the user whether to perform an update."""
    while True:
        choice = input("Would you like to perform an update? [y/n]: ").strip().lower()
        if choice in {"y", "yes"}:
            return True
        elif choice in {"n", "no"}:
            return False
        else:
            print(f"[{timestamp()}] [ERROR] Invalid input. Please enter 'y' or 'n'.")


def perform_update():
    """Performs the update by running the batch script."""
    if not os.path.exists(BATCH_FILE):
        print(f"[{timestamp()}] [ERROR] Batch file not found: {BATCH_FILE}")
        return

    if sys.platform != "win32":
        print(f"[{timestamp()}] [ERROR] Update script can only be executed on Windows.")
        return

    print(f"[{timestamp()}] [INFO] Starting update...")
    subprocess.run(BATCH_FILE, shell=True)
    print(f"[{timestamp()}] [INFO] Update completed.")
    write_last_update()


def main():
    title = "P-Terminal Repository Update (experimental):"
    line = "-" * len(title)

    print(f"\n{title}")
    print(f"{line}\n")
    print("Please note: This update function is experimental. Errors may occur.")
    print("We recommend using the following command instead:")
    print("git pull https://github.com/Peharge/p-terminal.git")
    print("If that's not possible, you can continue here...\n")

    print(f"[{timestamp()}] [INFO] Update data path: {DATA_FILE}")

    last_update = read_last_update()
    if last_update:
        print(f"[{timestamp()}] [INFO] Last update: {last_update}")
    else:
        print(f"[{timestamp()}] [INFO] No previous update date found.")

    if prompt_for_update():
        perform_update()
    else:
        print(f"[{timestamp()}] [INFO] Update aborted.")


if __name__ == "__main__":
    main()
