from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from dht20 import DHT20
import time

# Define LCD/sensor I2C pins/BUS/address
SDA = 14
SCL = 15
I2C_BUS = 1
LCD_ADDR = 0x27
TEMP_ADDR = 0x38

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

# Set up LCD I2C
lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# Set up temperature sensor I2C
tempi2c = I2C(I2C_BUS, sda=SDA, scl=SCL)
dht20 = DHT20(TEMP_ADDR, tempi2c)

# Write  static LCD text
lcd.putstr("Current:")
lcd.move_to(0, 1) # Move to second row
lcd.putstr("L:       H:")

#Take initial reading
measurements = dht20.measurements

# Create temp and humidity variables
# From initial readings
lowtemp = round(measurements['t'],1)
hightemp = round(measurements['t'],1)

# Write initial low temp value to LCD
lcd.move_to(3, 1)
lcd.putstr(str(lowtemp))

# Write initial high temp value to LCD
lcd.move_to(12, 1) # 12th column, 2nd row
lcd.putstr(str(hightemp))
    
while True:
    
    # Grab data from the sensor dictionary
    measurements = dht20.measurements
    
    # Create variable for current temp
    tempnow = round(measurements['t'],1)
    
    # Update current temp on display
    lcd.move_to(12, 0)
    lcd.putstr(str(tempnow))
    
    # If the lowest temp is HIGHER than current temp
    if tempnow < lowtemp:
        
        # Update the lowest recorded temp
        lowtemp = tempnow
        
        # Update the LCD data
        lcd.move_to(3, 1) # 3rd column, 2nd row
        lcd.putstr(str(lowtemp))
        
    # If the highest temp is LOWER than current temp
    if tempnow > hightemp:
        
        # Update the highest recorded temp
        hightemp = tempnow
        
        # Update the LCD data
        lcd.move_to(12, 1) # 12th column, 2nd row
        lcd.putstr(str(hightemp))
    
    # Check every 5 seconds
    time.sleep(5)
