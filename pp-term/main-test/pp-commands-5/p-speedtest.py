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
import math
import csv
from datetime import datetime

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFileDialog, QDialog, QTableWidget, QTableWidgetItem,
    QHeaderView
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QPointF, QRectF
from PyQt6.QtGui import QPainter, QPen, QFont, QColor, QIcon, QClipboard

import pyqtgraph as pg
from pyqtgraph import BarGraphItem  # Wichtig, damit das Balkendiagramm funktioniert
import speedtest  # pip install speedtest-cli


class SpeedometerWidget(QWidget):
    """
    Ein kreisförmiges Speedometer-Widget (Gauges).
    - title: z. B. "Download Speed", "Upload Speed"
    - current_speed: numerischer Wert (in der gewählten Einheit)
    - Skala von min_speed..max_speed (default 0..250)
    - unit: Einheiten-String (z. B. "Mbps" oder "MB/s")
    """
    def __init__(self, title: str = "", parent=None):
        super().__init__(parent)
        self.title = title
        self.current_speed = 0.0
        self.min_speed = 0.0
        self.max_speed = 250.0
        self.unit = "Mbps"
        self.setMinimumSize(300, 300)

    def setSpeed(self, speed: float):
        """Aktualisiere die angezeigte Geschwindigkeit und zeichne neu."""
        self.current_speed = speed
        self.update()

    def setUnit(self, unit: str):
        """Ändere den Einheitstext (z. B. 'Mbps' oder 'MB/s') und zeichne neu."""
        self.unit = unit
        self.update()

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        radius = min(width, height) / 2 * 0.8
        center = QPointF(width / 2, height / 2)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 1) Äußerer Kreis
        pen = QPen(Qt.GlobalColor.white, 4)
        painter.setPen(pen)
        painter.drawEllipse(center, radius, radius)

        # 2) Tick Marks und Labels
        painter.save()
        num_ticks = 10
        for i in range(num_ticks + 1):
            angle = 150 - (240 / num_ticks) * i  # von 150° bis -90°
            rad = math.radians(angle)

            inner_pt = QPointF(
                center.x() + (radius - 10) * math.cos(rad),
                center.y() - (radius - 10) * math.sin(rad),
            )
            outer_pt = QPointF(
                center.x() + radius * math.cos(rad),
                center.y() - radius * math.sin(rad),
            )
            painter.drawLine(inner_pt, outer_pt)

            # Numerisches Label an jedem Tick
            speed_val = int(self.min_speed + (self.max_speed - self.min_speed) * i / num_ticks)
            label_pt = QPointF(
                center.x() + (radius - 30) * math.cos(rad),
                center.y() - (radius - 30) * math.sin(rad),
            )
            font = QFont("Roboto", 8)
            painter.setFont(font)
            text = str(speed_val)
            text_rect = painter.fontMetrics().boundingRect(text)
            label_rect = QRectF(
                label_pt.x() - text_rect.width() / 2,
                label_pt.y() - text_rect.height() / 2,
                text_rect.width(),
                text_rect.height(),
            )
            painter.drawText(label_rect, Qt.AlignmentFlag.AlignCenter, text)
        painter.restore()

        # 3) Berechne Nadel-Winkel (150° bis -90°)
        speed = max(self.min_speed, min(self.current_speed, self.max_speed))
        needle_angle = 150 - ((speed - self.min_speed) / (self.max_speed - self.min_speed)) * 240
        rad = math.radians(needle_angle)

        # 4) Nadel zeichnen
        painter.save()
        pen = QPen(QColor("#FF4500"), 4)  # leuchtendes Orange
        painter.setPen(pen)
        needle_length = radius - 20
        end_pt = QPointF(
            center.x() + needle_length * math.cos(rad),
            center.y() - needle_length * math.sin(rad),
        )
        painter.drawLine(center, end_pt)
        painter.restore()

        # 5) Pivot (Mittelpunkt) malen
        painter.setBrush(QColor("#FF4500"))
        painter.drawEllipse(center, 5, 5)

        # 6) Aktueller Speed-Text unterhalb des Zentrums
        painter.setPen(QColor("#FFFFFF"))
        font = QFont("Roboto", 14, QFont.Weight.Bold)
        painter.setFont(font)
        speed_text = f"{speed:.1f} {self.unit}"
        text_rect = painter.fontMetrics().boundingRect(speed_text)
        painter.drawText(
            int(center.x() - text_rect.width() / 2),
            int(center.y() + radius / 2 + text_rect.height()),
            speed_text,
        )

        # 7) Titel oben zeichnen
        if self.title:
            title_font = QFont("Roboto", 16, QFont.Weight.Bold)
            painter.setFont(title_font)
            title_rect = painter.fontMetrics().boundingRect(self.title)
            painter.drawText(
                int(center.x() - title_rect.width() / 2),
                int(center.y() - radius - 10),
                self.title,
            )


