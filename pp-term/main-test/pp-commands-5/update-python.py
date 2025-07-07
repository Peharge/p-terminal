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
import sys
import logging
import getpass
import shutil

def configure_logging() -> None:
    """
    Configure the root logger to output timestamped messages to stdout with UTF-8 encoding.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s.%(msecs)03d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    try:
        sys.stdout.reconfigure(encoding='utf-8')  # Python 3.7+
    except AttributeError:
        pass

def is_rustup_available() -> bool:
    """
    Check if `rustup` is installed and available in PATH.

    Returns:
        bool: True if `rustup` is found, False otherwise.
    """
    return shutil.which('rustup') is not None


def run_rustup_update() -> int:
    """
    Execute `rustup update` and stream output to the logger.

    Returns:
        int: The return code of the `rustup` process.
    """
    command = ['rustup', 'update']
    logging.info(f"Running command: {' '.join(command)}")

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    assert process.stdout is not None
    for line in process.stdout:
        logging.info(line.strip())
    process.wait()
    return process.returncode


def is_pip_available() -> bool:
    """
    Check if `pip` is installed and available in PATH.

    Returns:
        bool: True if `pip` is found, False otherwise.
    """
    return shutil.which('pip') is not None or shutil.which('pip3') is not None


def run_pip_update() -> int:
    """
    Upgrade pip and all outdated packages.

    Returns:
        int: 0 if successful, non-zero otherwise.
    """
    pip_cmd = shutil.which('pip3') or shutil.which('pip')
    assert pip_cmd is not None

    # Upgrade pip itself first
    upgrade_pip_cmd = [pip_cmd, 'install', '--upgrade', 'pip']
    logging.info(f"Upgrading pip: {' '.join(upgrade_pip_cmd)}")
    result = subprocess.run(upgrade_pip_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    logging.info(result.stdout)
    if result.returncode != 0:
        return result.returncode

    # List outdated packages
    list_cmd = [pip_cmd, 'list', '--outdated', '--format=freeze']
    logging.info(f"Listing outdated packages: {' '.join(list_cmd)}")
    result = subprocess.run(list_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    logging.info(result.stdout)
    if result.returncode != 0:
        return result.returncode

    outdated = [line.split('==')[0] for line in result.stdout.splitlines() if '==' in line]
    if not outdated:
        logging.info("All packages are up to date.")
        return 0

    # Upgrade each package
    for pkg in outdated:
        cmd = [pip_cmd, 'install', '--upgrade', pkg]
        logging.info(f"Upgrading package: {pkg}")
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        assert proc.stdout is not None
        for line in proc.stdout:
            logging.info(line.strip())
        proc.wait()
        if proc.returncode != 0:
            return proc.returncode

    return 0


def main() -> None:
    configure_logging()
    user_name = getpass.getuser()
    logging.info(f"Executor: {user_name}")

    # Rustup update
    if not is_rustup_available():
        logging.error("`rustup` command not found in PATH. Please install Rustup first.")
    else:
        code = run_rustup_update()
        if code == 0:
            logging.info("Rustup update completed successfully.")
        else:
            logging.error(f"Rustup update failed with exit code {code}.")

    # Pip update
    if not is_pip_available():
        logging.error("`pip` command not found in PATH. Please ensure pip is installed.")
        sys.exit(1)
    pip_code = run_pip_update()
    if pip_code == 0:
        logging.info("Python packages update completed successfully.")
        sys.exit(0)
    else:
        logging.error(f"Python packages update failed with exit code {pip_code}.")
        sys.exit(pip_code)

if __name__ == '__main__':
    main()