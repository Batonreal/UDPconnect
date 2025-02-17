import sys
import socket
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextBrowser
from PySide6.QtCore import QThread, Signal

from UDPconnectQT import Ui_Dialog

portNumber = 6868

class UDPReceiverThread(QThread):
    message_received = Signal(str)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self.running = True
        self.sock = None

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", self.port))

        while self.running:
            try:
                data, addr = self.sock.recvfrom(1024)
                message = data.decode()
                self.message_received.emit(message)
            except OSError:
                break
        
        if self.sock:
            self.sock.close()

    def stop(self):
        self.running = False
        if self.sock:
            self.sock.close()
        self.quit()
        self.wait()

class UDPSenderApp(QDialog):
    def __init__(self):
        super(UDPSenderApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.initUI()

        self.rt = UDPReceiverThread(portNumber)
        self.rt.message_received.connect(self.display_received_message)
        self.rt.start()

    def initUI(self):
        self.ui.pushButton.clicked.connect(self.send_udp_message)

        ip_address = socket.gethostbyname(socket.gethostname())
        self.ui.ipInfo.setText(f"Ваш IP адрес: {ip_address}")
        
        self.ui.portInfo.setText(f"Ваш порт: {portNumber}")

        self.show()

    def send_udp_message(self):
        ip = self.ui.ipConfig.text()
        port = int(self.ui.portConfig.text())
        message = self.ui.textMessage.text()

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
    
    def display_received_message(self, message):
        self.ui.textBrowser.append(message)

    def closeEvent(self, event):
        self.rt.stop()
        self.rt.wait()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UDPSenderApp()
    ex.show()
    sys.exit(app.exec())