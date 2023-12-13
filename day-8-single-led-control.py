# Imports
from machine import Pin
from neopixel import NeoPixel

# Define the ring pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2), 12)
        
# Select the first LED (0)
# Set the RGB colour (red)
ring[0] = (10,0,0)

# Send the data to the ring
ring.write()

ring.fill((0,0,0)) # 'fill' addresses all LEDs
ring.write()
