from microbit import *
import distance
import neopixel
# MICROBIT PROJECT
# Pin 1: Ultrasonic Distance Sensor
# Pin 2: LED Bulb
# Pin 16: Fan

distance_sensor = distance.DISTANCE(pin1) # Distance sensor on pin 1
np = neopixel.NeoPixel(pin2, 1) # Neopixel LED on pin 2

uart.init(baudrate=9600)

buffer = ""

display.scroll("READY")


def serialconnection():
    global buffer # use global buffer to prevent that error of "buffer" being undefined
    data = uart.read() 
    
    if data:
    
        buffer += data.decode()
    
        while "\n" in buffer:
    
            line, buffer = buffer.split("\n", 1)
    
            line = line.strip()
    
            if "|" not in line:
                uart.write("ERROR|Invalid packet\n")
                continue
    
            command, value = line.split("|", 1)
    
            if command == "CROWD": # command to display the LED
    
                if value == "LOW":
                    np.clear()
                    display.show(Image.HAPPY)
                    np.fill((0, 255, 0)) # green
                    np.show()
    
                elif value == "CROWDED":
                    np.clear()
                    display.show(Image('00000:'
                        '09090:'
                        '00000:'
                        '99999:'
                        '00000')) # no expression face
                    np.fill((255, 165, 0)) # orange
                    np.show()
    
                elif value == "FULL":
                    np.clear()
                    display.show(Image.SAD)
                    np.fill((255, 0, 0)) # red
                    np.show()

                uart.write("OK|CROWD\n")

            elif command == "END": # end program
                np.clear()
                uart.write("OK|END\n")

            else:
                uart.write("ERROR|Unknown command\n")

def runfan():
    if distance_sensor.get_distance() < 25:
        pin16.write_digital(1)
        
    else:
        pin16.write_digital(0)

while True:
    serialconnection()
    runfan()