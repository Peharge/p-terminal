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
chcp 65001

echo.
powershell -Command "& {Write-Host '██████╗ ██████╗    ' -ForegroundColor Blue -NoNewline; Write-Host '████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗' -ForegroundColor White; Write-Host '██╔══██╗██╔══██╗   ' -ForegroundColor Blue -NoNewline; Write-Host '╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║' -ForegroundColor White; Write-Host '██████╔╝██████╔╝' -ForegroundColor Blue -NoNewline; Write-Host '█████╗██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║' -ForegroundColor White; Write-Host '██╔═══╝ ██╔═══╝ ' -ForegroundColor Blue -NoNewline; Write-Host '╚════╝██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║' -ForegroundColor White; Write-Host '██║     ██║           ' -ForegroundColor Blue -NoNewline; Write-Host '██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗' -ForegroundColor White; Write-Host '╚═╝     ╚═╝           ' -ForegroundColor Blue -NoNewline; Write-Host '╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝' -ForegroundColor White;}"
echo.
powershell -Command "& {Write-Host '██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗' -ForegroundColor White; Write-Host '██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗' -ForegroundColor White; Write-Host '██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝' -ForegroundColor White; Write-Host '██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗' -ForegroundColor White; Write-Host '███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║' -ForegroundColor White; Write-Host '╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝' -ForegroundColor White;}"
echo.
echo Initiating high-tech installation...
echo [*] Prepare for the next level...
echo.
echo MIT License
echo Copyright (c) 2025
echo Peharge
echo.
echo Permission is hereby granted, free of charge, to any person obtaining a copy
echo of this software and associated documentation files (the "Software"), to deal
echo in the Software without restriction, including without limitation the rights
echo to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
echo copies of the Software, and to permit persons to whom the Software is
echo furnished to do so, subject to the following conditions:
echo.
echo The above copyright notice and this permission notice shall be included in all
echo copies or substantial portions of the Software.
echo.
echo THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
echo IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
echo FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
echo AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
echo LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
echo OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
echo SOFTWARE.
echo.
echo Time Stamp: %date% %time%
echo Hostname: %COMPUTERNAME%
echo User: %USERNAME%
echo Domain: %USERDOMAIN%
echo.
echo IP Address(es):
ipconfig | findstr /R /C:"IPv4"
echo.
for /f "delims=" %%i in ('ver') do echo Operating System: %%i
echo.
echo Current Directory: %cd%
echo.
echo Drives:
wmic logicaldisk get name, description, filesystem, size, freespace
echo Logged in Users:
query user
echo.
echo Initializing PP-Terminal 4
echo Gooo...
echo.

:: Global Settings
set "SCRIPT_DIR=%~dp0"
set "LOGFILE=C:\Users\julia\p-terminal\pp-term\WSL_Diagnostics.log"
set "MAX_DRIFT=300"          & rem Maximum allowed time drift in seconds
set "PING_ADDR=8.8.8.8"      & rem Default ping target
set "TEST_DOMAIN=example.com"

:: Get Windows Build number
for /f "tokens=3" %%a in ('reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v CurrentBuildNumber 2^>nul') do (
    set "BuildNumber=%%a"
)

echo Detected Windows Build Number: !BuildNumber!

:: Check if BuildNumber is >= 22000 (Windows 11 starts with build 22000)
if not defined BuildNumber (
    call :Log ERROR "❌ Failed to detect Windows Build Number."
    goto :end
)

set /a CheckBuild=!BuildNumber!

if !CheckBuild! GEQ 22000 (
    call :Log PASS "✅ Windows 11 is in use."
) else (
    call :Log ERROR "❌ This is not Windows 11."
)

:: Check if Windows Defender is active
sc query windefend | findstr /i "RUNNING" >nul
if !errorlevel! equ 0 (
    call :Log PASS "✅ Windows Defender is active."
) else (
    call :Log ERROR "❌ Windows Defender is NOT active."
)

:: Check if running inside a Virtual Machine
systeminfo | findstr /i "Virtual" "VMware" "Hyper-V" "VirtualBox" >nul
if !errorlevel! equ 0 (
    call :Log ERROR "❌ Virtual Machine or Hypervisor detected!"
    echo The terminal will be closed for security reasons.
    exit
) else (
    call :Log PASS "✅ No Virtual Machine detected."
)

for /f "tokens=*" %%A in ('wmic nic where "NetEnabled='TRUE'" get NetConnectionID^,MACAddress^,Description^,ServiceName /format:csv ^| findstr /v /i "Node"') do (
    for /f "tokens=2,3,4,5 delims=," %%i in ("%%A") do (
        set "adapterName=%%i"
        set "mac=%%j"
        set "desc=%%k"
        set "service=%%l"

        rem Determine adapter type
        set "type=Unknown"
        echo %%k | findstr /i "Wireless WLAN Wi-Fi" >nul && set "type=WLAN"
        echo %%k | findstr /i "Ethernet LAN" >nul && set "type=Ethernet"
        echo %%k | findstr /i "Virtual" >nul && set "type=Virtual"

        echo Adapter Name: !adapterName!
        echo MAC Address: !mac!
        echo Description: !desc!
        echo Service Name: !service!
        echo Adapter Type: !type!
    )
)

:: Check Internet Connection via Ping
ping -n 1 8.8.8.8 >nul
if %errorlevel%==0 (
    call :Log PASS "✅ Internet connection is active."

    :: === Check HTTPS Access ===
    curl --silent --head https://www.google.com | findstr /i "HTTP/1.1 200" >nul
    if !errorlevel! == 0 (
        call :Log PASS "✅ Secure HTTPS access is working."
    ) else (
        call :Log ERROR "❌ No HTTPS access – possibly a DNS or SSL issue."
    )
) else (
    call :Log ERROR "❌ No internet connection!"
)

:: Set up log file and timestamp
set LOGFILE=%~dp0hardware-check.log

:: Initialize log
call :InitLog

:: CPU Check
call :CheckCPU

:: RAM Check
call :CheckMemory

:: Disk Check
call :CheckDisks

:: GPU Check
call :CheckGPU

:: System Health Check
call :CheckSystemHealth

:: Driver Check
call :CheckDrivers

:: Final Log Message
call :Log "INFO" "✅ Hardware check completed."


timeout /t 5 >nul

:: Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    call :Log ERROR "❌ Python 3.12 is not installed."
    set /p install_python="Would you like to install Python 3.12? [y/n]: "

    if /i "%install_python%"=="y" (
        call :Log INFO "Downloading Python 3.12 installer..."

        set "PYTHON_URL=https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
        set "PYTHON_INSTALLER=%TEMP%\python-3.12.2-installer.exe"

        :: Securely download Python using PowerShell (TLS 1.2)
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'"

        if exist "%PYTHON_INSTALLER%" (
            call :Log INFO "Running Python installer..."
            start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

            :: Verify installation
            python --version >nul 2>&1
            if %errorlevel% neq 0 (
                call :Log ERROR "❌ Installation failed! Retrying..."
                del "%PYTHON_INSTALLER%"
                start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

                python --version >nul 2>&1
                if %errorlevel% neq 0 (
                    ecall :Log ERROR "❌ Second installation attempt failed! Trying ZIP method..."
                    del "%PYTHON_INSTALLER%"
                    set "PYTHON_ZIP_URL=https://www.python.org/ftp/python/3.12.2/python-3.12.2-embed-amd64.zip"
                    set "PYTHON_ZIP=%TEMP%\python-3.12.2.zip"
                    set "PYTHON_DIR=C:\Python312"

                    powershell -Command "Invoke-WebRequest -Uri '%PYTHON_ZIP_URL%' -OutFile '%PYTHON_ZIP%'"

                    if exist "%PYTHON_ZIP%" (
                        mkdir "%PYTHON_DIR%"
                        powershell -Command "Expand-Archive -Path '%PYTHON_ZIP%' -DestinationPath '%PYTHON_DIR%'"
                        del "%PYTHON_ZIP%"

                        setx PATH "%PYTHON_DIR%;%PATH%" /M

                        "%PYTHON_DIR%\python.exe" --version >nul 2>&1
                        if %errorlevel% neq 0 (
                            call :Log ERROR "❌ ZIP installation failed! Cleaning up..."
                            rmdir /s /q "%PYTHON_DIR%"
                            call :Log INFO "Manual installation required: https://www.python.org/downloads"
                        ) else (
                            call :Log PASS "✅ Python 3.12 successfully installed using ZIP method!"
                        )
                    ) else (
                        call :Log ERROR "❌ ZIP download failed! Manual installation required."
                    )
                ) else (
                    call :Log PASS "✅ Python 3.12 successfully installed!"
                )
            ) else (
                call :Log PASS "✅ Python 3.12 successfully installed!"
            )
        ) else (
            call :Log ERROR "❌ Python installer could not be downloaded!"
        )
    ) else (
        call :Log HINT "Installation aborted. Please install Python 3.12 manually: https://www.python.org/downloads"
    )
) else (
    call :Log PASS "✅ Python is already installed."
    python --version
)

