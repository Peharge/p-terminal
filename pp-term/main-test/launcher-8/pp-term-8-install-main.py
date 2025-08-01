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

import sys
import os
import subprocess
import importlib.util
from pathlib import Path
import logging
from datetime import datetime

# Log setup: timestamp with milliseconds
log_path = Path(__file__).parent / "installer.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_path, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# List of required packages
REQUIRED_PACKAGES = [
    "requests", "ollama", "transformers", "numpy", "pandas", "python-dotenv", "beautifulsoup4",
    "PyQt6", "PyQt6-sip", "PyQt6-Charts", "PyQt6-WebEngine", "keyboard", "pyreadline3",
    "psutil", "speedtest-cli", "colorama", "pyperclip", "termcolor", "docker", "flask",
    "typer", "click", "blessed", "prompt-toolkit", "tqdm", "watchdog", "fire", "notebook", "jupyter",
    "jupyterlab", "jax", "chardet", "plotly", "py-cpuinfo", "gputil", "tabulate", "pyqtgraph",
    "deep-translator", "duckduckgo-search", "pillow", "GitPython", "matplotlib", "pyinstaller",
    "virtualenv", "legacy-cgi", "colorama", "ipykernel", "ipython", "bash_kernel", "urllib3",
    "markdown", "cirq", "mysql-connector-python", "psycopg2-binary", "cx_Oracle", "pyodbc",
    "ibm_db ibm_db_dbi", "redis", "pymongo", "bson", "cassandra-driver", "python-arango", "neo4j",
    "pyorient", "ravendb", "boto3", "yfinance", "monai", "nibabel", "monailabel", "monai-deploy-app-sdk",
    "scikit-image", "pydicom", "SimpleITK", "pywin32"
]


def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def activate_virtualenv(path: Path) -> None:
    """
    Activates a virtual environment at the given path.
    """
    activate_script = path / ("Scripts/activate" if os.name == "nt" else "bin/activate")
    if not activate_script.exists():
        logging.error(f"[ERROR] ❌ Virtual environment not found at: {path}")
        sys.exit(1)

    # Update environment variables
    os.environ["VIRTUAL_ENV"] = str(path)
    bin_dir = path / ('Scripts' if os.name == 'nt' else 'bin')
    os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ.get("PATH", "")
    logging.info(f"[INFO] Virtual environment activated: {path}")


def ensure_packages(packages: list[str]) -> None:
    """
    Checks and installs missing packages one by one, logging each step.
    """
    missing = []
    for pkg in packages:
        if importlib.util.find_spec(pkg) is None:
            missing.append(pkg)
    if not missing:
        logging.info("[PASS] ✅ All required packages are already installed.")
        return

    logging.info(f"[INFO] Found {len(missing)} missing packages: {', '.join(missing)}")
    for index, pkg in enumerate(missing, 1):
        print("")
        logging.info(f"[INFO] [{index}/{len(missing)}] Installing package: {pkg}")
        try:
            # Install the package
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", pkg, "--disable-pip-version-check"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode == 0:
                # Output the complete pip install result
                logging.info(f"[INFO] Running: pip install {pkg}")
                logging.info(f"[INFO] {result.stdout}")  # Full output
                logging.info(f"[PASS] ✅ {pkg} successfully installed.")
            else:
                # Error output in case of problems
                logging.error(f"[ERROR] ❌ Failed to install {pkg}:")
                logging.error(result.stderr)
        except Exception as e:
            logging.error(f"[ERROR] ❌ Error installing {pkg}: {e}")
    logging.info("[PASS] ✅ All missing packages processed.")


def main():
    venv_path = Path(os.getenv('VENV_PATH', Path.home() / 'p-terminal' / 'pp-term' / '.env'))
    logging.info("[INFO] Starting virtual environment activation...")
    activate_virtualenv(venv_path)
    logging.info("[INFO] Starting package checks and installations...")
    ensure_packages(REQUIRED_PACKAGES)
    logging.info("[PASS] ✅ Environment setup complete.")


if __name__ == '__main__':
    main()
