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

import subprocess
import requests
import sys
import os
from datetime import datetime
from pathlib import Path

# Timestamp helper
def timestamp() -> str:
    """Returns current time formatted with milliseconds."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

# === Terminal color definitions ===
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

# GitHub repository
repo_url = "https://github.com/Peharge/p-terminal.git"
repo_name = "p-terminal"

def get_expected_directory() -> Path:
    """Returns the expected working directory based on the current username."""
    user_dir = Path.home()
    return user_dir / "p-terminal"

def is_correct_directory() -> bool:
    """Checks if the current working directory is the expected Git root."""
    expected_path = os.path.join(os.path.expanduser("~"), "p-terminal")
    current_path = os.path.abspath(os.getcwd())
    return os.path.normcase(current_path) == os.path.normcase(expected_path)

def get_latest_commits():
    """Fetches and displays the latest commits from the GitHub repository."""
    try:
        github_api_url = f"https://api.github.com/repos/Peharge/{repo_name}/commits"
        response = requests.get(github_api_url)
        response.raise_for_status()

        commits = response.json()
        print(f"\n[{timestamp()}] [INFO] Latest commits on GitHub:")
        for commit in commits[:5]:
            sha = commit['sha'][:7]
            message = commit['commit']['message']
            author = commit['commit']['author']['name']
            print(f"[{timestamp()}] [INFO] Commit {sha}: {message} ({magenta}Author: {author}{reset})")
    except requests.exceptions.RequestException as e:
        print(f"[{timestamp()}] [ERROR] Failed to retrieve commits: {e}")

def update_repo():
    """Runs git pull to update the repository."""
    try:
        print(f"\n[{timestamp()}] [INFO] Starting update...")
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"[{timestamp()}] {green}[PASS]{reset} Repository successfully updated!")
        else:
            print(f"[{timestamp()}] {red}[ERROR]{reset} Update failed:\n{result.stderr}")
    except Exception as e:
        print(f"[{timestamp()}] {red}[ERROR]{reset} Unexpected error: {e}")

def is_git_repo() -> bool:
    """Checks whether the current directory is a Git repository."""
    try:
        result = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True)
        return result.returncode == 0 and "true" in result.stdout.lower()
    except Exception:
        return False

def main():
    expected_path = os.path.join(os.path.expanduser("~"), "p-terminal")

    # Versuche, ins richtige Verzeichnis zu wechseln
    if os.path.exists(expected_path):
        os.chdir(expected_path)
    else:
        print(f"[{timestamp()}] [ERROR] The current directory must be: {expected_path}")
        sys.exit(1)

    print(f"\n{bold}Repository Information:\n-----------------------{reset}")
    print(f"[{timestamp()}] [INFO] Changed working directory to: {os.getcwd()}")

    # Prüfen, ob jetzt Git-Repo
    if not is_git_repo():
        print(f"[{timestamp()}] [ERROR] The current directory is not a Git repository!")
        sys.exit(1)

    # Git fetch usw. ...
    try:
        result = subprocess.run(["git", "fetch"], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"[{timestamp()}] [ERROR] Failed to fetch changes from remote!")
            print(result.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Error during git fetch: {e}")
        sys.exit(1)

    result = subprocess.run(["git", "status"], capture_output=True, text=True)
    if "Your branch is up to date" in result.stdout:
        print(f"[{timestamp()}] [INFO] The repository is already up to date.")
        sys.exit(0)

    show_commits = input("\nWant to see the latest commits on GitHub? [y/n]: ").strip().lower()
    if show_commits in {'y', 'yes'}:
        get_latest_commits()

    update = input("\nDo you want to update the repository now? [y/n]: ").strip().lower()
    if update in {'y', 'yes'}:
        update_repo()
    else:
        print(f"[{timestamp()}] {green}[PASS]{reset} Update canceled.")

if __name__ == "__main__":
    main()