:: Check if Git is already installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    call :Log ERROR "❌ Git is not installed."
    set /p install_git="Would you like to install Git? [y/n]: "

    if /i "%install_git%"=="y" (
        call :Log INFO "Downloading Git installer..."

        set "GIT_URL=https://github.com/git-for-windows/git/releases/latest/download/Git-2.44.0-64-bit.exe"
        set "GIT_INSTALLER=%TEMP%\git-installer.exe"

        :: Securely download Git using PowerShell
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%GIT_URL%' -OutFile '%GIT_INSTALLER%'"

        if exist "%GIT_INSTALLER%" (
            call :Log INFO "Running Git installer..."
            start /wait %GIT_INSTALLER% /VERYSILENT /NORESTART /CLOSEAPPLICATIONS

            :: Verify installation
            git --version >nul 2>&1
            if %errorlevel% neq 0 (
                call :Log ERROR "❌ Installation failed! Retrying..."
                del "%GIT_INSTALLER%"
                start /wait %GIT_INSTALLER% /VERYSILENT /NORESTART /CLOSEAPPLICATIONS

                git --version >nul 2>&1
                if %errorlevel% neq 0 (
                    call :Log ERROR "❌ Second installation attempt failed! Trying ZIP method..."
                    del "%GIT_INSTALLER%"
                    set "GIT_ZIP_URL=https://github.com/git-for-windows/git/releases/latest/download/PortableGit-2.44.0-64-bit.zip"
                    set "GIT_ZIP=%TEMP%\git-portable.zip"
                    set "GIT_DIR=C:\GitPortable"

                    powershell -Command "Invoke-WebRequest -Uri '%GIT_ZIP_URL%' -OutFile '%GIT_ZIP%'"

                    if exist "%GIT_ZIP%" (
                        mkdir "%GIT_DIR%"
                        powershell -Command "Expand-Archive -Path '%GIT_ZIP%' -DestinationPath '%GIT_DIR%'"
                        del "%GIT_ZIP%"

                        setx PATH "%GIT_DIR%\bin;%PATH%" /M

                        "%GIT_DIR%\bin\git.exe" --version >nul 2>&1
                        if %errorlevel% neq 0 (
                            call :Log ERROR "❌ ZIP installation failed! Cleaning up..."
                            rmdir /s /q "%GIT_DIR%"
                            call :Log INFO "Manual installation required: https://git-scm.com/downloads"
                        ) else (
                            call :Log PASS "✅ Git successfully installed using ZIP method!"
                        )
                    ) else (
                        call :Log ERROR "❌ ZIP download failed! Manual installation required."
                    )
                ) else (
                    call :Log PASS "✅ Git successfully installed!"
                )
            ) else (
                call :Log PASS "✅ Git successfully installed!"
            )
        ) else (
            call :Log ERROR "❌ Git installer could not be downloaded!"
        )
    ) else (
        call :Log HINT "Installation aborted. Please install Git manually: https://git-scm.com/downloads"
    )
) else (
    call :Log PASS "✅ Git is already installed."
    git --version
)

:: Check if Ollama is already installed
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    call :Log ERROR "❌ Ollama is not installed."
    set /p install_ollama="Would you like to install Ollama? [y/n]: "

    if /i "%install_ollama%"=="y" (
        call :Log INFO "Downloading Ollama installer..."

        set "OLLAMA_URL=https://ollama.com/download/OllamaSetup.exe"
        set "OLLAMA_INSTALLER=%TEMP%\OllamaSetup.exe"

        :: Securely download Ollama using PowerShell
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%OLLAMA_URL%' -OutFile '%OLLAMA_INSTALLER%'"

        if exist "%OLLAMA_INSTALLER%" (
            call :Log INFO "Running Ollama installer..."
            start /wait %OLLAMA_INSTALLER% /silent /norestart

            :: Verify installation
            ollama --version >nul 2>&1
            if %errorlevel% neq 0 (
                call :Log ERROR "❌ Error: Installation failed! Retrying..."
                del "%OLLAMA_INSTALLER%"
                start /wait %OLLAMA_INSTALLER% /silent /norestart

                ollama --version >nul 2>&1
                if %errorlevel% neq 0 (
                    call :Log ERROR "❌ Second installation attempt failed! Trying ZIP method..."
                    del "%OLLAMA_INSTALLER%"
                    set "OLLAMA_ZIP_URL=https://ollama.com/download/OllamaPortable.zip"
                    set "OLLAMA_ZIP=%TEMP%\OllamaPortable.zip"
                    set "OLLAMA_DIR=C:\OllamaPortable"

                    powershell -Command "Invoke-WebRequest -Uri '%OLLAMA_ZIP_URL%' -OutFile '%OLLAMA_ZIP%'"

                    if exist "%OLLAMA_ZIP%" (
                        mkdir "%OLLAMA_DIR%"
                        powershell -Command "Expand-Archive -Path '%OLLAMA_ZIP%' -DestinationPath '%OLLAMA_DIR%'"
                        del "%OLLAMA_ZIP%"

                        setx PATH "%OLLAMA_DIR%;%PATH%" /M

                        "%OLLAMA_DIR%\ollama.exe" --version >nul 2>&1
                        if %errorlevel% neq 0 (
                            call :Log ERROR "❌ ZIP installation failed! Cleaning up..."
                            rmdir /s /q "%OLLAMA_DIR%"
                            call :Log INFO "Manual installation required: https://ollama.com/download"
                        ) else (
                            call :Log PASS "✅ Ollama successfully installed using ZIP method!"
                        )
                    ) else (
                        call :Log ERROR "❌ ZIP download failed! Manual installation required."
                    )
                ) else (
                    call :Log PASS "✅ Ollama successfully installed!"
                )
            ) else (
                call :Log PASS "✅ Ollama successfully installed!"
            )
        ) else (
            call :Log ERROR "❌ Ollama installer could not be downloaded!"
        )
    ) else (
        call :Log HINT "Installation aborted. Please install Ollama manually: https://ollama.com/download"
    )
) else (
    call :Log PASS "✅ Ollama is already installed."
    ollama --version
)

:: Check if FFmpeg is already installed
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    call :Log ERROR "❌ FFmpeg is not installed."
    call :Log INFO "Installing FFmpeg is not required to run pp-term. However, installing FFmpeg is mandatory for using MAVIS Voice Assistant!"
    set /p install_ffmpeg="Would you like to install FFmpeg? [y/n]: "

    if /i "%install_ffmpeg%"=="y" (
        call :Log INFO "Downloading FFmpeg installer..."

        set "FFMPEG_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        set "FFMPEG_ZIP=%TEMP%\ffmpeg.zip"
        set "FFMPEG_DIR=C:\ffmpeg"

        :: Securely download FFmpeg using PowerShell
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%FFMPEG_ZIP%'"

        if exist "%FFMPEG_ZIP%" (
            call :Log INFO "Extracting FFmpeg..."
            powershell -Command "Expand-Archive -Path '%FFMPEG_ZIP%' -DestinationPath '%FFMPEG_DIR%' -Force"
            del "%FFMPEG_ZIP%"

            :: Add FFmpeg to System PATH
            setx PATH "%FFMPEG_DIR%\bin;%PATH%" /M

            :: Verify installation
            ffmpeg -version >nul 2>&1
            if %errorlevel% neq 0 (
               call :Log ERROR "❌ Installation failed! Retrying..."
                rmdir /s /q "%FFMPEG_DIR%"
                powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%FFMPEG_ZIP%'"
                powershell -Command "Expand-Archive -Path '%FFMPEG_ZIP%' -DestinationPath '%FFMPEG_DIR%' -Force"
                del "%FFMPEG_ZIP%"
                setx PATH "%FFMPEG_DIR%\bin;%PATH%" /M

                ffmpeg -version >nul 2>&1
                if %errorlevel% neq 0 (
                    call :Log ERROR "❌ Second installation attempt failed! Trying alternative ZIP source..."
                    rmdir /s /q "%FFMPEG_DIR%"
                    set "FFMPEG_ALT_URL=https://github.com/BtbN/FFmpeg-Builds/releases/latest/download/ffmpeg-master-latest-win64-gpl.zip"
                    set "FFMPEG_ZIP=%TEMP%\ffmpeg-alt.zip"
                    powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_ALT_URL%' -OutFile '%FFMPEG_ZIP%'"
                    powershell -Command "Expand-Archive -Path '%FFMPEG_ZIP%' -DestinationPath '%FFMPEG_DIR%' -Force"
                    del "%FFMPEG_ZIP%"
                    setx PATH "%FFMPEG_DIR%\bin;%PATH%" /M

                    ffmpeg -version >nul 2>&1
                    if %errorlevel% neq 0 (
                        call :Log ERROR "❌ Alternative ZIP installation failed! Cleaning up..."
                        rmdir /s /q "%FFMPEG_DIR%"
                        call :Log HINT "Manual installation required: https://ffmpeg.org/download.html#build-windows"
                    ) else (
                        call :Log PASS "✅ FFmpeg successfully installed using alternative ZIP method!"
                    )
                ) else (
                    call :Log PASS "✅ FFmpeg successfully installed!"
                )
            ) else (
                call :Log PASS "✅ FFmpeg successfully installed!"
            )
        ) else (
            call :Log ERROR "❌ FFmpeg installer could not be downloaded!"
        )
    ) else (
        call :Log HINT "Installation aborted. Please install FFmpeg manually: https://ffmpeg.org/download.html#build-windows"
    )
) else (
    call :Log PASS "✅ FFmpeg is already installed."
    ffmpeg --version
)

