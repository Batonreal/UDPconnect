import sys
import socket
import struct
import random
import json
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QTextBrowser
from PySide6.QtCore import QThread, Signal

from QTmain import Ui_MainWindow

PORT_NUMBER = 6869


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


class UDPSenderApp(QMainWindow):
    def __init__(self):
        super(UDPSenderApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.initUI()

        self.rt = UDPReceiverThread(PORT_NUMBER)
        self.rt.message_received.connect(self.display_received_message)
        self.rt.start()

    def initUI(self):
        self.ui.pushButton.clicked.connect(self.send_udp_message)
        self.ui.pushButton_2.clicked.connect(self.send_bin_message)
        self.ui.action_save.triggered.connect(self.save_to_json)
        self.ui.action_exit.triggered.connect(self.exit_application)
        self.ui.action_about.triggered.connect(self.show_about_dialog)

        with open("config.json", "r") as json_file:
            config_data = json.load(json_file)

        self.ui.ipConfig.setText(config_data["ip_config"])
        self.ui.portConfig.setText(str(config_data["port_config"]))
        self.ui.k_value.setValue(config_data["k_data"])

        ip_address = socket.gethostbyname(socket.gethostname())
        self.ui.ipInfo.setText(f"Ваш IP адрес: {ip_address}")        
        self.ui.portInfo.setText(f"Ваш порт: {PORT_NUMBER}")

        self.show()

    def send_udp_message(self):
        ip = self.ui.ipConfig.text()
        port = int(self.ui.portConfig.text())
        message = self.ui.textMessage.text()
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
        try:
            message_bytes = struct.pack("B", 255) + message.encode()
    
            sock.sendto(message_bytes, (ip, port))
            print(f"Сообщение отправлено на {ip}:{port}")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
        finally:
            sock.close()
    
    def send_bin_message(self):
        ip = self.ui.ipConfig.text()
        port = int(self.ui.portConfig.text())
        k = self.ui.k_value.value()

        message = b''

        uint8_val = random.randint(0, 255)
        uint16_val = random.randint(0, 65535)
        uint32_val1 = random.randint(0, 4294967295)
        uint32_val2 = random.randint(0, 4294967295)

        message += struct.pack('!B', uint8_val)
        message += struct.pack('!H', uint16_val) 
        message += struct.pack('!I', uint32_val1)
        message += struct.pack('!I', uint32_val2)

        for _ in range(k):
            uint32_loop = random.randint(0, 4294967295)

            message += struct.pack('!I', uint32_loop) 

            for _ in range(10):
                uint32_inner = random.randint(0, 4294967295)
                message += struct.pack('!I', uint32_inner)

        # for _ in range(k):
        #     uint32_loop = 3333

        #     message += struct.pack('!I', uint32_loop) 

        #     for _ in range(10):
        #         uint32_inner = 1234
        #         message += struct.pack('!I', uint32_inner)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            sock.sendto(message, (ip, port))
            print(f"Сообщение отправлено на {ip}:{port} ({k} повторений)")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
        finally:
            sock.close()

    def save_to_json(self):
        config_data = {
            "ip_config": self.ui.ipConfig.text(),
            "port_config": int(self.ui.portConfig.text()),
            "k_data": self.ui.k_value.value()
        }

        with open("config.json", "w") as json_file:
            json.dump(config_data, json_file, indent=4)

        print("Настройки сохранены в config.json")
    
    def display_received_message(self, message):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.ui.textBrowser.append(f"[{current_time}] {message}")

    def closeEvent(self, event):
        self.rt.stop()
        self.rt.wait()
        event.accept()

    def show_about_dialog(self):
        QMessageBox.about(self, "О программе", "Разработано отделом 32451 для проверки работоспособности микрокомпьютера ЭЛВИС САЛЮТ по протоколу передачи данных по UDP.")

    def exit_application(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UDPSenderApp()
    ex.show()
    sys.exit(app.exec())