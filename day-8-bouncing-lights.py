# Imports
from machine import Pin
from neopixel import NeoPixel
import time

# Define the strip pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2), 12)

# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()
time.sleep(1)
        
while True:
    
    for i in range(12):
        
        ring[i] = (5,0,5)
        ring.write()
        
        # Show the light for this long
        time.sleep(0.09)
        
        #Clear the ring at the end of each loop
        ring.fill((0,0,0))
        ring.write()
        
    for i in reversed (range(12)):
        
        ring[i] = (5,0,5)
        ring.write()
        
        # Show the light for this long
        time.sleep(0.09)
        
        #Clear the ring at the end of each loop
        ring.fill((0,0,0))
        ring.write()