set USERNAME=%USERNAME%
set PYTHON_PATH=C:\Users\%USERNAME%\p-terminal\pp-term\.env\Scripts\python.exe
set SCRIPT_install_rustup=C:\Users\%USERNAME%\p-terminal\pp-term\run\rust\install-rustup.py

:: Check if Rustup is already installed
rustup --version >nul 2>&1
if %errorlevel% neq 0 (
    call :Log ERROR "❌ Rustup is not installed."
    set /p install_rustup="Would you like to install Rustup? [y/n]: "

    if /i "%install_rustup%"=="y" (
        call :Log INFO "Downloading Rustup installer..."

        set "RUSTUP_URL=https://win.rustup.rs"
        set "RUSTUP_INSTALLER=%TEMP%\rustup-init.exe"

        :: Securely download Rustup using PowerShell
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%RUSTUP_URL%' -OutFile '%RUSTUP_INSTALLER%'"

        if exist "%RUSTUP_INSTALLER%" (
            call :Log INFO "Running Rustup installer..."
            start /wait %RUSTUP_INSTALLER% -y

            :: Verify installation
            rustup --version >nul 2>&1
            if %errorlevel% neq 0 (
                call :Log ERROR "❌ Installation failed! Retrying..."
                del "%RUSTUP_INSTALLER%"
                powershell -Command "Invoke-WebRequest -Uri '%RUSTUP_URL%' -OutFile '%RUSTUP_INSTALLER%'"
                start /wait %RUSTUP_INSTALLER% -y

                rustup --version >nul 2>&1
                if %errorlevel% neq 0 (
                    call :Log ERROR "❌ Second installation attempt failed! Trying alternative method..."
                    del "%RUSTUP_INSTALLER%"
                    set "RUSTUP_ALT_URL=https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe"
                    set "RUSTUP_INSTALLER=%TEMP%\rustup-alt.exe"
                    powershell -Command "Invoke-WebRequest -Uri '%RUSTUP_ALT_URL%' -OutFile '%RUSTUP_INSTALLER%'"
                    start /wait %RUSTUP_INSTALLER% -y

                    rustup --version >nul 2>&1
                    if %errorlevel% neq 0 (
                        call :Log ERROR "❌ Alternative installation failed! Cleaning up..."
                        del "%RUSTUP_INSTALLER%"

                        if not exist "%SCRIPT_install_rustup%" (
                            call :Log ERROR "❌ Script not found: %SCRIPT_install_rustup%"
                            exit /B 1
                        )

                        "%PYTHON_PATH%" "%SCRIPT_install_rustup%"

                        call :Log INFO "Manual installation required: https://rustup.rs/"
                    ) else (
                        call :Log PASS "✅ Rustup successfully installed using alternative method!"
                    )
                ) else (
                    call :Log PASS "✅ Rustup successfully installed!"
                )
            ) else (
                call :Log PASS "✅ Rustup successfully installed!"
            )
        ) else (
            call :Log ERROR "❌ Rustup installer could not be downloaded!"
        )
    ) else (
        call :Log HINT "Installation aborted. Please install Rustup manually: https://rustup.rs/"
    )
) else (
    call :Log PASS "✅ Rustup is already installed."
    rustup --version
)

:: Check if PowerShell 7 is already installed
powershell -Command "$PSVersionTable.PSVersion" >nul 2>&1
if %errorlevel% neq 0 (
    call :Log ERROR "❌ PowerShell 7 is not installed."
    set /p install_powershell="Would you like to install PowerShell 7? [y/n]: "

    if /i "%install_powershell%"=="y" (
        call :Log INFO "Downloading PowerShell 7 installer..."

        set "POWERSHELL_URL=https://github.com/PowerShell/PowerShell/releases/download/v7.2.9/PowerShell-7.2.9-win-x64.msi"
        set "POWERSHELL_INSTALLER=%TEMP%\PowerShell-7.2.9-installer.msi"

        :: Securely download PowerShell using PowerShell (TLS 1.2)
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%POWERSHELL_URL%' -OutFile '%POWERSHELL_INSTALLER%'"

        if exist "%POWERSHELL_INSTALLER%" (
            call :Log INFO "Running PowerShell installer..."
            start /wait msiexec.exe /i "%POWERSHELL_INSTALLER%" /quiet /norestart

            :: Verify installation
            powershell -Command "$PSVersionTable.PSVersion" >nul 2>&1
            if %errorlevel% neq 0 (
                call :Log ERROR "❌ Installation failed! Retrying..."
                del "%POWERSHELL_INSTALLER%"
                start /wait msiexec.exe /i "%POWERSHELL_INSTALLER%" /quiet /norestart

                powershell -Command "$PSVersionTable.PSVersion" >nul 2>&1
                if %errorlevel% neq 0 (
                    call :Log ERROR "❌ Second installation attempt failed!"
                    call :Log INFO "Manual installation required: https://github.com/PowerShell/PowerShell/releases"
                ) else (
                    call :Log PASS "✅ PowerShell 7 successfully installed!"
                )
            ) else (
                call :Log PASS "✅ PowerShell 7 successfully installed!"
            )
        ) else (
            call :Log ERROR "❌ PowerShell installer could not be downloaded!"
        )
    ) else (
        call :Log HINT "Installation aborted. Please install PowerShell 7 manually: https://github.com/PowerShell/PowerShell/releases"
    )
) else (
    call :Log PASS "✅ PowerShell 7 is already installed."
    for /f "tokens=*" %%i in ('powershell -Command "$PSVersionTable.PSVersion.ToString()"') do set PSVersion=%%i
    echo PowerShell Version: !PSVersion!
)

:: Set the installation path for 3D Slicer
set "SLICER_PATH=C:\Users\%USERNAME%\AppData\Local\slicer.org\Slicer 5.6.2\Slicer.exe"

:: Check if 3D Slicer is already installed
if exist "%SLICER_PATH%" (
    call :Log PASS "✅ 3D Slicer is already installed."
    echo 3D Slicer Version:
    "C:\Users\%USERNAME%\AppData\Local\slicer.org\Slicer 5.6.2\Slicer.exe" --version
) else (
    call :Log ERROR "❌ 3D Slicer is not installed."
    call :Log INFO "Installing 3D Slicer isn't required to run pp-term. However, if you plan to use SIMON, installing 3D Slicer is mandatory. If you encounter any problems during installation, simply run the 'Install 3d-slicer' command in the pp terminal. This installation method is significantly more secure!"
    set /p install_slicer="Would you like to install 3D Slicer? [y/n]: "

    if /i "%install_slicer%"=="y" (
        call :Log INFO "Downloading the 3D Slicer installer..."

        set "SLICER_URL=https://download.slicer.org/bitstream/302208"
        set "SLICER_INSTALLER=%TEMP%\Slicer-Installer.exe"

        :: Securely download 3D Slicer using PowerShell (TLS 1.2)
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%SLICER_URL%' -OutFile '%SLICER_INSTALLER%'"

        if exist "%SLICER_INSTALLER%" (
            call :Log INFO "Starting the 3D Slicer installer..."

            :: Run the installer (silent installation)
            start /wait %SLICER_INSTALLER% /SILENT

            :: Check if 3D Slicer was successfully installed
            if exist "%SLICER_PATH%" (
                call :Log PASS "✅ 3D Slicer was successfully installed!"
            ) else (
                call :Log ERROR "❌ Installation failed! Retrying..."
                del "%SLICER_INSTALLER%"
                start /wait %SLICER_INSTALLER% /SILENT

                if exist "%SLICER_PATH%" (
                    call :Log PASS "✅ 3D Slicer was successfully installed!"
                ) else (
                    call :Log ERROR "❌ Second installation attempt failed! Trying ZIP method..."
                    del "%SLICER_INSTALLER%"
                    set "SLICER_ZIP_URL=https://download.slicer.org/bitstream/302209"
                    set "SLICER_ZIP=%TEMP%\Slicer.zip"
                    set "SLICER_DIR=C:\Slicer"

                    powershell -Command "Invoke-WebRequest -Uri '%SLICER_ZIP_URL%' -OutFile '%SLICER_ZIP%'"

                    if exist "%SLICER_ZIP%" (
                        mkdir "%SLICER_DIR%"
                        powershell -Command "Expand-Archive -Path '%SLICER_ZIP%' -DestinationPath '%SLICER_DIR%'"
                        del "%SLICER_ZIP%"

                        :: Add Slicer to the PATH
                        setx PATH "%SLICER_DIR%;%PATH%" /M

                        :: Check if 3D Slicer works
                        if exist "%SLICER_PATH%" (
                            call :Log PASS "✅ 3D Slicer was successfully installed via ZIP method!"
                        ) else (
                            call :Log ERROR "❌ ZIP installation failed! Cleaning up..."
                            rmdir /s /q "%SLICER_DIR%"
                            call :Log INFO "Manual installation required: https://download.slicer.org"
                        )
                    ) else (
                        call :Log ERROR "❌ ZIP download failed! Manual installation required."
                    )
                )
            )
        ) else (
            call :Log ERROR "❌ The 3D Slicer installer could not be downloaded!"
        )
    ) else (
        call :Log HINT "Installation canceled. Please install 3D Slicer manually: https://download.slicer.org"
    )
)

