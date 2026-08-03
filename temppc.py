import serial
import time

ser = serial.Serial("COM5", 115200, timeout=1)

# Give the micro:bit time to reset after opening the port
time.sleep(2)

print("Sending message...")
ser.write(b"SCROLL:Hello World!\n")
time.sleep(1)
ser.write(b"SCROLL:Hello World!\n")

print("Waiting for replies...\n")

start = time.time()

while time.time() - start < 10:
    if ser.in_waiting:
        message = ser.readline().decode(errors="replace").strip()
        print("[micro:bit]", message)

    time.sleep(0.05)

ser.close()
print("Done.")