from microbit import *
import distance

distance_sensor = distance.DISTANCE(pin1)

uart.init(baudrate=9600)

buffer = ""

display.scroll("READY")


def serialconnection():
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
    
            elif command == "LED":
    
                if value == "GREEN":
                    display.show(Image.YES)
    
                elif value == "RED":
                    display.show(Image.NO)
    
                uart.write("OK|LED\n")
    
            else:
    
                uart.write("ERROR|Unknown command\n")

def runfan():
    if distance_sensor.get_distance() < 25:
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)

while True:
    serialconnection()
    runfan()