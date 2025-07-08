<#
Englisch Peharge: This source code is released under the MIT License.

Usage Rights:
The source code may be copied, modified, and adapted to individual requirements.
Users are permitted to use this code in their own projects, both for private and commercial purposes.
However, it is recommended to modify the code only if you have sufficient programming knowledge,
as changes could cause unintended errors or security risks.

Dependencies and Additional Frameworks:
The code relies on the use of various frameworks and executes additional files.
Some of these files may automatically install further dependencies required for functionality.
It is strongly recommended to perform installation and configuration in an isolated environment
(e.g., a virtual environment) to avoid potential conflicts with existing software installations.

Disclaimer:
Use of the code is entirely at your own risk.
Peharge assumes no liability for damages, data loss, system errors, or other issues
that may arise directly or indirectly from the use, modification, or redistribution of the code.

Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

Deutsch Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.

Nutzungsrechte:
Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.

Abhängigkeiten und zusätzliche Frameworks:
Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.

Haftungsausschluss:
Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.

Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

Français Peharge: Ce code source est publié sous la licence MIT.

Droits d'utilisation:
Le code source peut être copié, édité et adapté aux besoins individuels.
Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.

Dépendances et frameworks supplémentaires:
Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
pour éviter d'éventuels conflits avec les installations de logiciels existantes.

Clause de non-responsabilité:
L'utilisation du code est entièrement à vos propres risques.
Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.

Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.
#>

<#
.SYNOPSIS
  Launch a Python script with full CPU affinity, highest priority, and run the entire environment in RAM for ultimate speed.
#>

param (
    [string]$ScriptPath = "$PSScriptRoot\pp-term-6-3.py",
    [string]$PythonEnvDir = "$PSScriptRoot\.env",
    [string]$LogFile    = "$HOME\p-terminal\pp-term\WSL_Diagnostics.log"
)

function Write-Log {
    param($Level, $Message)
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss.fff"
    $entry = "[{0}] [{1}] {2}" -f $ts, $Level.ToUpper(), $Message
    Add-Content -Path $LogFile -Value $entry
    Write-Host $entry
}

# Ensure log directory exists
$logDir = Split-Path $LogFile
if (!(Test-Path $logDir)) {
    New-Item -Path $logDir -ItemType Directory -Force | Out-Null
}

try {
    Write-Log INFO "Launching PP-Term 5 script with max CPU affinity, highest priority, and full RAM execution..."

    # Check for file existence
    if (!(Test-Path $PythonEnvDir)) {
        throw "Python environment not found: $PythonEnvDir"
    }
    if (!(Test-Path $ScriptPath)) {
        throw "Python script not found: $ScriptPath"
    }

    $OriginalPythonExe = "$PythonEnvDir\Scripts\python.exe"
    $PythonExe = $OriginalPythonExe
    $OriginalScriptPath = $ScriptPath

    # Detect number of logical processors (max 64)
    $maxProcs = [Math]::Min((Get-CimInstance Win32_ComputerSystem).NumberOfLogicalProcessors, 64)

    # Calculate affinity mask
    $affinity = 0
    for ($i = 0; $i -lt $maxProcs; $i++) {
        $affinity = $affinity -bor (1 -shl $i)
    }

    # Setup RAM disk
    $ramDisk = $false
    $ramDiskPath = "$env:TEMP\ppterm-ramdisk"
    $ramDiskSize = "8G"  # Adjust to your available RAM for large workloads!

    if (Get-Command imdisk -ErrorAction SilentlyContinue) {
        try {
            if (!(Test-Path $ramDiskPath)) {
                mkdir $ramDiskPath | Out-Null
            }
            imdisk -a -t tmpfs -s $ramDiskSize -m $ramDiskPath
            Write-Log INFO "RAM disk created via ImDisk: $ramDiskPath ($ramDiskSize)"

            # Copy Python environment and script into RAM disk
            Copy-Item $PythonEnvDir "$ramDiskPath\.env" -Recurse -Force
            Copy-Item $ScriptPath "$ramDiskPath\pp-term-6-3.py" -Force

            $PythonExe = "$ramDiskPath\.env\Scripts\python.exe"
            $ScriptPath = "$ramDiskPath\pp-term-6-3.py"
            Push-Location $ramDiskPath
            $ramDisk = $true
        } catch {
            Write-Log WARN "Failed to set up full RAM disk environment: $_"
            $PythonExe = $OriginalPythonExe
            $ScriptPath = $OriginalScriptPath
            Push-Location $HOME
        }
    } else {
        Write-Log WARN "No RAM disk utility found, running from disk."
        $PythonExe = $OriginalPythonExe
        $ScriptPath = $OriginalScriptPath
        Push-Location $HOME
    }

    # Validate PythonExe before proceeding
    if (![System.IO.File]::Exists($PythonExe)) {
        throw "Python executable not found: $PythonExe"
    }

    # Start Python process with maximum resources and highest priority
    $proc = Start-Process -FilePath $PythonExe `
                          -ArgumentList @("$ScriptPath") `
                          -NoNewWindow -PassThru

    Start-Sleep -Milliseconds 800  # Allow process to initialize

    # Set CPU affinity and highest priority (Realtime if available, else High)
    $proc.ProcessorAffinity = $affinity
    try {
        $proc.PriorityClass = "RealTime"
        Write-Log INFO "Set process priority to 'RealTime'."
    } catch {
        $proc.PriorityClass = "High"
        Write-Log INFO "Set process priority to 'High' (RealTime not available)."
    }
    Write-Log INFO "CPU affinity set to $maxProcs cores."

    $proc.WaitForExit()

    if ($proc.ExitCode -ne 0) {
        Write-Log ERROR "Python script terminated with exit code $($proc.ExitCode)."
        exit $proc.ExitCode
    } else {
        Write-Log INFO "Python script completed successfully."
    }

    # Cleanup RAM disk
    if ($ramDisk) {
        try {
            Pop-Location
            Remove-Item "$ramDiskPath\*" -Recurse -Force
            imdisk -D -m $ramDiskPath
            Remove-Item $ramDiskPath -Recurse -Force
            Write-Log INFO "RAM disk cleaned up."
        } catch {
            Write-Log WARN "Failed to clean up RAM disk: $_"
        }
    } else {
        Pop-Location
    }

} catch {
    Write-Log ERROR "Error launching the script: $_"
    exit 1
}