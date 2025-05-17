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

from PyQt6.QtWidgets          import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QFileDialog, QMessageBox
)
from PyQt6.QtGui              import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore             import QUrl

import plotly.graph_objects as go


def create_plotly_map_html() -> str:
    """
    Erzeugt eine Plotly Mapbox-Figur mit OpenStreetMap-Stil
    und gibt sie als HTML-String zurück.
    """
    # Beispielkoordinaten und Marker
    latitudes  = [52.5200, 48.1351, 50.1109]
    longitudes = [13.4050, 11.5820, 8.6821]
    # cities     = ["Berlin", "München", "Frankfurt"]

    fig = go.Figure(go.Scattermapbox(
        lat=latitudes,
        lon=longitudes,
        mode="markers+text",
        # text=cities,
        marker=dict(size=12)
    ))

    # OpenStreetMap-Kachelstil setzen
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=5,
        mapbox_center={"lat": 51.1657, "lon": 10.4515},
        margin={"l":0, "r":0, "t":0, "b":0}
    )

    # Als HTML-String exportieren (Plotly.js per CDN)
    return fig.to_html(include_plotlyjs="cdn")


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Professionelle Mapbox-Karte mit PyQt6")
        self.resize(1200, 800)

        # Zentrales Widget und Layout
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # WebEngineView für die Karte
        self.view = QWebEngineView()
        layout.addWidget(self.view)

        # Menü zum Laden externer HTML-Dateien
        self._create_menu()

        # Die initiale Karte laden
        self._load_internal_map()

    def _create_menu(self):
        menu = self.menuBar().addMenu("")

        load_html = QAction("HTML laden…", self)
        load_html.triggered.connect(self._open_file)
        menu.addAction(load_html)

        reload_map = QAction("Standardkarte neu laden", self)
        reload_map.triggered.connect(self._load_internal_map)
        menu.addAction(reload_map)

        exit_app = QAction("Beenden", self)
        exit_app.triggered.connect(self.close)
        menu.addAction(exit_app)

    def _load_internal_map(self):
        """Lädt die von Plotly erzeugte HTML-Karte."""
        html_str = create_plotly_map_html()
        self.view.setHtml(html_str, QUrl(""))

    def _open_file(self):
        """Öffnet einen Dateidialog und lädt eine externe HTML-Datei."""
        path, _ = QFileDialog.getOpenFileName(
            self,
            "HTML-Datei auswählen",
            "",
            "HTML Files (*.html *.htm)"
        )
        if path and os.path.exists(path):
            url = QUrl.fromLocalFile(os.path.abspath(path))
            self.view.load(url)
        elif path:
            QMessageBox.warning(self, "Fehler", "Datei nicht gefunden.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec())
