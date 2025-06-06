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

//! P-Terminal (Rust-Version, stabile & performant)
//!
//! Eine plattformübergreifende Terminal-Emulation / Shell in Rust mit Fokus auf Stabilität und Geschwindigkeit.
//!
//! Funktionen:
//!  1. ASCII‐Banner mit Versionen aus JSON.
//!  2. 16‐Farb‐Palette (ANSI Colors 0–15).
//!  3. REPL‐Loop mit `rustyline` (Prompt, Eingabe, Shell‐Dispatch).
//!  4. Built‐in‐Befehle: `cd`, `exit`, `clear`, `help`, `sysinfo`.
//!  5. `rustyline` für Line‐Editing, History, Pfad‐Completion.
//!  6. Git‐Branch im Prompt, wenn in einem Git‐Repo via `git2`.
//!  7. Systemlast & Speicher‐Nutzung über `sysinfo` (synchron).
//!  8. Strg+C fängt ab (Return zum Prompt), Strg+D beendet.
//!  9. Speichert History in `~/.p-terminal_history`.
//! 10. Logging via `tracing`/`tracing-subscriber`.
//! 11. Fehlerbehandlung mit `anyhow`.

use anyhow::Result;
use chrono::Local;
use directories::BaseDirs;
use git2::Repository;
use rustyline::completion::FilenameCompleter;
use rustyline::error::ReadlineError;
use rustyline::highlight::MatchingBracketHighlighter;
use rustyline::hint::{HistoryHinter, Hinter};
use rustyline::validate::{ValidationContext, ValidationResult, Validator};
use rustyline::{Config, Editor, Helper};
use rustyline::history::FileHistory;
use serde_json::Value;
use std::env;
use std::fs::File;
use std::io::BufReader;
use std::path::PathBuf;
use std::process::{Command, Stdio};
use sysinfo::{CpuExt, System, SystemExt};
use tracing::{error, info};
use tracing_subscriber;
use whoami;

/// ANSI‐Farb‐Codes
const BLUE: &str = "\x1b[34m";
const CYAN: &str = "\x1b[36m";
const GREEN: &str = "\x1b[32m";
const RED: &str = "\x1b[31m";
const WHITE: &str = "\x1b[37m";
const RESET: &str = "\x1b[0m";

/// Custom Helper für `rustyline`: Completion, Hinting, Highlighting.
struct PHelper {
    completer: FilenameCompleter,
    hinter: HistoryHinter,
    highlighter: MatchingBracketHighlighter,
}

impl PHelper {
    fn new() -> Self {
        PHelper {
            completer: FilenameCompleter::new(),
            hinter: HistoryHinter {},
            highlighter: MatchingBracketHighlighter::new(),
        }
    }
}

impl Helper for PHelper {}

impl rustyline::completion::Completer for PHelper {
    type Candidate = rustyline::completion::Pair;
    fn complete(
        &self,
        line: &str,
        pos: usize,
        ctx: &rustyline::Context<'_>,
    ) -> rustyline::Result<(usize, Vec<Self::Candidate>)> {
        self.completer.complete(line, pos, ctx)
    }
}

impl Hinter for PHelper {
    type Hint = String;
    fn hint(
        &self,
        line: &str,
        pos: usize,
        ctx: &rustyline::Context<'_>,
    ) -> Option<String> {
        self.hinter.hint(line, pos, ctx)
    }
}

impl rustyline::highlight::Highlighter for PHelper {
    fn highlight_hint<'h>(&self, hint: &'h str) -> std::borrow::Cow<'h, str> {
        self.highlighter.highlight_hint(hint)
    }
    fn highlight<'l>(&self, line: &'l str, pos: usize) -> std::borrow::Cow<'l, str> {
        self.highlighter.highlight(line, pos)
    }
    fn highlight_char(&self, line: &str, pos: usize) -> bool {
        self.highlighter.highlight_char(line, pos)
    }
}

impl Validator for PHelper {
    fn validate(
        &self,
        _ctx: &mut ValidationContext<'_>,
    ) -> rustyline::Result<ValidationResult> {
        Ok(ValidationResult::Valid(None))
    }
}

