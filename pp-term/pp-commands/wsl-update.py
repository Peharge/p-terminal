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
import shlex
import traceback
from datetime import datetime

def timestamp() -> str:
    """Returns current time formatted with milliseconds."""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

def run_command(cmd: str) -> int:
    """Run a shell command, print detailed logs in your style, and return the exit code."""
    try:
        print(f"[{timestamp()}] [INFO] Executing command: {cmd}")
        args = shlex.split(cmd)
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print(f"[{timestamp()}] [SUCCESS] Command succeeded: {cmd}")
            if stdout.strip():
                print(f"[{timestamp()}] [INFO] Output:\n{stdout.strip()}")
        else:
            print(f"[{timestamp()}] [ERROR] Command failed (Return code {process.returncode}): {cmd}")
            if stderr.strip():
                print(f"[{timestamp()}] [ERROR] Error output:\n{stderr.strip()}")

        return process.returncode

    except Exception as e:
        print(f"[{timestamp()}] [ERROR] Exception while executing command '{cmd}': {e}")
        print(traceback.format_exc())
        return -1

def update_wsl_with_fallback():
    """Try updating WSL kernel normally; on failure, print instructions and try fallback."""
    ret = run_command("wsl --update")
    if ret != 0:
        print(f"[{timestamp()}] [ERROR] ❌ WSL update with 'wsl --update' failed!")
        print(f"[{timestamp()}] [ERROR] ❌ Step 2: Abort & Restart")
        print(f"[{timestamp()}] [ERROR] Please press Ctrl + C to abort the current process if it's still running.")
        print(f"[{timestamp()}] [ERROR] Then try running the following command manually or let this script try it automatically:")
        print(f"[{timestamp()}] [ERROR] wsl --update --web-download")
        print(f"[{timestamp()}] [ERROR] This command downloads the kernel update directly via the browser, bypassing the Microsoft Store.")

        # Try fallback automatically
        ret_fallback = run_command("wsl --update --web-download")
        if ret_fallback != 0:
            print(f"[{timestamp()}] [ERROR] ❌ The fallback 'wsl --update --web-download' also failed!")
            print(f"[{timestamp()}] [ERROR] Please try updating manually by downloading from: https://aka.ms/wsl2kernel")
        else:
            print(f"[{timestamp()}] [SUCCESS] ✅ WSL was successfully updated using the web-download fallback.")
    else:
        print(f"[{timestamp()}] [SUCCESS] ✅ WSL was successfully updated.")

if __name__ == "__main__":
    update_wsl_with_fallback()

    # Check WSL version, description printed inline in the print statement
    print(f"[{timestamp()}] [INFO] Executing command: wsl --version (Checking WSL version to verify installation and update status)")
    run_command("wsl --version")
