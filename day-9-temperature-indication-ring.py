from machine import Pin, I2C
import time
from dht20 import DHT20
from neopixel import NeoPixel

# Set up I2C pins
i2c1_sda = Pin(14)
i2c1_scl = Pin(15)

# Set up I2C
i2c1 = I2C(1, sda=i2c1_sda, scl=i2c1_scl)

# Set up DHT20 device with I2C address
dht20 = DHT20(0x38, i2c1)

# Define the ring pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2), 12)

# Create a temperature/LED dictionary for our scale
# Temperature is the key (left), LED index is the value (right)
LEDdict = {
  14: 0,
  15: 1,
  16: 2,
  17: 3,
  18: 4,
  19: 5,
  20: 6, # Top-middle LED (index 6 / LED #7) for 20°C
  21: 7,
  22: 8,
  23: 9,
  24: 10,
  25: 11,
}

while True:
      
    # Grab data from the sensor dictionary
    measurements = dht20.measurements
    
    # Create a rounded variable for the temperature
    temperature = round(measurements['t'])
    
    if temperature not in LEDdict:
        
        pass
        print("*** Out of temperature range ***")
        
    else:
        
        # Use our temperature variable with our dictionary
        # To convert it from the temperature to the LED index
        LEDindex = (LEDdict[temperature])
        
        # Print the temperature and index
        print("Temperature:",temperature)
        print("LED index:  ",LEDindex)
        print("----------------")
            
        # Clear the ring
        ring.fill((0,0,0))
        ring.write()
    
        ring[LEDindex] = (10,0,0) # Light the index LED
        ring.write() # Write the LED data
        
    # Wait 5 second before looping again
    time.sleep(5)