/// Lade Versionen‐JSON synchron (einfach synchron, kein Cache).
fn load_versions() -> Option<serde_json::Map<String, Value>> {
    let username = whoami::username();
    let json_path: PathBuf = if cfg!(windows) {
        let base = env::var("USERPROFILE").unwrap_or_else(|_| format!("C:\\Users\\{}", username));
        PathBuf::from(base)
            .join("p-terminal")
            .join("p-term")
            .join("p-term-versions.json")
    } else {
        let base = BaseDirs::new()?.home_dir().to_path_buf();
        base.join("p-terminal")
            .join("p-term")
            .join("p-term-versions.json")
    };

    if let Ok(file) = File::open(&json_path) {
        let reader = BufReader::new(file);
        if let Ok(Value::Object(map)) = serde_json::from_reader(reader) {
            return Some(map);
        }
    }
    None
}

/// Drucke ASCII‐Banner mit ANSI‐Farben und Versions‐Informationen.
fn print_banner() {
    let user_name = whoami::username();

    println!(
        "{}██████╗{}{}    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗     {}",
        BLUE, RESET, WHITE, RESET
    );
    println!(
        "{}██╔══██╗{}{}   ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║     {}",
        BLUE, RESET, WHITE, RESET
    );
    println!(
        "{}██████╔╝{}{}█████╗██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║     {}",
        BLUE, RESET, WHITE, RESET
    );
    println!(
        "{}██╔═══╝ {}{}╚════╝██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║     {}",
        BLUE, RESET, WHITE, RESET
    );
    println!(
        "{}██║     {}{}      ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗{}",
        BLUE, RESET, WHITE, RESET
    );
    println!(
        "{}╚═╝     {}{}      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝{}",
        BLUE, RESET, WHITE, RESET
    );
    println!();
    println!(
        "{}A warm welcome, {}{}{}, to P-Terminal!{}",
        WHITE, CYAN, user_name, WHITE, RESET
    );
    println!(
        "{}Developed by Peharge and JK (Peharge Projects 2025){}",
        WHITE, RESET
    );
    println!(
        "{}Thank you so much for using P-Terminal. We truly appreciate your support ❤️{}",
        WHITE, RESET
    );
    println!();

    let github = hyperlink("[GitHub Repository]", "https://github.com/Peharge/p-terminal");
    let website = hyperlink("[Project Website]", "https://peharge.github.io/MAVIS-web/p-term.html");
    let learn = hyperlink("[Learn P-Terminal]", "https://peharge.github.io/MAVIS-web/p-term-hole.html");
    println!("{} {} {}", github, website, learn);
    println!();

    if let Some(map) = load_versions() {
        for (key, value) in &map {
            println!("{}{}{}: {}", BLUE, key, RESET, value);
        }
    } else {
        let username = whoami::username();
        let fallback_path = if cfg!(windows) {
            format!("C:\\Users\\{}\\p-terminal\\p-term\\p-term-versions.json", username)
        } else {
            let home = BaseDirs::new().unwrap().home_dir().to_string_lossy().into_owned();
            format!("{}/p-terminal/p-term/p-term-versions.json", home)
        };
        eprintln!(
            "[{}] [INFO] Version file nicht gefunden unter {}{}",
            Local::now().format("%Y-%m-%d %H:%M:%S"),
            fallback_path,
            RESET
        );
    }

    println!();

    // 16-Farb-Palette anzeigen
    for i in 0..8 {
        print!("\x1b[48;5;{}m  \x1b[0m", i);
    }
    println!();
    for i in 8..16 {
        print!("\x1b[48;5;{}m  \x1b[0m", i);
    }
    println!("\n");
}

/// OSC 8 Hyperlink‐Helper
fn hyperlink(text: &str, url: &str) -> String {
    format!("\x1b]8;;{}\x1b\\{}\x1b]8;;\x1b\\", url, text)
}

/// Retourniere " (branch)" falls aktuelles Verzeichnis in Git‐Repo liegt
fn git_branch_suffix() -> String {
    if let Ok(repo) = Repository::discover(env::current_dir().unwrap_or_else(|_| PathBuf::from("."))) {
        if let Ok(head) = repo.head() {
            if let Some(name) = head.shorthand() {
                return format!(" {}({}){}", BLUE, name, RESET);
            }
        }
    }
    String::new()
}

