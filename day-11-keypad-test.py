from machine import Pin
import time

# Set up column pins (inputs)
key1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
key2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
key3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
key4 = Pin(12, Pin.IN, Pin.PULL_DOWN)

while True:
    
    if key1.value() == 1:
        print("Button 1")

    if key2.value() == 1:
        print("Button 2")
        
    if key3.value() == 1:
        print("Button 3")
    
    if key4.value() == 1:
        print("Button 4")
    
    time.sleep(0.3)
