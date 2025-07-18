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

REM Set variables
set USERNAME=%USERNAME%
set PYTHON_PATH=C:\Users\%USERNAME%\p-terminal\pp-term\.env\Scripts\python.exe
set SCRIPT_PATH_1=C:\Users\%USERNAME%\p-terminal\pp-term\update\update.py

:: Global Settings
set "SCRIPT_DIR=%~dp0"
set "LOGFILE=C:\Users\julia\p-terminal\pp-term\WSL_Diagnostics.log"
set "MAX_DRIFT=300"          & rem Maximum allowed time drift in seconds
set "PING_ADDR=8.8.8.8"      & rem Default ping target
set "TEST_DOMAIN=example.com"

REM Check if Python interpreter exists
if not exist "%PYTHON_PATH%" (
    call :Log ERROR "Python interpreter not found: %PYTHON_PATH%"
    exit /b 1
)

REM Check if script exists
if not exist "%SCRIPT_PATH_1%" (
    call :Log ERROR "Script not found: %SCRIPT_PATH_1%"
    exit /b 1
)

REM Execute the Python script
"%PYTHON_PATH%" "%SCRIPT_PATH_1%"

REM Output success message
echo.
call :Log INFO "The update Repository scripts have been executed."

REM Wait for user input before exiting
pause

:: Functions
:InitLog
    (echo [%DATE% %TIME%] [LOG INIT] Log created >"%LOGFILE%"
    ) 2>nul
    goto :eof

:Timestamp
    rem Set TS variable to timestamp YYYY-MM-DD HH:MM:SS.mmm
    for /F "tokens=* delims=" %%D in ('powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss.fff'"') do set "TS=%%D"
    goto :eof

:Log
    rem call :Log LEVEL Message
    setlocal EnableDelayedExpansion
    call :Timestamp
    set "LEVEL=%~1"
    shift
    set "MSG="
    :buildMsg
    if "%~1"=="" goto continueLog
    set "MSG=!MSG! %~1"
    shift
    goto buildMsg

:continueLog
    set "MSG=!MSG:~1!"  & rem entfernt führendes Leerzeichen
    echo [!TS!] [!LEVEL!] !MSG!
    >>"%LOGFILE%" echo [!TS!] [!LEVEL!] !MSG!
    endlocal
    goto :eof

:Run
    rem call :Run command arguments
    setlocal
    set "CMD=%*"
    rem echo [COMMAND] %CMD%
    >>"%LOGFILE%" echo [COMMAND] %CMD%
    cmd /C %CMD%
    endlocal
    goto :eof

:BlankLine
    echo.
    goto :eof

