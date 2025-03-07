# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Capacitive Touch Example for Rotary Trinkey"""
import time
import board
import touchio
import digitalio
from rainbowio import colorwheel
import neopixel
import rotaryio

touch = touchio.TouchIn(board.TOUCH)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB)
switch = digitalio.DigitalInOut(board.SWITCH)

last_position = -1
color = 0

while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
        if not switch.value:
            if position > last_position:
                color += 15
            else:
                color -= 15
            color = (color + 256) % 256
            pixel.fill(colorwheel(color))
        else:
            if position > last_position:
                pixel.brightness = min(1.0, pixel.brightness + 0.1)
            else:
                pixel.brightness = max(0, pixel.brightness - 0.1)
    last_position = position

    if touch.value:
        print("Pad touched!")