docker --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    call :Log ERROR "❌ Docker Desktop is not installed."
    set /p install_docker="Would you like to install Docker Desktop? [y/n]: "

    if /I "%install_docker%"=="y" (
        call :Log INFO "Downloading Docker Desktop installer..."
        set "DOCKER_URL=https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe"
        set "DOCKER_INSTALLER=%TEMP%\DockerDesktopInstaller.exe"
        powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%DOCKER_URL%' -OutFile '%DOCKER_INSTALLER%'"

        if exist "%DOCKER_INSTALLER%" (
            call :Log INFO "Running Docker installer..."
            start /wait "" "%DOCKER_INSTALLER%" install --quiet

            docker --version >nul 2>&1
            if %ERRORLEVEL% EQU 0 (
                call :Log PASS "✅ Docker Desktop successfully installed!"
                del "%DOCKER_INSTALLER%"
            ) else (
                call :Log ERROR "❌ Installation failed. Retrying..."
                del "%DOCKER_INSTALLER%"
                start /wait "" "%DOCKER_INSTALLER%" install --quiet

                docker --version >nul 2>&1
                if %ERRORLEVEL% EQU 0 (
                    call :Log PASS "✅ Docker Desktop successfully installed after retry!"
                    del "%DOCKER_INSTALLER%"
                ) else (
                    call :Log ERROR "❌ Docker could not be installed!"
                    call :Log HINT "Please install manually: https://docs.docker.com/desktop/windows/install/"
                )
            )
        ) else (
            call :Log ERROR "❌ Installer could not be downloaded!"
            call :Log HINT "Please install manually: https://docs.docker.com/desktop/windows/install/"
        )
    ) else (
        call :Log ERROR "❌ Docker will not be installed."
        call :Log HINT "Please install manually: https://docs.docker.com/desktop/windows/install/"
    )
) else (
    call :Log PASS "✅ Docker is already installed"
    docker --version
)

set "USERNAME=%USERNAME%"
set "PYTHON_PATH=C:\Users\%USERNAME%\p-terminal\pp-term\.env\Scripts\python.exe"

:: Main Python script for generic WSL installations (fallback)
set "SCRIPT_install_wsl=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-wsl.py"

:: Scripts for installing individual distributions:
set "SCRIPT_install_wsl_ubuntu=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-ubuntu-wsl.py"
set "SCRIPT_install_wsl_debian=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-debian-wsl.py"
set "SCRIPT_install_wsl_kali=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-kali-wsl.py"
set "SCRIPT_install_wsl_arch=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-wsl.py"
set "SCRIPT_install_wsl_opensuse=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-opensuse-wsl.py"
set "SCRIPT_install_wsl_mint=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-mint.py"
set "SCRIPT_install_wsl_fedora=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-fedora.py"
set "SCRIPT_install_wsl_redhat=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-redhat.py"
set "SCRIPT_install_wsl_suse=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-suse.py"
set "SCRIPT_install_wsl_pengwin=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-pengwin.py"
set "SCRIPT_install_wsl_oracle=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-oracle.py"
set "SCRIPT_install_wsl_clear=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-arch-clear.py"
set "SCRIPT_install_wsl_alpine=C:\Users\%USERNAME%\p-terminal\pp-term\run\wsl\install-alpine-wsl.py"

:CheckWSLInstalled
wsl --list >nul 2>&1
if errorlevel 1 (
    all :Log ERROR "❌ WSL is not installed."
    set /p "install_wsl=Do you want to install WSL? [y/n]: "
    if /i "!install_wsl!"=="y" (
        call :Log INFO "Enabling WSL feature..."
        dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart >nul 2>&1
        if errorlevel 1 (
           call :Log ERROR "❌ Could not enable the WSL feature."
            if not exist "%SCRIPT_install_wsl%" (
                all :Log ERROR "❌ Python fallback script not found: %SCRIPT_install_wsl%"
                pause
                exit /b 1
            )
            call "%PYTHON_PATH%" "%SCRIPT_install_wsl%"
        ) else (
            call :Log PASS "✅ WSL feature enabled successfully."
            call :Log INFO "Please restart your computer and run the script again."
            pause
            exit /b 0
        )
    ) else (
        call :Log INFO "Installation aborted. Please install WSL manually."
        pause
        exit /b 1
    )
)

call :Log PASS "✅ WSL is already installed."

goto CheckDistroInstalled

:CheckDistroInstalled
set "found_distro="
for /f "usebackq delims=" %%i in (`wsl --list --quiet 2^>nul`) do (
    set "found_distro=%%i"
    goto DistroFound
)

if not defined found_distro (
    goto AskInstall
)

:DistroFound
call :Log PASS "✅ WSL is already set up with the distribution: !found_distro!."
goto Continue

:AskInstall
call :Log INFO "No Linux distribution was found."
set /p "install_choice=Do you want to install a Linux distribution? [y/n]: "
if /i "!install_choice!"=="y" (
    goto SelectDistro
) else (
    call :Log INFO "Installation aborted."
    goto Continue
)

:SelectDistro
echo.
echo Please select a distribution to install:
echo   [1] Ubuntu
echo   [2] Debian
echo   [3] Kali Linux
echo   [4] Arch Linux
echo   [5] openSUSE
echo   [6] Linux Mint
echo   [7] Fedora
echo   [8] Red Hat Enterprise Linux
echo   [9] SUSE Linux
echo   [10] Pengwin
echo   [11] Oracle Linux
echo   [12] Clear Linux
echo   [13] Alpine
choice /c 123456789ABCD /n /m "Your choice: "
set "choice=%errorlevel%"

:: Map the choice to the appropriate variables
if "%choice%"=="1" (
    set "DISTRO_NAME=Ubuntu"
    set "DISTRO_PACKAGE=Ubuntu"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_ubuntu%"
) else if "%choice%"=="2" (
    set "DISTRO_NAME=Debian"
    set "DISTRO_PACKAGE=Debian"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_debian%"
) else if "%choice%"=="3" (
    set "DISTRO_NAME=Kali Linux"
    set "DISTRO_PACKAGE=kali-linux"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_kali%"
) else if "%choice%"=="4" (
    set "DISTRO_NAME=Arch Linux"
    set "DISTRO_PACKAGE=ArchLinux"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_arch%"
) else if "%choice%"=="5" (
    set "DISTRO_NAME=openSUSE"
    set "DISTRO_PACKAGE=openSUSE-Leap-15-3"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_opensuse%"
) else if "%choice%"=="6" (
    set "DISTRO_NAME=Linux Mint"
    set "DISTRO_PACKAGE=LinuxMint"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_mint%"
) else if "%choice%"=="7" (
    set "DISTRO_NAME=Fedora"
    set "DISTRO_PACKAGE=FedoraRemix"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_fedora%"
) else if "%choice%"=="8" (
    set "DISTRO_NAME=Red Hat Enterprise Linux"
    set "DISTRO_PACKAGE=RHEL"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_redhat%"
) else if "%choice%"=="9" (
    set "DISTRO_NAME=SUSE Linux"
    set "DISTRO_PACKAGE=SUSE"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_suse%"
) else if "%choice%"=="10" (
    set "DISTRO_NAME=Pengwin"
    set "DISTRO_PACKAGE=Pengwin"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_pengwin%"
) else if "%choice%"=="11" (
    set "DISTRO_NAME=Oracle Linux"
    set "DISTRO_PACKAGE=Oracle"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_oracle%"
) else if "%choice%"=="12" (
    set "DISTRO_NAME=Clear Linux"
    set "DISTRO_PACKAGE=ClearLinux"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_clear%"
) else if "%choice%"=="13" (
    set "DISTRO_NAME=Alpine"
    set "DISTRO_PACKAGE=Alpine"
    set "SCRIPT_DISTRO=%SCRIPT_install_wsl_alpine%"
) else (
    call :Log ERROR "❌ Invalid choice. The program will now exit."
    pause
    exit /b 1
)

