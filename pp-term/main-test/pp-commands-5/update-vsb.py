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
import shutil


def setup_logging():
    """
    Konfiguriert das Logging-Framework für konsistente Log-Ausgaben.
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


def check_vs_installer() -> str:
    """
    Prüft, ob der Visual Studio Installer vorhanden ist, und gibt den Pfad zurueck.
    :return: Pfad zum vs_installer.exe oder leerer String
    """
    default_path = r"C:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\\vs_installer.exe"
    if shutil.which("vs_installer.exe"):
        return "vs_installer.exe"
    elif shutil.os.path.exists(default_path):
        return default_path
    else:
        logging.error("Visual Studio Installer wurde nicht gefunden.")
        return ""


def update_vs_buildtools(installer_path: str) -> int:
    """
    Startet das Update der Visual Studio Build Tools über den Installer.
    :param installer_path: Pfad zur vs_installer.exe
    :return: Exit-Code
    """
    cmd = [
        installer_path,
        "update",
        "--quiet",
        "--norestart"
    ]

    logging.info(f"Starte Visual Studio Build Tools Update mit: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        logging.info("Visual Studio Build Tools wurden erfolgreich aktualisiert.")
        logging.debug(f"Installer-Ausgabe:\n{result.stdout}")
        return result.returncode
    except subprocess.CalledProcessError as e:
        logging.error(f"Fehler beim Update der Build Tools (Exit-Code: {e.returncode}).")
        logging.error(f"Fehlermeldung:\n{e.stderr}")
        return e.returncode


def parse_args():
    parser = argparse.ArgumentParser(
        description="Script zum Aktualisieren der Visual Studio Build Tools"
    )
    parser.add_argument(
        '--check', action='store_true',
        help='Nur prüfen, ob der Visual Studio Installer vorhanden ist'
    )
    return parser.parse_args()


def main():
    setup_logging()
    user_name = getpass.getuser()
    logging.info(f"Ausführung durch Benutzer: {user_name}")

    args = parse_args()

    installer_path = check_vs_installer()
    if not installer_path:
        sys.exit(1)

    if args.check:
        logging.info("Nur Prüfung (--check) gewünscht. Beende.")
        sys.exit(0)

    exit_code = update_vs_buildtools(installer_path)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
