/*
   Englisch | Peharge: This source code is released under the MIT License.

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
*/

/*
   Deutsch | Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.

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
*/

/*
   Français | Peharge: Ce code source est publié sous la licence MIT.

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
*/

// src/main.rs

use clap::Parser;
use chrono::{DateTime, Local};
use flexi_logger::{Duplicate, FileSpec, Logger, WriteMode, Criterion, Naming, Cleanup};
use log::{info, warn, LevelFilter};
use signal_hook::consts::signal::*;
use signal_hook::iterator::Signals;
use std::collections::{HashMap, HashSet};
use std::ffi::OsStr;
use std::fs;
use std::io::{self, BufRead};
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};
use std::sync::{Arc, Mutex};
use std::thread;
use threadpool::ThreadPool;
use walkdir::WalkDir;
use regex::Regex;
use wait_timeout::ChildExt;
use std::time::{Duration, SystemTime};
use once_cell::sync::Lazy;
use glob::glob;

/// Konfigurationen und Konstanten
static DEFAULT_THREADS_IO: usize = 8;
static DEFAULT_PROCESSES_CPU: usize = num_cpus::get();
static LOG_FILE: &str = "doctor.log";

static EXCLUDE_DIRS: Lazy<HashSet<&'static str>> = Lazy::new(|| {
    let mut s = HashSet::new();
    for &d in &[
        ".git", ".venv", "__pycache__", "Lib", "Scripts", "Include",
        "site-packages", "dist-packages", ".env", "main-test", "icons", "static",
    ] {
        s.insert(d);
    }
    s
});
static EXCLUDE_PATTERNS: Lazy<Vec<Regex>> = Lazy::new(|| {
    vec![
        Regex::new(r"^\..*").unwrap(),     // Versteckte Dateien/Ordner (beginnt mit Punkt)
        Regex::new(r"~$").unwrap(),        // Backup-Dateien (endet mit ~)
    ]
});

static FILE_SIZE_LIMIT: u64 = 10 * 1024 * 1024; // 10 MB
static FILE_AGE_LIMIT_DAYS: i64 = 365;

/// Mapping Endung -> Check-Funktion
type CheckerFn = fn(PathBuf, Arc<Report>);

static mut CHECK_MAP: Option<HashMap<&'static str, CheckerFn>> = None;

/// CLI-Argumente
#[derive(Parser)]
#[command(name = "Doctor", about = "Doctor Script für Full-Stack Checks")]
struct Args {
    /// Pfad, der gescannt werden soll
    #[arg(short, long, value_name = "PATH", default_value_t = default_scan_path())]
    path: PathBuf,

    /// Anzahl Threads für I/O-intensive Checks
    #[arg(short = 't', long = "threads-io", default_value_t = DEFAULT_THREADS_IO)]
    threads_io: usize,
}

fn default_scan_path() -> PathBuf {
    // Standardpfad: C:\Users\<User>\p-terminal\pp-term
    let home = std::env::var("USERPROFILE").unwrap_or_else(|_| ".".into());
    Path::new(&home).join("p-terminal").join("pp-term")
}

/// Bericht-Struktur für Passes und Issues
struct Report {
    passes: Mutex<Vec<String>>,
    issues: Mutex<Vec<String>>,
}

impl Report {
    fn new() -> Self {
        Report {
            passes: Mutex::new(Vec::new()),
            issues: Mutex::new(Vec::new()),
        }
    }

    fn add_pass(&self, msg: String) {
        info!("{}", &msg);
        if let Ok(mut v) = self.passes.lock() {
            v.push(msg);
        }
    }

    fn add_issue(&self, msg: String) {
        warn!("{}", &msg);
        if let Ok(mut v) = self.issues.lock() {
            v.push(msg);
        }
    }

    fn summary(&self) {
        println!();
        let issues = self.issues.lock().unwrap();
        if !issues.is_empty() {
            info!("Scan summary ({} issues):", issues.len());
            for issue in issues.iter() {
                println!("❌ {}", issue);
            }
        } else {
            info!("✅ PP-Term Scan did not detect any problems.");
        }
    }
}

