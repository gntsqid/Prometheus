# NOTE TO SELF ---- I don't remember what this does entirely....please read carefully..
import board
import time
import digitalio
import rotaryio
import pwmio
from adafruit_motor import servo
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import busio

words = ["hello", "good-bye", "working"]
#setting up I2C display
displayio.release_displays()
i2c = busio.I2C(board.GP11,board.GP10) #(SCL,SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
WIDTH = 128
HEIGHT = 64
BORDER = 5
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
splash = displayio.Group()
display.show(splash)
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
splash.append(inner_sprite)
text = words[0]
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1)
splash.append(text_area)

#setting up servo
pwm_servo = pwmio.PWMOut(board.GP19, duty_cycle=2 ** 15, frequency=50) #not sure what these mean just yet
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2200)
#created a servo which goes from 50 to 220 pwm. The usual is 100 to 200 (1000 min 2000 max)

#setting up encoder
encoder = rotaryio.IncrementalEncoder(board.GP16, board.GP17) #rota A and rot B are pin placeholders
switch = digitalio.DigitalInOut(board.GP18)                 #switch is a pin placeholder
last_position = -1
button_state  = 0


text_count = 0
time_count = .01
while True:

    text_area.x -= 1

    time.sleep(time_count)

    if(text_area.x < -len(words[text_count])):
        text_count += 1
        time_count /= 2
        if(text_count >= len(words)):
            text_count = 0

        text_area.x = WIDTH

    text_area.text = words[text_count]





    current_position = encoder.position
    position_change = current_position - last_position
    current_angle = servo1.angle

    if last_position is None or current_position != last_position:
        #print(current_position)
        time.sleep(0.1)
        if position_change > 0:
            current_angle += 25
            if(current_angle > 180):
                current_angle = current_angle %180
            servo1.angle = current_angle
            print(servo1.angle)
            time.sleep(0.1)
        elif position_change < 0:
            current_angle -= 25
            if(current_angle < 0):
                current_angle = 180
            servo1.angle = current_angle
            print(servo1.angle)
            time.sleep(0.1)
    if switch.value:
        servo1.angle = 0
        print("Button Pressed!")

    last_position = current_position #updates position to compare
