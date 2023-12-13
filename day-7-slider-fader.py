# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2), 1)

# Create a variable for our analogue reading
analoguereading = 0

# Create a variable for our converted GRB value
GRBvalue = 0

while True:
    
    # Read the potentiometer value
    analoguereading = potentiometer.read_u16() 
    
    # Take the analogue range (65535), divide it by the GRB range (255)
    # Then take the analogue reading and multiply it by that number
    # Round the number as our RGB code does not want floats (decimal places)
    GRBvalue = round(analoguereading * (255 / 65535))
    
    # Print the values, with text to indicate which is which
    print("Analogue: ",analoguereading) # original analogue value
    print("GRB:      ",GRBvalue) # converted RGB value
     
    # Light the LED with the converted BRG value
    GRBled.fill((0,0,GRBvalue))
    GRBled.write()
    
    time.sleep(0.1)
