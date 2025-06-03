//! P-Terminal (Rust version, stable & high-performance)
//!
//! A cross-platform terminal emulator/shell written in Rust, focusing on stability and speed.
//!
//! Features:
//!  1. Prints a colored banner on startup (with versions loaded from a JSON file).
//!  2. Shows a 16-color palette (ANSI colors 0–15).
//!  3. Provides a REPL loop using `rustyline` (prompt, read input, dispatch to OS shell).
//!  4. Supports built-in commands: `cd`, `exit`, `clear`, `help`, `sysinfo`.
//!  5. Uses `rustyline` for line editing, history, and filesystem path completion.
//!  6. Includes `git`-branch in prompt when inside a Git repository via `git2`.
//!  7. Displays system load & memory usage using `sysinfo`.
//!  8. Handles Ctrl+C gracefully (returns to prompt), Ctrl+D exits.
//!  9. Saves history in `~/.p-terminal_history`.
//! 10. Uses `tracing`/`tracing-subscriber` for logging.
//! 11. Employs `anyhow` for error handling.

use anyhow::Result;
use chrono::Local;
use directories::BaseDirs;
use git2::Repository;
use rustyline::completion::FilenameCompleter;
use rustyline::error::ReadlineError;
use rustyline::highlight::MatchingBracketHighlighter;
use rustyline::hint::{Hinter, HistoryHinter};
use rustyline::validate::{Validator, ValidationContext, ValidationResult};
use rustyline::{Config, Editor, Helper};
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

/// ANSI color codes
const BLUE: &str = "\x1b[34m";
const CYAN: &str = "\x1b[36m";
const GREEN: &str = "\x1b[32m";
const RED: &str = "\x1b[31m";
const WHITE: &str = "\x1b[37m";
const RESET: &str = "\x1b[0m";

/// Custom Helper for rustyline, providing completion, hints, and highlighting.
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

/// Load versions JSON from default path:
///   Windows: C:\Users\<username>\p-terminal\p-term\p-term-versions.json
///   Unix:    /home/<username>/p-terminal/p-term/p-term-versions.json
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

/// Print ASCII-art banner with ANSI colors
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
            "[{}] [INFO] Version file not found under {}{}",
            Local::now().format("%Y-%m-%d %H:%M:%S"),
            fallback_path,
            RESET
        );
    }

    println!();

    // Show 16-color palette
    for i in 0..8 {
        print!("\x1b[48;5;{}m  \x1b[0m", i);
    }
    println!();
    for i in 8..16 {
        print!("\x1b[48;5;{}m  \x1b[0m", i);
    }
    println!("\n");
}

/// OSC 8 hyperlink helper
fn hyperlink(text: &str, url: &str) -> String {
    format!("\x1b]8;;{}\x1b\\{}\x1b]8;;\x1b\\", url, text)
}

/// Return " (branch)" if current dir is in a Git repo
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

/// Display system info via sysinfo
fn display_sysinfo() {
    let mut sys = System::new_all();
    sys.refresh_all();
    let total_mem = sys.total_memory() / 1024;
    let used_mem = sys.used_memory() / 1024;
    let cpu_usage: f32 = sys.cpus().iter().map(|c| c.cpu_usage()).sum::<f32>() / sys.cpus().len() as f32;
    println!(
        "{}System Info:{} CPU Usage: {:.2}% | Memory: {} MiB / {} MiB",
        GREEN, RESET, cpu_usage, used_mem, total_mem
    );
}

/// Built-in commands
enum Builtin {
    Cd,
    Exit,
    Clear,
    Help,
    SysInfo,
    Other,
}

/// Parse first token for built-ins
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

/// Change directory: `cd <path>` or `cd` → home
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

/// Print built-in help
fn handle_help() {
    println!(
        "{}Built-in commands:{}\n  {}cd{} [<path>]    Change directory\n  {}exit{}, {}quit{}    Exit P-Terminal\n  {}clear{}         Clear screen\n  {}help{}          Show this help\n  {}sysinfo{}       Display system info\n",
        GREEN, RESET,
        CYAN, RESET,
        CYAN, RESET,
        CYAN, RESET,
        CYAN, RESET,
        CYAN, RESET,
        CYAN, RESET
    );
}

/// Clear screen (ANSI)
fn handle_clear() {
    print!("\x1B[2J\x1B[H");
}

/// Spawn external command synchronously (blocking until completion)
fn spawn_command(line: &str) {
    if cfg!(windows) {
        match Command::new("cmd.exe")
            .args(&["/C", line])
            .stdin(Stdio::inherit())
            .stdout(Stdio::inherit())
            .stderr(Stdio::inherit())
            .status()
        {
            Ok(_) => {}
            Err(e) => {
                eprintln!("{}Failed to spawn command: {}{}", RED, e, RESET);
            }
        }
    } else {
        match Command::new("sh")
            .arg("-c")
            .arg(line)
            .stdin(Stdio::inherit())
            .stdout(Stdio::inherit())
            .stderr(Stdio::inherit())
            .status()
        {
            Ok(_) => {}
            Err(e) => {
                eprintln!("{}Failed to spawn command: {}{}", RED, e, RESET);
            }
        }
    }
}

fn main() -> Result<()> {
    // Initialize tracing subscriber for logging
    let subscriber = tracing_subscriber::FmtSubscriber::builder()
        .with_max_level(tracing::Level::INFO)
        .finish();
    tracing::subscriber::set_global_default(subscriber)?;

    print_banner();

    // Prepare rustyline with history, completion, hints, etc.
    let config = Config::builder()
        .history_ignore_space(true)
        .auto_add_history(true)
        .build();
    let mut rl: Editor<PHelper, FileHistory> = Editor::with_config(config)?;
    rl.set_helper(Some(PHelper::new()));

    // Load history from file
    let history_path = BaseDirs::new()
        .map(|d| d.home_dir().join(".p-terminal_history"))
        .unwrap_or_else(|| PathBuf::from(".p-terminal_history"));
    if let Some(hp_str) = history_path.to_str() {
        let _ = rl.load_history(hp_str);
    }

    loop {
        // Build prompt: username@hostname(git_branch) cwd>
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
                match parse_builtin(trimmed) {
                    Builtin::Cd => {
                        let args: Vec<&str> = trimmed.split_whitespace().collect();
                        handle_cd(&args);
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
                        spawn_command(trimmed);
                    }
                }
            }
            Err(ReadlineError::Interrupted) => {
                // Ctrl+C: just print newline and reprompt
                println!();
            }
            Err(ReadlineError::Eof) => {
                // Ctrl+D: exit
                println!("{}Exiting P-Terminal. Goodbye!{}", GREEN, RESET);
                break;
            }
            Err(err) => {
                error!("Error reading line: {:?}", err);
                break;
            }
        }
    }

    // On exit: save history
    if let Some(hp_str) = history_path.to_str() {
        let _ = rl.save_history(hp_str);
    }

    Ok(())
}
