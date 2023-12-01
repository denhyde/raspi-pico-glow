from machine import Pin

onboardLED = Pin(25, Pin.OUT)
onboardLED.value(1)

print("Light on")

