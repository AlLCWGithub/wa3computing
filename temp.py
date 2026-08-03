from microbit import *

uart.init(baudrate=115200)

while True:
    message = uart.readline()

    if message:
        display.show(Image.HEART)
        sleep(500)

        try:
            message = message.decode().strip()

            # Send the exact message back to the PC
            uart.write("DEBUG:" + message + "\n")

            if ":" in message:
                command, data = message.split(":", 1)

                uart.write("COMMAND:" + command + "\n")

                if command == "SCROLL":
                    uart.write("SCROLLING\n")
                    display.scroll(data)

        except Exception as e:
            uart.write("ERROR:" + str(e) + "\n")