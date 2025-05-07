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
import signal
import logging
import threading
import subprocess
from pathlib import Path
from datetime import datetime
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from typing import List, Dict, Callable, Tuple
from pathlib import Path
from typing import Tuple
import logging.handlers


# Konfiguration
DEFAULT_THREADS_IO      = 8
DEFAULT_PROCESSES_CPU   = os.cpu_count() or 4
LOG_FILE                = Path("doctor.log")
EXCLUDE_DIRS = {
    ".git", ".venv", "__pycache__",
    "Lib", "Scripts", "Include",         # typische venv-Ordner
    "site-packages", "dist-packages",
    ".env", "main-test"
}
EXCLUDE_PATTERNS        = {".*"}  # regex für versteckte Dateien/Ordner
FILE_SIZE_LIMIT         = 10 * 1024 * 1024
FILE_AGE_LIMIT_DAYS     = 365

# Zu-COMMAND-Mapping pro Dateiendung
CHECK_MAP: Dict[str, Callable[[Path], Tuple[bool, str]]] = {}

# Logging Setup
logger = logging.getLogger("Doctor")
logger.setLevel(logging.INFO)
fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
# Console
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(fmt)
# Rolling File
fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=3)
fh.setFormatter(fmt)
logger.addHandler(ch)
logger.addHandler(fh)

# Global Report
class Report:
    def __init__(self):
        self.passes = []
        self.issues = []
        self._lock  = threading.Lock()

    def add_pass(self, msg: str):
        with self._lock:
            logger.info(msg)
            self.passes.append(msg)

    def add_issue(self, msg: str):
        with self._lock:
            logger.warning(msg)
            self.issues.append(msg)

    def summary(self):
        print("")
        logger.info(f"SCAN SUMMARY ({len(self.issues)} issues):")
        for m in self.issues:
            print(f"❌ {m}")

report = Report()

# Abbruch-Handling
def _handle_exit(signum, frame):
    report.summary()
    sys.exit(0)

signal.signal(signal.SIGINT, _handle_exit)
signal.signal(signal.SIGTERM, _handle_exit)

def monitor_quit():
    try:
        while True:
            if input().strip().lower() == 'q':
                logger.info("Quit key detected.")
                report.summary()
                os._exit(0)
    except Exception:
        pass

threading.Thread(target=monitor_quit, daemon=True).start()

# Hilfsfunktionen
def run_cmd(cmd: List[str], cwd: Path = None, timeout: int = 30) -> Tuple[int, str, str]:
    try:
        res = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True, timeout=timeout,
                             encoding="utf-8", errors="replace")

        return res.returncode, res.stdout.strip(), res.stderr.strip()
    except Exception as e:
        return -1, "", str(e)

def is_excluded(path: Path) -> bool:
    # Exclude hidden or configured folders
    if any(part in EXCLUDE_DIRS for part in path.parts):
        return True
    name = path.name
    if any(name.startswith(pat) for pat in EXCLUDE_PATTERNS):
        return True
    return False

def check_file_properties(path: Path):
    try:
        stat = path.stat()
        size = stat.st_size
        mtime= datetime.fromtimestamp(stat.st_mtime)
        # Size
        if size > FILE_SIZE_LIMIT:
            report.add_issue(f"Large file ({size}B): {path}")
        else:
            report.add_pass(f"Size OK: {path}")
        # Age
        if (datetime.now() - mtime).days > FILE_AGE_LIMIT_DAYS:
            report.add_issue(f"Old file ({mtime.date()}): {path}")
        else:
            report.add_pass(f"Recent file: {path}")
        # Permissions
        perms = "".join(p for p, ok in [("r", os.R_OK), ("w", os.W_OK), ("x", os.X_OK)]
                        if os.access(path, ok))
        if perms:
            report.add_pass(f"Perms [{perms}]: {path}")
        else:
            report.add_issue(f"No perms: {path}")
    except Exception as e:
        report.add_issue(f"Prop check failed: {path} ({e})")

# Datei-Checks pro Sprache/Extension
def python_check(path: Path):
    try:
        import ast, py_compile
        src = path.read_text(encoding="utf-8", errors="replace")
        ast.parse(src)
        report.add_pass(f"Python syntax OK: {path}")
        py_compile.compile(str(path), doraise=True)
        report.add_pass(f"Python bytecode OK: {path}")
    except Exception as e:
        report.add_issue(f"Python error: {path} ({e})")

from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

def _vs_build_check(args):
    path, bat_path, report_label = args
    if not bat_path.is_file():
        report.add_issue(f"{report_label} batch not found: {bat_path}")
        return
    code, out, err = run_cmd(["cmd", "/C", str(bat_path), str(path)])
    msg = err or out or f"Exit code {code}"
    if code == 0:
        report.add_pass(f"{report_label} syntax OK: {path}")
    else:
        report.add_issue(f"{report_label} syntax fail: {path} ({msg})")