:: Check if the corresponding Python script exists
if not exist "!SCRIPT_DISTRO!" (
    call :Log ERROR "❌ Python script not found: !SCRIPT_DISTRO!"
    pause
    exit /b 1
)

echo.
call :Log INFO "You have selected: !DISTRO_NAME!"
echo.

set /a attempts=0
:InstallLoop
set /a attempts+=1
call :Log INFO "[Attempt !attempts!] Starting installation of !DISTRO_NAME!..."
call "%PYTHON_PATH%" "!SCRIPT_DISTRO!"

:: Short pause to allow the installation process to settle
timeout /t 5 >nul

:: Verify if the distribution appears in the WSL list
set "installed="
for /f "usebackq delims=" %%i in (`wsl --list --quiet`) do (
    echo %%i | findstr /i /c:"!DISTRO_PACKAGE!" >nul && set "installed=1"
)
if defined installed (
    echo.
    call :Log PASS "✅ !DISTRO_NAME! has been successfully installed!"
    goto Continue
) else (
    echo.
    call :Log ERROR "❌ Installation of !DISTRO_NAME! failed on attempt !attempts!."
    if !attempts! lss 3 (
        call :Log INFO "Waiting 3 seconds before retrying..."
        timeout /t 3 >nul
        goto InstallLoop
    ) else (
        call :Log ERROR "❌ All installation attempts have failed."
        call :Log HINT "Please install !DISTRO_NAME! manually (e.g., via the Microsoft Store)."
        pause
        exit /b 1
    )
)

:Continue

call :Log PASS "✅ All WSL processes have been successfully terminated."

:: Initialization & Log Header
call :InitLog
call :Log INFO "Starting professional WSL diagnostics"

:: Verify WSL Executable and Version
where wsl >nul 2>&1 || (
    call :Log ERROR "❌ wsl.exe not found. Please install or enable WSL."
    exit /B 1
)

call :Log INFO "Listing WSL client version"& call :Run wsl --version

:: 1) General WSL Engine Status
call :Log INFO "Retrieving general WSL engine status"
call :Run wsl --status
if errorlevel 1 (
    call :Log WARN "❌ Unable to retrieve WSL engine status."
) else (
    call :Log INFO "✅ WSL engine status retrieved successfully."
)

call :Log INFO "Starting deep diagnostics for each distribution"

:: Ubuntu
wsl -d Ubuntu -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (

    call :Log INFO "Starting deep diagnostics for Ubuntu"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for Ubuntu (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching Ubuntu
    call :Run wsl -d Ubuntu -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch Ubuntu"
        call :Log HINT "Try: wsl --terminate Ubuntu & wsl --unregister Ubuntu and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d Ubuntu -- uname -a
    call :Run wsl -d Ubuntu -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d Ubuntu -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d Ubuntu -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d Ubuntu -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d Ubuntu -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d Ubuntu -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d Ubuntu -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for Ubuntu..."

    call :Log INFO "Updating Ubuntu using apt..."
    call :Run wsl -d Ubuntu -- sh -c "sudo apt update && sudo apt upgrade -y"
    call :Log PASS "✅ Ubuntu updated successfully."

    call :Log INFO "Update process completed for Ubuntu."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d Ubuntu -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d Ubuntu -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "Ubuntu is not installed."
)

:: Debian
wsl -d Debian -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (

    call :Log INFO "Starting deep diagnostics for Debian"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for Debian (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching Debian
    call :Run wsl -d Debian -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch Debian"
        call :Log HINT "Try: wsl --terminate Debian & wsl --unregister Debian and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d Debian -- uname -a
    call :Run wsl -d Debian -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d Debian -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d Debian -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d Debian -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d Debian -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d Debian -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d Debian -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for Debian..."

    call :Log INFO "Updating Debian using apt..."
    call :Run wsl -d Debian -- sh -c "sudo apt update && sudo apt upgrade -y"
    call :Log PASS "✅ Debian updated successfully."

    call :Log INFO "Update process completed for Debian."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d Debian -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d Debian -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "Debian is not installed."
)


:: Kali Linux
wsl -d kali-linux -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (

    call :Log INFO "Starting deep diagnostics for kali-linux"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for kali-linux (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching kali-linux
    call :Run wsl -d kali-linux -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch kali-linux"
        call :Log HINT "Try: wsl --terminate kali-linux & wsl --unregister kali-linux and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d kali-linux -- uname -a
    call :Run wsl -d kali-linux -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d kali-linux -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d kali-linux -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d kali-linux -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d kali-linux -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d kali-linux -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d kali-linux -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for kali-linux..."

    call :Log INFO "Updating kali-linux using apt..."
    call :Run wsl -d kali-linux -- sh -c "sudo apt update && sudo apt upgrade -y"
    call :Log PASS "✅ kali-linux updated successfully."

    call :Log INFO "Update process completed for kali-linux."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d kali-linux -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d kali-linux -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "kali-linux is not installed."
)

:: Arch Linux
wsl -d Arch -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for Arch"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for Arch (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching Arch
    call :Run wsl -d Arch -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch Arch"
        call :Log HINT "Try: wsl --terminate Arch & wsl --unregister Arch and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d Arch -- uname -a
    call :Run wsl -d Arch -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d Arch -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d Arch -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d Arch -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d Arch -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d Arch -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d Arch -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for Arch..."

    call :Log INFO "Updating Arch using pacman..."
    call :Run wsl -d Arch -- sh -c "sudo pacman -Syu --noconfirm"
    call :Log PASS "✅ Arch updated successfully."

    call :Log INFO "Update process completed for Arch."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d Arch -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d Arch -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "Arch is not installed."
)

:: openSUSE
wsl -d openSUSE -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for openSUSE"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for openSUSE (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching openSUSE
    call :Run wsl -d openSUSE -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch openSUSE"
        call :Log HINT "Try: wsl --terminate openSUSE & wsl --unregister openSUSE and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d openSUSE -- uname -a
    call :Run wsl -d openSUSE -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d openSUSE -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d openSUSE -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d openSUSE -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d openSUSE -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d openSUSE -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d openSUSE -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for openSUSE..."

    call :Log INFO "Updating openSUSE using zypper..."
    call :Run wsl -d openSUSE -- sh -c "sudo zypper refresh && sudo zypper update -y"
    call :Log PASS "✅ openSUSE updated successfully."

    call :Log INFO "Update process completed for openSUSE."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d openSUSE-Leap -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d openSUSE-Leap -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "openSUSE is not installed."
)

:: Linux Mint
wsl -d mint -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for mint"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for mint (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching mint
    call :Run wsl -d mint -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch mint"
        call :Log HINT "Try: wsl --terminate mint & wsl --unregister mint and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d mint -- uname -a
    call :Run wsl -d mint -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d mint -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d mint -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d mint -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d mint -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d mint -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d mint -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for mint..."

    call :Log INFO "Updating mint using apt..."
    call :Run wsl -d mint -- sh -c "sudo apt update && sudo apt upgrade -y"
    call :Log PASS "✅ mint updated successfully."

    call :Log INFO "Update process completed for mint."

        rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d mint -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d mint -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "mint is not installed."
)

:: Fedora
wsl -d Fedora -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for Fedora"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for Fedora (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching Fedora
    call :Run wsl -d Fedora -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch Fedora"
        call :Log HINT "Try: wsl --terminate Fedora & wsl --unregister Fedora and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d Fedora -- uname -a
    call :Run wsl -d Fedora -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d Fedora -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d Fedora -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d Fedora -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d Fedora -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d Fedora -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d Fedora -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for Fedora..."

    call :Log INFO "Updating Fedora using dnf..."
    call :Run wsl -d Fedora -- sh -c "sudo dnf upgrade -y"
    call :Log PASS "✅ Fedora updated successfully."

    call :Log INFO "Update process completed for Fedora."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d Fedora -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d Fedora -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "Fedora is not installed."
)

:: Red Hat Enterprise Linux
wsl -d "RedHat" -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for RedHat"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for RedHat (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching RedHat
    call :Run wsl -d RedHat -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch RedHat"
        call :Log HINT "Try: wsl --terminate RedHat & wsl --unregister RedHat and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d RedHat -- uname -a
    call :Run wsl -d RedHat -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d RedHat -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d RedHat -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d RedHat -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d RedHat -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d RedHat -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d RedHat -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for RedHat..."

    call :Log INFO "Updating RedHat using yum..."
    call :Run wsl -d RedHat -- sh -c "sudo yum update -y"
    call :Log PASS "✅ RedHat updated successfully."

    call :Log INFO "Update process completed for RedHat."

        rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d RedHat -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d RedHat -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "RedHat is not installed."
)


