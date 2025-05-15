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

setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul

:: Config
set "USERNAME=%USERNAME%"
set "LOGFILE=C:\Users\%USERNAME%\p-terminal\pp-term\WSL_Diagnostics.log"
set "PYTHON_EXE=C:\Users\%USERNAME%\p-terminal\pp-term\.env\Scripts\python.exe"
set "SCRIPT_PATH=C:\Users\%USERNAME%\p-terminal\pp-term\pp-term-4.py"
set "WORKDIR=C:\Users\%USERNAME%"

:: Change to target working directory
cd /d "%WORKDIR%"

:: CPU affinity mask
for /f "tokens=2 delims==" %%A in ('wmic cpu get NumberOfLogicalProcessors /value ^| find "NumberOfLogicalProcessors"') do set /A "LOGPROC=%%A"
if %LOGPROC% GTR 64 set "LOGPROC=64"
setlocal EnableDelayedExpansion
set "AFF_MASK=0"
for /L %%I in (0,1,%LOGPROC%-1) do (
    set /A "AFF_MASK|=(1<<%%I)"
)
endlocal & set "AFFINITY=%AFF_MASK%"

:: Launch Python script with full CPU and high priority
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$p = Start-Process -FilePath '%PYTHON_EXE%' -ArgumentList '%SCRIPT_PATH%' -WorkingDirectory '%WORKDIR%' -NoNewWindow -Wait -PassThru; ^
   $p.PriorityClass = 'High'; ^
   $p.ProcessorAffinity = 0x%AFFINITY%" 2>>"%LOGFILE%"

if errorlevel 1 (
    call :Log ERROR "❌ Failed to start Python script"
    exit /B 1
)

exit /B 0

:: Logging Functions
:Timestamp
for /F "usebackq tokens=* delims=" %%D in (`powershell -NoProfile -Command "Get-Date -Format \"yyyy-MM-dd HH:mm:ss.fff\""`) do set "TS=%%D"
goto :eof

:Log
setlocal EnableDelayedExpansion
call :Timestamp
set "LEVEL=%~1"
shift
set "MSG="
:buildMsg
if "%~1"=="" goto logIt
set "MSG=!MSG! %~1"
shift
goto buildMsg
:logIt
set "MSG=!MSG:~1!"
echo [!TS!] [!LEVEL!] !MSG! >>"%LOGFILE%"
echo [!TS!] [!LEVEL!] !MSG!
endlocal
goto :eof
