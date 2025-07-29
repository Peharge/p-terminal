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

# -*- coding: utf-8 -*-
"""
Installationsskript für die Visual Studio C++ Build Tools Umgebung.
Dieses Skript ermittelt das Projektverzeichnis (basierend auf dem aktuellen Benutzer) und
erstellt darin den Ordner "peharge-cpp-compiler". In diesem Ordner wird nach erfolgreichem
Test der Visual Studio Umgebung (über vcvarsall.bat und cl.exe) ein Batch-Skript abgelegt,
das die Umgebung initialisiert und ein Beispiel-Kompilierungskommando ausführt.
"""

from datetime import datetime

def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

print("""
WARNING: It is recommended to install Visual Studio C++ Build Tools
from the official Microsoft website:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

This script is unofficial and may pose security risks.
Use at your own risk!

Do you really want to proceed with the installation of Visual Studio C++ Build Tools? [y/n]:
""", end='')

choice = input().strip().lower()
if choice != 'y':
    print(f"[{timestamp()}] [INFO] Installation aborted by user.")
    exit(0)

# Hier kann der Installationscode für Visual Studio C++ Build Tools folgen
print(f"[{timestamp()}] [INFO] Proceeding with Visual Studio C++ Build Tools installation...")

import os
import sys
import subprocess
import traceback
import getpass
import platform
import shutil
import logging
from pathlib import Path

log_path = Path(__file__).parent / "peharge-compiler.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_path, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

def find_vcvarsall():
    """
    Recursively searches for the 'vcvarsall.bat' file required to initialize the Visual Studio
    development environment.

    Returns:
        str: Full path to 'vcvarsall.bat' or None if not found.
    """
    possible_paths = [
        os.environ.get("VSINSTALLDIR", ""),
        os.path.join(os.environ.get("ProgramFiles(x86)", ""), "Microsoft Visual Studio"),
        os.path.join(os.environ.get("ProgramFiles", ""), "Microsoft Visual Studio"),
    ]
    for base in possible_paths:
        if not base or not os.path.exists(base):
            continue
        for root, dirs, files in os.walk(base):
            if "vcvarsall.bat" in files:
                path_found = os.path.join(root, "vcvarsall.bat")
                logging.info("Found vcvarsall.bat: %s", path_found)
                return path_found
    return None

def write_logfile(target_dir, vcvarsall_path):
    """
    Writes a log file with information about the detected Visual Studio environment.

    Args:
        target_dir (str): Target directory where the log file will be placed.
        vcvarsall_path (str): Path to the 'vcvarsall.bat' file.
    """
    log_file = os.path.join(target_dir, "compiler_installed.txt")
    try:
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("Visual Studio C++ Build Tools detected and ready.\n")
            f.write(f"vcvarsall.bat path: {vcvarsall_path}\n")
        logging.info("Installation status logged in: %s", log_file)
    except Exception as e:
        logging.warning("Could not write log file: %s", e)

def verify_compiler(vcvarsall_path, temp_dir):
    """
    Creates a temporary test C++ file and compiles it using cl.exe to verify
    that the Visual Studio environment is properly set up.

    Args:
        vcvarsall_path (str): Path to the Visual Studio environment initializer.
        temp_dir (str): Temporary directory for the compilation test.

    Returns:
        bool: True if the test succeeded, otherwise False.
    """
    logging.info("Testing compiler availability...")
    test_cpp = os.path.join(temp_dir, "test.cpp")
    exe_output = os.path.join(temp_dir, "test.exe")

    # Create test CPP file
    try:
        with open(test_cpp, "w", encoding="utf-8") as f:
            f.write("#include <iostream>\nint main() { std::cout << \"Hello from cl.exe!\" << std::endl; return 0; }")
    except Exception as e:
        logging.error("Error creating test file: %s", e)
        return False

    # Create batch script to initialize environment and compile the test file
    bat_script = os.path.join(temp_dir, "compile_test.bat")
    try:
        with open(bat_script, "w", encoding="utf-8") as f:
            # "x64" is the target here; adjust as needed (e.g., x86)
            f.write(f'"{vcvarsall_path}" x64 && cl.exe /EHsc "{test_cpp}" /Fe"{exe_output}"\n')
    except Exception as e:
        logging.error("Error creating batch script: %s", e)
        return False

    try:
        result = subprocess.run(
            ['cmd', '/c', bat_script],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='cp850',  # Windows console encoding
            errors='replace',
            check=False
        )
        logging.info("Output of the compilation test:\n%s", result.stdout)
    except Exception as e:
        logging.error("Error running compilation test: %s", e)
        return False

    if os.path.exists(exe_output):
        logging.info("Compilation successful. cl.exe works perfectly.")
        return True
    else:
        logging.error(
            "Compilation failed. Please ensure that Visual Studio C++ Build Tools are correctly installed.")
        return False

