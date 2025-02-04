import sys
import socket
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMainWindow

from UDPconnectQT import Ui_Dialog

class UDPSenderApp(QMainWindow):
    def __init__(self):
        super(UDPSenderApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # self.initUI()

    # def initUI(self):
    #     # Создаем layout
    #     layout = QVBoxLayout()

    #     # Поле для ввода IP-адреса
    #     self.ip_input = QLineEdit(self)
    #     self.ip_input.setPlaceholderText("Введите IP-адрес")
    #     layout.addWidget(QLabel("IP-адрес:"))
    #     layout.addWidget(self.ip_input)

    #     # Поле для ввода порта
    #     self.port_input = QLineEdit(self)
    #     self.port_input.setPlaceholderText("Введите порт")
    #     layout.addWidget(QLabel("Порт:"))
    #     layout.addWidget(self.port_input)

    #     # Поле для ввода сообщения
    #     self.message_input = QLineEdit(self)
    #     self.message_input.setPlaceholderText("Введите сообщение")
    #     layout.addWidget(QLabel("Сообщение:"))
    #     layout.addWidget(self.message_input)

    #     # Кнопка для отправки сообщения
    #     self.send_button = QPushButton("Отправить", self)
    #     self.send_button.clicked.connect(self.send_udp_message)
    #     layout.addWidget(self.send_button)

    #     # Устанавливаем layout для основного окна
    #     self.setLayout(layout)
    #     self.setWindowTitle("UDP Sender")
    #     self.show()

    # def send_udp_message(self):
    #     # Получаем данные из полей ввода
    #     ip = self.ip_input.text()
    #     port = int(self.port_input.text())
    #     message = self.message_input.text()

    #     # Создаем UDP сокет
    #     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #     try:
    #         # Отправляем сообщение
    #         sock.sendto(message.encode(), (ip, port))
    #         print(f"Сообщение отправлено на {ip}:{port}")
    #     except Exception as e:
    #         print(f"Ошибка при отправке сообщения: {e}")
    #     finally:
    #         # Закрываем сокет
    #         sock.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UDPSenderApp()
    ex.show()
    sys.exit(app.exec())