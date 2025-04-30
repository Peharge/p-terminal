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
import os

def check_and_install_winget():
    """Überprüft, ob winget installiert ist, und installiert es gegebenenfalls."""
    try:
        # Überprüfen, ob winget installiert ist
        subprocess.run(["winget", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("winget ist bereits installiert.")
    except subprocess.CalledProcessError:
        print("winget ist nicht installiert. Installiere winget...")
        install_winget()

def install_winget():
    """Installiert winget (Windows Package Manager)."""
    if sys.platform == "win32":
        try:
            # Versucht winget von Microsoft zu installieren
            subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser"], check=True)
            subprocess.run(["powershell", "-Command", "iwr https://aka.ms/install-winget.ps1 -OutFile install-winget.ps1"], check=True)
            subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Unrestricted -Scope CurrentUser"], check=True)
            subprocess.run(["powershell", "-Command", "powershell -ExecutionPolicy Bypass -File install-winget.ps1"], check=True)
            print("winget wurde erfolgreich installiert.")
        except subprocess.CalledProcessError as e:
            print(f"Fehler bei der Installation von winget: {e}")
            sys.exit(1)

def install_oh_my_posh():
    """Installiert OhMyPosh über winget."""
    try:
        # Installiert OhMyPosh
        print("Installiere OhMyPosh...")
        subprocess.run(["winget", "install", "JanDeDobbeleer.OhMyPosh"], check=True)
        print("OhMyPosh wurde erfolgreich installiert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Installation von OhMyPosh: {e}")
        sys.exit(1)

def initialize_oh_my_posh():
    """Initialisiert OhMyPosh für PowerShell mit dem angegebenen Konfigurationsdateipfad."""
    try:
        # Initialisiert OhMyPosh
        config_path = os.path.expanduser("~") + r"\AppData\Local\Programs\oh-my-posh\themes\jandedobbeleer.omp.json"
        command = f"oh-my-posh --init --shell pwsh --config {config_path} | Invoke-Expression"
        subprocess.run(["powershell", "-Command", command], check=True)
        print("OhMyPosh wurde erfolgreich initialisiert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Initialisierung von OhMyPosh: {e}")
        sys.exit(1)

def upgrade_oh_my_posh():
    """Aktualisiert OhMyPosh mit winget."""
    try:
        # Aktualisiert OhMyPosh
        print("Aktualisiere OhMyPosh...")
        subprocess.run(["winget", "upgrade", "JanDeDobbeleer.OhMyPosh"], check=True)
        print("OhMyPosh wurde erfolgreich aktualisiert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Aktualisierung von OhMyPosh: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Überprüft und installiert winget, falls erforderlich
    check_and_install_winget()

    # Installiert OhMyPosh
    install_oh_my_posh()

    # Initialisiert OhMyPosh
    initialize_oh_my_posh()

    # Aktualisiert OhMyPosh
    upgrade_oh_my_posh()

    print("Alle Schritte wurden erfolgreich ausgeführt.")