/// Läuft einen externen Befehl mit Timeout und gibt (Exit-Code, stdout, stderr) zurück
fn run_cmd(cmd: &[&str], cwd: Option<&Path>, timeout_secs: u64) -> (i32, String, String) {
    let mut command = Command::new(cmd[0]);
    for arg in &cmd[1..] {
        command.arg(arg);
    }
    if let Some(c) = cwd {
        command.current_dir(c);
    }
    command.stdin(Stdio::null())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped());

    match command.spawn() {
        Ok(mut child) => {
            let timeout = Duration::from_secs(timeout_secs);
            match child.wait_timeout(timeout).unwrap() {
                Some(status) => {
                    let code = status.code().unwrap_or(-1);
                    let mut stdout = String::new();
                    let mut stderr = String::new();
                    if let Some(mut out) = child.stdout.take() {
                        let _ = io::Read::read_to_string(&mut out, &mut stdout);
                    }
                    if let Some(mut err) = child.stderr.take() {
                        let _ = io::Read::read_to_string(&mut err, &mut stderr);
                    }
                    (code, stdout.trim().into(), stderr.trim().into())
                }
                None => {
                    // Timeout: Prozess beenden
                    let _ = child.kill();
                    ( -1, "".into(), format!("Timeout after {}s", timeout_secs) )
                }
            }
        }
        Err(e) => (-1, "".into(), format!("Spawn failed: {}", e)),
    }
}

/// Prüft, ob ein Pfad ausgeschlossen werden soll (Verzeichnisname oder versteckt/Backup)
fn is_excluded(path: &Path) -> bool {
    for part in path.components() {
        if let std::path::Component::Normal(os_str) = part {
            if let Some(s) = os_str.to_str() {
                if EXCLUDE_DIRS.contains(s) {
                    return true;
                }
            }
        }
    }
    if let Some(fname) = path.file_name().and_then(OsStr::to_str) {
        for re in EXCLUDE_PATTERNS.iter() {
            if re.is_match(fname) {
                return true;
            }
        }
    }
    false
}

/// Prüft Dateigröße, Alter und Berechtigungen
fn check_file_properties(path: PathBuf, report: Arc<Report>) {
    match fs::metadata(&path) {
        Ok(metadata) => {
            let size = metadata.len();
            let mtime = metadata.modified().unwrap_or(SystemTime::UNIX_EPOCH);
            let mtime_dt: DateTime<Local> = mtime.into();

            // Größe
            if size > FILE_SIZE_LIMIT {
                report.add_issue(format!("Large file ({} B): {}", size, path.display()));
            } else {
                report.add_pass(format!("Size OK: {}", path.display()));
            }

            // Alter
            let age_days = Local::now().signed_duration_since(mtime_dt).num_days().abs();
            if age_days > FILE_AGE_LIMIT_DAYS {
                report.add_issue(format!("Old file ({}): {}", mtime_dt.format("%Y-%m-%d"), path.display()));
            } else {
                report.add_pass(format!("Recent file: {}", path.display()));
            }

            // Berechtigungen
            let mut perms = String::new();
            if metadata.permissions().readonly() {
                perms.push('r');
            } else {
                perms.push_str("rw");
            }
            if perms.is_empty() {
                report.add_issue(format!("No perms: {}", path.display()));
            } else {
                report.add_pass(format!("Perms [{}]: {}", perms, path.display()));
            }
        }
        Err(e) => {
            report.add_issue(format!("Prop check failed: {} ({})", path.display(), e));
        }
    }
}

/// Python-Datei syntaktisch prüfen (py_compile)
fn python_check(path: PathBuf, report: Arc<Report>) {
    let path_str = path.to_string_lossy();
    let (code, _out, err) = run_cmd(&["python", "-m", "py_compile", &path_str], None, 30);
    if code == 0 {
        report.add_pass(format!("Python syntax OK: {}", path.display()));
    } else {
        report.add_issue(format!("Python error: {} ({})", path.display(), err));
    }
}

