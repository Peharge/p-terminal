use anyhow::Result;
use chrono::Local;
use directories::BaseDirs;
use git2::Repository;
use rustyline::error::ReadlineError;
use rustyline::Editor;
use rustyline::history::FileHistory;
use serde_json::Value;
use std::env;
use std::fs::File;
use std::io::BufReader;
use std::path::PathBuf;
use std::process::{Command, Stdio};
use sysinfo::{CpuExt, System, SystemExt};
use tracing::error;
use tracing_subscriber;
use whoami;

/// ANSI‐Farben
const BLUE: &str = "\x1b[34m";
const GREEN: &str = "\x1b[32m";
const RED: &str = "\x1b[31m";
const WHITE: &str = "\x1b[37m";
const RESET: &str = "\x1b[0m";

/// Lädt Versions‐JSON (falls vorhanden)
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

/// Druckt ASCII‐Banner mit Farben und Versionsinfos
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
        WHITE, BLUE, user_name, WHITE, RESET
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

/// Gibt Git-Branch‐Suffix zurück (wenn aktuelles Verzeichnis Git-Repo ist)
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

/// Zeigt System‐Info synchron via `sysinfo`
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

/// Verfügbare Built‐in‐Befehle
enum Builtin {
    Cd,
    Exit,
    Clear,
    Help,
    SysInfo,
    Other,
}

/// Parst das erste Token auf einen Built‐in‐Befehl
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

/// Wechselt das Verzeichnis: `cd <Pfad>` oder ohne Argument → Home
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

/// Gibt die Hilfe‐Ansicht aus (farblich)
fn handle_help() {
    println!("{}Built-in Befehle:{}", GREEN, RESET);
    println!("  {}cd{} [<Pfad>]    Verzeichnis wechseln", BLUE, RESET);
    println!("  {}exit{}, {}quit{}   P-Terminal beenden", BLUE, RESET, BLUE, RESET);
    println!("  {}clear{}         Screen clearen", BLUE, RESET);
    println!("  {}help{}          Diese Hilfe anzeigen", BLUE, RESET);
    println!("  {}sysinfo{}       System-Info anzeigen", BLUE, RESET);
}

/// Leert den Screen (ANSI)
fn handle_clear() {
    print!("\x1B[2J\x1B[H");
}

/// Führt externe Befehle synchron aus (PowerShell/pwsh ↔ cmd/sh)
fn spawn_shell_command(line: &str) {
    #[cfg(windows)]
    {
        // Prüfe PowerShell
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

            if let Err(e) = status {
                error!("Fehler beim Ausführen von PowerShell: {}", e);
            }
        } else {
            // Fallback: cmd.exe
            let status = Command::new("cmd.exe")
                .arg("/C")
                .arg(line)
                .stdin(Stdio::inherit())
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .status();

            if let Err(e) = status {
                error!("Fehler beim Ausführen von cmd.exe: {}", e);
            }
        }
    }

    #[cfg(not(windows))]
    {
        // Unter Unix: Zuerst pwsh, sonst sh
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

            if let Err(e) = status {
                error!("Fehler beim Ausführen von pwsh: {}", e);
            }
        } else {
            let status = Command::new("sh")
                .arg("-c")
                .arg(line)
                .stdin(Stdio::inherit())
                .stdout(Stdio::inherit())
                .stderr(Stdio::inherit())
                .status();

            if let Err(e) = status {
                error!("Fehler beim Ausführen von sh: {}", e);
            }
        }
    }
}

fn main() -> Result<()> {
    // Logging initialisieren (Level via ENV: `export RUST_LOG=info`)
    let subscriber = tracing_subscriber::FmtSubscriber::builder()
        .with_env_filter(tracing_subscriber::EnvFilter::from_default_env())
        .finish();
    tracing::subscriber::set_global_default(subscriber)?;

    // Banner ausgeben
    print_banner();

    // Editor ohne Helper (keine Autovervollständigung, kein Highlighting)
    let mut rl: Editor<(), FileHistory> = Editor::new()?;

    // History‐Datei festlegen und laden
    let history_path = BaseDirs::new()
        .map(|d| d.home_dir().join(".p-terminal_history"))
        .unwrap_or_else(|| PathBuf::from(".p-terminal_history"));
    if let Some(hp_str) = history_path.to_str() {
        let _ = rl.load_history(hp_str);
    }

    // REPL‐Loop
    loop {
        // Prompt zusammenbauen: user@host(git_branch) cwd>
        let username = whoami::username();
        let hostname = whoami::fallible::hostname().unwrap_or_else(|_| "unknown".into());
        let cwd = env::current_dir().unwrap_or_else(|_| PathBuf::from("."));
        let cwd_str = cwd.to_string_lossy();
        let git_suffix = git_branch_suffix();

        // Prompt endet hier direkt mit '>', ohne nachfolgende Leerzeichen:
        let prompt = format!(
            "{}{}@{}{}{} {}>{}",
            BLUE, username, hostname, RESET, git_suffix, cwd_str, RESET
        );

        match rl.readline(&prompt) {
            Ok(line) => {
                // 1) trim_start() entfernt alle führenden Leerzeichen.
                // 2) Deshalb bleibt der Befehl direkt an '>' stehen, egal wie viele Spaces
                //    der Nutzer vor dem eigentlichen Wort eingibt.
                let trimmed = line.trim_start();

                // Leere Eingabe überspringen
                if trimmed.is_empty() {
                    continue;
                }

                // Eingabe in Historie speichern und möglichen Fehler ignorieren
                let _ = rl.add_history_entry(trimmed);

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
                        // Externe Befehle ausführen
                        let command = trimmed.to_string();
                        // In eigenem Thread ausführen und blockieren, bis es fertig ist
                        std::thread::spawn(move || {
                            spawn_shell_command(&command);
                        })
                        .join()
                        .unwrap();
                    }
                }
            }
            Err(ReadlineError::Interrupted) => {
                // Strg+C → Neue Zeile + Prompt erneut
                println!();
                continue;
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
