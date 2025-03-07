# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials: PWM with Fixed Frequency example."""
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

# Servo setup
pwm_servo = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(
    pwm_servo, min_pulse=500, max_pulse=2200
)  # tune pulse for specific servo





while True:


    for angle in range(0, 180, 1):
        servo1.angle = angle

    for angle in range(180, 0, -1):
        servo1.angle = angle
