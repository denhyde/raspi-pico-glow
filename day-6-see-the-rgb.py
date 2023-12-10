# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the RGB LEDs
GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

# Activity 1: Multiple colour examples
# Define some GRB colour variables
white = 240,140,255 #White-ish!
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238, 223, 105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215, 100, 0

GRBled1.fill((purple))
GRBled1.write()

# Activity 2: Colour cycling
# Define our colour list
colours = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey]

while True:
    
    for colour in colours:
        
        GRBled.fill((colour))
        
        GRBled.write()
        
        time.sleep(0.1)

# Activity 3: GRB value change and light passing
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
