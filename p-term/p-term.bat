@echo off
:: -----------------------------------------------------------------------------
:: Batch-Skript: Installiert ggf. Visual Studio C++ Build Tools und kompiliert
::               und startet dann das Programm p-term.cpp
:: -----------------------------------------------------------------------------
setlocal enableextensions enabledelayedexpansion

REM === 1. Visual Studio Install-Skript ausführen ===
set "INSTALL_SCRIPT=%USERPROFILE%\p-terminal\p-term\install\cpp\install-vs.py"
if not exist "%INSTALL_SCRIPT%" (
    echo Fehler: Installationsskript nicht gefunden: %INSTALL_SCRIPT%
    goto :error
)
echo.
echo *** Schritt 1: Installationsskript fuer VS Build Tools ausfuehren ***
python "%INSTALL_SCRIPT%"
if errorlevel 1 (
    echo Fehler: Installationsskript schlug fehl.
    goto :error
)
echo.

REM === 2. Visual Studio Umgebungs-Init (vcvarsall.bat) ===
echo *** Schritt 2: Visual Studio-Umgebung initialisieren ***

REM Default-Installation-Verzeichnis setzen (fallback)
set "VSINSTALL=%ProgramFiles%\Microsoft Visual Studio\2022\Community"

REM Versuche VS-Installation via vswhere.exe zu finden und überschreibe VSINSTALL
set "VSWHERE=%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe"
if exist "%VSWHERE%" (
    for /f "usebackq tokens=* delims=" %%i in (`"%VSWHERE%" -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath`) do (
        set "VSINSTALL=%%i"
    )
) else (
    echo vswhere.exe nicht gefunden, verwende Standard: %VSINSTALL%
)

set "VCVARSALL=%VSINSTALL%\VC\Auxiliary\Build\vcvarsall.bat"
if not exist "%VCVARSALL%" (
    echo Fehler: vcvarsall.bat nicht gefunden unter %VCVARSALL%
    goto :error
)
call "%VCVARSALL%" x64
if errorlevel 1 (
    echo Fehler: VS-Umgebung konnte nicht initialisiert werden.
    goto :error
)
echo.

REM === 3. C++-Datei kompilieren und ausfuehren ===
set "SRC=%USERPROFILE%\p-terminal\p-term\p-term.cpp"
set "EXE=%USERPROFILE%\p-terminal\p-term\p-term.exe"
if not exist "%SRC%" (
    echo Fehler: Quelldatei nicht gefunden: %SRC%
    goto :error
)
echo *** Schritt 3: Kompilieren von %SRC% ***
cl.exe /EHsc "%SRC%" /Fe"%EXE%"
if errorlevel 1 (
    echo Fehler: Kompilierung schlug fehl.
    goto :error
)
echo.
echo *** Ausfuehren von %EXE% ***
"%EXE%"

goto :end

:error
echo.
echo *** Skript wurde mit Fehler beendet ***
pause
exit /b 1

:end
echo.
echo *** Fertig ***
endlocal