class SpeedTestWorker(QThread):
    """
    Worker-Thread, der den echten Speedtest (speedtest-cli) ausführt.
    Signale:
      - server_info(str)
      - download_speed(float in Mbps)
      - upload_speed(float in Mbps)
      - ping_latency(float in ms)
      - finished()
    """
    server_info = pyqtSignal(str)
    download_speed = pyqtSignal(float)
    upload_speed = pyqtSignal(float)
    ping_latency = pyqtSignal(float)
    finished = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        try:
            st = speedtest.Speedtest()
            best = st.get_best_server()
            server_str = f"{best['sponsor']} ({best['name']}, {best['country']})"
            self.server_info.emit(server_str)

            download_bps = st.download()
            download_mbps = download_bps / 1e6
            self.download_speed.emit(download_mbps)

            upload_bps = st.upload(pre_allocate=False)
            upload_mbps = upload_bps / 1e6
            self.upload_speed.emit(upload_mbps)

            ping_ms = best.get("latency", 0.0)
            self.ping_latency.emit(ping_ms)

        except Exception as e:
            print("Error in SpeedTestWorker:", e)
            self.server_info.emit("Error fetching server")
            self.download_speed.emit(0.0)
            self.upload_speed.emit(0.0)
            self.ping_latency.emit(0.0)
        finally:
            self.finished.emit()


