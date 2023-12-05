from machine import Pin
import time
import random

# Set up input pins
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up the LED pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Create a list of LEDs
segments = [seg1, seg2, seg3, seg4, seg5]



# LED Scanner
#while True:
#
#    # For loop to turn each LED on then off in order of the list
#    for led in segments:
#        
#        led.value(1)
#        time.sleep(0.08)
#        led.value(0)
#        
#    # For loop in reverse, running backwards through the list
#    for led in reversed(segments):
#        
#        led.value(1)
#        time.sleep(0.08)
#        led.value(0)



# Random LEDs
#while True:
#    
#    r = random.randint(0,4) # set r to a random number between 0 and 4
#    
#    segments[r].value(1) # light the segment from the list with the index of r
#    
#    time.sleep(0.1)
#    
#    segments[r].value(0) # Turn off the same LED



# Button press counter

# Set the initial count for the index
count = -1

# Turn off all LEDs to start
seg1.value(0)
seg2.value(0)
seg3.value(0)
seg4.value(0)
seg5.value(0)

while True:
    
    time.sleep(0.01) # Short delay to avoid the program running too fast
    
    if redbutton.value() == 1: # If red button pressed
        
        if count == 4: # If the count is already 4
            pass # Do nothing
            
        else:
            count = count + 1 # Add 1 to our counter
            segments[count].value(1) # Light the LED index for the count
            time.sleep(0.2)
            
    if greenbutton.value() == 1: # If green button pressed
        
        if count == -1: # If count is already -1
            pass # Do nothing
            
        else:   
            segments[count].value(0) # Turn off the LED index for the count
            time.sleep(0.2)
            count = count -1 # Remove 1 from our counter
