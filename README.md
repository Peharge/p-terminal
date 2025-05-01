<p align="center">
 <img width="400" src="./icons/p-term-icon-3.png" alt="peharge"/>
</p>

# **_P-Terminal_**

<p align="left">
    <img src="./icons/p-term-banner-3.svg" alt="peharge"/>
    <img src="./icons/pp-term-banner-3.svg" alt="peharge"/>
    <img src="./icons/peharge-banner-3.svg" alt="peharge"/>
    <img src="./icons/MAVIS-icon-banner-3.svg" alt="mavis">
    <img src="./icons/MAVIS-launcher-icon-banner-3.svg" alt="mavis-launcher">
    <img src="./icons/MAVIS-terminal-icon-banner-3.svg" alt="mavis-terminal">
    <img alt="c++" src="https://img.shields.io/badge/-C++-555555?style=flat&logo=cplusplus">
    <img alt="c" src="https://img.shields.io/badge/C-555555?logo=C&logoColor=white">
    <img alt="rust" src="https://img.shields.io/badge/Rust-555555?logo=rust&logoColor=white">
    <img alt="python" src="https://img.shields.io/badge/Python-3.11 / 3.12 / (3.13)-555555?&style=flat&logo=Python&logoColor=white">
    <img alt="batch" src="https://img.shields.io/badge/Bat-555555?style=flat&logo=bat">
    <img alt="bash" src="https://img.shields.io/badge/Shell-555555?&style=flat&logo=gnu-bash&logoColor=white">
	<img alt="bash" src="https://img.shields.io/badge/WSL-555555?logo=linux&logoColor=white"><br><br>
    <img alt="bash" src="https://img.shields.io/badge/Visual_Studio-555555?logo=visualstudio">
    <img alt="bash" src="https://img.shields.io/badge/PyCharm-555555?logo=pycharm">
    <img alt="bash" src="https://img.shields.io/badge/CLion-555555?logo=clion">
    <img alt="bash" src="https://img.shields.io/badge/RustRover-555555?logo=rustrover">
</p>

