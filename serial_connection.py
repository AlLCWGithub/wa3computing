import serial
import time
# CHANGE TO COM4/5 

# How this works:
# The micro:bit sends data to the PC in the format "command|value\n"

class Packet:
    def __init__(self, command, data):
        self.command = command
        self.data = data

    def __repr__(self):
        return f"Packet({self.command}, {self.data})"


class SerialConnection:

    def __init__(self, port="COM5", baudrate=9600):

        self.ser = serial.Serial(port, baudrate, timeout=0.1)

        # Give the micro:bit time to reboot
        time.sleep(5)

        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

        self.buffer = ""

    def send(self, command, data=""):

        packet = f"{command}|{data}\n"

        self.ser.write(packet.encode())

        print("[PC -> micro:bit]", packet.strip())

    def receive(self):

        data = self.ser.read(self.ser.in_waiting or 1)

        if data:
            self.buffer += data.decode(errors="ignore")

        if "\n" not in self.buffer:
            return None

        line, self.buffer = self.buffer.split("\n", 1)

        line = line.strip()

        print("[micro:bit -> PC]", line)

        if "|" not in line:
            return Packet(line, "")

        command, value = line.split("|", 1)

        return Packet(command, value)

    def close(self):

        self.ser.close()