import sys
import random
import math
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton
)
from PyQt6.QtCore import Qt, QTimer, QRectF, QPointF
from PyQt6.QtGui import QPainter, QPen, QFont, QColor, QIcon
import pyqtgraph as pg


class SpeedometerWidget(QWidget):
    def __init__(self, title="", parent=None):
        super().__init__(parent)
        self.title = title            # Title for the gauge (e.g., "Download", "Upload")
        self.current_speed = 0        # Current speed value (Mbps)
        self.min_speed = 0
        self.max_speed = 250          # Maximum speed for the gauge
        self.setMinimumSize(300, 300)

    def setSpeed(self, speed):
        self.current_speed = speed
        self.update()

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        radius = min(width, height) / 2 * 0.8
        center = QPointF(width / 2, height / 2)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw outer circle
        pen = QPen(Qt.GlobalColor.white, 4)
        painter.setPen(pen)
        painter.drawEllipse(center, radius, radius)

        # Draw tick marks and numeric labels
        painter.save()
        num_ticks = 10
        for i in range(num_ticks + 1):
            angle = 150 - (240 / num_ticks) * i  # Gauge arc from 150° to -90°
            rad = math.radians(angle)
            inner_point = QPointF(center.x() + (radius - 10) * math.cos(rad),
                                  center.y() - (radius - 10) * math.sin(rad))
            outer_point = QPointF(center.x() + radius * math.cos(rad),
                                  center.y() - radius * math.sin(rad))
            painter.drawLine(inner_point, outer_point)
            # Labels for ticks
            speed_val = int(self.min_speed + (self.max_speed - self.min_speed) * i / num_ticks)
            label_point = QPointF(center.x() + (radius - 30) * math.cos(rad),
                                  center.y() - (radius - 30) * math.sin(rad))
            font = QFont("Roboto", 8)
            painter.setFont(font)
            text = str(speed_val)
            text_rect = painter.fontMetrics().boundingRect(text)
            label_rect = QRectF(label_point.x() - text_rect.width() / 2,
                                label_point.y() - text_rect.height() / 2,
                                text_rect.width(), text_rect.height())
            painter.drawText(label_rect, Qt.AlignmentFlag.AlignCenter, text)
        painter.restore()

        # Clamp current_speed within limits
        speed = max(self.min_speed, min(self.current_speed, self.max_speed))
        # Map speed value to needle angle (150° for min to -90° for max)
        needle_angle = 150 - ((speed - self.min_speed) / (self.max_speed - self.min_speed)) * 240
        rad = math.radians(needle_angle)

        # Draw the needle
        painter.save()
        pen = QPen(QColor("#FF4500"), 4)
        painter.setPen(pen)
        needle_length = radius - 20
        end_point = QPointF(center.x() + needle_length * math.cos(rad),
                            center.y() - needle_length * math.sin(rad))
        painter.drawLine(center, end_point)
        painter.restore()

        # Draw pivot circle
        painter.setBrush(QColor("#FF4500"))
        painter.drawEllipse(center, 5, 5)

        # Draw the current speed text below gauge center
        painter.setPen(QColor("#FFFFFF"))
        font = QFont("Roboto", 14, QFont.Weight.Bold)
        painter.setFont(font)
        speed_text = f"{speed:.1f} Mbps"
        text_rect = painter.fontMetrics().boundingRect(speed_text)
        painter.drawText(int(center.x() - text_rect.width() / 2),
                         int(center.y() + radius / 2 + text_rect.height()), speed_text)

        # Draw gauge title at top-center of the widget
        if self.title:
            title_font = QFont("Roboto", 16, QFont.Weight.Bold)
            painter.setFont(title_font)
            title_rect = painter.fontMetrics().boundingRect(self.title)
            painter.drawText(int(center.x() - title_rect.width() / 2),
                             int(center.y() - radius - 10), self.title)


class SpeedTestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P-Term Speed Test")
        self.setGeometry(100, 100, 1000, 700)
        self.duration = 20  # Duration of the test in seconds
        self.elapsed = 0
        self.download_data = []     # List to store download speeds per second
        self.upload_data = []       # List to store upload speeds per second

        self.initUI()
        self.setStyleSheet(self.loadStylesheet())

        user = os.getenv("USERNAME") or os.getenv("USER")
        self.repo_path = f"C:/Users/{user}/p-terminal/pp-term"
        icon_path = f"C:/Users/{user}/p-terminal/pp-term/icons/p-term-logo-5.ico"
        self.setWindowIcon(QIcon(icon_path))

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Pyqtgraph chart to display speed history
        self.chart = pg.PlotWidget(title="Internet Speed History (Mbps)")
        self.chart.setBackground(None)
        self.chart.getAxis("bottom").setPen(pg.mkPen(color="#FFFFFF"))
        self.chart.getAxis("left").setPen(pg.mkPen(color="#FFFFFF"))
        self.chart.showGrid(x=True, y=True, alpha=0.3)
        # Two curves: one for download, one for upload speeds
        self.download_curve = self.chart.plot(pen=pg.mkPen(color="#1E90FF", width=2), name="Download")
        self.upload_curve = self.chart.plot(pen=pg.mkPen(color="#32CD32", width=2), name="Upload")

        # Create download and upload speedometers
        gauges_layout = QHBoxLayout()
        self.download_speedometer = SpeedometerWidget(title="Download Speed")
        self.upload_speedometer = SpeedometerWidget(title="Upload Speed")
        gauges_layout.addWidget(self.download_speedometer)
        gauges_layout.addWidget(self.upload_speedometer)

        # Info label for status
        self.info_label = QLabel("Press the button to start the speed test!")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Start test button
        self.start_button = QPushButton("Start Speed Test")
        self.start_button.clicked.connect(self.startTest)

        # Add widgets to main layout
        main_layout.addWidget(self.chart, 2)
        main_layout.addLayout(gauges_layout, 3)
        main_layout.addWidget(self.info_label)
        main_layout.addWidget(self.start_button)

        # Timer to update speeds every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTest)

    def loadStylesheet(self):
        return """
            QWidget {
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1b2631, stop:1 #0f1626);
                color: #FFFFFF;
                font-family: 'Roboto', sans-serif;
                font-size: 14px;
            }
            QLineEdit {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
                border: 1px solid #778899;
                border-radius: 5px;
                padding: 5px;
                color: #FFFFFF;
            }
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #2c3e50, stop:1 #1c2833);
                border: none;
                border-radius: 5px;
                padding: 5px 10px;
                color: #FFFFFF;
            }
            QPushButton:hover {
                background-color: #1c2833;
            }
            QTreeWidget {
                background-color: transparent;
                border: 1px solid #778899;
                border-radius: 8px;
            }
            QTreeWidget::item {
                padding: 8px;
                border-bottom: 1px solid #778899;
            }
            QTreeWidget::item:selected {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
                color: #FFFFFF;
            }
            QHeaderView::section {
                background-color: transparent;
                padding: 8px;
                border: none;
            }
            QLabel {
                background: transparent;
                font-size: 16px;
            }
            QTextEdit {
                background-color: transparent;
                border: 1px solid #778899;
                border-radius: 8px;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
            QTabBar::tab {
                background: transparent;
                padding: 8px;
                margin: 2px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #34495e, stop:1 #1c2833);
                color: #FFFFFF;
            }
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                background-color: transparent;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background-color: #ffffff;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: transparent;
            }
            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical {
                background: transparent;
            }
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: transparent;
            }
            QScrollBar:horizontal {
                background-color: transparent;
                height: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:horizontal {
                background-color: #ffffff;
                min-width: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                background: transparent;
            }
            QScrollBar::left-arrow:horizontal,
            QScrollBar::right-arrow:horizontal {
                background: transparent;
            }
            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: transparent;
            }
        """

    def startTest(self):
        self.elapsed = 0
        self.download_data = []
        self.upload_data = []
        self.download_curve.clear()
        self.upload_curve.clear()
        self.start_button.setEnabled(False)
        self.info_label.setText("Speed test in progress...")
        # Start timer: update every 1000 ms (1 second)
        self.timer.start(1000)
        # Annahme: Das Repository befindet sich im p-terminal-Ordner des aktuellen Benutzers

    def updateTest(self):
        if self.elapsed >= self.duration:
            self.timer.stop()
            if self.download_data and self.upload_data:
                avg_download = sum(self.download_data) / len(self.download_data)
                avg_upload = sum(self.upload_data) / len(self.upload_data)
            else:
                avg_download = avg_upload = 0
            self.info_label.setText(f"Test completed! Average Download: {avg_download:.1f} Mbps | Average Upload: {avg_upload:.1f} Mbps")
            self.start_button.setEnabled(True)
        else:
            # Simulate random speeds
            download_speed = random.uniform(50, 150)  # Mbps for download
            upload_speed = random.uniform(10, 60)      # Mbps for upload

            self.download_data.append(download_speed)
            self.upload_data.append(upload_speed)

            # Update speedometers
            self.download_speedometer.setSpeed(download_speed)
            self.upload_speedometer.setSpeed(upload_speed)

            # Update chart data
            self.download_curve.setData(self.download_data, pen=pg.mkPen(color="#1E90FF", width=2))
            self.upload_curve.setData(self.upload_data, pen=pg.mkPen(color="#32CD32", width=2))

            self.elapsed += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpeedTestWindow()
    window.show()
    sys.exit(app.exec())