/// Zeige System‐Info synchron via `sysinfo`
fn display_sysinfo() {
    let mut sys = System::new_all();
    sys.refresh_all();
    let total_mem = sys.total_memory() / 1024;
    let used_mem = sys.used_memory() / 1024;
    let cpu_usage: f32 = sys
        .cpus()
        .iter()
        .map(|c| c.cpu_usage())
        .sum::<f32>()
        / sys.cpus().len() as f32;
    println!(
        "{}System Info:{} CPU Usage: {:.2}% | Memory: {} MiB / {} MiB",
        GREEN, RESET, cpu_usage, used_mem, total_mem
    );
}

/// Built‐in‐Befehle
enum Builtin {
    Cd,
    Exit,
    Clear,
    Help,
    SysInfo,
    Other,
}

/// Parst das erste Token auf einen Built‐in
fn parse_builtin(cmd: &str) -> Builtin {
    let mut parts = cmd.trim().split_whitespace();
    match parts.next() {
        Some("cd") => Builtin::Cd,
        Some("exit") | Some("quit") => Builtin::Exit,
        Some("clear") => Builtin::Clear,
        Some("help") => Builtin::Help,
        Some("sysinfo") => Builtin::SysInfo,
        _ => Builtin::Other,
    }
}

/// Change directory: `cd <Pfad>` oder ohne Arg → Home
fn handle_cd(args: &[&str]) {
    let target = if args.len() >= 2 {
        args[1]
    } else if cfg!(windows) {
        &env::var("USERPROFILE").unwrap_or_else(|_| ".".into())
    } else {
        &env::var("HOME").unwrap_or_else(|_| ".".into())
    };
    if let Err(e) = env::set_current_dir(target) {
        eprintln!("{}cd: {}: {}{}", RED, target, e, RESET);
    }
}

/// Zeigt die Hilfe‐Ansicht (farblich formatiert)
fn handle_help() {
    println!("{}Built-in Befehle:{}", GREEN, RESET);
    println!("  {}cd{} [<Pfad>]    Verzeichnis wechseln", CYAN, RESET);
    println!("  {}exit{}, {}quit{}   P-Terminal beenden", CYAN, RESET, CYAN, RESET);
    println!("  {}clear{}         Screen clearen", CYAN, RESET);
    println!("  {}help{}          Diese Hilfe anzeigen", CYAN, RESET);
    println!("  {}sysinfo{}       System-Info anzeigen", CYAN, RESET);
}

/// Clear Screen (ANSI)
fn handle_clear() {
    print!("\x1B[2J\x1B[H");
}

/// Führt externe Befehle synchron aus. Dabei wird zuerst versucht, PowerShell (bzw. pwsh) zu verwenden.
/// Falls das gewählte Shell-Programm nicht verfügbar ist, wird automatisch auf cmd (Windows) bzw. sh (Unix) umgeschaltet.
fn spawn_shell_command(line: &str) {
    #[cfg(windows)]
    {
        // Prüfe, ob PowerShell verfügbar ist
        let use_powershell = Command::new("powershell.exe")
            .arg("-NoLogo")
            .arg("-Command")
            .arg("exit")
            .status()
            .map(|s| s.success())
            .unwrap_or(false);

        if use_powershell {
            let status = Command::new("powershell.exe")
                .arg("-NoLogo")
                .arg("-NoProfile")
                .arg("-Command")
                .arg(line)
                .stdin(Stdio::inherit())
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .status();

            match status {
                Ok(s) if s.success() => (),
                Ok(s) => error!("PowerShell-Befehl `{}` mit Exit-Code {:?} beendet.", line, s.code()),
                Err(e) => error!("Fehler beim Ausführen von PowerShell: {}", e),
            }
        } else {
            // Fallback zu cmd.exe
            let status = Command::new("cmd.exe")
                .arg("/C")
                .arg(line)
                .stdin(Stdio::inherit())
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .status();

            match status {
                Ok(s) if s.success() => (),
                Ok(s) => error!("cmd.exe-Befehl `{}` mit Exit-Code {:?} beendet.", line, s.code()),
                Err(e) => error!("Fehler beim Ausführen von cmd.exe: {}", e),
            }
        }
    }

    #[cfg(not(windows))]
    {
        // Unter Unix: Zuerst versuchen wir pwsh, andernfalls sh
        let use_pwsh = Command::new("pwsh")
            .arg("-NoLogo")
            .arg("-Command")
            .arg("exit")
            .status()
            .map(|s| s.success())
            .unwrap_or(false);

        if use_pwsh {
            let status = Command::new("pwsh")
                .arg("-NoLogo")
                .arg("-NoProfile")
                .arg("-Command")
                .arg(line)
                .stdin(Stdio::inherit())
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .status();

            match status {
                Ok(s) if s.success() => (),
                Ok(s) => error!("pwsh-Befehl `{}` mit Exit-Code {:?} beendet.", line, s.code()),
                Err(e) => error!("Fehler beim Ausführen von pwsh: {}", e),
            }
        } else {
            let status = Command::new("sh")
                .arg("-c")
                .arg(line)
                .stdin(Stdio::inherit())
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .status();

            match status {
                Ok(s) if s.success() => (),
                Ok(s) => error!("sh-Befehl `{}` mit Exit-Code {:?} beendet.", line, s.code()),
                Err(e) => error!("Fehler beim Ausführen von sh: {}", e),
            }
        }
    }
}

