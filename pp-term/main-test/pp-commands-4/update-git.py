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
import subprocess
import logging
import getpass
import argparse
import platform
import shutil


def setup_logging():
    """
    Configures the logging framework for consistent log output.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s.%(msecs)03d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    sys.stdout.reconfigure(encoding='utf-8')


def check_git_installed() -> bool:
    """
    Checks if 'git' is available in the PATH.
    :return: True if installed, otherwise False
    """
    try:
        subprocess.run(['git', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        logging.info("Git is installed.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        logging.error("Git is not installed or not in the PATH.")
        return False


def update_git(force: bool = False) -> int:
    """
    Updates Git depending on the operating system.
    :param force: Forces the update if possible.
    :return: Exit code of the update command
    """
    system = platform.system()
    if system == 'Linux':
        pkg_mgr = detect_linux_package_manager()
        cmd = [pkg_mgr, 'update'] if pkg_mgr != 'pacman' else [pkg_mgr, '-Sy']
        if pkg_mgr in ('apt', 'apt-get'):
            cmd += ['&&', pkg_mgr, 'install', '--only-upgrade', 'git']
        elif pkg_mgr == 'dnf':
            cmd += ['&&', pkg_mgr, 'upgrade', 'git']
        elif pkg_mgr == 'pacman':
            cmd += ['git']
    elif system == 'Darwin':  # macOS
        cmd = ['brew', 'upgrade', 'git']
    elif system == 'Windows':
        cmd = ['choco', 'upgrade', 'git', '-y']
    else:
        logging.error(f"Unknown operating system: {system}")
        return 1

    logging.info(f"Starting Git update with command: {' '.join(cmd)}")
    try:
        result = subprocess.run(' '.join(cmd), shell=True, check=True, text=True, capture_output=True)
        logging.info("Git was successfully updated.")
        logging.debug(f"Update output:\n{result.stdout}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        logging.error(f"Error while updating Git (Exit code: {e.returncode}).")
        logging.error(f"Error message:\n{e.stderr}")
        return e.returncode


def detect_linux_package_manager() -> str:
    """
    Detects the package manager used on Linux systems.
    Supports: apt, apt-get, dnf, pacman
    """
    for mgr in ('apt', 'apt-get', 'dnf', 'pacman'):
        if shutil.which(mgr):
            return mgr
    return 'apt'


def parse_args():
    parser = argparse.ArgumentParser(
        description="Script to update Git with logging"
    )
    parser.add_argument(
        '--force', '-f', action='store_true',
        help='Forces an update if supported'
    )
    parser.add_argument(
        '--check', action='store_true',
        help='Only checks if Git is installed'
    )
    return parser.parse_args()


def main():
    setup_logging()
    user_name = getpass.getuser()
    logging.info(f"Executing user: {user_name}")

    args = parse_args()
    if not check_git_installed():
        sys.exit(1)

    if args.check:
        logging.info("Aborted: Check only requested (--check).")
        sys.exit(0)

    exit_code = update_git(force=args.force)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
