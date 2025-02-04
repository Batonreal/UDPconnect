import sys
import socket
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel

from UDPconnectQT import Ui_Dialog

class UDPSenderApp(QDialog):
    def __init__(self):
        super(UDPSenderApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.initUI()

    def initUI(self):
        self.ui.pushButton.clicked.connect(self.send_udp_message)
        self.show()

    def send_udp_message(self):
        # Получаем данные из полей ввода
        ip = self.ui.ipConfig.text()
        port = int(self.ui.portConfig.text())
        message = self.ui.lineEdit_3.text()

        # Создаем UDP сокет
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            # Отправляем сообщение
            sock.sendto(message.encode(), (ip, port))
            print(f"Сообщение отправлено на {ip}:{port}")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
        finally:
            # Закрываем сокет
            sock.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UDPSenderApp()
    ex.show()
    sys.exit(app.exec())