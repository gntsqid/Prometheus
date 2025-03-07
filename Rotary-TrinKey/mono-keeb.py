import time
import board
import touchio
import digitalio
import neopixel
import rotaryio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

cc = ConsumerControl(usb_hid.devices)


touch = touchio.TouchIn(board.TOUCH)
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB)
switch = digitalio.DigitalInOut(board.SWITCH)
switch.switch_to_input(pull=digitalio.Pull.DOWN)

last_position = -1
boolnum = 0

kbd = Keyboard(usb_hid.devices)

letters = [Keycode.A, Keycode.B, Keycode.C, Keycode.D, Keycode.E, Keycode.F, Keycode.G,
Keycode.H, Keycode.I, Keycode.J, Keycode.K, Keycode.L, Keycode.M, Keycode.N, Keycode.O,
Keycode.P, Keycode.Q, Keycode.R, Keycode.S, Keycode.T, Keycode.U, Keycode.V, Keycode.W,
Keycode.X, Keycode.Y, Keycode. Z ]

i = 0



while True:
    key =  letters[i]
    position = encoder.position
    if last_position is None or position != last_position:
        #print(position)
        if last_position > position:
            i += 1
            print(i)
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        if last_position < position:
            i -= 1
            print(i)
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)

    last_position = position

    if(i < 0):
        i = len(letters) - 1
    if(i >= len(letters)):
        i = 0

    if switch.value:
        kbd.send(Keycode.SPACEBAR)
    #    cc.send(ConsumerControlCode.MUTE)

    if switch.value and boolnum == 0 :
        print("Button pushed!")
        pixel.fill((255,0,0))
        time.sleep(1)
        boolnum += 1
    if switch.value and boolnum ==1:
        print("Button pushed!")
        pixel.fill((0,255,0))
        time.sleep(1)
        boolnum += 1
    if switch.value and boolnum == 2:
        print("Button pushed!")
        pixel.fill((0,255,255))
        time.sleep(1)
        boolnum = 0
    if switch.value and touch.value: #note: it works but very difficult to physically do
        print("Fancy!")
        pixel.fill((0,0,0))
        time.sleep(1)


    if touch.value:
        print("Pad touched!")

        kbd.send(key)

        pixel.fill((0,0,0))
        time.sleep(1)
