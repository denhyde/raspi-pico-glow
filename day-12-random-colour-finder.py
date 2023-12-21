from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from neopixel import NeoPixel
import time
import random

# LED details
GPIOnumber = 2
LEDcount = 15

# Define the strand pin number and number of LEDs from variables
strand = NeoPixel(Pin(GPIOnumber), LEDcount)

# Define LCD I2C pins/BUS/address
SDA = 14
SCL = 15
I2C_BUS = 1
LCD_ADDR = 0x27

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# Set up LCD I2C
lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# Turn off all LEDs before program start
strand.fill((0,0,0))
strand.write()
time.sleep(1)

while True:
    
    lcd.clear()
    
    # Add surrounding text
    lcd.putstr("This colour is:")
    lcd.move_to(0, 1)
    lcd.putstr("R:   G    B")
    
    # Create random RGB values
    r = random.randint(0,127)	# can use 0..255
    g = random.randint(0,127)
    b = random.randint(0,127)
        
    # Fill the strand with the current colour
    strand.fill((r,g,b))
    strand.write()
    
    # Display the RGB values on the LCD
    lcd.move_to(1, 1)
    lcd.putstr(str(r)) # R value
    
    lcd.move_to(6, 1)
    lcd.putstr(str(g)) # G value
    
    lcd.move_to(11, 1)
    lcd.putstr(str(b)) # B value
        
    time.sleep(5)
