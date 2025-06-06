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

//! P-Terminal (Rust version)
//!
//! A cross‐platform terminal emulator/shell written in Rust.  
//! Features:
//!  1. Prints a colored banner on startup (with versions loaded from a JSON file).
//!  2. Shows a 16-color palette (ANSI colors 0–15).
//!  3. Provides a basic REPL loop: prompt, read input, dispatch to OS shell (`cmd.exe` / PowerShell on Windows; `/bin/sh` on Unix).
//!  4. Supports built‐in `cd` and `exit` commands.
//!  5. Uses `rustyline` for line editing, history, and basic completion.

use crossterm::style::{Color, ResetColor, SetForegroundColor};
use serde::Deserialize;
use serde_json::Value;
use std::env;
use std::fs::File;
use std::io::{self, BufReader, Write};
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};
use whoami;
use rustyline::error::ReadlineError;
use rustyline::{Config, Editor};

/// ANSI color codes (8 colors + reset)
const BLUE: &str = "\x1b[34m";
const WHITE: &str = "\x1b[37m";
const RESET: &str = "\x1b[0m";

/// Hyperlink helper (some terminals support OSC 8 hyperlinks).
/// Format: ESC ] 8 ;; URL BEL (text) ESC ] 8 ;; BEL
fn hyperlink(text: &str, url: &str) -> String {
    // Note: Not every terminal supports this. Fallback to plain text if not supported.
    format!("\x1b]8;;{}\x1b\\{}\x1b]8;;\x1b\\", url, text)
}

/// Load the versions JSON from the default path:
///   C:\Users\<username>\p-terminal\pp-term\pp-term-versions.json   (on Windows)
///   /home/<username>/p-terminal/pp-term/pp-term-versions.json      (on *nix)
fn load_versions() -> Option<serde_json::Map<String, Value>> {
    let username = whoami::username();
    let json_path: PathBuf = if cfg!(windows) {
        // On Windows, usually USERPROFILE points to C:\Users\<username>
        let base = env::var("USERPROFILE").unwrap_or_else(|_| format!("C:\\Users\\{}", username));
        Path::new(&base)
            .join("p-terminal")
            .join("p-term")
            .join("p-term-versions.json")
    } else {
        // On Unix, HOME is /home/<username>
        let base = dirs::home_dir().unwrap_or_else(|| PathBuf::from("/home").join(&username));
        base.join("p-terminal")
            .join("p-term")
            .join("p-term-versions.json")
    };

    if let Ok(file) = File::open(&json_path) {
        let reader = BufReader::new(file);
        if let Ok(v) = serde_json::from_reader(reader) {
            if let Value::Object(map) = v {
                return Some(map);
            }
        }
    }
    None
}

/// Print the ASCII‐art banner exactly as requested, substituting ANSI codes.
fn print_banner() {
    // Get the current username
    let user_name = whoami::username();

    // Print the ASCII art with color variables
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
        "{}A warm welcome, {}{}{}, to Peharge Terminal!{}",
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
    // Hyperlinks (if the terminal supports OSC 8). Otherwise, they'll appear as plain text.
    let github = hyperlink("[GitHub Repository]", "https://github.com/Peharge/p-terminal");
    let website = hyperlink(
        "[Project Website]",
        "https://peharge.github.io/MAVIS-web/p-term.html",
    );
    let learn = hyperlink(
        "[Learn P-Term]",
        "https://peharge.github.io/MAVIS-web/p-term-hole.html",
    );
    println!("{} {} {}", github, website, learn);
    println!();

    // Load and print versions from JSON
    if let Some(map) = load_versions() {
        for (key, value) in &map {
            // Each `value` is a serde_json::Value – just print it as string
            println!("{}{}{}: {}", BLUE, key, RESET, value);
        }
    } else {
        // If not found or invalid JSON
        let username = whoami::username();
        let fallback_path = if cfg!(windows) {
            format!("C:\\Users\\{}\\p-terminal\\p-term\\p-term-versions.json", username)
        } else {
            let home = dirs::home_dir()
                .unwrap_or_else(|| PathBuf::from("/home").join(&username))
                .to_string_lossy()
                .into_owned();
            format!("{}/p-terminal/p-term/p-term-versions.json", home)
        };
        eprintln!(
            "[{}] [INFO] Version file not found under {}{}",
            chrono::Local::now().format("%Y-%m-%d %H:%M:%S"),
            fallback_path,
            RESET
        );
    }

    println!();

    // Show the 16-color palette (colors 0–7, then 8–15)
    fn show_color_palette() {
        // First row: ANSI 0..7
        for i in 0..8 {
            // Background color 48;5;i, then two spaces, then reset
            print!("\x1b[48;5;{}m  \x1b[0m", i);
        }
        println!();
        // Second row: ANSI 8..15
        for i in 8..16 {
            print!("\x1b[48;5;{}m  \x1b[0m", i);
        }
        println!();
    }

    show_color_palette();
    println!();
}

