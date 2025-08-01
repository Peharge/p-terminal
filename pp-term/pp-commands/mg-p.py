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

import shutil
import sys
import io
import re
import json
import getpass

# UTF-8-Ausgabe für Windows-Terminals sicherstellen
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Farbcodes definieren (kleingeschrieben)
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
magenta = "\033[95m"
cyan = "\033[96m"
white = "\033[97m"
black = "\033[30m"
orange = "\033[38;5;214m"
purple = "\033[95m"
dim = "\033[2m"
reset = "\033[0m"
bold = "\033[1m"

def state_info():
    with open(f"C:/Users/{getpass.getuser()}/p-terminal/pp-term/state-info.json", "r") as file:
        data = json.load(file)
    return data["state"]

if "adv" in state_info():
    main_color = "\033[92m"
elif "evil" in state_info():
    main_color = "\033[91m"
else:
    main_color = "\033[94m"

# Globale Inhalte
ASCII_BILD = r'''

[color=#808080] [/color]
[color=#808080] [/color]
[color=#808080]                            [/color][color=#717171]░[/color][color=#6e6e6e]░░░[/color][color=#6c6d6c]░░[/color][color=#6a6a6a]░░[/color][color=#686868]░[/color][color=#666666]░░[/color][color=#636363]▒[/color][color=#616161]▒[/color][color=#5f5f5f]▒[/color][color=#5d5d5d]▒[/color][color=#5b5b5b]▒[/color][color=#595959]▒║[/color][color=#5f5f5f]@[/color][color=#696969]╖[/color]
[color=#808080]                             [/color][color=#6f6f6f]░[/color][color=#6c6c6c]░[/color][color=#6b6b6b]░░░░[/color][color=#676767]░[/color][color=#666666]░▒[/color][color=#636363]▒[/color][color=#616161]▒[/color][color=#5f5f5f]▒[/color][color=#5e5e5e]▒[/color][color=#5c5c5c]▒[/color][color=#595959]▒[/color][color=#575757]▒[/color][color=#555555]▒[/color][color=#535353]▒[/color][color=#505050]▒[/color][color=#4e4e4e]╣[/color][color=#555555]@[/color][color=#727272],[/color]
[color=#808080]                              [/color][color=#5a5a5a]"[/color][color=#595959]""""""""""╙╙[/color][color=#545454]▀[/color][color=#484848]▀[/color][color=#3c3c3c]▓[/color][color=#505050]▒[/color][color=#4e4e4e]╣[/color][color=#4c4c4c]╢[/color][color=#49494a]╢[/color][color=#474747]╢[/color][color=#606060]╗[/color]
[color=#808080]                                              [/color][color=#505050]▀[/color][color=#464747]▒[/color][color=#4a4a4a]╢╢╢[/color][color=#424242]╢[/color]
[color=#808080]                                               ║[/color][color=#474747]╢[/color][color=#444444]╢[/color][color=#424242]╢[/color][color=#404040]╣[/color][color=#595959][[/color]
[color=#808080]                                               [/color][color=#414242]╣[/color][color=#434344]╢╢╣[/color][color=#3d3d3d]▓[/color]
[color=#808080]                                            [/color][color=#737373],[/color][color=#5f5f5f]g[/color][color=#454545]▓[/color][color=#424242]╢[/color][color=#404040]╣[/color][color=#3e3e3e]▓[/color][color=#3c3c3c]▓[/color][color=#535353]▀[/color]
[color=#808080]                                     [/color][color=#5a5a5a]║[/color][color=#4d4d4d]╢[/color][color=#4b4b4b]╢╢[/color][color=#494949]╢[/color][color=#474747]╢╢[/color][color=#444444]╢[/color][color=#424242]╢[/color][color=#404040]╣[/color][color=#3e3e3e]▓[/color][color=#3c3c3c]▓▓[/color][color=#676767]"[/color]
[color=#808080]                                     [/color][color=#555555]╟[/color][color=#484848]╢[/color][color=#464646]╢╢[/color][color=#444444]╢[/color][color=#424242]╢╣[/color][color=#3f3f3f]╣[/color][color=#3d3e3e]▓[/color][color=#464646]▓[/color][color=#565656]╜[/color]
[color=#808080]                                     [/color][color=#515151]╟[/color][color=#424242]╢[/color][color=#414141]╣╣[/color][color=#3f3f3f]▓[/color][color=#686868]`[/color]
[color=#808080]                                     [/color][color=#4c4d4d]╟[/color][color=#3d3d3d]▓[/color][color=#3c3c3c]▓▓[/color][color=#3a3a3a]▓[/color]
[color=#808080]                                     [/color][color=#484848]╟[/color][color=#383838]▓[/color][color=#373737]▓▓▓[/color]
[color=#808080]                                     [/color][color=#444444]▓[/color][color=#333333]▓[/color][color=#323232]▓▓▓[/color]
[color=#808080]                                     [/color][color=#404140]▓[/color][color=#2e2e2e]▓[/color][color=#2d2e2e]▓▓▓[/color]
[color=#808080]                                     [/color][color=#505050]╚[/color][color=#2b2b2b]▓[/color][color=#292929]▓▓▓[/color]
[color=#808080]                                       [/color][color=#606061]╙[/color][color=#3f3f3f]▀[/color][color=#252525]▓[/color]
[color=#808080] [/color]
[color=#808080] [/color]

'''

