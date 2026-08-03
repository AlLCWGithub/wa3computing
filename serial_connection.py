import serial
import time

ser = serial.Serial("COM5", 115200, timeout=1)
time.sleep(2)

class Message:
    def __init__(self, command, data):
        self.command = command
        self.data = data

    def execute(self):
        if self.command == None:
            return
        if self.command == "ERROR":
            print("Error: ", self.data)
    

def send(message):
    ser.write((message + "\n").encode())
    print("[PC -> micro:bit]", message)

def receive():
    if ser.in_waiting:
        message = ser.readline().decode().strip()
        print("[micro:bit -> PC]", message)
        if ":" not in message:
            return Message(None, None)
        command, data = message.split(":", 1)
        return Message(command, data)
    return Message(None, None)


def close():
    if ser is not None:
        ser.close()