In development: Peharge Terminal: The fastest terminal in the world - More [p-terminal.com](https://peharge.github.io/MAVIS-web/p-term.html).

# NEWS

- **[23.04.2025]** Developmentstart of P-Term and PP-Ptem!!!
- **[24.04.2025]** PP-Term EAP release: [pp-term.bat](https://github.com/Peharge/p-terminal/blob/main/pp-term/run-pp-term.bat)!!!
- **[28.08.2025]** PP-Term 1 release!!!
- **[01.05.2025]** PP-Term 3 EAP release!!!
- **[01.06.2025]** P-Term 1.1 release!!!
- **[01.06.2025]** PP-Term 3 release!!!

# Install

<p align="center">
 <img width="800" src="https://github.com/Peharge/p-terminal-images/raw/main/images/p-term-demo-3.png" alt="peharge"/>
</p>

P-Terminal:
soon

PP-Terminal:
Download the [pp-term.bat](https://github.com/Peharge/p-terminal/blob/main/pp-term/run-pp-term.bat) file and double-click it. You're ready to go! Have fun with pp-terminal and you can always start it with `pp-term/pp-term.exe` after installation. If you want, you can further enhance your terminal with PP Terminal Themes/Pins: [PP Terminal Themes/Pins](./pp-term/THEMES.md)
<details>
  <summary>Problems installing the PP-Terminal</summary>

## Problems installing the PP-Terminal

The PP Terminal should normally be installed automatically. However, problems may arise during installation that require you to install certain dependencies manually.

Usually, all required dependencies are included in the automatic installation. However, if a dependency was not installed correctly, only those specific dependencies need to be installed subsequently.

### 1. **Git**

Git is required to clone code and track changes.  
[Download Git](https://git-scm.com/downloads)

### 2. **Python**

It is recommended to use Python 3.12 (Python 3.11 is also supported, but not Python 3.13).  
[Download Python](https://www.python.org/downloads/) or install via the Microsoft Store.

### 3. **Ollama**

Ollama is a necessary tool for the PP Terminal.  
[Download Ollama](https://ollama.com/download)

### 4. **FFmpeg**

FFmpeg is another important dependency for the PP Terminal.  
[Visit the official FFmpeg website](https://ffmpeg.org/)

### 5. **Rustup**

Rustup is required to install Rust and related tools.  
[Download Rustup](https://rustup.rs/)

### 6. **3D Slicer**

Installing 3D Slicer is not required to run PP-Term. However, it is mandatory if you plan to use SIMON.  
If installation fails, you can run the `Install 3d-slicer` command in the PP Terminal for a safer setup.  
Otherwise, install it manually: [Download 3D Slicer](https://download.slicer.org)

### 7. **PowerShell 7**

PowerShell 7 is recommended for use with the PP Terminal.  
[Download PowerShell 7](https://github.com/PowerShell/PowerShell/releases)

### 8. **Windows Subsystem for Linux (WSL)**

To make optimal use of the PP Terminal, you need WSL. Supported distributions:

- **Ubuntu**  
  [Microsoft Store Link](https://aka.ms/wslubuntu)  
  ```bash
  wsl --install -d Ubuntu
  ```

- **Debian**  
  [Microsoft Store Link](https://aka.ms/wsldebian)  
  ```bash
  wsl --install -d Debian
  ```

- **Kali Linux**  
  [Microsoft Store Link](https://aka.ms/wslkali)  
  ```bash
  wsl --install -d Kali-Linux
  ```

- **Arch Linux**  
  Not available via Store. Use [WSL Installation Scripts](https://github.com/yuk7/wsldl)  
  Or install manually via AUR.

- **openSUSE**  
  [Microsoft Store Link](https://aka.ms/wslsuse)  
  ```bash
  wsl --install -d openSUSE
  ```

- **Linux Mint**  
  Not available via Store. Install via [Linux Mint](https://www.linuxmint.com/) and follow instructions.

- **Fedora**  
  [Microsoft Store Link](https://aka.ms/wslfedora)  
  ```bash
  wsl --install -d Fedora
  ```

- **Red Hat**  
  [Installation Instructions](https://developers.redhat.com/blog/2020/06/25/introducing-red-hat-enterprise-linux-on-wsl)

- **SUSE Linux**  
  [Microsoft Store Link](https://aka.ms/wslopensuse)  
  ```bash
  wsl --install -d openSUSE-42
  ```

- **Pengwin**  
  [Microsoft Store Link](https://aka.ms/wsl-pengwin)  
  ```bash
  wsl --install -d Pengwin
  ```

- **Oracle Linux**  
  [Microsoft Store Link](https://aka.ms/wsl-oracle)  
  ```bash
  wsl --install -d OracleLinux_8_5
  ```

- **Clear Linux**  
  [Microsoft Store Link](https://aka.ms/wsl-clearlinux)  
  ```bash
  wsl --install -d ClearLinux
  ```

- **Alpine**  
  [Microsoft Store Link](https://aka.ms/wsl-alpine)  
  ```bash
  wsl --install -d Alpine
  ```

For more information on WSL:  
[Installing WSL – Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/install)

### 9. **PP Terminal Repository**

Clone the repository from GitHub:  
[PP Terminal GitHub Repository](https://github.com/Peharge/P-Terminal)

### 10. **C++ Extensions for Desktop Development**

To develop and run the PP Terminal, you also need the C++ extensions for Visual Studio.  
[Download C++ Extensions](https://visualstudio.microsoft.com/de/downloads/)

</details>

# Commands

- `p` - Peharge command  
	- `p git` - Peharge git command - Opens a P-Term Commit Explorer  
	- `p htop` - Peharge git command - Opens a P-Term Taskmanager  
	- `p ls` - Peharge git command - Opens a P-Term File Explorer  
	- `p simon` - Peharge git command - Opens a P-Term SIMON Explorer
	- `p wsl` - Peharge git command - Opens a P-Term WSL Explorer  
	- `p pip` - Peharge git command - Opens a P-Term PIP Explorer  
	- `p models` - Peharge git command - Opens a P-Term MAVIS Models Explorer  
	- `p ubuntu` - Peharge git command - Opens a P-Term Ubuntu Explorer  
	etc.  
  
- `pp` - Peharge permission command  
- `pp-c` - Peharge permission compile command  
- `pp-p` - Peharge permission publish command  
- `ps` - Peharge search command  
	- `ps-github` - Peharge GitHub search command  
	- `ps-huggingface` - Huggingface GitHub search command  
	- `ps-ollama` - Peharge Ollama search command    
	- `ps-stackoverflow` - Stack Overflow GitHub search command  
	- `ps-arxiv` - Peharge ArXiv search command  
	etc.  
  
- `pa` - Peharge AI command: Ask a question (AI functionality) -> qwen3:14b  
- `lx` - Linux command  
- `lx-c` - Linux command with Peharge C compiler 
- `lx-p` - Linux command with Python 
- `lx-cpp-c` - Linux command with Peharge C++ compiler  
- `lx-c-c` - Linux command with Peharge C compiler 
- `lx-p-c` - Linux command with Python
- `ubuntu` - Ubuntu command  
- `ubuntu-c` - Ubuntu command with Peharge C compiler 
- `ubuntu-p` - Ubuntu command with Python 
- `debian` - Debian command  
- `debian-c` - Debian command with Peharge C compiler 
- `debian-p` - Debian command with Python 
- `kali` - Kali Linux command  
- `kali-c` - Kali command with Peharge C compiler 
- `kali-p` - Kali command with Python 
- `hack` - Hack command (functionality-specific)  
- `arch` - Arch Linux command  
- `arch-c` - Arch command with Peharge C compiler 
- `arch-p` - Arch command with Python 
- `opensuse` - openSUSE Linux command  
- `opensuse-c` - openSUSE command with Peharge C compiler 
- `opensuse-p` - openSUSE command with Python 
- `mint` - Linux Mint command  
- `mint-c` - Linux Mint command with Peharge C compiler 
- `mint-p` - Linux Mint command with Python 
- `fedora` - Fedora Linux command  
- `fedora-c` - Fedora command with Peharge C compiler 
- `fedora-p` - Fedora command with Python 
- `redhat` - Red Hat Linux command  
- `redhat-c` - Red Hat Linux command with Peharge C compiler 
- `redhat-p` - Red Hat Linux command with Python 
- `sles` - SUSE Linux Enterprise Server command  
- `sles-c` - SUSE Linux command with Peharge C compiler 
- `sles-p` - SUSE Linux command with Python 
- `pengwin` - Pengwin WSL Linux command  
- `pengwin-c` - Pengwin WSL Linux command with Peharge C compiler 
- `pengwin-p` - Pengwin WSL Linux command with Python 
- `oracle` - Oracle Linux command  
- `oracle-c` - Oracle Linux command with Peharge C compiler 
- `oracle-p` - Oracle Linux command with Python
- `cd` - Change directory  
- `cls` - Clear screen (Windows)  
- `clear` - Clear screen (Linux)  
- `dir` - List directory contents (Windows)  
- `ls` - List directory contents (Linux)  
- `mkdir` - Create a new directory  
- `rmdir` - Remove a directory  
- `del` - Delete a file (Windows)  
- `rm` - Remove a file (Linux)  
- `echo` - Print text to output  
- `type` - Display contents of a file (Windows)  
- `cat` - Display contents of a file (Linux)  
- `exit` - Exit application  
- `alpine` - Alpine Linux command  
- `scoop` - Manage apps via Scoop package manager (Windows)  
- `choco` - Manage apps via Chocolatey package manager (Windows)  
- `winget` - Manage apps via Winget package manager (Windows)  
- `speedtest` - Run internet speed test  
- `kill` - Kill a running process  
- `download` - Download a file from a URL  
- `cputemp` - Display CPU temperature  
- `chucknorris` - Show Chuck Norris jokes  
- `theme` - Change the application's theme  
- `cleantemp` - Clean temporary files  
- `selfupdate` - Update the application to latest version  
- `tree` - Display directory tree structure  
- `py` - Execute Python code  
- `ask` - Ask a question (AI interaction)  
- `weather` - Show current weather information  
- `whoami` - Display current user information  
- `hostname` - Display machine hostname  
- `ip` - Display IP address information  
- `os` - Display operating system information  
- `time` - Display current time  
- `date` - Display current date  
- `open` - Open a file or application  
- `fortune` - Display a random fortune quote  
- `history` - Show command history  
- `search` - Search for files or commands  
- `zip` - Compress files into a zip archive  
- `unzip` - Extract files from a zip archive  
- `sysinfo` - Show system information  
- `clip set` - Set clipboard content  
- `clip get` - Get clipboard content  
- `ping` - Ping a network address  
- `emptytrash` - Empty the trash/recycle bin  
- `launch` - Launch an application
- `doctor` - Run system doctor check
- `mavis env install` - Install Mavis environment
- `install mavis env` - Install Mavis environment
- `install mavis3` - Install Mavis version 3
- `install mavis3.3` - Install Mavis version 3.3
- `install mavis4` - Install Mavis version 4
- `install mavis4.3` - Install Mavis version 4.3
- `mavis env update` - Update Mavis environment
- `update mavis env` - Update Mavis environment
- `mavis update` - Update Mavis repository
- `update mavis` - Update Mavis repository
- `security` - Run security check
- `p-terminal security` - Run security check in terminal
- `securitycheck` - Run security check
- `info` - Show general information
- `mavis info` - Show Mavis information
- `info mavis` - Show Mavis information
- `p-term info` - Show terminal information
- `info p-term` - Show terminal information
- `neofetch` - Display system information
- `fastfetch` - Display system information quickly
- `screenfetch` - Display system information
- `jupyter` - Run Jupyter
- `run jupyter` - Run Jupyter
- `run ju` - Run Jupyter
- `run mavis-4` - Run Mavis version 4
- `run mavis-4-3` - Run Mavis version 4.3
- `run mavis-4-fast` - Run Mavis version 4 fast
- `run mavis-4-3-fast` - Run Mavis version 4.3 fast
- `run mavis-launcher-4` - Run Mavis launcher
- `run ollama mavis-4` - Install Ollama Mavis version 4
- `install ollama mavis-4` - Install Ollama Mavis version 4
- `change models mavis-4` - Change models for Mavis version 4
- `change models` - Change models
- `grafana` - Run Grafana
- `run grafana` - Run Grafana
- `install grafana` - Install Grafana
- `account` - Manage Mavis account
- `run qwen3:0.6b` - Run Qwen 3 model version 0.6b
- `run qwen3:1.7b` - Run Qwen 3 model version 1.7b
- `run qwen3:4b` - Run Qwen 3 model version 4b
- `run qwen3:8b` - Run Qwen 3 model version 8b
- `run qwen3:14b` - Run Qwen 3 model version 14b
- `run qwen3:32b` - Run Qwen 3 model version 32b
- `run qwen3:30b` - Run Qwen 3 model version 30b
- `run qwen3:235b` - Run Qwen 3 model version 235b
- `run deepseek-r1:1.5b` - Run DeepSeek model version 1.5b
- `run deepseek-r1:7b` - Run DeepSeek model version 7b
- `run deepseek-r1:8b` - Run DeepSeek model version 8b
- `run deepseek-r1:14b` - Run DeepSeek model version 14b
- `run deepseek-r1:32b` - Run DeepSeek model version 32b
- `run deepseek-r1:70b` - Run DeepSeek model version 70b
- `run deepseek-r1:671b` - Run DeepSeek model version 671b
- `run deepscaler` - Run DeepScaler
- `run llama3.1:8b` - Run Llama3.1 model version 8b
- `run llama3.1:70b` - Run Llama3.1 model version 70b
- `run llama3.1:405` - Run Llama3.1 model version 405b
- `run llama3.2:1b` - Run Llama3.2 model version 1b
- `run llama3.2:3b` - Run Llama3.2 model version 3b
- `run llama3.3` - Run Llama3.3 model
- `run llama3:8b` - Run Llama3 model version 8b
- `run llama3:70b` - Run Llama3 model version 70b
- `run mistral` - Run Mistral model
- `run mistral-large` - Run Mistral large model
- `run mistral-nemo` - Run Mistral Nemo model
- `run mistral-openorca` - Run Mistral OpenOrca model
- `run mistral-small:22b` - Run Mistral small model version 22b
- `run mistral-small:24b` - Run Mistral small model version 24b
- `run phi4` - Run Phi4 model
- `run qwen2.5:0.5b` - Run Qwen2.5 model version 0.5b
- `run qwen2.5:1.5b` - Run Qwen2.5 model version 1.5b
- `run qwen2.5:3b` - Run Qwen2.5 model version 3b
- `run qwen2.5:7b` - Run Qwen2.5 model version 7b
- `run qwen2.5:14b` - Run Qwen2.5 model version 14b
- `run qwen2.5:32b` - Run Qwen2.5 model version 32b
- `run qwen2.5:72b` - Run Qwen2.5 model version 72b
- `run qwen2.5-coder:0.5b` - Run Qwen2.5 Coder model version 0.5b
- `run qwen2.5-coder:1.5b` - Run Qwen2.5 Coder model version 1.5b
- `run qwen2.5-coder:3b` - Run Qwen2.5 Coder model version 3b
- `run qwen2.5-coder:7b` - Run Qwen2.5 Coder model version 7b
- `run qwen2.5-coder:14b` - Run Qwen2.5 Coder model version 14b
- `run qwen2.5-coder:32b` - Run Qwen2.5 Coder model version 32b
- `run gemma3:1b` - Run Gemma3 model version 1b
- `run gemma3:4b` - Run Gemma3 model version 4b
- `run gemma3:12b` - Run Gemma3 model version 12b
- `run gemma3:27b` - Run Gemma3 model version 27b
- `run qwq` - Run QwQ model
- `run command-a` - Run Command-A
- `run phi4-mini` - Run Phi4 mini model
- `run granite3.2:8b` - Run Granite3.2 model version 8b
- `run granite3.2:2b` - Run Granite3.2 model version 2b
- `run granite3.2-vision:2b` - Run Granite3.2 Vision model version 2b
- `run qwen-2-5-omni:7b` - Run Qwen-2.5 Omni model version 7b
- `run qvq:72b` - Run QVQ model version 72b
- `run qwen-2-5-vl:32b` - Run Qwen-2.5 VL model version 32b
- `run qwen-2-5-vl:72b` - Run Qwen-2.5 VL model version 72b
- `run llama-4-maverick:17b` - Run Llama-4 Maverick model version 17b
- `run llama-4-scout:17b` - Run Llama-4 Scout model version 17b
- `run deepcoder:1.5b` - Run DeepCoder model version 1.5b
- `run deepcoder:14b` - Run DeepCoder model version 14b
- `run mistral-small3.1` - Run Mistral small model version 3.1
- `help` - Display help information
- `image generation` - Generate images
- `video generation` - Generate videos
- `models` - List available models
- `models ls` - List available models
- `install 3d-slicer` - Install 3D Slicer
- `run 3d-slicer` - Run 3D Slicer
- `install simon` - Install Simon
- `run simon` - Run Simon
- `jupyter --version` - Display Jupyter version
- `grafana --version` - Display Grafana version
- `3d-slicer --version` - Display 3D Slicer version  
- `pin-evil` - evil mode
- `pin-main` - main mode
- `pin-cool` - cool mode
  - `install cool pin`
- `pin-cool-3` - cool-3 mode
  - `install cool pin-3`
- `pin-cool-4` - cool-4 mode
	- `install cool pin-4`  

etc.  

# Problems

| **Terminal** | **Problem description**      | **Cause**                                                                               | **Solution** | **Status** |
|--------------|------------------------------|-----------------------------------------------------------------------------------------|--------------|------------|
| P-Term       | p-term.bat                   | Die .bat  muss eine .env erstellen um `./install/cpp/install-vs.py` auszuführen!!!      | morgen...    | ✖          |
| PP-Term      | run-pp-term.bat /pp-term.exe | Verbessere der Instation von PP-Term                                                    | ...          | ✖          |
| PP-Term      | pp-term-3.py                 | Dur die neue Eingegabe von `user_input = input_line(pin)` ist tap nicht mher möglich!!! | ...          | ✖          |

## Lizenz

This project is licensed under the MIT license – see the [LICENSE](LICENSE) file for details.
