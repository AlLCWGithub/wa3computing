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
    
            if command == "SCROLL":
    
                display.scroll(value)
    
                uart.write("OK|SCROLL\n")
    
            elif command == "TABLE_OCCUPIED":
    
                zone, size = value.split("|")
    
                display.scroll("Zone: {}, Size: {}".format(zone, size))
    
                uart.write("OK|TABLE_OCCUPIED\n")

            elif command == "THANK_YOU":

                display.scroll("THANK YOU")

                uart.write("OK|THANK_YOU\n")
    
            elif command == "CROWD":
    
                if value == "LOW":
                    display.show(Image.YES)
                    np.fill((0, 255, 0)) # green
                    np.show()
    
                elif value == "CROWDED":
                    display.show(Image('00000:'
                        '09090:'
                        '00000:'
                        '99999:'
                        '00000')) # no expression face
                    np.fill((255, 165, 0)) # orange
                    np.show()
    
                elif value == "FULL":
                    display.show(Image.NO)
                    np.fill((255, 0, 0)) # red
                    np.show()
    
                uart.write("OK|CROWD\n")
    
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