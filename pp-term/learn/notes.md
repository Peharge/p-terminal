# PP-Terminal Notes

Drücke Strg + Shift + P (Windows) und tippe „Einstellungen (JSON) öffnen“ oder gehe auf Datei > Einstellungen > Einstellungen und dann oben rechts auf das Symbol {} klicken.

```json
{
    "python.defaultInterpreterPath": "C:\\Users\\julia\\p-terminal\\pp-term",
    "editor.fontSize": 16,
    "editor.unicodeHighlight.nonBasicASCII": false,

    "terminal.integrated.profiles.windows": {
        "MeinEigenesTerminal": {
            "path": "C:\\Windows\\System32\\cmd.exe",
            "args": ["/c", "C:\\Users\\julia\\p-terminal\\pp-term\\run-pp-term-fast.bat"]
        }
    }
}
```