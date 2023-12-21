from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from neopixel import NeoPixel
import time

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

mycolours ={
    "Red":(255,0,0),
    "Green":(0,255,0),
    "Blue":(0,0,255),
    "White":(255,255,255),
}

# Turn off all LEDs before program start
strand.fill((0,0,0))
strand.write()
time.sleep(1)

while True:
    
    for i in mycolours:
        
        print(i)
        
        # Clear the LCD
        lcd.clear()
        
        # Fill the strand with the current colour
        strand.fill(mycolours[i])
        strand.write()
        
        # Update display with the key of the colour
        lcd.putstr("Strand colour:")
        lcd.move_to(0, 1) # 2nd row
        lcd.putstr(str(i)) # Show the dictionary key name
        
        time.sleep(2)
