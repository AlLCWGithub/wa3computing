from microbit import *

uart.init(baudrate=115200)

while True:
    try:
        message = uart.readline()

        if message:
            message = message.decode('utf-8').strip()
            if ":" in message:
                command, data = message.split(":", 1)
                if command == "SCROLL":
                    display.scroll(data)
    except Exception as e:
       uart.write("ERROR: " + str(e))