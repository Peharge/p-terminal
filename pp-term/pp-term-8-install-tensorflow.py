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

import sys
import os
import subprocess
import logging
from pathlib import Path
from datetime import datetime
import re

# Log setup: timestamp with milliseconds
log_path = Path(__file__).parent / "installer_tf.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_path, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)


def timestamp() -> str:
    """Returns current time formatted with milliseconds"""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


# Immer zu verwendendes Standardverzeichnis für die virtuelle Umgebung
DEFAULT_ENV_DIR = os.path.join("p-terminal", "pp-term", ".env")

def activate_virtualenv(path: Path = Path(DEFAULT_ENV_DIR)) -> None:
    """Aktiviert die virtuelle Umgebung im angegebenen Pfad."""
    activate_script = path / ("Scripts/activate" if os.name == "nt" else "bin/activate")

    if not activate_script.exists():
        logging.error(f"[ERROR] ❌ Virtual environment not found at: {path}")
        sys.exit(1)

    os.environ["VIRTUAL_ENV"] = str(path)
    bin_dir = path / ('Scripts' if os.name == 'nt' else 'bin')
    os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ.get("PATH", "")

    logging.info(f"[INFO] ✅ Virtual environment activated: {path}")


def detect_cuda_available() -> bool:
    """
    Checks if CUDA toolkit (nvcc) is available on the system.
    Returns True if nvcc is found, False otherwise.
    """
    try:
        subprocess.check_output(['nvcc', '--version'], stderr=subprocess.STDOUT)
        logging.info("[INFO] nvcc detected -> GPU-supported TensorFlow install")
        return True
    except Exception:
        logging.info("[INFO] nvcc not found -> CPU-only TensorFlow install")
        return False


def install_tensorflow(gpu: bool) -> None:
    """
    Installs TensorFlow via pip3.
    Uses tensorflow package which includes GPU support on compatible systems,
    or installs CPU-only TensorFlow if nvcc not found.
    """
    if gpu:
        pkg = 'tensorflow'
        logging.info(f"[INFO] Installing GPU-enabled TensorFlow: pip3 install {pkg}")
        cmd = ['pip3', 'install', pkg]
    else:
        pkg = 'tensorflow-cpu'
        logging.info(f"[INFO] Installing CPU-only TensorFlow: pip3 install {pkg}")
        cmd = ['pip3', 'install', pkg]

    logging.info(f"[INFO] Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode == 0:
        logging.info(f"[PASS] ✅ TensorFlow installation succeeded:\n{res.stdout}")
    else:
        logging.error(f"[ERROR] ❌ TensorFlow installation failed:\n{res.stderr}")


def main():
    venv = Path(os.getenv('VENV_PATH', Path.home() / '.venv'))
    logging.info(f"[INFO] [{timestamp()}] Starting virtual environment activation...")
    if venv.exists():
        activate_virtualenv(venv)
    else:
        logging.info(f"[INFO] [{timestamp()}] No venv at {venv}, using current environment")

    logging.info(f"[INFO] [{timestamp()}] Checking CUDA availability...")
    gpu_available = detect_cuda_available()

    logging.info(f"[INFO] [{timestamp()}] Starting TensorFlow installation...")
    install_tensorflow(gpu_available)
    logging.info(f"[PASS] ✅ Installation process complete.")


if __name__ == '__main__':
    main()
