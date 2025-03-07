# FULLY WORKING
import board
import time

# display stuff
import digitalio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306 
import busio

import rotaryio # rotary encoder controls

# Initialize display
displayio.release_displays()
i2c = busio.I2C(board.GP17, board.GP16)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
WIDTH, HEIGHT = 128, 64
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Initialize encoder and button
encoder = rotaryio.IncrementalEncoder(board.GP3, board.GP2)
last_position = encoder.position
switch = digitalio.DigitalInOut(board.GP18)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP
button_last_state = switch.value

# Prepare display for text
splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="WELCOME", color=0xFFFFFF)  
text_area.x = (WIDTH - len(text_area.text) * 6) // 2  
text_area.y = (HEIGHT - 8) // 2
splash.append(text_area)
display.show(splash)

# Helper function to update a character in a string
def update_char(string, pos, shift):
    char = string[pos]
    new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    return string[:pos] + new_char + string[pos+1:]

# Initial state
solution = "ENIGMA" # Like the Riddler, get it?
message = "RAVTZN" # Simple ROT13
cursor_pos = 0  # Cursor starts at the first character

scroll_pos = 0
scroll_direction = 2

time.sleep(1.5)
text_area.text = "RIDDLE TIME!"
time.sleep(1.5)

while True:
    # Rotate through alphabet with encoder turn
    current_position = encoder.position
    if current_position != last_position:
        shift = current_position - last_position
        message = update_char(message, cursor_pos, shift)
        last_position = current_position

    # Switches selected character with encoder click
    button_state = switch.value
    if button_state != button_last_state:
        if not button_state:  # Button pressed
            cursor_pos = (cursor_pos + 1) % len(message)
        button_last_state = button_state

    # Update the display
    if message == solution:
        text_area.text = "YOU WIN!"
        scroll_pos += scroll_direction
        if scroll_pos >= WIDTH - len(text_area.text) * 6 or scroll_pos <= 0:
            scroll_direction *= -1
        text_area.x = scroll_pos

    else:
        display_text = message[:cursor_pos] + '>' + message[cursor_pos] + '<' + message[cursor_pos + 1:]
        text_area.text = display_text
        text_area.x = (WIDTH - len(text_area.text) * 6) // 2

    time.sleep(0.1)
