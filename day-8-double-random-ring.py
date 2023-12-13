from machine import Pin
from neopixel import NeoPixel

ring = NeoPixel(Pin(2), 12)

ring.fill((0,0,0)) # 'fill' addresses all LEDs
ring.write()
