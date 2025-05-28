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


def is_tool_available(tool_name: str) -> bool:
    """
    Check if a given tool is installed and available in PATH.

    Args:
        tool_name (str): Name of the CLI tool to check.

    Returns:
        bool: True if tool is found, False otherwise.
    """
    return shutil.which(tool_name) is not None


def run_command(cmd: list) -> subprocess.CompletedProcess:
    """
    Execute a command and capture its output.

    Args:
        cmd (list): Command and arguments.

    Returns:
        subprocess.CompletedProcess: The result object.
    """
    logging.info(f"Executing: {' '.join(cmd)}")
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


def stream_subprocess(cmd: list) -> int:
    """
    Execute a subprocess, streaming stdout/stderr to logger.

    Args:
        cmd (list): Command and arguments.

    Returns:
        int: The subprocess exit code.
    """
    logging.info(f"Streaming command: {' '.join(cmd)}")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert process.stdout is not None
    for line in process.stdout:
        logging.info(line.strip())
    process.wait()
    return process.returncode


def run_rustup_update() -> int:
    return stream_subprocess(['rustup', 'update'])


def run_pip_update() -> int:
    pip_cmd = shutil.which('pip3') or shutil.which('pip')
    assert pip_cmd is not None

    # Upgrade pip
    result = run_command([pip_cmd, 'install', '--upgrade', 'pip'])
    logging.info(result.stdout)
    if result.returncode != 0:
        return result.returncode

    # List outdated packages
    result = run_command([pip_cmd, 'list', '--outdated', '--format=freeze'])
    logging.info(result.stdout)
    if result.returncode != 0:
        return result.returncode

    outdated = [line.split('==')[0] for line in result.stdout.splitlines() if '==' in line]
    if not outdated:
        logging.info("All Python packages are up to date.")
        return 0

    # Upgrade each package
    for pkg in outdated:
        code = stream_subprocess([pip_cmd, 'install', '--upgrade', pkg])
        if code != 0:
            return code
    return 0


def run_docker_update() -> int:
    result = run_command(['docker', 'images', '--format', '{{.Repository}}:{{.Tag}}'])
    logging.info(result.stdout)
    if result.returncode != 0:
        return result.returncode

    images = [line for line in result.stdout.splitlines() if line and '<none>' not in line]
    if not images:
        logging.info("No Docker images to update.")
        return 0

    for img in images:
        code = stream_subprocess(['docker', 'pull', img])
        if code != 0:
            return code
    return 0


def run_wsl_update() -> int:
    # Update WSL kernel
    code = stream_subprocess(['wsl', '--update'])
    if code != 0:
        return code

    # List installed distributions
    result = run_command(['wsl', '--list', '--quiet'])
    logging.info(result.stdout)
    if result.returncode != 0:
        return result.returncode

    distros = [distro.strip() for distro in result.stdout.splitlines() if distro.strip()]
    for distro in distros:
        code = stream_subprocess(['wsl', '--set-version', distro, 'latest'])
        if code != 0:
            logging.warning(f"Failed to upgrade distro {distro}, continuing.")
    return 0


def run_powershell_update() -> int:
    """
    Update key PowerShell modules: PowerShellGet and PackageManagement.

    Returns:
        int: 0 if successful, non-zero on first failure.
    """
    # Update PowerShellGet
    code = stream_subprocess(['powershell', '-Command', 'Update-Module -Name PowerShellGet -Force'])
    if code != 0:
        return code

    # Update PackageManagement
    code = stream_subprocess(['powershell', '-Command', 'Update-Module -Name PackageManagement -Force'])
    if code != 0:
        return code

    return 0


def main() -> None:
    configure_logging()
    user_name = getpass.getuser()
    logging.info(f"Executor: {user_name}")

    # Rustup
    if not is_tool_available('rustup'):
        logging.error("`rustup` not found. Skipping Rust update.")
    else:
        code = run_rustup_update()
        logging.info("Rustup update completed successfully." if code == 0 else f"Rustup update failed (exit {code}).")

    # Python pip
    if not is_tool_available('pip') and not is_tool_available('pip3'):
        logging.error("`pip` not found. Skipping Python package updates.")
    else:
        code = run_pip_update()
        logging.info("Python packages updated successfully." if code == 0 else f"Python update failed (exit {code}).")

    # Docker
    if not is_tool_available('docker'):
        logging.error("`docker` not found. Skipping Docker image updates.")
    else:
        code = run_docker_update()
        logging.info("Docker images updated successfully." if code == 0 else f"Docker update failed (exit {code}).")

    # WSL
    if not is_tool_available('wsl'):
        logging.error("`wsl` not found. Skipping WSL updates.")
    else:
        code = run_wsl_update()
        logging.info("WSL updated successfully." if code == 0 else f"WSL update failed (exit {code}).")

    # PowerShell
    if not is_tool_available('powershell'):
        logging.error("`powershell` not found. Skipping PowerShell module updates.")
    else:
        code = run_powershell_update()
        logging.info("PowerShell modules updated successfully." if code == 0 else f"PowerShell update failed (exit {code}).")

    sys.exit(0)


if __name__ == '__main__':
    main()
