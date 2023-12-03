# Imports
from machine import Pin
import time

# Pin setup
greenOnBoard = Pin(25, Pin.OUT)	# Set GPIO 25 as an output
redBlock = Pin(14, Pin.OUT)		# Set GPIO 14 as an output

# Program Start #
print("Green LED ON, Red blinking!")

greenOnBoard.value(1)	# LED on

#while True:				# Loop forever
for i in range(10):		# Run the code below 10 times (i = 0..9)
    redBlock.value(1)	# LED on
    time.sleep(0.5)		# Wait half a second

    redBlock.value(0)	# LED off
    time.sleep(0.5)		# Wait half a second

greenOnBoard.value(0)	# LED off

print("Both LEDs OFF!")