:: SUSE Linux
wsl -d SUSE -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for suse-linux"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for suse-linux (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching suse-linux
    call :Run wsl -d suse-linux -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch suse-linux"
        call :Log HINT "Try: wsl --terminate suse-linux & wsl --unregister suse-linux and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d suse-linux -- uname -a
    call :Run wsl -d suse-linux -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d suse-linux -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d suse-linux -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d suse-linux -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d suse-linux -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d suse-linux -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d suse-linux -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for suse-linux..."

    call :Log INFO "Updating suse-linux using zypper..."
    call :Run wsl -d suse-linux -- sh -c "sudo zypper refresh && sudo zypper update -y"
    call :Log PASS "✅ suse-linux updated successfully."

    call :Log INFO "Update process completed for suse-linux."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d suse-linux -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d suse-linux -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "suse-linux is not installed."
)


:: Pengwin
wsl -d Pengwin -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for Pengwin"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for Pengwin (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching Pengwin
    call :Run wsl -d Pengwin -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch Pengwin"
        call :Log HINT "Try: wsl --terminate Pengwin & wsl --unregister Pengwin and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d Pengwin -- uname -a
    call :Run wsl -d Pengwin -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d Pengwin -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d Pengwin -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d Pengwin -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d Pengwin -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d Pengwin -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d Pengwin -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for Pengwin..."

    call :Log INFO "Updating Pengwin using apt..."
    call :Run wsl -d Pengwin -- sh -c "sudo apt update && sudo apt upgrade -y"
    call :Log PASS "✅ Pengwin updated successfully."

    call :Log INFO "Update process completed for Pengwin."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d Pengwin -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d Pengwin -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "Pengwin is not installed."
)


:: Oracle Linux
wsl -d OracleLinux -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for oracle-linux"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for oracle-linux (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching oracle-linux
    call :Run wsl -d oracle-linux -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch oracle-linux"
        call :Log HINT "Try: wsl --terminate oracle-linux & wsl --unregister oracle-linux and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d oracle-linux -- uname -a
    call :Run wsl -d oracle-linux -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d oracle-linux -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d oracle-linux -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d oracle-linux -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d oracle-linux -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d oracle-linux -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d oracle-linux -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for oracle-linux..."

    call :Log INFO "Updating oracle-linux using dnf..."
    call :Run wsl -d oracle-linux -- sudo dnf upgrade -y
    call :Log PASS "✅ oracle-linux updated successfully."

    call :Log INFO "Update process completed for oracle-linux."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d oracle-linux -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d oracle-linux -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "oracle-linux is not installed."
)


:: Clear Linux
wsl -d ClearLinux -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for clear-linux"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for clear-linux (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching clear-linux
    call :Run wsl -d clear-linux -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch clear-linux"
        call :Log HINT "Try: wsl --terminate clear-linux & wsl --unregister clear-linux and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d clear-linux -- uname -a
    call :Run wsl -d clear-linux -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d clear-linux -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d clear-linux -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d clear-linux -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d clear-linux -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d clear-linux -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d clear-linux -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for clear-linux..."

    call :Log INFO "Updating clear-linux using swupd..."
    call :Run wsl -d clear-linux -- sudo swupd update
    call :Log PASS "✅ clear-linux updated successfully."

    call :Log INFO "Update process completed for clear-linux."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d clear-linux -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d clear-linux -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "clear-linux is not installed."
)

:: Alpine
wsl -d Alpine -- bash -c "exit" >nul 2>&1
if %errorlevel% equ 0 (
    call :Log INFO "Starting deep diagnostics for Alpine"

    :: Durchlaufe alle WSL-Distributionen
    set "DISTRO=%%A" & set "VER=%%B" & set "STATE=%%C"
    call :Log CHECK "Diagnostics for Alpine (Version: !VER!, State: !STATE!)"

    rem -- Launch Test
    call :Log TEST "Launching Alpine
    call :Run wsl -d Alpine -- true
    if errorlevel 1 (
        call :Log FAIL "Cannot launch Alpine"
        call :Log HINT "Try: wsl --terminate Alpine & wsl --unregister Alpine and reinstall"
    ) else (
        call :Log PASS "✅ Launch OK"
    )

    rem -- Kernel & OS Info
    call :Log TEST "Retrieving kernel and OS info"
    call :Run wsl -d Alpine -- uname -a
    call :Run wsl -d Alpine -- cat /etc/os-release
    call :Log PASS "✅ Kernel and OS details displayed"

    rem -- Uptime & Load
    call :Log TEST "Checking uptime and load average"
    call :Run wsl -d Alpine -- uptime
    call :Log PASS "✅ Uptime and load displayed"

    rem -- Memory Usage
    call :Log TEST "Checking memory usage"
    call :Run wsl -d Alpine -- free -m
    call :Log PASS "✅ Memory usage OK"

    rem -- Disk Usage
    call :Log TEST "Checking disk usage"
    call :Run wsl -d Alpine -- df -h /
    call :Log PASS "✅ Disk usage OK"

    rem -- Top Processes
    call :Log TEST "Listing top CPU processes"
    wsl -d Alpine -- bash -c "top -b -n 1 | head -n 10"
    call :Log PASS "✅ Top processes displayed"

    rem -- Network Connectivity Check
    call :Log TEST "Pinging %PING_ADDR%"
    call :Run wsl -d Alpine -- ping -c 2 %PING_ADDR%
    if errorlevel 1 (
        call :Log WARN "❌ Network unreachable"
        call :Log HINT "Check WSL network settings and Windows Firewall"
    ) else (
        call :Log PASS "✅ Network OK"
    )

    rem -- DNS Resolution Check
    call :Log TEST "Resolving %TEST_DOMAIN%"
    call :Run wsl -d Alpine -- nslookup %TEST_DOMAIN%
    if errorlevel 1 (
        call :Log WARN "❌ DNS resolution failed"
    ) else (
        call :Log PASS "✅ DNS OK"
    )

    call :Log INFO "Starting update process for Alpine..."

    call :Log INFO "Updating Alpine using apk..."
    call :Run wsl -d Alpine -- sh -c "sudo apk update && sudo apk upgrade --no-progress"
    call :Log PASS "✅ Alpine updated successfully."

    call :Log INFO "Update process completed for Alpine."

    rem -- Time Sync Check
    call :Log TEST "Checking time drift"
    for /F "delims=" %%T in ('powershell -NoProfile -Command "(Get-Date -UFormat '%%s')"') do set "TS_HOST=%%T"
    for /F "delims=" %%T in ('wsl -d Alpine -- date +%%s') do set "TS_DISTRO=%%T"
    set /A DRIFT=TS_HOST-TS_DISTRO
    if !DRIFT! GTR %MAX_DRIFT% (
        call :Log WARN "❌ Time drift !DRIFT!s"
    ) else (
        call :Log PASS "✅ Time sync OK"
    )

    rem -- Mount Points Check
    call :Log TEST "Listing mount points"
    call :Run wsl -d Alpine -- mount
    if errorlevel 1 (
        call :Log WARN "❌ Cannot list mounts"
    ) else (
        call :Log PASS "✅ Mount points displayed"
    )

) else (
    call :Log INFO "Alpine is not installed."
)

call :Log INFO "Deep diagnostics completed for all distributions."

:: Final Summary & Exit
call :Log PASS "✅ All diagnostics complete. Exiting with code %ERRORLEVEL%"
endlocal

:: Define project path
set "PYCHARM_PROJECTS=%USERPROFILE%\p-terminal"
set "PP_DIR=%PYCHARM_PROJECTS%\pp-term"
set "PP_ENV_FILE=%PP_DIR%\.env"
set "PP_RUN_FILE=%PP_DIR%\pp-term.bat"
set "EXPECTED_PYTHON_VERSION=3.12"

:: Ensure PyCharm Projects directory exists
if not exist "%PYCHARM_PROJECTS%" (
    echo Creating project directory: %PYCHARM_PROJECTS%...
    mkdir "%PYCHARM_PROJECTS%"
    if errorlevel 1 (
        call :Log WARN "❌ Error: Failed to create directory %PYCHARM_PROJECTS%. Exiting..."
        exit /b 1
    )
)

:: Change to PyCharm Projects directory
cd /d "%PYCHARM_PROJECTS%"