/// Built-in commands that PP-Terminal handles itself.
enum Builtin {
    Cd,
    Exit,
    Other,
}

/// Parse the first token of the line to see if it is `cd`, `exit`, or something else.
fn parse_builtin(cmd: &str) -> Builtin {
    let mut parts = cmd.trim().split_whitespace();
    match parts.next() {
        Some("cd") => Builtin::Cd,
        Some("exit") | Some("quit") => Builtin::Exit,
        _ => Builtin::Other,
    }
}

/// Change directory. We assume syntax: `cd <path>` (if no `<path>`, go to home dir).
fn handle_cd(args: &[&str]) {
    let target = if args.len() >= 2 {
        // e.g. ["cd", "C:\\Windows"] or ["cd", "/usr/local"]
        args[1]
    } else {
        // Without argument, go to HOME on Unix, USERPROFILE on Windows
        if cfg!(windows) {
            &env::var("USERPROFILE").unwrap_or_else(|_| ".".into())
        } else {
            &env::var("HOME").unwrap_or_else(|_| ".".into())
        }
    };
    if let Err(e) = env::set_current_dir(target) {
        eprintln!("cd: {}: {}", target, e);
    }
}

/// Spawn an external command using the system shell:
/// - On Windows: `cmd.exe /C "<user_input>"`
///   (this dispatches to built-in `dir`, `del`, PowerShell commands if user has set default shell accordingly)
/// - On Unix: `/bin/sh -c "<user_input>"`
fn spawn_command(line: &str) {
    if cfg!(windows) {
        // On Windows, use cmd.exe /C
        let mut child = Command::new("cmd.exe")
            .args(&["/C", line])
            .stdin(Stdio::inherit())
            .stdout(Stdio::inherit())
            .stderr(Stdio::inherit())
            .spawn();
        match child {
            Ok(mut c) => {
                let _ = c.wait();
            }
            Err(e) => {
                eprintln!("Failed to spawn command: {}", e);
            }
        }
    } else {
        // On Unix, use /bin/sh -c
        let mut child = Command::new("sh")
            .arg("-c")
            .arg(line)
            .stdin(Stdio::inherit())
            .stdout(Stdio::inherit())
            .stderr(Stdio::inherit())
            .spawn();
        match child {
            Ok(mut c) => {
                let _ = c.wait();
            }
            Err(e) => {
                eprintln!("Failed to spawn command: {}", e);
            }
        }
    }
}

fn main() {
    // First, print the banner and versions
    print_banner();

    // Initialize rustyline (line editor + history).
    // We configure a basic completer that just does file path completion.
    let config = Config::builder()
        .history_ignore_space(true)
        .auto_add_history(true)
        .build();
    let mut rl = Editor::<()>::with_config(config);
    // Load history from a file (optional)
    let history_path = dirs::home_dir()
        .map(|h| h.join(".p-terminal_history"))
        .unwrap_or_else(|| PathBuf::from(".p-terminal_history"));
    if let Some(ref hp) = history_path.to_str() {
        let _ = rl.load_history(hp);
    }

    loop {
        // Build the prompt string: e.g. "username@hostname C:\current\dir> "
        let username = whoami::username();
        let hostname = whoami::hostname();
        let cwd = env::current_dir().unwrap_or_else(|_| PathBuf::from("."));
        let cwd_str = cwd.to_string_lossy();

        // You can add color to prompt if desired
        let prompt = format!(
            "{}{}@{}{} {}> {}",
            BLUE, username, hostname, RESET, cwd_str, RESET
        );

        // Read a line from user
        match rl.readline(&prompt) {
            Ok(line) => {
                let trimmed = line.trim();
                if trimmed.is_empty() {
                    continue;
                }
                // Check for built-in commands
                match parse_builtin(trimmed) {
                    Builtin::Cd => {
                        let args: Vec<&str> = trimmed.split_whitespace().collect();
                        handle_cd(&args);
                    }
                    Builtin::Exit => {
                        println!("Exiting P-Terminal. Goodbye!");
                        break;
                    }
                    Builtin::Other => {
                        // Spawn as external
                        spawn_command(trimmed);
                    }
                }
            }
            Err(ReadlineError::Interrupted) => {
                // Ctrl-C pressed
                println!();
                continue;
            }
            Err(ReadlineError::Eof) => {
                // Ctrl-D pressed
                println!("Exiting P-Terminal. Goodbye!");
                break;
            }
            Err(err) => {
                eprintln!("Error reading line: {:?}", err);
                break;
            }
        }
    }

    // On exit: save history
    let _ = rl.save_history(
        history_path
            .to_str()
            .expect("Failed to convert history path to str"),
    );
}