/// Rust-Datei syntaktisch prüfen (rustc --emit=metadata)
fn rust_file_check(path: PathBuf, report: Arc<Report>) {
    let path_str = path.to_string_lossy();
    let (code, _out, err) = run_cmd(&["rustc", "--emit", "metadata", &path_str], None, 30);
    if code == 0 {
        report.add_pass(format!(".rs syntax OK: {}", path.display()));
    } else {
        report.add_issue(format!(".rs error: {} ({})", path.display(), err));
    }
}

/// C/C++-Dateien per externem Batch-Skript prüfen (VS Build)
fn vs_build_check(args: (PathBuf, PathBuf, String), report: Arc<Report>) {
    let (path, bat_path, label) = args;
    if !bat_path.is_file() {
        report.add_issue(format!("{} batch not found: {}", label, bat_path.display()));
        return;
    }
    let path_str = path.to_string_lossy();
    let bat_str = bat_path.to_string_lossy();
    let (code, out, err) = run_cmd(&["cmd", "/C", &bat_str, &path_str], None, 30);
    let msg = if !err.is_empty() { err } else if !out.is_empty() { out } else { format!("Exit code {}", code) };
    if code == 0 {
        report.add_pass(format!("{} syntax OK: {}", label, path.display()));
    } else {
        report.add_issue(format!("{} syntax fail: {} ({})", label, path.display(), msg));
    }
}

fn parallel_checks(path: PathBuf, report: Arc<Report>) {
    let exe_dir = std::env::current_exe().unwrap_or_else(|_| PathBuf::from("."));
    let base = exe_dir.parent().unwrap_or(&exe_dir);
    let c_bat = base.join("peharge-c-compiler").join("build_peharge_c.bat");
    let cpp_bat = base.join("peharge-cpp-compiler").join("build_peharge.bat");

    let mut handles = Vec::new();
    let report_clone = Arc::clone(&report);
    let path_clone = path.clone();
    let c_label = String::from("C");
    let cpp_label = String::from("C++");

    {
        let report_inner = Arc::clone(&report_clone);
        let path_inner = path_clone.clone();
        let bat_inner = c_bat.clone();
        let label_inner = c_label.clone();
        handles.push(thread::spawn(move || {
            vs_build_check((path_inner, bat_inner, label_inner), report_inner);
        }));
    }
    {
        let report_inner = Arc::clone(&report_clone);
        let path_inner = path_clone;
        let bat_inner = cpp_bat.clone();
        let label_inner = cpp_label.clone();
        handles.push(thread::spawn(move || {
            vs_build_check((path_inner, bat_inner, label_inner), report_inner);
        }));
    }

    for h in handles {
        let _ = h.join();
    }
}

/// Batch-Datei nur lesbar prüfen
fn bat_check(path: PathBuf, report: Arc<Report>) {
    match fs::read_to_string(&path) {
        Ok(_) => report.add_pass(format!("Batch readable: {}", path.display())),
        Err(e) => report.add_issue(format!("Batch error: {} ({})", path.display(), e)),
    }
}

/// Go-Projekte: build + test
fn go_project_check(root: PathBuf, report: Arc<Report>) {
    let go_mod = root.join("go.mod");
    if go_mod.exists() {
        let (code_build, _o, eb) = run_cmd(&["go", "build", "./..."], Some(&root), 60);
        if code_build == 0 {
            report.add_pass(format!("Go build OK: {}", root.display()));
        } else {
            report.add_issue(format!("Go build fail: {} ({})", root.display(), eb));
        }
        let (code_test, _o, et) = run_cmd(&["go", "test", "./..."], Some(&root), 60);
        if code_test == 0 {
            report.add_pass(format!("Go test OK: {}", root.display()));
        } else {
            report.add_issue(format!("Go test fail: {} ({})", root.display(), et));
        }
    }
}