BB_CODE_TEXT = "MG - A Peharge developer\nPeharge Projects 2025"
NORMAL_TEXT = f"""Welcome, {main_color}{getpass.getuser()}{reset}, to the Peharge Python Terminal.
 A cutting-edge Terminal crafted by Peharge and JK.

 Thank you for choosing PP-Terminal.
 We sincerely appreciate your trust and support as we empower your Python journey. ❤️"""

# --- Hilfsfunktionen ---

def hex_to_rgb(hex_str: str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def ansi_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def apply_size(text: str, size: int) -> str:
    """Simuliert größere Schrift durch Großbuchstaben und Dopplung."""
    if size <= 1:
        return text
    enlarged = ""
    for c in text:
        if c.isalpha():
            enlarged += c.upper() * size
        else:
            enlarged += c * size
    return enlarged

# --- BBCode-Parser ---

def parse_bbcode(text: str) -> str:
    output = ""
    color_stack = []
    size_stack = [1]
    bold = False
    pos = 0
    pattern = re.compile(
        r'\[color=#([0-9a-fA-F]{6})\]|\[/color\]'
        r'|\[b\]|\[/b\]'
        r'|\[size=(\d+)\]|\[/size\]'
    )

    for match in pattern.finditer(text):
        start, end = match.span()
        raw = text[pos:start]
        size = size_stack[-1]
        raw = apply_size(raw, size)
        if bold:
            raw = f"\033[1m{raw}\033[22m"
        output += raw
        tag = match.group(0)

        if tag.startswith('[color='):
            r, g, b = hex_to_rgb(match.group(1))
            color_stack.append((r, g, b))
            output += ansi_color(r, g, b)
        elif tag == '[/color]':
            if color_stack:
                color_stack.pop()
            output += ansi_color(*color_stack[-1]) if color_stack else '\033[0m'
        elif tag == '[b]':
            bold = True
        elif tag == '[/b]':
            bold = False
        elif tag.startswith('[size='):
            size_stack.append(int(match.group(2)))
        elif tag == '[/size]':
            if len(size_stack) > 1:
                size_stack.pop()

        pos = end

    # Letzter Textabschnitt nach letztem Tag
    rest = apply_size(text[pos:], size_stack[-1])
    if bold:
        rest = f"\033[1m{rest}\033[22m"
    output += rest + '\033[0m'
    return output

# --- Zentrierfunktionen ---

import shutil

def center_text(text: str) -> str:
    width = shutil.get_terminal_size((80, 20)).columns
    lines = text.splitlines()
    max_line_len = max(len(line) for line in lines) if lines else 0

    # Abstand, um den gesamten Textblock in der Terminalbreite zu zentrieren
    left_padding = (width - max_line_len) // 2 if width > max_line_len else 0

    centered_lines = []
    for line in lines:
        # Linke Einrückung plus restlichen Platz rechts, um die Zeile relativ zum längsten Text zu zentrieren
        spaces = left_padding + (max_line_len - len(line)) // 2
        centered_lines.append(' ' * spaces + line)

    return "\n".join(centered_lines)

def center_ascii_art(ascii_art: str) -> str:
    lines = ascii_art.strip("\n").splitlines()
    return "\n".join(center_text(parse_bbcode(line)) for line in lines)

# --- Hauptfunktion ---

def main():
    print()
    print(center_ascii_art(ASCII_BILD))
    print()
    print(center_text(BB_CODE_TEXT))
    print()
    print(center_text(NORMAL_TEXT))
    print()

if __name__ == "__main__":
    main()
