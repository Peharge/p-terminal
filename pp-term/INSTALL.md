# **_Installing PP-Terminal_**

<p align="left">
    <img src="./icons/p-term-banner-3.svg" alt="peharge"/>
    <img src="./icons/pp-term-banner-3.svg" alt="peharge"/>
    <img src="./icons/peharge-banner-3.svg" alt="peharge"/>
</p>

<p align="center">
 <img width="600" src="https://github.com/Peharge/p-terminal-images/raw/main/images/p-term-demo-5.png" alt="peharge"/>
</p>

Download the [pp-term.bat](https://github.com/Peharge/p-terminal/blob/main/pp-term/run-pp-term.bat) file and double-click it. You're ready to go! Have fun with pp-terminal and you can always start it with `pp-term/run-pp-term.bat` (ca. 5 min) / `pp-term/run-pp-term-fast.bat` (ca. 3-5 sek) after installation. If you want, you can further enhance your terminal with PP Terminal Themes/Pins: [PP Terminal Themes/Pins](./pp-term/THEMES.md)

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