def parallel_checks(paths: list[Path]):
    tasks = []
    base = Path(__file__).parent
    for path in paths:
        tasks.append((path, base / "peharge-c-compiler" / "build_peharge_c.bat", "C"))
        tasks.append((path, base / "peharge-cpp-compiler" / "build_peharge.bat", "C++"))
    # Anzahl Workers anpassen: z. B. CPU-Kerne × 2
    with ProcessPoolExecutor(max_workers=8) as exe:
        futures = [exe.submit(_vs_build_check, t) for t in tasks]
        for f in as_completed(futures):
            # hier ggf. Exceptions abfangen
            f.result()

""" 
def rust_project_check(root: Path):
    code, out, err = run_cmd(["cargo","check"], cwd=root)
    if code == 0:
        report.add_pass(f"Rust cargo OK: {root}")
    else:
        report.add_issue(f"Rust cargo fail: {root} ({err or out})")
"""

def bat_check(path: Path):
    try:
        _ = path.read_text(encoding="utf-8", errors="replace")
        report.add_pass(f"Batch readable: {path}")
    except Exception as e:
        report.add_issue(f"Batch error: {path} ({e})")

def go_project_check(root: Path):
    if (root/"go.mod").exists():
        for cmd,name in [(["go","build","./..."],"Go build"), (["go","test","./..."],"Go test")]:
            code,out,err = run_cmd(cmd, cwd=root)
            (report.add_pass if code==0 else report.add_issue)(f"{name} {('OK' if code==0 else 'fail')}: {root}")

def node_project_check(root: Path):
    if (root/"package.json").exists():
        code,out,err = run_cmd(["npm","ci","--dry-run"], cwd=root)
        (report.add_pass if code==0 else report.add_issue)(f"npm ci {'OK' if code==0 else 'fail'}: {root}")
        code,out,err = run_cmd(["npx","eslint","."], cwd=root)
        (report.add_pass if code==0 else report.add_issue)(f"ESLint {'OK' if code==0 else 'fail'}: {root}")

def dotnet_project_check(root: Path):
    for sln in root.glob("*.sln"):
        for cmd,name in [(["dotnet","build",str(sln)],".NET build"), (["dotnet","test",str(sln)],".NET test")]:
            code,out,err = run_cmd(cmd, cwd=root)
            (report.add_pass if code==0 else report.add_issue)(f"{name} {'OK' if code==0 else 'fail'}: {sln}")

def docker_project_check(root: Path):
    if (root/"Dockerfile").exists():
        code,out,err = run_cmd(["docker","build","-t","doctor-img","."], cwd=root)
        (report.add_pass if code==0 else report.add_issue)(f"Docker build {'OK' if code==0 else 'fail'}: {root}")
    if (root/"docker-compose.yml").exists():
        code,out,err = run_cmd(["docker-compose","config"], cwd=root)
        (report.add_pass if code==0 else report.add_issue)(f"docker-compose config {'OK' if code==0 else 'fail'}: {root}")

# Mapping Endungen → Funktionen
CHECK_MAP.update({
    ".py":   python_check,
    ".c":    parallel_checks,
    ".cpp":  parallel_checks, ".cc": parallel_checks, ".cxx": parallel_checks,
    ".h":    parallel_checks, ".hpp": parallel_checks,
    ".bat":  bat_check, ".cmd": bat_check,
})

# Haupt-Scan-Logik
def scan_project(root: Path, args):
    # 1) Einmalige Projekt-Checks für Cargo, Go, Node, .NET, Docker
    with ThreadPoolExecutor(max_workers=DEFAULT_THREADS_IO) as tpe:
        # tpe.submit(rust_project_check, root)
        tpe.submit(go_project_check, root)
        tpe.submit(node_project_check, root)
        tpe.submit(dotnet_project_check, root)
        tpe.submit(docker_project_check, root)

    # 2) Dateien sammeln
    files = [p for p in root.rglob("*") if p.is_file() and not is_excluded(p)]
    logger.info(f"Found {len(files)} files to check.")

    # 3) File-Props und Sprach-Checks parallel
    def worker(path: Path):
        check_file_properties(path)
        ext = path.suffix.lower()
        func = CHECK_MAP.get(ext)
        if func:
            func(path)

    # I/O-lastige Dateieigenschaften per ThreadPool
    with ThreadPoolExecutor(max_workers=args.threads_io) as tpe:
        futures = [tpe.submit(worker, p) for p in files]
        for _ in as_completed(futures): pass

    report.summary()

# CLI
def main():
    p = ArgumentParser(description="Doctor Script for full-stack checks")
    p.add_argument("-p","--path",      type=Path, default=Path(r"C:\Users\julia\p-terminal\pp-term"))
    p.add_argument("-tio","--threads-io", type=int, default=DEFAULT_THREADS_IO)
    args = p.parse_args()

    logger.info(f"Start scanning {args.path}")
    scan_project(args.path, args)
    print("")

if __name__ == "__main__":
    main()
