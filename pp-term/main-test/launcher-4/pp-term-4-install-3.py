import sys
import getpass
import subprocess
import threading
import time
import importlib.util
import os
import logging
from datetime import datetime

# Get current time
now = datetime.now()

# List of required packages
required_packages = [
    "requests", "ollama", "transformers", "numpy", "pandas", "python-dotenv", "beautifulsoup4",
    "PyQt6", "PyQt6-sip", "PyQt6-Charts", "PyQt6-WebEngine", "PyQt6-Charts", "keyboard", "pyreadline3",
    "requests", "psutil", "speedtest-cli", "colorama", "pyperclip", "termcolor", "docker", "flask", "rich",
    "typer", "click", "blessed", "prompt-toolkit", "tqdm", "watchdog", "fire", "torch", "torchvision", "torchaudio",
    "tensorflow", "tf-nightly", "notebook", "jupyterlab", "jax", "transformers", "chardet", "plotly"
]


# Function to activate the virtual environment
def activate_virtualenv(venv_path):
    """Activates an existing virtual environment."""
    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] Checking virtual environment path...")
    activate_script = os.path.join(venv_path, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_path,
                                                                                                          "bin",
                                                                                                          "activate")

    if not os.path.exists(activate_script):
        print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [ERROR] ❌ Virtual environment not found at {venv_path}.")
        sys.exit(1)

    os.environ["VIRTUAL_ENV"] = venv_path
    os.environ["PATH"] = os.path.join(venv_path, "Scripts") + os.pathsep + os.environ["PATH"]
    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] Virtual environment {venv_path} activated.")


# Function to ensure the required packages are installed
def ensure_packages_installed(packages: list[str]) -> None:
    """
    Ensures that the specified Python packages are installed.

    Installs only missing packages. Quietly, fast, and robust.
    """

    logging.basicConfig(level=logging.INFO, format='%(message)s')

    missing = [pkg for pkg in packages if importlib.util.find_spec(pkg) is None]

    if not missing:
        print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] ✅ All required packages are already installed.")
        return

    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] Missing packages: {', '.join(missing)}")

    try:
        print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] Starting installation of missing packages...")

        # Run subprocess without --quiet so full output is shown
        result = subprocess.run(
            [
                sys.executable, "-m", "pip", "install", "--disable-pip-version-check",
                *missing
            ],
            check=True,
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE  # Capture standard error
        )

        # Print the full output from the installation process
        print(f"{result.stdout.decode()}")

        # If there are any errors during installation, print the error
        if result.stderr:
            print(
                f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [ERROR] Installation errors:\n{result.stderr.decode()}")

        print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] ✅ All missing packages installed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [ERROR] ❌ Failed to install required packages.")
        print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] Error details: {e}")


# Activate virtual environment and ensure packages are installed
venv_path = f"C:\\Users\\{os.getlogin()}\\p-terminal\\pp-term\\.env"
print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] Starting to activate the virtual environment...")
activate_virtualenv(venv_path)
print(f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] Checking and installing required packages...")
ensure_packages_installed(required_packages)
print(
    f"[{now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}] [INFO] All packages are now installed and the environment is activated.")
