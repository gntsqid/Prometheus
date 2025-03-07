import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
import board
from adafruit_neokey.neokey1x4 import NeoKey1x4
from adafruit_seesaw import seesaw, rotaryio, digitalio

# import busio



i2c_bus = board.I2C()
neokey = NeoKey1x4(i2c_bus, addr=0x30)
rotary = seesaw.Seesaw(i2c_bus, 0x36)
rotary.pin_mode(24, rotary.INPUT_PULLUP) # allows rotary press
button = digitalio.DigitalIO(rotary, 24)
button_held = False
encoder = rotaryio.IncrementalEncoder(rotary)
last_position = None

kbd = Keyboard(usb_hid.devices)

# Start of running code
while True:
    # Button is pressed, send the keycode
    if neokey[0]:  
            #kbd.press(Keycode.LEFT_ARROW)  
            kbd.press(Keycode.A) 
            neokey.pixels[0] = 0xFF0000
            time.sleep(0.1)  # Debounce
            kbd.release_all()  # Release all keys after debounce
    else:
        neokey.pixels[0] = 0x0
    if neokey[1]:  
            #kbd.press(Keycode.UP_ARROW)  
            kbd.press(Keycode.W)  
            neokey.pixels[1] = 0xFF0000
            time.sleep(0.1)  # Debounce
            kbd.release_all()  # Release all keys after debounce
    else:
        neokey.pixels[1] = 0x0
    if neokey[2]:  
            #kbd.press(Keycode.RIGHT_ARROW)  
            kbd.press(Keycode.D)  
            neokey.pixels[2] = 0xFF0000
            time.sleep(0.1)  # Debounce
            kbd.release_all()  # Release all keys after debounce
    else:
        neokey.pixels[2] = 0x0
    if neokey[3]:  
            #kbd.press(Keycode.DOWN_ARROW)  
            kbd.press(Keycode.S)  
            neokey.pixels[3] = 0xFF0000
            time.sleep(0.1)  # Debounce
            kbd.release_all()  # Release all keys after debounced
    else:
        neokey.pixels[3] = 0x0 

    # Rotary
    #position = -encoder.position # negate the position to make clockwise rotation positive
    position = encoder.position
    if position != last_position:
        last_position = position
        print("Position: {}".format(position))

    if not button.value and not button_held:
        button_held = True
        print("Button pressed")
        kbd.press(Keycode.CONTROL)

    if button.value and button_held:
        button_held = False
        print("Button released")
        kbd.release_all()

    while position % 2 == 0:
         #for i in range (0,4):
         #     neokey.pixels[i] = 0xFF
         #     time.sleep(0.1)
         neokey.pixels[0] = 0xF87B90
         neokey.pixels[1] = 0xF87B90
         neokey.pixels[2] = 0xF87B90
         neokey.pixels[3] = 0xF87B90
         position = encoder.position
        
         

# This is only for the stratagems and will not allow you to walk with wasd.
# TODO: Add possible dictionary of stratagems where if pattern is met then flash color.
        # Example: Flash white rapidly a few times on successfull reinforcement.
        # aka: up down right left up 
        # How would this get stored? What if the ctrl button stops being held down? Tough, may not be feasible. 

        # Add a 3D printed case of course.
        # Wire it up permanently.aawdss
