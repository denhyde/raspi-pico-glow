# Copy the DHT20 library code from
# https://github.com/flrrth/pico-dht20/blob/main/dht20/dht20.py
# and save it on RaspberryPi Pico (not local computer!)
# as dht20.py file

from machine import Pin, I2C
import time
from dht20 import DHT20

# Set up I2C pins
i2c1_sda = Pin(14)
i2c1_scl = Pin(15)

# Set up I2C
i2c1 = I2C(1, sda=i2c1_sda, scl=i2c1_scl)

# Set up DHT20 device with I2C address
dht20 = DHT20(0x38, i2c1)

while True:
    
    # Grab data from the sensor dictionary
    measurements = dht20.measurements

    # Print the data
    print("-- Environment ---------") # Heading
    print(f"Temperature:      {round(measurements['t'],1)}°C")
    print(f"Humidity:         {round(measurements['rh'],1)}%")
    print("------------------------") # Divider
    print("                        ") # Empty line
    
    # Wait 5 seconds
    time.sleep(60)
