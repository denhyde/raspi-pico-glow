# Rainbow NeoPixel strip with a push-button on/off toggle
# Save this ON THE BOARD as main.py so it starts by itself when powered up.

from machine import Pin
from neopixel import NeoPixel
import time

# LED details
GPIOnumber = 2
LEDcount = 15

# Button: one leg to GP14 (physical pin 19), the other to GND (physical pin 18)
BUTTON_GPIO = 14
DEBOUNCE_MS = 200

strand = NeoPixel(Pin(GPIOnumber), LEDcount)
button = Pin(BUTTON_GPIO, Pin.IN, Pin.PULL_UP)  # reads 1 normally, 0 when pressed

# Brightness factor (0.0 to 1.0, where 1.0 is full brightness)
brightness = 0.1


def scale_brightness(color, factor):
    """Scale RGB color values by a brightness factor."""
    return tuple(int(c * factor) for c in color)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)


# Button handling: returns True once per click, ignoring contact bounce
last_state = 1
last_press = 0


def button_clicked():
    global last_state, last_press
    state = button.value()
    clicked = False
    if state == 0 and last_state == 1:
        now = time.ticks_ms()
        if time.ticks_diff(now, last_press) > DEBOUNCE_MS:
            clicked = True
            last_press = now
    last_state = state
    return clicked


def all_off():
    strand.fill((0, 0, 0))
    strand.write()


# Start with everything off, then begin in the "on" state
all_off()
time.sleep(1)

running = True
j = 0  # position in the rainbow cycle; kept while off so it resumes smoothly

while True:
    if button_clicked():
        running = not running
        if not running:
            all_off()

    if running:
        for i in range(LEDcount):
            pixel_index = (i * 256 // LEDcount + j) % 256
            strand[i] = scale_brightness(wheel(pixel_index), brightness)
        strand.write()
        j = (j + 1) % 256

    time.sleep(0.005)  # Reduce this value for faster changes
