import sys
import socket
import struct
import random
import json
import datetime
import os
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QThread, Signal, QTimer

from QTmain import Ui_MainWindow

PORT_NUMBER = 19002


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
                uint8_values = [f"{byte:02X}" for byte in data]
                message = " ".join(uint8_values)
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

        self.time_data_timer = QTimer(self)
        self.time_data_timer.timeout.connect(self.precise_send_saved_data_message)
        self.time_data_active = False
        self.next_send_time = None

        self.cyclic_counter = 0

    def initUI(self):
        self.ui.pushButton.clicked.connect(self.send_udp_message)
        self.ui.pushButton_2.clicked.connect(self.send_bin_message)
        self.ui.action_save.triggered.connect(self.save_to_json)
        self.ui.action_exit.triggered.connect(self.exit_application)
        self.ui.action_about.triggered.connect(self.show_about_dialog)
        self.ui.pushAmplitude.clicked.connect(self.send_amplitude_message)
        self.ui.time_data.clicked.connect(self.toggle_time_data) 
        self.ui.SPI_button.clicked.connect(self.SPI_input)
        self.ui.time_period_button.clicked.connect(self.send_time_period_message)

        config_file = "config.json"
        default_config = {
            "ip_config": "192.168.0.56",
            "port_config": 19001,
            "k_data": 50
        }

        if not os.path.exists(config_file):
            with open(config_file, "w") as json_file:
                json.dump(default_config, json_file, indent=4)
            print(f"Файл {config_file} создан с настройками по умолчанию.")

        with open(config_file, "r") as json_file:
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
        uint16_val = 11 + k * 44

        # Placeholder for checksum (4 bytes)
        checksum_placeholder = b'\x00\x00\x00\x00'

        # Формируем Набор фаз по битам:
        num_impulses = 10  # 0-5 бит
        impulse_phases = 0b0000000000  # читать справа налево, 0-9 биты
        impulse_presence = 0b0111111111
        reserved = 0  # 26-31 бит

        phases_and_impulses = (
            (reserved << 26) |
            (impulse_presence << 16) |
            (impulse_phases << 6) |
            num_impulses
        )

        self.cyclic_counter = self.cyclic_counter + 1

        message += struct.pack('!B', uint8_val)
        message += struct.pack('!H', uint16_val)
        message += checksum_placeholder
        message += struct.pack('!I', self.cyclic_counter)

        for i in range(k):
            message += struct.pack('!I', phases_and_impulses)
            impulse_ns_1 = 10000000
            impulse_ns_2 = 10000000
            impulse_ns_3 = 10000000
            impulse_ns_4 = 10000000
            impulse_ns_5 = 10000000
            impulse_ns_6 = 10000000
            impulse_ns_7 = 10000000
            impulse_ns_8 = 10000000
            impulse_ns_9 = 12000000
            impulse_ns_10 = 0

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

        # Calculate checksum
        data_for_checksum = message[:3] + message[7:]
        print(len(data_for_checksum))
        checksum = self.calculate_crc32(data_for_checksum)
        # print(struct.pack('!I', checksum))
        # print(f"Сообщение длиной {len(message)} байт: {message}")

        # Insert checksum into the message
        message = message[:3] + struct.pack('!I', checksum) + message[7:]
        # print(f"Сообщение длиной {len(message)} байт: {message}")

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            sock.sendto(message, (ip, port))
            # print(f"Сообщение отправлено на {ip}:{port} ({k} повторений)")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
        finally:
            sock.close()

        current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.ui.textBrowser.append(f"[{current_time}] Сообщение отправлено на {ip}:{port} ({k} повторений)")

    def send_saved_data_message(self):
        ip = self.ui.ipConfig.text()
        port = int(self.ui.portConfig.text())
        k = self.ui.k_value.value()

        message = b''

        uint8_val = 3
        uint16_val = 15 + k * 44

        # Placeholder for checksum (4 bytes)
        checksum_placeholder = b'\x00\x00\x00\x00'

        # Формируем Набор фаз по битам:
        num_impulses = 10  # 0-5 бит
        impulse_phases = 0b0000000000  # читать справа налево, 0-9 биты
        impulse_presence = 0b0111111111
        reserved = 0  # 26-31 бит

        phases_and_impulses = (
            (reserved << 26) |
            (impulse_presence << 16) |
            (impulse_phases << 6) |
            num_impulses
        )

        self.cyclic_counter = self.cyclic_counter + 1
        # self.cyclic_counter = 1
        time_delay = self.ui.time_delay_box.value() * 10

        message += struct.pack('!B', uint8_val)
        message += struct.pack('!H', uint16_val)
        message += checksum_placeholder
        message += struct.pack('!I', self.cyclic_counter)
        message += struct.pack('!i', time_delay)

        for i in range(k):
            message += struct.pack('!I', phases_and_impulses)

            if i == 0:
                impulse_ns_1 = 0
            else:
                impulse_ns_1 = 318000000
            impulse_ns_2 = 10000000
            impulse_ns_5 = 10000000
            impulse_ns_3 = 10000000
            impulse_ns_4 = 10000000
            impulse_ns_6 = 10000000
            impulse_ns_7 = 10000000
            impulse_ns_8 = 10000000
            impulse_ns_9 = 12000000
            impulse_ns_10 = 0

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

        # Calculate checksum
        data_for_checksum = message[:3] + message[7:]
        print(len(data_for_checksum))
        checksum = self.calculate_crc32(data_for_checksum)
        # print(struct.pack('!I', checksum))
        # print(f"Сообщение длиной {len(message)} байт: {message}")

        # Insert checksum into the message
        message = message[:3] + struct.pack('!I', checksum) + message[7:]
        # print(f"Сообщение длиной {len(message)} байт: {message}")

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            sock.sendto(message, (ip, port))
            # print(f"Сообщение отправлено на {ip}:{port} ({k} повторений)")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
        finally:
            sock.close()

        current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.ui.textBrowser.append(f"[{current_time}] Сообщение отправлено на {ip}:{port} ({k} повторений)")

    def mode_amplitude(self, message, mode):
        if (mode == 1):
            self.message += struct.pack('!B', 5)
            self.message += struct.pack('!B', 5)
            self.message += struct.pack('!B', 14)
            self.message += struct.pack('!B', 14)
            self.message += struct.pack('!B', 16)
            self.message += struct.pack('!B', 16)
            self.message += struct.pack('!B', 16)
            self.message += struct.pack('!B', 16)
            self.message += struct.pack('!B', 14)
            self.message += struct.pack('!B', 14)
            self.message += struct.pack('!B', 11)
            self.message += struct.pack('!B', 11)
            self.message += struct.pack('!B', 8)
            self.message += struct.pack('!B', 8)
            self.message += struct.pack('!B', 6)
            self.message += struct.pack('!B', 6)
            self.message += struct.pack('!B', 4)
            self.message += struct.pack('!B', 4)
            self.message += struct.pack('!B', 2)
            self.message += struct.pack('!B', 2)
            self.message += struct.pack('!B', 1)
            self.message += struct.pack('!B', 1)
            self.message += struct.pack('!B', 0)
            self.message += struct.pack('!B', 0)
            # message += struct.pack('!B', 0)
            # message += struct.pack('!B', 0)
            # message += struct.pack('!B', 0)
            # message += struct.pack('!B', 0)
            # message += struct.pack('!B', 0)
            # message += struct.pack('!B', 0)
            # message += struct.pack('!B', 0)
            # message += struct.pack('!B', 0)
            
            for _ in range(20):
                uint8_loop = 0
                self.message += struct.pack('!B', uint8_loop)
                self.message += struct.pack('!B', uint8_loop)

            # message += struct.pack('!B', 10)
            # message += struct.pack('!B', 10)

        elif (mode == 2):
            self.message += struct.pack('!B', 4)
            self.message += struct.pack('!B', 4)
            self.message += struct.pack('!B', 13)
            self.message += struct.pack('!B', 13)
            self.message += struct.pack('!B', 16)
            self.message += struct.pack('!B', 16)
            self.message += struct.pack('!B', 16)
            self.message += struct.pack('!B', 16)
            self.message += struct.pack('!B', 14)
            self.message += struct.pack('!B', 14)
            self.message += struct.pack('!B', 12)
            self.message += struct.pack('!B', 12)
            self.message += struct.pack('!B', 9)
            self.message += struct.pack('!B', 9)
            self.message += struct.pack('!B', 7)
            self.message += struct.pack('!B', 7)
            self.message += struct.pack('!B', 5)
            self.message += struct.pack('!B', 5)
            self.message += struct.pack('!B', 3)
            self.message += struct.pack('!B', 3)
            self.message += struct.pack('!B', 2)
            self.message += struct.pack('!B', 2)
            self.message += struct.pack('!B', 1)
            self.message += struct.pack('!B', 1)
            
            for _ in range(20):
                uint8_loop = 0
                self.message += struct.pack('!B', uint8_loop)
                self.message += struct.pack('!B', uint8_loop)

        elif (mode == 3):
            print("Пока не закончено")

    def send_amplitude_message(self):
        ip = self.ui.ipConfig.text()
        port = int(self.ui.portConfig.text())

        self.message = b''

        uint8_val = 5
        uint16_val = random.randint(0, 65535)
        checksum_placeholder = b'\x00\x00\x00\x00'
        uint32_val2 = random.randint(0, 4294967295)
        uint8_val2 = 0x80

        self.message += struct.pack('!B', uint8_val)
        self.message += struct.pack('!H', uint16_val)
        self.message += checksum_placeholder
        self.message += struct.pack('!I', uint32_val2)
        self.message += struct.pack('!B', uint8_val2)

        self.mode_amplitude(self.message, self.ui.select_mode.value())

        data_for_checksum = self.message[:3] + self.message[7:]
        print(len(data_for_checksum))
        checksum = self.calculate_crc32(data_for_checksum)
        print(struct.pack('!I', checksum))
        print(f"Сообщение длиной {len(self.message)} байт: {self.message}")

        # Insert checksum into the message
        self.message = self.message[:3] + struct.pack('!I', checksum) + self.message[7:]
        print(f"Сообщение длиной {len(self.message)} байт: {self.message}")

        # Send the message via UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            sock.sendto(self.message, (ip, port))
            print(f"Amplitude message sent to {ip}:{port}")
        except Exception as e:
            print(f"Error sending amplitude message: {e}")
        finally:
            sock.close()

    def SPI_input(self):
        ip = self.ui.ipConfig.text()
        port = int(self.ui.portConfig.text())
        message = b''
        
        uint8_val = 30
        message += struct.pack('!B', uint8_val)
        checksum = self.calculate_crc32(message)
        message += struct.pack('!I', checksum)
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
        try:
            sock.sendto(message, (ip, port))
            print(f"SPI send message {ip}:{port}")
        except Exception as e:
            print(f"Ошибка при отправке сообщения (SPI): {e}")
        finally:
            sock.close()

    def send_time_period_message(self):
        """Отправка сообщения с ID 41 и 8 значениями времени"""
        ip = self.ui.ipConfig.text()
        port = int(self.ui.portConfig.text())

        message = b''

        uint8_val = 41
        uint16_val = 27
        checksum_placeholder = b'\x00\x00\x00\x00'

        self.cyclic_counter = self.cyclic_counter + 1

        message += struct.pack('!B', uint8_val)
        message += struct.pack('!H', uint16_val)
        message += checksum_placeholder
        message += struct.pack('!I', self.cyclic_counter)

        time_values = [
            self.ui.time_period_1.value(),
            self.ui.time_period_2.value(),
            self.ui.time_period_3.value(),
            self.ui.time_period_4.value(),
            self.ui.time_period_5.value(),
            self.ui.time_period_6.value(),
            self.ui.time_period_7.value(),
            self.ui.time_period_8.value()
        ]

        for time_val in time_values:
            message += struct.pack('!H', time_val)

        data_for_checksum = message[:3] + message[7:]
        checksum = self.calculate_crc32(data_for_checksum)

        message = message[:3] + struct.pack('!I', checksum) + message[7:]

        print(f"Сообщение времен периодов длиной {len(message)} байт: {message.hex()}")
        print(f"Времена: {time_values}")

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            sock.sendto(message, (ip, port))
            print(f"Time period message (ID 41) sent to {ip}:{port}")
        except Exception as e:
            print(f"Ошибка при отправке сообщения времен периодов: {e}")
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
        
    def calculate_crc32(self, data):
        crc = 0xFFFFFFFF
        polinomial = 0xEDB88320
        # polinomial = 0x11111111 # fake polynomial for testing
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 1:
                    crc = (crc >> 1) ^ polinomial
                else:
                    crc >>= 1
        return crc ^ 0xFFFFFFFF
    
    def display_received_message(self, message):
        current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.ui.textBrowser.append(f"[{current_time}] {message}")

    def closeEvent(self, event):
        self.rt.stop()
        self.rt.wait()
        event.accept()

    def show_about_dialog(self):
        QMessageBox.about(self, "О программе", "Разработано отделом 32451 для проверки работоспособности микрокомпьютера ЭЛВИС САЛЮТ по протоколу передачи данных по UDP.")

    def exit_application(self):
        self.close()

    def toggle_time_data(self):
        if not self.time_data_active:
            self.time_data_active = True
            self.next_send_time = time.perf_counter()
            print("Периодическая отправка данных запущена")
            self.ui.time_data.setText("Остановить отправку")
            self.precise_send_saved_data_message()
        else:
            self.time_data_active = False
            print("Периодическая отправка данных остановлена")
            self.ui.time_data.setText("Фазы и временные данные")

    def precise_send_saved_data_message(self):
        if not self.time_data_active:
            return
        self.send_saved_data_message()
        now = time.perf_counter()
        if self.next_send_time is None:
            self.next_send_time = now + 1.0
        else:
            self.next_send_time += 1.0
        delay = max(0, self.next_send_time - time.perf_counter())
        QTimer.singleShot(round(delay * 1000), self.precise_send_saved_data_message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UDPSenderApp()
    ex.show()
    sys.exit(app.exec())