# Imports
from machine import Pin
from neopixel import NeoPixel
import time

# LED details
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs from variables
strand = NeoPixel(Pin(GPIOnumber), LEDcount)

# Brightness factor (0.0 to 1.0, where 1.0 is full brightness)
brightness = 0.1  # Adjust this value to make the lights dimmer

# Function to scale brightness
def scale_brightness(color, factor):
    """Scale RGB color values by a brightness factor."""
    return tuple(int(c * factor) for c in color)

# Function to generate rainbow colors
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

# Turn off all LEDs before program start
strand.fill((0, 0, 0))
strand.write()
time.sleep(1)

while True:
    for j in range(256):  # Cycle through the full rainbow
        for i in range(LEDcount):
            pixel_index = (i * 256 // LEDcount + j) % 256
            color = wheel(pixel_index)
            dimmed_color = scale_brightness(color, brightness)
            strand[i] = dimmed_color
        strand.write()
        time.sleep(0.005)  # Reduce this value for faster changes

