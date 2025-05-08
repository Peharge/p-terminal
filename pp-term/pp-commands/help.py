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

from datetime import datetime

def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

# Farbcodes definieren (kleingeschrieben)
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
white = "\033[97m"
black = "\033[30m"
orange = "\033[38;5;214m"
reset = "\033[0m"
bold = "\033[1m"

def show_help():
    # Kopfzeile
    print("\n[{timestamp()}] [INFO] This guide provides descriptions of the available terminal commands and usage instructions.\n")

    # Verfügbare Befehle und Beschreibungen
    print("Available Commands and Their Descriptions")
    print("-----------------------------------------")

    commands = {
        "p": "Peharge command",
        "p git": "Peharge git command - Opens a P-Term Commit Explorer",
        "p htop": "Peharge git command - Opens a P-Term Taskmanager",
        "p ls": "Peharge git command - Opens a P-Term File Explorer",
        "p simon": "Peharge git command - Opens a P-Term SIMON Explorer",
        "p wsl": "Peharge git command - Opens a P-Term WSL Explorer",
        "p pip": "Peharge git command - Opens a P-Term PIP Explorer",
        "p models": "Peharge git command - Opens a P-Term MAVIS Models Explorer",
        "p ubuntu": "Peharge git command - Opens a P-Term Ubuntu Explorer",
        "pp": "Peharge permission command",
        "pp-c": "Peharge permission compile command",
        "pp-p": "Peharge permission publish command",
        "ps": "Peharge search command",
        "ps-github": "Peharge GitHub search command",
        "ps-huggingface": "Huggingface GitHub search command",
        "ps-ollama": "Peharge Ollama search command",
        "ps-stackoverflow": "Stack Overflow GitHub search command",
        "ps-arxiv": "Peharge ArXiv search command",
        "pa": "Peharge AI command: Ask a question (AI functionality) -> deepcoder:14b",
        "lx": "Linux command",
        "lx-c": "Linux command with Peharge C compiler",
        "lx-p": "Linux command with Python",
        "lx-cpp-c": "Linux command with Peharge C++ compiler",
        "lx-c-c": "Linux command with Peharge C compiler",
        "lx-p-c": "Linux command with Python",
        "ubuntu": "Ubuntu command",
        "ubuntu-c": "Ubuntu command with Peharge C compiler",
        "ubuntu-p": "Ubuntu command with Python",
        "debian": "Debian command",
        "debian-c": "Debian command with Peharge C compiler",
        "debian-p": "Debian command with Python",
        "kali": "Kali Linux command",
        "kali-c": "Kali command with Peharge C compiler",
        "kali-p": "Kali command with Python",
        "hack": "Hack command (functionality-specific)",
        "arch": "Arch Linux command",
        "arch-c": "Arch command with Peharge C compiler",
        "arch-p": "Arch command with Python",
        "opensuse": "openSUSE Linux command",
        "opensuse-c": "openSUSE command with Peharge C compiler",
        "opensuse-p": "openSUSE command with Python",
        "mint": "Linux Mint command",
        "mint-c": "Linux Mint command with Peharge C compiler",
        "mint-p": "Linux Mint command with Python",
        "fedora": "Fedora Linux command",
        "fedora-c": "Fedora command with Peharge C compiler",
        "fedora-p": "Fedora command with Python",
        "redhat": "Red Hat Linux command",
        "redhat-c": "Red Hat Linux command with Peharge C compiler",
        "redhat-p": "Red Hat Linux command with Python",
        "sles": "SUSE Linux Enterprise Server command",
        "sles-c": "SUSE Linux command with Peharge C compiler",
        "sles-p": "SUSE Linux command with Python",
        "pengwin": "Pengwin WSL Linux command",
        "pengwin-c": "Pengwin WSL Linux command with Peharge C compiler",
        "pengwin-p": "Pengwin WSL Linux command with Python",
        "oracle": "Oracle Linux command",
        "oracle-c": "Oracle Linux command with Peharge C compiler",
        "oracle-p": "Oracle Linux command with Python",
        "cd": "Change directory",
        "cls": "Clear screen (Windows)",
        "clear": "Clear screen (Linux)",
        "dir": "List directory contents (Windows)",
        "ls": "List directory contents (Linux)",
        "mkdir": "Create a new directory",
        "rmdir": "Remove a directory",
        "del": "Delete a file (Windows)",
        "rm": "Remove a file (Linux)",
        "echo": "Print text to output",
        "type": "Display contents of a file (Windows)",
        "cat": "Display contents of a file (Linux)",
        "exit": "Exit application",
        "alpine": "Alpine Linux command",
        "scoop": "Manage apps via Scoop package manager (Windows)",
        "choco": "Manage apps via Chocolatey package manager (Windows)",
        "winget": "Manage apps via Winget package manager (Windows)",
        "speedtest": "Run internet speed test",
        "kill": "Kill a running process",
        "download": "Download a file from a URL",
        "cputemp": "Display CPU temperature",
        "chucknorris": "Show Chuck Norris jokes",
        "theme": "Change the application's theme",
        "cleantemp": "Clean temporary files",
        "selfupdate": "Update the application to latest version",
        "tree": "Display directory tree structure",
        "py": "Execute Python code",
        "ask": "Ask a question (AI interaction)",
        "weather": "Show current weather information",
        "whoami": "Display current user information",
        "hostname": "Display machine hostname",
        "ip": "Display IP address information",
        "os": "Display operating system information",
        "time": "Display current time",
        "date": "Display current date",
        "open": "Open a file or application",
        "fortune": "Display a random fortune quote",
        "history": "Show command history",
        "search": "Search for files or commands",
        "zip": "Compress files into a zip archive",
        "unzip": "Extract files from a zip archive",
        "sysinfo": "Show system information",
        "clip set": "Set clipboard content",
        "clip get": "Get clipboard content",
        "ping": "Ping a network address",
        "emptytrash": "Empty the trash/recycle bin",
        "launch": "Launch an application",
        "doctor": "Run system doctor check",
        "mavis env install": "Install Mavis environment",
        "install mavis env": "Install Mavis environment",
        "install mavis3": "Install Mavis version 3",
        "install mavis3.3": "Install Mavis version 3.3",
        "install mavis4": "Install Mavis version 4",
        "install mavis4.3": "Install Mavis version 4.3",
        "mavis env update": "Update Mavis environment",
        "update mavis env": "Update Mavis environment",
        "mavis update": "Update Mavis repository",
        "update mavis": "Update Mavis repository",
        "security": "Run security check",
        "p-terminal security": "Run security check in terminal",
        "securitycheck": "Run security check",
        "info": "Show general information",
        "mavis info": "Show Mavis information",
        "info mavis": "Show Mavis information",
        "p-term info": "Show terminal information",
        "info p-term": "Show terminal information",
        "neofetch": "Display system information",
        "fastfetch": "Display system information quickly",
        "screenfetch": "Display system information",
        "jupyter": "Run Jupyter",
        "run jupyter": "Run Jupyter",
        "run ju": "Run Jupyter",
        "run mavis-4": "Run Mavis version 4",
        "run mavis-4-3": "Run Mavis version 4.3",
        "run mavis-4-fast": "Run Mavis version 4 fast",
        "run mavis-4-3-fast": "Run Mavis version 4.3 fast",
        "run mavis-launcher-4": "Run Mavis launcher",
        "run ollama mavis-4": "Install Ollama Mavis version 4",
        "install ollama mavis-4": "Install Ollama Mavis version 4",
        "change models mavis-4": "Change models for Mavis version 4",
        "change models": "Change models",
        "grafana": "Run Grafana",
        "run grafana": "Run Grafana",
        "install grafana": "Install Grafana",
        "account": "Manage Mavis account",
        "run deepseek-r1:1.5b": "Run DeepSeek model version 1.5b",
        "run deepseek-r1:7b": "Run DeepSeek model version 7b",
        "run deepseek-r1:8b": "Run DeepSeek model version 8b",
        "run deepseek-r1:14b": "Run DeepSeek model version 14b",
        "run deepseek-r1:32b": "Run DeepSeek model version 32b",
        "run deepseek-r1:70b": "Run DeepSeek model version 70b",
        "run deepseek-r1:671b": "Run DeepSeek model version 671b",
        "run deepscaler": "Run DeepScaler",
        "run llama3.1:8b": "Run Llama3.1 model version 8b",
        "run llama3.1:70b": "Run Llama3.1 model version 70b",
        "run llama3.1:405": "Run Llama3.1 model version 405b",
        "run llama3.2:1b": "Run Llama3.2 model version 1b",
        "run llama3.2:3b": "Run Llama3.2 model version 3b",
        "run llama3.3": "Run Llama3.3 model",
        "run llama3:8b": "Run Llama3 model version 8b",
        "run llama3:70b": "Run Llama3 model version 70b",
        "run mistral": "Run Mistral model",
        "run mistral-large": "Run Mistral large model",
        "run mistral-nemo": "Run Mistral Nemo model",
        "run mistral-openorca": "Run Mistral OpenOrca model",
        "run mistral-small:22b": "Run Mistral small model version 22b",
        "run mistral-small:24b": "Run Mistral small model version 24b",
        "run phi4": "Run Phi4 model",
        "run qwen2.5:0.5b": "Run Qwen2.5 model version 0.5b",
        "run qwen2.5:1.5b": "Run Qwen2.5 model version 1.5b",
        "run qwen2.5:3b": "Run Qwen2.5 model version 3b",
        "run qwen2.5:7b": "Run Qwen2.5 model version 7b",
        "run qwen2.5:14b": "Run Qwen2.5 model version 14b",
        "run qwen2.5:32b": "Run Qwen2.5 model version 32b",
        "run qwen2.5:72b": "Run Qwen2.5 model version 72b",
        "run qwen2.5-coder:0.5b": "Run Qwen2.5 Coder model version 0.5b",
        "run qwen2.5-coder:1.5b": "Run Qwen2.5 Coder model version 1.5b",
        "run qwen2.5-coder:3b": "Run Qwen2.5 Coder model version 3b",
        "run qwen2.5-coder:7b": "Run Qwen2.5 Coder model version 7b",
        "run qwen2.5-coder:14b": "Run Qwen2.5 Coder model version 14b",
        "run qwen2.5-coder:32b": "Run Qwen2.5 Coder model version 32b",
        "run gemma3:1b": "Run Gemma3 model version 1b",
        "run gemma3:4b": "Run Gemma3 model version 4b",
        "run gemma3:12b": "Run Gemma3 model version 12b",
        "run gemma3:27b": "Run Gemma3 model version 27b",
        "run qwq": "Run QwQ model",
        "run command-a": "Run Command-A",
        "run phi4-mini": "Run Phi4 mini model",
        "run granite3.2:8b": "Run Granite3.2 model version 8b",
        "run granite3.2:2b": "Run Granite3.2 model version 2b",
        "run granite3.2-vision:2b": "Run Granite3.2 Vision model version 2b",
        "run qwen-2-5-omni:7b": "Run Qwen-2.5 Omni model version 7b",
        "run qvq:72b": "Run QVQ model version 72b",
        "run qwen-2-5-vl:32b": "Run Qwen-2.5 VL model version 32b",
        "run qwen-2-5-vl:72b": "Run Qwen-2.5 VL model version 72b",
        "run llama-4-maverick:17b": "Run Llama-4 Maverick model version 17b",
        "run llama-4-scout:17b": "Run Llama-4 Scout model version 17b",
        "run deepcoder:1.5b": "Run DeepCoder model version 1.5b",
        "run deepcoder:14b": "Run DeepCoder model version 14b",
        "run mistral-small3.1": "Run Mistral small model version 3.1",
        "help": "Display help information",
        "image generation": "Generate images",
        "video generation": "Generate videos",
        "models": "List available models",
        "models ls": "List available models",
        "install 3d-slicer": "Install 3D Slicer",
        "run 3d-slicer": "Run 3D Slicer",
        "install simon": "Install Simon",
        "run simon": "Run Simon",
        "jupyter --version": "Display Jupyter version",
        "grafana --version": "Display Grafana version",
        "3d-slicer --version": "Display 3D Slicer version"
    }

    # Drucken der Befehle in einem übersichtlichen, tabellenähnlichen Format
    for command, description in commands.items():
        print(f"{blue}{command}{reset}: {description}")

    print("and more...")

    # How to use the terminal command execution script
    print("\nHow to Use the Linux Command Executor")
    print("-------------------------------------")

    # Instructions for the terminal command execution
    print(f"1. To execute a Linux command on a specific distribution, use the following format:")
    print(f"  {blue}lx <command>{reset}, {blue}ubuntu <command>{reset}, {blue}debian <command>{reset},")
    print(f"  {blue}kali <command>{reset}, {blue}arch <command>{reset}, {blue}mint <command>{reset},")
    print(f"  {blue}redhat <command>{reset}")
    print(f"  Example: {blue}lx neofetch{reset} will execute 'neofetch' on the default Linux distro (WSL).")
    print(f"  Example: {blue}ubuntu sudo apt update{reset} will run 'sudo apt update' on an Ubuntu system.")
    print(f"  Example: {blue}arch pacman -Syu{reset} will update Arch Linux with the command 'pacman -Syu'.\n")

    # Example of how each distribution works
    print(f"2. Example Commands (You can replace <command> with any Linux command):")
    print(f" - To execute a command on {blue}Linux (WSL){reset}:")
    print(f"  {blue}lx <command>{reset} (e.g., {blue}lx neofetch{reset})")
    print(f" - To execute a command on {blue}Ubuntu{reset}:")
    print(f"  {blue}ubuntu <command>{reset} (e.g., {blue}ubuntu sudo apt update{reset})")
    print(f" - To execute a command on {blue}Debian{reset}:")
    print(f"  {blue}debian <command>{reset} (e.g., {blue}debian sudo apt upgrade{reset})")
    print(f" - To execute a command on {blue}Kali Linux{reset}:")
    print(f"  {blue}kali <command>{reset} (e.g., {blue}kali apt-get install nmap{reset})")
    print(f" - To execute a command on {blue}Arch Linux{reset}:")
    print(f"  {blue}arch <command>{reset} (e.g., {blue}arch pacman -Syu{reset})")
    print(f" - To execute a command on {blue}Mint{reset}:")
    print(f"  {blue}mint <command>{reset} (e.g., {blue}mint sudo apt install vlc{reset})")
    print(f" - To execute a command on {blue}Red Hat{reset}:")
    print(f"  {blue}redhat <command>{reset} (e.g., {blue}redhat sudo yum install git{reset})")

    print(f"\n3. Notes:")
    print(f" - You can replace <command> with any valid Linux command, e.g., {blue}lx neofetch{reset}, {blue}ubuntu ls -l{reset}, {blue}kali sudo apt install nmap{reset}.")
    print(f" - The distribution alias (e.g., lx, ubuntu, debian) determines which environment the command will be executed in.\n")

    # How to use pip and PowerShell
    print("\nHow to Use pip and PowerShell")
    print("-----------------------------")

    # pip instructions
    print(f"1. Using {blue}pip` (Python Package Installer){reset}:")
    print(f" - To install a Python package, execute the following command in your terminal or command prompt:")
    print(f"  {blue}pip install <package_name>{reset}")
    print(f"  Example: pip install numpy")
    print(f" - To upgrade pip itself, run:")
    print(f"  {blue}python -m pip install --upgrade pip{reset}")
    print(f" - Note: In some environments, you may need to use `pip3` instead of `pip`.\n")

    # PowerShell instructions
    print(f"2. Using PowerShell:")
    print(f" - To {blue}run Python scripts{blue} in PowerShell, navigate to the script directory and execute the command:")
    print(f"  {blue}python <script_name>.py{reset}")
    print(f"  Example: python my_script.py")
    print(f" - To install Python packages in PowerShell using pip, run:")
    print(f"  {blue}pip install <package_name>{reset}")
    print(f"  Example: pip install requests")
    print(f" - If you're using PowerShell as an administrator and face any permission issues, try running it as Administrator.\n")

    print("\nHow to Use Ollama")
    print("-----------------")
    # Added third point for using Ollama
    print(f" - To {blue}use Ollama{blue} in PowerShell, you first need to have Ollama installed. If it's not installed, run:")
    print(f"  {blue}pip install ollama{reset}")
    print(f"  Example: pip install ollama")
    print(f" - After installation, you can use the following commands to interact with Ollama:\n")

    # Listing Ollama commands
    print(f"  Available Ollama commands:")
    print(f"  {blue}serve{reset}: Start Ollama server")
    print(f"  {blue}create{reset}: Create a model from a Modelfile")
    print(f"  {blue}show{reset}: Show information for a model")
    print(f"  {blue}run{reset}: Run a model")
    print(f"  {blue}stop{reset}: Stop a running model")
    print(f"  {blue}pull{reset}: Pull a model from a registry")
    print(f"  {blue}push{reset}: Push a model to a registry")
    print(f"  {blue}list{reset}: List available models")
    print(f"  {blue}ps{reset}: List running models")
    print(f"  {blue}cp{reset}: Copy a model")
    print(f"  {blue}rm{reset}: Remove a model")
    print(f"  {blue}help{reset}: Get help for any command\n")

    # Flags and version
    print(f" - To see version information, use the command:")
    print(f"  {blue}ollama --version{reset}")
    print(f"  Example: ollama --version")

    print(f" - For additional help on any command, type:")
    print(f"  {blue}ollama [command] --help{reset}")
    print(f"  Example: ollama run --help")

    print("\nHow to Use PowerShell")
    print("---------------------")

    # PowerShell instructions
    print(f" - To {blue}run a basic command{blue}, just type it and press Enter.")
    print(f"  Example: {blue}dir{reset} - Lists the contents of the current directory.")
    print(f" - To navigate between directories, use the {blue}cd{reset} command:")
    print(f"  Example: {blue}cd C:\\Users\\UserName\\Documents{reset} - Changes the directory to Documents.")
    print(f" - To go back to the previous directory, use {blue}cd ..{reset}.")
    print(f" - To go to the root of the current drive, use {blue}cd \\{reset}.")
    print(f" - To create a new directory, use {blue}mkdir{reset}:")
    print(f"  Example: {blue}mkdir NewFolder{reset} - Creates a new folder called 'NewFolder'.")
    print(f" - To remove a file, use {blue}rm{reset}, and to remove an empty directory, use {blue}rmdir{reset}:")
    print(f"  Example: {blue}rm file.txt{reset} - Deletes the file 'file.txt'.")
    print(f"  Example: {blue}rmdir EmptyFolder{reset} - Removes the empty folder 'EmptyFolder'.")
    print(f" - To view the contents of a file, use the {blue}cat{reset} command:")
    print(f"  Example: {blue}cat file.txt{reset} - Displays the contents of 'file.txt'.")
    print(f" - To copy files or directories, use {blue}cp{reset}:")
    print(f"  Example: {blue}cp file.txt D:\\Backup{reset} - Copies 'file.txt' to the 'D:\\Backup' directory.")
    print(f" - To move or rename files, use {blue}mv{reset}:")
    print(f"  Example: {blue}mv file.txt newfile.txt{reset} - Renames 'file.txt' to 'newfile.txt'.")
    print(f" - To find files or folders, use the {blue}find{reset} command:")
    print(f"  Example: {blue}find . -name 'file.txt'{reset} - Searches for 'file.txt' in the current directory and subdirectories.")
    print(f" - To search inside a file, use the {blue}select-string{reset} command:")
    print(f"  Example: {blue}select-string -Path 'file.txt' -Pattern 'keyword'{reset} - Searches for 'keyword' in 'file.txt'.")
    print(f" - To get a list of running processes, use {blue}Get-Process{reset}:")
    print(f"  Example: {blue}Get-Process{reset} - Lists all active processes.")
    print(f" - To stop a process, use {blue}Stop-Process{reset}:")
    print(f"  Example: {blue}Stop-Process -Name notepad{reset} - Stops the Notepad process.")
    print(f" - To view system information, use {blue}Get-ComputerInfo{reset} or {blue}systeminfo{reset}.")
    print(f" - To get help on a specific command, use {blue}Get-Help <command>{reset}:")
    print(f"  Example: {blue}Get-Help dir{reset} - Displays help for the 'dir' command.")
    print(f" - To view the command history, use {blue}Get-History{reset}.")
    print(f" - To clear the screen, use {blue}Clear{reset}.")
    print(f" - To get the current working directory, use {blue}Get-Location{reset}.")
    print(f" - To set the current location (directory), use {blue}Set-Location{reset}:")
    print(f"  Example: {blue}Set-Location C:\\Users\\UserName{reset} - Changes the current directory to 'C:\\Users\\UserName'.")
    print(f" - To run a script, make sure the execution policy allows it. To set the execution policy, use:")
    print(f"  {blue}Set-ExecutionPolicy RemoteSigned{reset} - Allows running scripts locally and downloaded ones if signed.")
    print(f" - To run a script, navigate to its location and type the script name with a .ps1 extension:")
    print(f"  Example: {blue}.\\script.ps1{reset}")
    print(f" - To see all the environment variables, use {blue}Get-ChildItem Env:{reset}.")
    print(f" - To add a new environment variable, use {blue}$env:VariableName = 'Value'{reset}:")
    print(f"  Example: {blue}$env:MyVar = 'Hello'{reset} - Sets the environment variable 'MyVar' to 'Hello'.")
    print(f" - To display the contents of an environment variable, use {blue}$env:VariableName{reset}:")
    print(f"  Example: {blue}$env:MyVar{reset} - Displays the value of 'MyVar'.")
    print(f" - To change the default drive, use the {blue}cd{reset} command followed by the drive letter:")
    print(f"  Example: {blue}cd D:\\{reset} - Switches to the D: drive.")
    print(f" - To get the current date and time, use {blue}Get-Date{reset}.")
    print(f"  Example: {blue}Get-Date{reset} - Displays the current date and time.")
    print(f" - To format the date and time output, use {blue}Get-Date -Format <format>{reset}:")
    print(f"  Example: {blue}Get-Date -Format 'yyyy-MM-dd HH:mm:ss'{reset} - Displays the date in the specified format.")
    print(f" - For advanced scripting, you can write scripts in .ps1 files, which are executed by typing:")
    print(f"  {blue}.\\script_name.ps1{reset} - Executes the 'script_name.ps1' script.")
    print(f" - To make sure scripts can run, set the execution policy with {blue}Set-ExecutionPolicy RemoteSigned{reset}.")
    print(f" - To use pipelines in PowerShell (sending the output of one command to another), use {blue}|{reset}:")
    print(f'  Example: {blue}Get-Process | Where-Object (Curly bracket open)$_.CPU -gt 100(Curly bracket closed){reset} - Filters processes with CPU usage greater than 100.')
    print(f" - To create a loop, use {blue}for, foreach, while, do{reset} loops. Example:")
    print(f"  {blue}foreach ($item in 1..5) {{Write-Output $item}}{reset} - Prints numbers 1 to 5.")
    print(f" - You can use {blue}if{reset} statements for conditional execution:")
    print(f"  Example: {blue}if ($a -gt $b) {{Write-Output 'a is greater than b'}}{reset}")
    print(f" - PowerShell supports object-oriented scripting, allowing you to work with .NET objects, classes, and methods.")

    print("For more information, refer to the official documentation or contact support.")

# Call the help function
show_help()
