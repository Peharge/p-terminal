@echo off

REM Englisch Peharge: This source code is released under the MIT License.
REM
REM Usage Rights:
REM The source code may be copied, modified, and adapted to individual requirements.
REM Users are permitted to use this code in their own projects, both for private and commercial purposes.
REM However, it is recommended to modify the code only if you have sufficient programming knowledge,
REM as changes could cause unintended errors or security risks.
REM
REM Dependencies and Additional Frameworks:
REM The code relies on the use of various frameworks and executes additional files.
REM Some of these files may automatically install further dependencies required for functionality.
REM It is strongly recommended to perform installation and configuration in an isolated environment
REM (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
REM
REM Disclaimer:
REM Use of the code is entirely at your own risk.
REM Peharge assumes no liability for damages, data loss, system errors, or other issues
REM that may arise directly or indirectly from the use, modification, or redistribution of the code.
REM
REM Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

REM Deutsch Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
REM
REM Nutzungsrechte:
REM Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
REM Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
REM Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
REM da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
REM
REM Abhängigkeiten und zusätzliche Frameworks:
REM Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
REM Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
REM Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
REM um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
REM
REM Haftungsausschluss:
REM Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
REM Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
REM die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
REM
REM Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

REM Français Peharge: Ce code source est publié sous la licence MIT.
REM
REM Droits d'utilisation:
REM Le code source peut être copié, édité et adapté aux besoins individuels.
REM Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
REM Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
REM car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
REM
REM Dépendances et frameworks supplémentaires:
REM Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
REM Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
REM Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
REM pour éviter d'éventuels conflits avec les installations de logiciels existantes.
REM
REM Clause de non-responsabilité:
REM L'utilisation du code est entièrement à vos propres risques.
REM Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
REM pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
REM
REM Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

setlocal EnableDelayedExpansion

:: Setze festes Arbeitsverzeichnis
set "PROJECT_PATH=C:\Users\%USERNAME%\p-terminal\p-term"
cd /d "%PROJECT_PATH%" || (
    echo [FEHLER] Projektverzeichnis nicht gefunden: "%PROJECT_PATH%"
    goto :Ende
)

echo =========================================
echo      Rust-Projekt-Setup (Batch-Skript)
echo =========================================

:: -----------------------------------------
:: 1) Rustup prüfen und ggf. installieren
:: -----------------------------------------
where rustup >nul 2>&1
if errorlevel 1 (
    echo [INFO] Rustup nicht gefunden. Installation wird gestartet...

    where curl >nul 2>&1
    if errorlevel 1 (
        echo [FEHLER] curl ist nicht installiert. Bitte curl installieren oder PowerShell verwenden.
        goto :Ende
    )

    echo [INFO] Lade rustup-init.exe herunter...
    curl -s -o "%PROJECT_PATH%\rustup-init.exe" https://win.rustup.rs
    if not exist "%PROJECT_PATH%\rustup-init.exe" (
        echo [FEHLER] Download von rustup-init.exe fehlgeschlagen.
        goto :Ende
    )

    echo [INFO] Führe rustup-Installer aus...
    "%PROJECT_PATH%\rustup-init.exe" -y
    if errorlevel 1 (
        echo [FEHLER] Rust-Installation über rustup ist fehlgeschlagen.
        goto :CleanupInstaller
    )

    echo [INFO] Rustup erfolgreich installiert.

:CleanupInstaller
    del "%PROJECT_PATH%\rustup-init.exe" >nul 2>&1
    set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"
) else (
    echo [INFO] Rustup ist bereits installiert.
)

:: -----------------------------------------
:: 2) Cargo prüfen
:: -----------------------------------------
where cargo >nul 2>&1
if errorlevel 1 (
    echo [WARNUNG] cargo nicht in PATH gefunden. Versuche PATH zu aktualisieren...
    set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"
    where cargo >nul 2>&1
    if errorlevel 1 (
        echo [FEHLER] cargo ist immer noch nicht erreichbar. Bitte Terminal neu starten oder neu einloggen.
        goto :Ende
    ) else (
        echo [INFO] cargo jetzt verfügbar.
    )
) else (
    echo [INFO] cargo ist vorhanden.
)

:: -----------------------------------------
:: 3) Projektpfad anzeigen
:: -----------------------------------------
echo [INFO] Projektverzeichnis: "%PROJECT_PATH%"

:: -----------------------------------------
:: 4) Build-Prozess starten
:: -----------------------------------------
echo ----------------------------------------
echo [SCHRITT] cargo build
echo ----------------------------------------
cargo build
if errorlevel 1 (
    echo [FEHLER] "cargo build" ist fehlgeschlagen.
    goto :Ende
)

:: -----------------------------------------
:: 5) Projekt starten
:: -----------------------------------------
echo ----------------------------------------
echo [SCHRITT] cargo run
echo ----------------------------------------
cargo run
if errorlevel 1 (
    echo [FEHLER] "cargo run" ist fehlgeschlagen.
    goto :Ende
)

echo =========================================
echo [ERFOLG] Alle Aufgaben erfolgreich ausgeführt.
echo =========================================

:Ende
echo.
pause
exit /b 0