fn main() -> Result<()> {
    // Initialisiere Logging (Level wird per ENV gesetzt, z.B. `export RUST_LOG=info`)
    let subscriber = tracing_subscriber::FmtSubscriber::builder()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .finish();
    tracing::subscriber::set_global_default(subscriber)?;

    // Banner ausgeben
    print_banner();

    // Konfiguriere rustyline
    let config = Config::builder()
        .history_ignore_space(true)
        .auto_add_history(true)
        .build();
    let mut rl: Editor<PHelper, FileHistory> = Editor::with_config(config)?;
    rl.set_helper(Some(PHelper::new()));

    // Lade History
    let history_path = BaseDirs::new()
        .map(|d| d.home_dir().join(".p-terminal_history"))
        .unwrap_or_else(|| PathBuf::from(".p-terminal_history"));
    if let Some(hp_str) = history_path.to_str() {
        let _ = rl.load_history(hp_str);
    }

    // REPL-Loop
    loop {
        // Prompt bauen: user@host(git_branch) cwd>
        let username = whoami::username();
        let hostname = whoami::fallible::hostname().unwrap_or_else(|_| "unknown".into());
        let cwd = env::current_dir().unwrap_or_else(|_| PathBuf::from("."));
        let cwd_str = cwd.to_string_lossy();
        let git_suffix = git_branch_suffix();
        let prompt = format!(
            "{}{}@{}{}{} {}> {}",
            BLUE, username, hostname, RESET, git_suffix, cwd_str, RESET
        );

        match rl.readline(&prompt) {
            Ok(line) => {
                let trimmed = line.trim();
                if trimmed.is_empty() {
                    continue;
                }
                let parts: Vec<&str> = trimmed.split_whitespace().collect();
                match parse_builtin(trimmed) {
                    Builtin::Cd => {
                        handle_cd(&parts);
                    }
                    Builtin::Exit => {
                        println!("{}Exiting P-Terminal. Goodbye!{}", GREEN, RESET);
                        break;
                    }
                    Builtin::Clear => {
                        handle_clear();
                    }
                    Builtin::Help => {
                        handle_help();
                    }
                    Builtin::SysInfo => {
                        display_sysinfo();
                    }
                    Builtin::Other => {
                        // Führe externe Befehle aus, wobei mehrere CPUs stärker genutzt werden können,
                        // indem der Befehl in einem separaten Thread ausgeführt wird.
                        let command = trimmed.to_string();
                        std::thread::spawn(move || {
                            spawn_shell_command(&command);
                        }).join().unwrap();
                    }
                }
            }
            Err(ReadlineError::Interrupted) => {
                // Strg+C → Neue Zeile und erneuter Prompt
                println!();
            }
            Err(ReadlineError::Eof) => {
                // Strg+D → Exit
                println!("{}Exiting P-Terminal. Goodbye!{}", GREEN, RESET);
                break;
            }
            Err(err) => {
                error!("Error reading line: {:?}", err);
                break;
            }
        }
    }

    // History speichern
    if let Some(hp_str) = history_path.to_str() {
        let _ = rl.save_history(hp_str);
    }

    Ok(())
}