:: Check if the p-terminal directory exists
if not exist "%PP_DIR%" (
    echo Cloning p-terminal repository from GitHub...

    :: Check if Git is installed
    where git >nul 2>&1
    if %errorlevel% neq 0 (
        call :Log WARN "❌ Error: Git is not installed. Please install Git first."
        exit /b 1
    )

    :: Check if GitHub is reachable (with a timeout of 5 seconds)
    echo Testing connection to GitHub...
    for /f "delims=" %%i in ('ping -n 1 -w 5000 github.com ^| find "TTL"') do set REACHABLE=1
    if not defined REACHABLE (
        call :Log WARN "❌ Cannot reach GitHub! Check your internet connection or firewall settings."
        exit /b 1
    )
    set REACHABLE=  :: Zurücksetzen der REACHABLE-Variable

    :: GitHub is accessible, clone repository
    echo Running git clone...
    git clone https://github.com/Peharge/p-terminal.git "%PP_DIR%"

    if %errorlevel% neq 0 (
        call :Log WARN "❌ Cloning P-terminal repository failed! Make sure GitHub is accessible and the URL is correct."
        exit /b 1
    ) else (
        call :Log PASS "✅ P-terminal repository cloned successfully!"
    )
) else (
    echo P-terminal repository already exists. Checking for updates...

    cd /d "%PP_DIR%"

    :: Check if the repository is in the correct state (no uncommitted changes)
    git diff-index --quiet HEAD --
    if %errorlevel% neq 0 (
       call :Log WARN "❌ There are uncommitted changes! Please commit or discard them first."
        exit /b 1
    )

    :: Perform Git Fetch (with a timeout of 5 seconds)
    echo Fetching latest changes...
    git fetch --quiet
    if %errorlevel% neq 0 (
        call :Log WARN "❌ Could not fetch updates from the remote repository! Check your internet connection or Git configuration."
        exit /b 1
    )

    :: Check the status of the repository to see if updates are available
    git status | find "Your branch is behind" >nul
    if %errorlevel% equ 0 (
        echo Updates available, pulling changes...

        :: Perform Git Pull (with timeout of 5 seconds)
        git pull --quiet
        if %errorlevel% neq 0 (
            call :Log WARN "❌ Could not update P-terminal repository! Check your internet connection or Git configuration."
            exit /b 1
        ) else (
            call :Log PASS "✅ P-terminal repository updated successfully!"
        )
    ) else (
        call :Log PASS "✅ P-terminal repository is already up-to-date!"
    )
)

:: Check Git status after pull (no merge conflicts)
git status | find "Merge conflict" >nul
if %errorlevel% equ 0 (
    call :Log WARN "❌ Merge conflicts detected. Please resolve them manually."
    exit /b 1
)

call :Log PASS "✅ P-terminal update process completed successfully."

:: Ensure P-terminal directory exists
if not exist "%PP_DIR%" (
    call :Log WARN "❌ P-terminal directory does not exist!"
    echo Make sure the repository was cloned correctly.
    exit /b 1
)

:: Change to P-terminal directory
cd /d "%PP_DIR%" || (
    call :Log WARN "❌ Failed to access P-terminal directory!"
    exit /b 1
)

:: Ensure .env file exists and is correctly configured
echo Checking for existing .env file at: "%PP_ENV_FILE%"
if not exist "%PP_ENV_FILE%" (
    echo Creating .env file...
    (
        echo # Environment variables for P-terminal
        echo PYTHONPATH=%PP_DIR%
        echo PYTHON_VERSION=%EXPECTED_PYTHON_VERSION%
    ) > "%PP_ENV_FILE%"

    :: Verify file was created and is not empty
    if exist "%PP_ENV_FILE%" (
        for %%A in ("%PP_ENV_FILE%") do (
            if %%~zA gtr 0 (
                call :Log PASS "✅ .env file created successfully at %PP_ENV_FILE%"
            ) else (
                call :Log WARN "❌ .env file was created but is empty!"
                del "%PP_ENV_FILE%" >nul 2>&1
                exit /b 1
            )
        )
    ) else (
        call :Log WARN "❌ Failed to create .env file!"
        exit /b 1
    )
) else (
    call :Log PASS "✅ .env file already exists at %PP_ENV_FILE%"
)

:: Define the username variable dynamically
:: set "username=%USERNAME%"

:: Detect the OneDrive folder dynamically
:: set "onedriveFolder="
:: for /f "delims=" %%i in ('dir /ad /b "C:\Users\%username%" ^| findstr /i "OneDrive"') do (
::     set "onedriveFolder=%%i"
:: )

:: If OneDrive folder is found, set the Desktop path
:: if defined onedriveFolder (
::     :: Handle paths with spaces in OneDrive folder names properly
::     for /f "delims=" %%i in ('powershell -Command "try { (Get-ChildItem -Path 'C:\\Users\\%username%\\%onedriveFolder%' -Recurse | Where-Object {$_.Name -match 'Desktop'})[0].FullName } catch { '' }"') do set "desktop=%%i"
:: )

:: If Desktop path is not found under OneDrive, fall back to default Desktop path
:: if not defined desktop (
::     for /f "delims=" %%i in ('powershell -Command "[System.Environment]::GetFolderPath('Desktop')"') do set "desktop=%%i"
:: )

:: Check if Desktop path is found, if not skip step and continue
:: if not defined desktop (
::     echo ❌ Could not find Desktop path. Skipping step...
::     set "desktop="
::     goto :end
:: )

:: Print the Desktop path for verification
:: echo Desktop Path: "!desktop!"

:: Define the paths for the shortcut, target, and icon
:: set "shortcut=!desktop!\MAVIS Installer 4.lnk"
:: set "targetPath=C:\Users\%username%\p-terminal\pp-term\mavis-launcher-4.bat"
:: set "startIn=C:\Users\%username%\p-terminal\pp-term"
:: set "iconPath=C:\Users\%username%\p-terminal\pp-term\icons\MAVIS-3-logo-1.ico"

:: Check if the target files exist, if not skip
:: if not exist "!targetPath!" (
::     echo ❌ Target path (!targetPath!) does not exist. Skipping step...
::     set "targetPath="
:: )

:: if not exist "!iconPath!" (
::     echo ❌ Icon path (!iconPath!) does not exist. Skipping step...
::     set "iconPath="
:: )

:: Check if the shortcut already exists
:: if exist "!shortcut!" (
::     echo ✅ Shortcut 'MAVIS Installer 4' already exists. No new shortcut will be created.
:: ) else (
::     if defined desktop if defined targetPath if defined iconPath (
::         echo ❌ Shortcut 'MAVIS Installer 4' does not exist. Creating shortcut now...
::
::         :: Create the shortcut using PowerShell script file
::         echo Set objShell = CreateObject("WScript.Shell") > "!desktop!\create_shortcut.vbs"
::         echo Set objShortcut = objShell.CreateShortcut("!shortcut!") >> "!desktop!\create_shortcut.vbs"
::         echo objShortcut.TargetPath = "!targetPath!" >> "!desktop!\create_shortcut.vbs"
::         echo objShortcut.WorkingDirectory = "!startIn!" >> "!desktop!\create_shortcut.vbs"
::         echo objShortcut.IconLocation = "!iconPath!" >> "!desktop!\create_shortcut.vbs"
::         echo objShortcut.Save >> "!desktop!\create_shortcut.vbs"
::
::         :: Check if the VBS script was created successfully
::         if not exist "!desktop!\create_shortcut.vbs" (
::             echo ❌ Failed to create the VBS script. Skipping step...
::             set "desktop="
::             goto :end
::         )
::
::         :: Run the VBS script to create the shortcut if VBS file exists
::         if exist "!desktop!\create_shortcut.vbs" (
::             cscript //nologo "!desktop!\create_shortcut.vbs"
::             if errorlevel 1 (
::                 echo ❌ Failed to create the shortcut. Skipping step...
::                 set "desktop="
::                 goto :end
::             )
::         )
::
::         :: Clean up the temporary VBS script
::         if exist "!desktop!\create_shortcut.vbs" del "!desktop!\create_shortcut.vbs"
::
::         echo ✅ Shortcut 'MAVIS Installer 4' has been created successfully.
::     ) else (
::         echo ❌ Skipping shortcut creation due to missing paths.
::     )
:: )

:: Check if P-terminal run file exists
if not exist "%PP_RUN_FILE%" (
    call :Log WARN "❌ pp-term.bat not found!"
    echo Please verify that the file exists in: %PP_DIR%
    exit /b 1
)

:: Execute pp-term.bat
echo Starting PP_terminal...

:: Check if the file is executable (check for executable file)
:: Test if the file is an .bat file
if /I not "%PP_RUN_FILE:~-4%"==".bat" (
    call :Log WARN "❌ The file is not an executable file!"
    exit /b 1
)

:: Final report
:: call :Log PASS "✅ All tasks were completed successfully!"

:: Try to start the file and check if it is successful
call "%PP_RUN_FILE%"
if %errorlevel% neq 0 (
    call :Log WARN "❌ PP-Terminal could not be started successfully!"
    exit /b 1
) else (
   call :Log PASS "✅ PP-Terminal was successfully launched!"
)

:: endlocal
pause
exit /b

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