class HistoryDialog(QDialog):
    """
    Ein modales Dialogfenster, das die Historie aller Speedtests in einer Tabelle zeigt.
    Ermöglicht auch den Export der gesamten Historie als CSV.
    """
    def __init__(self, parent, history_data):
        super().__init__(parent)
        self.setWindowTitle("Test History")
        self.resize(700, 400)
        self.history_data = history_data  # Liste von Dictionaries

        layout = QVBoxLayout(self)

        # Tabelle mit Spalten: Timestamp | Download | Upload | Ping | Server
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Timestamp", "Download", "Upload", "Ping (ms)", "Server"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)

        self.loadHistory()

        # Button: gesamte Historie exportieren
        self.export_btn = QPushButton("Export Entire History to CSV", self)
        self.export_btn.clicked.connect(self.exportHistory)
        layout.addWidget(self.export_btn)

    def loadHistory(self):
        self.table.setRowCount(len(self.history_data))
        for row, entry in enumerate(self.history_data):
            ts_item = QTableWidgetItem(entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S"))
            dl = entry["download"]
            ul = entry["upload"]
            unit = entry["unit"]
            dl_item = QTableWidgetItem(f"{dl:.2f} {unit}")
            ul_item = QTableWidgetItem(f"{ul:.2f} {unit}")
            ping_item = QTableWidgetItem(f"{entry['ping']:.1f}")
            server_item = QTableWidgetItem(entry["server"])

            # Nur lesbar, nicht editierbar
            ts_item.setFlags(ts_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            dl_item.setFlags(dl_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            ul_item.setFlags(ul_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            ping_item.setFlags(ping_item.flags() ^ Qt.ItemFlag.ItemIsEditable)
            server_item.setFlags(server_item.flags() ^ Qt.ItemFlag.ItemIsEditable)

            self.table.setItem(row, 0, ts_item)
            self.table.setItem(row, 1, dl_item)
            self.table.setItem(row, 2, ul_item)
            self.table.setItem(row, 3, ping_item)
            self.table.setItem(row, 4, server_item)

    def exportHistory(self):
        if not self.history_data:
            return

        default_name = f"speedtest_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        path, _ = QFileDialog.getSaveFileName(self, "Save Full History as CSV", default_name, "CSV Files (*.csv)")
        if not path:
            return

        try:
            with open(path, mode="w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=";")
                writer.writerow(["Timestamp", "Download", "Upload", "Ping (ms)", "Server"])
                for entry in self.history_data:
                    writer.writerow([
                        entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
                        f"{entry['download']:.2f} {entry['unit']}",
                        f"{entry["upload"]:.2f} {entry["unit"]}",
                        f"{entry["ping"]:.1f}",
                        entry["server"],
                    ])
            self.accept()
        except Exception as e:
            print("Error saving history:", e)
            # Optional: QMessageBox anzeigen


class SpeedTestWindow(QMainWindow):
    """
    Hauptfenster der Speedtest-Anwendung. Enthält:
      - Zwei SpeedometerWidgets (Download & Upload)
      - Ein pyqtgraph-Bar-Chart (zeigt die finalen Werte)
      - Labels: Status, Ping, Server
      - Buttons: Start Test, Toggle Unit, Copy Result, View History, Export Result
      - Eine In-Memory-Historie aller durchgeführten Tests
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P-Term Speed Test (English Version)")
        self.setGeometry(100, 100, 1000, 700)

        # Letztes Test-Ergebnis
        self.last_download = 0.0  # in Mbps
        self.last_upload = 0.0    # in Mbps
        self.last_ping = 0.0
        self.last_server = ""
        self.last_unit = "Mbps"
        self.test_timestamp = None

        # In-Memory-Historie: Liste von Dictionary-Einträgen
        self.history = []

        self.initUI()
        self.setStyleSheet(self.loadStylesheet())

        user = os.getenv("USERNAME") or os.getenv("USER")
        icon_path = f"C:/Users/{user}/p-terminal/pp-term/icons/p-term-logo-5.ico"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.worker = None  # SpeedTestWorker-Thread

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # --- Bar Chart (pyqtgraph) für finale Werte --- #
        self.chart = pg.PlotWidget(title="Internet Speed (Mbps)")
        self.chart.setBackground(None)
        self.chart.getAxis("bottom").setPen(pg.mkPen(color="#FFFFFF"))
        self.chart.getAxis("left").setPen(pg.mkPen(color="#FFFFFF"))
        self.chart.showGrid(x=True, y=True, alpha=0.3)
        main_layout.addWidget(self.chart, stretch=2)

        # --- Speedometer-Gauges --- #
        gauges_layout = QHBoxLayout()
        self.download_gauge = SpeedometerWidget(title="Download Speed")
        self.upload_gauge = SpeedometerWidget(title="Upload Speed")
        gauges_layout.addWidget(self.download_gauge)
        gauges_layout.addWidget(self.upload_gauge)
        main_layout.addLayout(gauges_layout, stretch=3)

        # --- Info-Labels (Status, Ping, Server) --- #
        self.status_label = QLabel("Click “Start Test” to begin.")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ping_label = QLabel("")
        self.ping_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.server_label = QLabel("")
        self.server_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.ping_label)
        main_layout.addWidget(self.server_label)

        # --- Buttons-Zeile --- #
        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Start Test")
        self.start_btn.clicked.connect(self.startTest)

        self.unit_btn = QPushButton("Unit: Mbps")
        self.unit_btn.clicked.connect(self.toggleUnit)

        self.copy_btn = QPushButton("Copy Result")
        self.copy_btn.setEnabled(False)
        self.copy_btn.clicked.connect(self.copyToClipboard)

        self.history_btn = QPushButton("View History")
        self.history_btn.clicked.connect(self.showHistory)

        self.export_btn = QPushButton("Export Result as CSV")
        self.export_btn.setEnabled(False)
        self.export_btn.clicked.connect(self.exportSingleResult)

        btn_layout.addStretch()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.unit_btn)
        btn_layout.addWidget(self.copy_btn)
        btn_layout.addWidget(self.history_btn)
        btn_layout.addWidget(self.export_btn)
        btn_layout.addStretch()

        main_layout.addLayout(btn_layout)

    def loadStylesheet(self) -> str:
        return """
            QWidget {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1b2631, stop:1 #0f1626
                );
                color: #FFFFFF;
                font-family: 'Roboto', sans-serif;
                font-size: 14px;
            }
            QPushButton {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2c3e50, stop:1 #1c2833
                );
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
                color: #FFFFFF;
            }
            QPushButton:hover {
                background-color: #1c2833;
            }
            QLabel {
                background: transparent;
                font-size: 16px;
            }
        """

    def startTest(self):
        """Wird aufgerufen, wenn der Nutzer “Start Test” klickt."""
        # Buttons deaktivieren, bis der Test fertig ist
        self.start_btn.setEnabled(False)
        self.copy_btn.setEnabled(False)
        self.export_btn.setEnabled(False)
        self.status_label.setText("Running speed test… please wait.")
        self.ping_label.setText("")
        self.server_label.setText("")
        self.chart.clear()

        # Zeitstempel merken
        self.test_timestamp = datetime.now()

        # Worker-Thread starten
        self.worker = SpeedTestWorker()
        self.worker.server_info.connect(self.onServerReceived)
        self.worker.download_speed.connect(self.onDownloadReceived)
        self.worker.upload_speed.connect(self.onUploadReceived)
        self.worker.ping_latency.connect(self.onPingReceived)
        self.worker.finished.connect(self.onTestFinished)
        self.worker.start()

    def onServerReceived(self, server_str: str):
        """Server-Info vom Worker erhalten."""
        self.last_server = server_str
        self.server_label.setText(f"Server: {server_str}")

    def onDownloadReceived(self, mbps: float):
        """Download-Speed (in Mbps) vom Worker erhalten."""
        # Anzeige in gewählter Einheit: Mbps oder MB/s
        if self.last_unit == "MB/s":
            display_val = mbps / 8.0
        else:
            display_val = mbps
        self.last_download = mbps  # intern immer in Mbps speichern
        self.download_gauge.setUnit(self.last_unit)
        self.download_gauge.setSpeed(display_val)

    def onUploadReceived(self, mbps: float):
        """Upload-Speed (in Mbps) vom Worker erhalten."""
        if self.last_unit == "MB/s":
            display_val = mbps / 8.0
        else:
            display_val = mbps
        self.last_upload = mbps
        self.upload_gauge.setUnit(self.last_unit)
        self.upload_gauge.setSpeed(display_val)

    def onPingReceived(self, ping_ms: float):
        """Ping-Latenz (in ms) vom Worker erhalten."""
        self.last_ping = ping_ms
        self.ping_label.setText(f"Ping: {ping_ms:.1f} ms")

    def onTestFinished(self):
        """Wird aufgerufen, sobald der SpeedTestWorker fertig ist."""
        # Anzeige-Variablen anlegen (in der gewählten Einheit)
        display_dl = self.last_download / 8.0 if self.last_unit == "MB/s" else self.last_download
        display_ul = self.last_upload / 8.0 if self.last_unit == "MB/s" else self.last_upload

        # Status-Label setzen
        self.status_label.setText(
            f"Test complete! Download: {display_dl:.2f} {self.last_unit} | "
            f"Upload: {display_ul:.2f} {self.last_unit} | Ping: {self.last_ping:.1f} ms"
        )

        # Bar Chart zeichnen
        self.chart.clear()
        x_vals = [1, 2]
        y_vals = [display_dl, display_ul]
        colors = [QColor("#1E90FF"), QColor("#32CD32")]  # Blau / Grün

        bar_item = BarGraphItem(x=x_vals, height=y_vals, width=0.6, brush=colors)
        self.chart.addItem(bar_item)
        self.chart.getAxis("bottom").setTicks([[(1, "Download"), (2, "Upload")]])

        # Y-Achse so skalieren, dass 10% Spielraum bleibt, aber mind. bis 10
        y_max = max(display_dl, display_ul) * 1.1
        self.chart.setYRange(0, max(y_max, 10))

        # Buttons wieder aktivieren
        self.copy_btn.setEnabled(True)
        self.export_btn.setEnabled(True)
        self.start_btn.setEnabled(True)

        # Ergebnis in Historie speichern
        self.history.append({
            "timestamp": self.test_timestamp,
            "download": self.last_download,
            "upload": self.last_upload,
            "ping": self.last_ping,
            "server": self.last_server,
            "unit": self.last_unit
        })

    def toggleUnit(self):
        """Zwischeneinheit umschalten (Mbps ⇆ MB/s) und Gauges/Chart aktualisieren."""
        if self.last_unit == "Mbps":
            self.last_unit = "MB/s"
            self.unit_btn.setText("Unit: MB/s")
        else:
            self.last_unit = "Mbps"
            self.unit_btn.setText("Unit: Mbps")

        # Falls bereits ein Ergebnis existiert, Gauges und Chart umrechnen
        if self.test_timestamp:
            dl = self.last_download / 8.0 if self.last_unit == "MB/s" else self.last_download
            ul = self.last_upload / 8.0 if self.last_unit == "MB/s" else self.last_upload

            # Gauges updaten
            self.download_gauge.setUnit(self.last_unit)
            self.upload_gauge.setUnit(self.last_unit)
            self.download_gauge.setSpeed(dl)
            self.upload_gauge.setSpeed(ul)

            # Status-Label anpassen
            self.status_label.setText(
                f"Last result: Download {dl:.2f} {self.last_unit} | "
                f"Upload {ul:.2f} {self.last_unit} | Ping {self.last_ping:.1f} ms"
            )

            # Bar Chart neu zeichnen
            self.chart.clear()
            x_vals = [1, 2]
            y_vals = [dl, ul]
            colors = [QColor("#1E90FF"), QColor("#32CD32")]
            bar_item = BarGraphItem(x=x_vals, height=y_vals, width=0.6, brush=colors)
            self.chart.addItem(bar_item)
            self.chart.getAxis("bottom").setTicks([[(1, "Download"), (2, "Upload")]])
            y_max = max(dl, ul) * 1.1
            self.chart.setYRange(0, max(y_max, 10))

    def copyToClipboard(self):
        """Kopiere die Zusammenfassung des letzten Tests in die Zwischenablage."""
        if not self.test_timestamp:
            return
        dl = self.last_download / 8.0 if self.last_unit == "MB/s" else self.last_download
        ul = self.last_upload / 8.0 if self.last_unit == "MB/s" else self.last_upload

        summary = (
            f"Speed Test Result ({self.test_timestamp.strftime('%Y-%m-%d %H:%M:%S')}):\n"
            f"- Download: {dl:.2f} {self.last_unit}\n"
            f"- Upload: {ul:.2f} {self.last_unit}\n"
            f"- Ping: {self.last_ping:.1f} ms\n"
            f"- Server: {self.last_server}"
        )
        clipboard: QClipboard = QApplication.clipboard()
        clipboard.setText(summary)
        self.status_label.setText("Result copied to clipboard.")

    def exportSingleResult(self):
        """
        Exportiert nur das letzte Testergebnis als CSV.
        Spalten: Timestamp; Download; Upload; Ping (ms); Server
        """
        if not self.test_timestamp:
            return

        default_name = f"speedtest_{self.test_timestamp.strftime('%Y%m%d_%H%M%S')}.csv"
        path, _ = QFileDialog.getSaveFileName(
            self, "Save Result as CSV", default_name, "CSV Files (*.csv)"
        )
        if not path:
            return

        try:
            with open(path, mode="w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=";")
                writer.writerow(["Timestamp", "Download", "Upload", "Ping (ms)", "Server"])
                dl = self.last_download / 8.0 if self.last_unit == "MB/s" else self.last_download
                ul = self.last_upload / 8.0 if self.last_unit == "MB/s" else self.last_upload
                writer.writerow([
                    self.test_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    f"{dl:.2f} {self.last_unit}",
                    f"{ul:.2f} {self.last_unit}",
                    f"{self.last_ping:.1f}",
                    self.last_server
                ])
            self.status_label.setText(f"Result saved: {os.path.basename(path)}")
        except Exception as e:
            self.status_label.setText(f"Error saving result: {e}")

    def showHistory(self):
        """Öffnet Dialog mit voller Test-Historie."""
        dlg = HistoryDialog(self, self.history)
        dlg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpeedTestWindow()
    window.show()
    sys.exit(app.exec())
