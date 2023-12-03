# Imports
from machine import Pin
import time

# Set up our button name and GPIO pin number
# Set the pin as an input and use a pull down
redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up output pins
redLED = Pin(14, Pin.OUT)
onboardLED = Pin(25, Pin.OUT)

# Set up counter variable
count = 0 # Start at zero

while True: # Loop forever

    time.sleep(0.2) # Short delay to allow to debounce the button
    
#    if redButton.value() == 1: # If the red button is pressed
#        print("Light OFF")
#        redLED.value(0) # LED pin LOW
#
#    if greenButton.value() == 1: # If the green button is pressed
#        print("Light ON")
#        redLED.value(1) # LED pin HIGH

#     if redButton.value() == 1: # If the red button is pressed
#         redLED.toggle()

    redLED.value(0) # LED off until button press
    onboardLED.value(0) # LED off until button press

    if redButton.value() == 1:
        count = count - 1 # Reduce count by 1
        redLED.value(1) # LED on
        print(count) # Print our updated count
        
    if greenButton.value() == 1:
        count = count + 1 # Increase count by 1
        onboardLED.value(1) # LED on
        print(count) # Print our updated count