/// Node-Projekte: npm ci dry-run + ESLint
fn node_project_check(root: PathBuf, report: Arc<Report>) {
    let pkg = root.join("package.json");
    if pkg.exists() {
        let (code_ci, _o, eci) = run_cmd(&["npm", "ci", "--dry-run"], Some(&root), 60);
        if code_ci == 0 {
            report.add_pass(format!("npm ci OK: {}", root.display()));
        } else {
            report.add_issue(format!("npm ci fail: {} ({})", root.display(), eci));
        }
        let (code_eslint, _o, eel) = run_cmd(&["npx", "eslint", "."], Some(&root), 60);
        if code_eslint == 0 {
            report.add_pass(format!("ESLint OK: {}", root.display()));
        } else {
            report.add_issue(format!("ESLint fail: {} ({})", root.display(), eel));
        }
    }
}

/// .NET-Projekte: build + test für *.sln Dateien
fn dotnet_project_check(root: PathBuf, report: Arc<Report>) {
    for entry in glob(&format!("{}/*.sln", root.display())).unwrap().flatten() {
        let sln = entry.clone();
        let (code_build, _o, eb) = run_cmd(&["dotnet", "build", sln.to_str().unwrap()], Some(&root), 120);
        if code_build == 0 {
            report.add_pass(format!(".NET build OK: {}", sln.display()));
        } else {
            report.add_issue(format!(".NET build fail: {} ({})", sln.display(), eb));
        }
        let (code_test, _o, et) = run_cmd(&["dotnet", "test", sln.to_str().unwrap()], Some(&root), 120);
        if code_test == 0 {
            report.add_pass(format!(".NET test OK: {}", sln.display()));
        } else {
            report.add_issue(format!(".NET test fail: {} ({})", sln.display(), et));
        }
    }
}

/// Docker-Projekte: Dockerfile build + docker-compose config
fn docker_project_check(root: PathBuf, report: Arc<Report>) {
    let dockerfile = root.join("Dockerfile");
    if dockerfile.exists() {
        let (code_build, _o, eb) = run_cmd(&["docker", "build", "-t", "doctor-img", "."], Some(&root), 120);
        if code_build == 0 {
            report.add_pass(format!("Docker build OK: {}", root.display()));
        } else {
            report.add_issue(format!("Docker build fail: {} ({})", root.display(), eb));
        }
    }
    let compose = root.join("docker-compose.yml");
    if compose.exists() {
        let (code_cfg, _o, ec) = run_cmd(&["docker-compose", "config"], Some(&root), 60);
        if code_cfg == 0 {
            report.add_pass(format!("docker-compose config OK: {}", root.display()));
        } else {
            report.add_issue(format!("docker-compose config fail: {} ({})", root.display(), ec));
        }
    }
}

/// Rust-Projekt mit Cargo check prüfen
fn rust_project_check(root: PathBuf, report: Arc<Report>) {
    let cargo_toml = root.join("Cargo.toml");
    if cargo_toml.exists() {
        let (code, _o, e) = run_cmd(&["cargo", "check"], Some(&root), 120);
        if code == 0 {
            report.add_pass(format!("Cargo check OK: {}", root.display()));
        } else {
            report.add_issue(format!("Cargo check fail: {} ({})", root.display(), e));
        }
    }
}

/// Initialisierung der CHECK_MAP
fn init_check_map() {
    let mut m: HashMap<&'static str, CheckerFn> = HashMap::new();
    m.insert(".py", python_check as CheckerFn);
    m.insert(".rs", rust_file_check as CheckerFn);
    m.insert(".c", parallel_checks as CheckerFn);
    m.insert(".cpp", parallel_checks as CheckerFn);
    m.insert(".cc", parallel_checks as CheckerFn);
    m.insert(".cxx", parallel_checks as CheckerFn);
    m.insert(".h", parallel_checks as CheckerFn);
    m.insert(".hpp", parallel_checks as CheckerFn);
    m.insert(".bat", bat_check as CheckerFn);
    m.insert(".cmd", bat_check as CheckerFn);
    unsafe {
        CHECK_MAP = Some(m);
    }
}