def create_compiler_folder(target_dir, vcvarsall_path):
    """
    Creates a batch file in the specified target directory ('peharge-cpp-compiler') that
    initializes the Visual Studio environment and runs a sample compile command.

    Args:
        target_dir (str): Directory where the "compiler" will be set up.
        vcvarsall_path (str): Path to the 'vcvarsall.bat' file.
    """
    os.makedirs(target_dir, exist_ok=True)

    batch_file = os.path.join(target_dir, "build_peharge.bat")
    try:
        with open(batch_file, "w", encoding="utf-8") as f:
            f.write("@echo off\n")
            f.write(f'call "{vcvarsall_path}" x64\n')
            f.write("echo Visual Studio Compiler Environment enabled.\n")
            # Example: Navigate to project directory and compile a specific source file
            f.write('cd /d "%~dp0\\..\\..\\peharge"\n')
            f.write("echo Start compiling the peharge project...\n")
            # Placeholder: Adapt the cl.exe call to your project structure
            f.write('cl.exe /EHsc main.cpp /Fe:peharge_project.exe\n')
            f.write("pause\n")
        logging.info("Batch file created for the compiler: %s", batch_file)
    except Exception as e:
        logging.error("Error creating compiler batch file: %s", e)

def main():
    """
    Main function controlling the workflow:
      - Determine the project directory
      - Search for the Visual Studio environment
      - Test the compiler
      - Create the 'peharge-cpp-compiler' folder with a batch file
        that can be used to compile the peharge project
      - Write a log file in the target directory
    """
    try:
        if platform.system() != "Windows":
            raise EnvironmentError("This installation script is intended for Windows only.")

        username = getpass.getuser()
        project_root = os.path.join("C:\\Users", username, "p-terminal", "pp-term")
        compiler_dir = os.path.join(project_root, "peharge-cpp-compiler")
        os.makedirs(compiler_dir, exist_ok=True)
        logging.info("Project directory: %s", project_root)

        temp_dir = os.path.join(project_root, "vs_test")
        os.makedirs(temp_dir, exist_ok=True)

        logging.info("Searching for the Visual Studio C++ development environment...")
        vcvarsall_path = find_vcvarsall()
        if not vcvarsall_path:
            raise FileNotFoundError("Visual Studio environment could not be found."
                                    " Please make sure that Visual Studio with the C++ Build Tools is installed.")

        if verify_compiler(vcvarsall_path, temp_dir):
            write_logfile(compiler_dir, vcvarsall_path)
            create_compiler_folder(compiler_dir, vcvarsall_path)
            logging.info("Visual Studio C++ Build Tools successfully detected and tested.")
        else:
            raise Exception("The compilation test failed.")

        shutil.rmtree(temp_dir, ignore_errors=True)
        logging.info("Temporary files have been removed.")

    except Exception as e:
        logging.error("An error occurred during installation:")
        logging.error(str(e))
        logging.error("Stacktrace:\n%s", traceback.format_exc())
        logging.error("Please make sure that Visual Studio is installed with the required C++ components.")
        sys.exit(1)

if __name__ == "__main__":
    main()
