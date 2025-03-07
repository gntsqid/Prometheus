import board
import time
import random
import digitalio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import busio
import rotaryio

# Initialize display
displayio.release_displays()
i2c = busio.I2C(board.GP17, board.GP16)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
WIDTH, HEIGHT = 128, 64
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Initialize rotary encoder
encoder = rotaryio.IncrementalEncoder(board.GP2, board.GP3)
last_position = encoder.position

# Initialize button
switch = digitalio.DigitalInOut(board.GP18)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# Prepare display for text
splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="PASSWORD GEN", color=0xFFFFFF)
text_area.x = (WIDTH - len(text_area.text) * 6) // 2
text_area.y = (HEIGHT - 8) // 2
splash.append(text_area)
display.show(splash)

# Initialize password options
options = ["Simple", "Medium", "Strong"]
option_index = 0
password_generated = False

while True:
    # Read encoder
    current_position = encoder.position
    if current_position != last_position:
        shift = current_position - last_position
        option_index = (option_index + shift) % len(options)
        last_position = current_position
    
    # Generate password
    if not switch.value and not password_generated:
        if options[option_index] == "Simple":
            charset = "ABC123"
        elif options[option_index] == "Medium":
            charset = "ABCD1234abcd"
        else:
            charset = "ABCDE12345!@#"
        
        password = "".join(random.choice(charset) for _ in range(8))
        text_area.text = f"Password: {password}"
        password_generated = True  # Lock in the password until restart
    
    # Update text area
    if not password_generated:
        text_area.text = f"Select: {options[option_index]}"
    
    text_area.x = (WIDTH - len(text_area.text) * 6) // 2
    time.sleep(0.1)