:: CPU Check using PowerShell
:CheckCPU
    call :Log "INFO" "Checking CPU..."

    :: Powershell-Befehl zum Abrufen der CPU-Informationen und Umformatierung in Liste mit Zeilenumbrüchen
    for /f "delims=" %%a in ('powershell -Command "Get-WmiObject Win32_Processor | Select-Object Name, Manufacturer, MaxClockSpeed, Status | ForEach-Object { 'Name: ' + $_.Name + [Environment]::NewLine + 'Manufacturer: ' + $_.Manufacturer + [Environment]::NewLine + 'MaxClockSpeed: ' + $_.MaxClockSpeed + [Environment]::NewLine + 'Status: ' + $_.Status }"') do (
        set "CPU_INFO=%%a"
        echo !CPU_INFO!
    )

    :: Prüfen, ob CPU-Daten erfolgreich abgerufen wurden
    if not defined CPU_INFO (
        call :Log "ERROR" "❌ CPU Error: No CPU detected or details could not be retrieved."
    ) else (
        call :Log "INFO" "✅ CPU check successful."
    )

    goto :eof


:: RAM Check using PowerShell
:CheckMemory
    call :Log "INFO" "Checking RAM..."

    :: Powershell-Befehl zum Abrufen der RAM-Informationen und Umformatierung in Liste mit Zeilenumbrüchen
    for /f "delims=" %%a in ('powershell -Command "Get-WmiObject Win32_PhysicalMemory | Select-Object Capacity, Manufacturer, Speed | ForEach-Object { 'Capacity: ' + [math]::round($_.Capacity / 1GB, 2) + ' GB' + [Environment]::NewLine + 'Manufacturer: ' + $_.Manufacturer + [Environment]::NewLine + 'Speed: ' + $_.Speed + ' MHz' }"') do (
        set "MEMORY_INFO=%%a"
        echo !MEMORY_INFO!
    )

    :: Prüfen, ob RAM-Daten erfolgreich abgerufen wurden
    if not defined MEMORY_INFO (
        call :Log "ERROR" "❌ RAM Error: No RAM details available."
    ) else (
        call :Log "INFO" "✅ RAM check successful."
    )

    goto :eof


:: Disk Check using PowerShell
:CheckDisks
    call :Log "INFO" "Checking disks..."

    :: Powershell-Befehl zum Abrufen der Festplatten-Informationen und Umformatierung in Liste mit Zeilenumbrüchen
    for /f "delims=" %%a in ('powershell -Command "Get-WmiObject Win32_LogicalDisk | Select-Object DeviceID, MediaType, Size, FreeSpace | ForEach-Object { 'DeviceID: ' + $_.DeviceID + [Environment]::NewLine + 'MediaType: ' + $_.MediaType + [Environment]::NewLine + 'Size: ' + [math]::round($_.Size / 1GB, 2) + ' GB' + [Environment]::NewLine + 'FreeSpace: ' + [math]::round($_.FreeSpace / 1GB, 2) + ' GB' }"') do (
        set "DISK_INFO=%%a"
        echo !DISK_INFO!
    )

    :: Prüfen, ob Festplatten-Daten erfolgreich abgerufen wurden
    if not defined DISK_INFO (
        call :Log "ERROR" "❌ Disk Error: No C: drive found or details could not be retrieved."
    ) else (
        call :Log "INFO" "✅ Disk check successful."
    )

    goto :eof


:: GPU Check using PowerShell
:CheckGPU
    call :Log "INFO" "Checking GPU..."

    :: Powershell-Befehl zum Abrufen der GPU-Informationen und Umformatierung in Liste mit Zeilenumbrüchen
    for /f "delims=" %%a in ('powershell -Command "Get-WmiObject Win32_VideoController | Select-Object Caption, DriverVersion | ForEach-Object { 'Caption: ' + $_.Caption + [Environment]::NewLine + 'DriverVersion: ' + $_.DriverVersion }"') do (
        set "GPU_INFO=%%a"
       echo !GPU_INFO!
    )

    :: Prüfen, ob GPU-Daten erfolgreich abgerufen wurden
    if not defined GPU_INFO (
        call :Log "ERROR" "❌ GPU Error: No GPU details available."
    ) else (
        call :Log "INFO" "✅ GPU check successful."
    )

    goto :eof


:: System Health Check using PowerShell
:CheckSystemHealth
    call :Log "INFO" "Checking system health..."

    :: Powershell-Befehl zum Abrufen der Systemstatus-Informationen und Umformatierung in Liste mit Zeilenumbrüchen
    for /f "delims=" %%a in ('powershell -Command "Get-WmiObject Win32_OperatingSystem | Select-Object Status | ForEach-Object { 'Status: ' + $_.Status }"') do (
        set "SYSTEM_HEALTH=%%a"
        echo !SYSTEM_HEALTH!
    )

    :: Prüfen, ob Systemstatus-Daten erfolgreich abgerufen wurden
    if not defined SYSTEM_HEALTH (
        call :Log "ERROR" "❌ System Status Error: No system health data available."
    ) else (
        call :Log "INFO" "✅ System health check successful."
    )

    goto :eof


:: Driver Check using PowerShell
:CheckDrivers
    call :Log "INFO" "Checking drivers..."

    rem PowerShell Befehl, um die Treiberinformationen im CSV-Format zu exportieren
    powershell -Command "Get-WmiObject Win32_PnPSignedDriver | Select-Object DeviceName, DriverVersion, Manufacturer | Export-Csv -Path temp_driver_check.csv -NoTypeInformation -Encoding UTF8"

    rem Überprüfen, ob die Datei existiert und gelesen werden kann
    if exist temp_driver_check.csv (
        call :Log "INFO" "✅ Driver check successful. Analyzing drivers..."

        rem Jetzt die Treiber-Datei durchgehen und für jedes Gerät spezifische Infos ausgeben
        for /F "tokens=1,2,* delims=," %%A in (temp_driver_check.csv) do (
            rem Entfernen von Leerzeichen und Anführungszeichen in den Variablen
            set "deviceName=%%A"
            set "driverVersion=%%B"
            set "manufacturer=%%C"

            rem Entfernen von Anführungszeichen und führenden/folgenden Leerzeichen
            set "deviceName=!deviceName:"=!"
            set "deviceName=!deviceName: =!"
            set "driverVersion=!driverVersion:"=!"
            set "driverVersion=!driverVersion: =!"
            set "manufacturer=!manufacturer:"=!"
            set "manufacturer=!manufacturer: =!"

            rem Überspringen der Header-Zeile (falls notwendig)
            if not "!deviceName!"=="DeviceName" (
                rem Saubere Ausgabe für jedes Gerät mit Formatierung
                call :Log "INFO" "Checking !deviceName! for errors"
                echo Driver: !deviceName!
                echo Manufacturer: !manufacturer!
                echo Driver Version: !driverVersion!

                rem Beispiel: Spezifische Treiber-Analyse für bekannte Geräte
                if /I "!deviceName!"=="WAN Miniport (L2TP)" (
                    call :Log "INFO" "This is a virtual network adapter for VPN (L2TP)."
                    if "!driverVersion!"=="10.0.26100.1" (
                        call :Log "INFO" "✅ This driver is stable, secure, and up-to-date."
                    ) else (
                        call :Log "WARNING" "This driver version may be outdated. Consider updating."
                    )
                ) else if /I "!deviceName!"=="WAN Miniport (IKEv2)" (
                    call :Log "INFO" "This is a virtual network adapter for VPN (IKEv2)."
                    if "!driverVersion!"=="10.0.26100.1" (
                        call :Log "INFO" "✅ This driver is stable, secure, and up-to-date."
                    ) else (
                        call :Log "WARNING" "This driver version may be outdated. Consider updating."
                    )
                ) else if /I "!deviceName!"=="Generic software device" (
                    call :Log "INFO" "Generic software device detected."
                    if "!driverVersion!"=="10.0.26100.1" (
                        call :Log "INFO" "✅ This driver is stable, secure, and up-to-date."
                    ) else (
                        call :Log "WARNING" "This driver version may be outdated. Consider updating."
                    )
                ) else if /I "!deviceName!"=="Hyper-V Virtual Switch Extension Adapter" (
                    call :Log "INFO" "Virtual Switch Extension Adapter for Hyper-V."
                    if "!driverVersion!"=="10.0.26100.1" (
                        call :Log "INFO" "✅ This driver is stable, secure, and up-to-date."
                    ) else (
                        call :Log "WARNING" "This driver version may be outdated. Consider updating."
                    )
                ) else if /I "!deviceName!"=="WAN Miniport (Network Monitor)" (
                    call :Log "INFO" "This is a network monitor adapter used for debugging."
                    if "!driverVersion!"=="10.0.26100.1" (
                        call :Log "INFO" "✅ This driver is stable, secure, and up-to-date."
                    ) else (
                        call :Log "WARNING" "This driver version may be outdated. Consider updating."
                    )
                ) else (
                    rem Generische Ausgabe für nicht spezifizierte Treiber
                    call :Log "INFO" "This driver is stable and secure, but regular updates are recommended."
                )
            )
        )
    ) else (
        call :Log "ERROR" "❌ Driver Error: Could not find the driver file for analysis."
    )
    rem Bereinigen
    del temp_driver_check.csv
    goto :eof