/// Haupt-Scan-Logik
fn scan_project(root: &Path, args: &Args, report: Arc<Report>) {
    // 1) Einmalige Projekt-Checks parallel (I/O-lastig)
    let tpe = ThreadPool::new(DEFAULT_THREADS_IO);

    {
        let rc = Arc::clone(&report);
        let rb = root.to_path_buf();
        tpe.execute(move || rust_project_check(rb, rc));
    }
    {
        let rc = Arc::clone(&report);
        let rb = root.to_path_buf();
        tpe.execute(move || go_project_check(rb, rc));
    }
    {
        let rc = Arc::clone(&report);
        let rb = root.to_path_buf();
        tpe.execute(move || node_project_check(rb, rc));
    }
    {
        let rc = Arc::clone(&report);
        let rb = root.to_path_buf();
        tpe.execute(move || dotnet_project_check(rb, rc));
    }
    {
        let rc = Arc::clone(&report);
        let rb = root.to_path_buf();
        tpe.execute(move || docker_project_check(rb, rc));
    }

    tpe.join();

    // 2) Dateien sammeln
    let mut files: Vec<PathBuf> = Vec::new();
    for entry in WalkDir::new(root).into_iter().filter_map(|e| e.ok()) {
        let p = entry.path().to_path_buf();
        if p.is_file() && !is_excluded(&p) {
            files.push(p);
        }
    }
    info!("Found {} files to check.", files.len());

    // 3) File-Props und Sprach-Checks parallel
    let pool = ThreadPool::new(args.threads_io);
    for path in files.into_iter() {
        let rep = Arc::clone(&report);
        pool.execute(move || {
            check_file_properties(path.clone(), Arc::clone(&rep));
            let ext = path.extension().and_then(OsStr::to_str).unwrap_or("").to_lowercase();
            unsafe {
                if let Some(ref cmap) = CHECK_MAP {
                    if let Some(f) = cmap.get(ext.as_str()) {
                        f(path.clone(), Arc::clone(&rep));
                    }
                }
            }
        });
    }
    pool.join();

    report.summary();
}

/// Thread, der auf 'q' in stdin wartet und Programm beendet
fn monitor_quit(report: Arc<Report>) {
    thread::spawn(move || {
        let stdin = io::stdin();
        for line in stdin.lock().lines() {
            if let Ok(inp) = line {
                if inp.trim().eq_ignore_ascii_case("q") {
                    info!("Quit key detected.");
                    report.summary();
                    std::process::exit(0);
                }
            }
        }
    });
}

/// Gibt aktuellen Timestamp mit Millisekunden
fn timestamp() -> String {
    let now: DateTime<Local> = Local::now();
    now.format("%Y-%m-%d %H:%M:%S.%3f").to_string()
}

fn main() {
    // CLI parsen
    let args = Args::parse();

    // Logging initialisieren (Konsolen- + Rolling File-Logger)
    Logger::try_with_str("info")
        .unwrap()
        .log_to_file(
            FileSpec::default().basename("doctor").suffix("log")
        )
        .duplicate_to_stdout(Duplicate::Info)
        .write_mode(WriteMode::BufferAndFlush)
        .rotate(
            Criterion::Size(5_000_000),
            Naming::Numbers,
            Cleanup::KeepLogFiles(3),
        )
        .start()
        .unwrap();

    // CHECK_MAP initialisieren
    init_check_map();

    let report = Arc::new(Report::new());

    // Signal-Handler für SIGINT und SIGTERM
    let signals = Signals::new(&[SIGINT, SIGTERM]).unwrap();
    let rep_for_signals = Arc::clone(&report);
    thread::spawn(move || {
        for _sig in signals.forever() {
            rep_for_signals.summary();
            std::process::exit(0);
        }
    });

    // 'q'-Monitor starten
    monitor_quit(Arc::clone(&report));

    info!(
        "Start scanning {} with PP-Term Scanner",
        args.path.display()
    );
    scan_project(&args.path, &args, Arc::clone(&report));
    println!(
        "[{}] [PASS] ✅ All tasks were completed successfully!\n",
        timestamp()
    );
}
