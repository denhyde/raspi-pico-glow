# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the RGB LEDs
GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

while True:
    
    # First LED fades in
    for i in range(255):
        GRBled1.fill((i,0,0))
        GRBled1.write()
        time.sleep(0.005)

    for i in reversed (range(255)):
        GRBled1.fill((i,0,0))
        GRBled1.write()        
        time.sleep(0.005)

    #Turn off the first LED
    GRBled1.fill((0,0,0)) # All zero = no light!
    GRBled1.write()
    
    # Second LED fades out (using reversed)
    for i in range(255):
        GRBled2.fill((0,i,0))
        GRBled2.write()
        time.sleep(0.005)

    for i in reversed (range(255)):
        GRBled2.fill((0,i,0))
        GRBled2.write()
        time.sleep(0.005)
