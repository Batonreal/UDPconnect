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

        self.uint8_packet_id = 0  # Initialize packet ID

    def initUI(self):
        self.ui.pushButton.clicked.connect(self.send_udp_message)
        self.ui.pushButton_2.clicked.connect(self.send_bin_message)
        self.ui.action_save.triggered.connect(self.save_to_json)
        self.ui.action_exit.triggered.connect(self.exit_application)
        self.ui.action_about.triggered.connect(self.show_about_dialog)
        self.ui.pushAmplitude.clicked.connect(self.send_amplitude_message)

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

        uint8_val = 3
        uint16_val = random.randint(0, 65535)
        uint32_val1 = random.randint(0, 4294967295)
        uint32_val2 = random.randint(0, 4294967295)

        message += struct.pack('!B', uint8_val)
        message += struct.pack('!H', uint16_val)
        message += struct.pack('!I', uint32_val1)
        message += struct.pack('!I', uint32_val2)

        for _ in range(k):
            uint32_loop = random.randint(0, 4294967295)

            message += struct.pack('!B', self.uint8_packet_id)
            message += struct.pack('!I', uint32_loop)

            impulse_ns_1 = random.randint(0, 10000000)
            impulse_ns_2 = random.randint(0, 10000)
            impulse_ns_3 = random.randint(0, 10000)
            impulse_ns_4 = random.randint(0, 10000)
            impulse_ns_5 = random.randint(0, 10000)
            impulse_ns_6 = random.randint(0, 10000)
            impulse_ns_7 = random.randint(0, 10000)
            impulse_ns_8 = random.randint(0, 10000)
            impulse_ns_9 = random.randint(0, 10000)
            impulse_ns_10 = random.randint(0, 10000)

            message += struct.pack('!I', impulse_ns_1)
            message += struct.pack('!I', impulse_ns_2)
            message += struct.pack('!I', impulse_ns_3)
            message += struct.pack('!I', impulse_ns_4)
            message += struct.pack('!I', impulse_ns_5)
            message += struct.pack('!I', impulse_ns_6)
            message += struct.pack('!I', impulse_ns_7)
            message += struct.pack('!I', impulse_ns_8)
            message += struct.pack('!I', impulse_ns_9)
            message += struct.pack('!I', impulse_ns_10)

            self.uint8_packet_id = (self.uint8_packet_id + 1) % 256

        self.uint8_packet_id = self.uint8_packet_id - 3

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            sock.sendto(message, (ip, port))
            print(f"Сообщение отправлено на {ip}:{port} ({k} повторений)")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
        finally:
            sock.close()

    def send_amplitude_message(self):
        ip = self.ui.ipConfig.text()
        port = int(self.ui.portConfig.text())

        message = b''

        # Generate random values for each field
        uint8_val = 5
        uint16_val = random.randint(0, 65535)
        uint32_val1 = random.randint(0, 4294967295)
        uint32_val2 = random.randint(0, 4294967295)
        uint8_val2 = random.randint(0, 255)
        uint128_val = random.getrandbits(128)  # Generate a 128-bit random number
        uint32_val3 = random.randint(0, 4294967295)

        # Pack the values into the message
        message += struct.pack('!B', uint8_val)
        message += struct.pack('!H', uint16_val)
        message += struct.pack('!I', uint32_val1)
        message += struct.pack('!I', uint32_val2)
        message += struct.pack('!B', uint8_val2)
        message += uint128_val.to_bytes(16, byteorder='big')  # Convert 128-bit number to bytes
        message += struct.pack('!I', uint32_val3)

        # Send the message via UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            sock.sendto(message, (ip, port))
            print(f"Amplitude message sent to {ip}:{port}")
        except Exception as e:
            print(f"Error sending amplitude message: {e}")
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