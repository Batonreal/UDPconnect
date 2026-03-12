from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QRadialGradient
from PySide6.QtCore import Qt


class ColorLed(QWidget):
    """Круглый LED-индикатор с 3 цветами: красный, жёлтый, зелёный. По умолчанию серый."""

    RED = QColor(255, 0, 0)
    YELLOW = QColor(255, 255, 0)
    GREEN = QColor(0, 200, 0)
    GRAY = QColor(160, 160, 160)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._color = self.GRAY

    def setColor(self, color: QColor):
        self._color = color
        self.update()

    def setRed(self):
        self.setColor(self.RED)

    def setYellow(self):
        self.setColor(self.YELLOW)

    def setGreen(self):
        self.setColor(self.GREEN)

    def setGray(self):
        self.setColor(self.GRAY)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        side = min(self.width(), self.height())
        x = (self.width() - side) / 2
        y = (self.height() - side) / 2

        gradient = QRadialGradient(x + side * 0.4, y + side * 0.4, side * 0.5)
        gradient.setColorAt(0.0, self._color.lighter(180))
        gradient.setColorAt(0.5, self._color)
        gradient.setColorAt(1.0, self._color.darker(150))

        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(int(x), int(y), side, side)
        painter.end()
