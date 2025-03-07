# We've already used a servo with a pico, but how about with a pi!
# usage: python3 servo.py [1 >= int <= 180]
# Sets the servo to the desired angle as a proof of concept that we can control servos with a pi.
# The next step is to try out with multiple at once, but this will do for now.

import RPi.GPIO as GPIO
import sys
from time import sleep

# Constants for servo angles and corresponding duty cycles
MIN_ANGLE = 0
MAX_ANGLE = 180
MIN_DUTY_CYCLE = 2.5
MAX_DUTY_CYCLE = 12.5

# Function to calculate duty cycle from angle
def angle_to_duty_cycle(angle):
    return ((angle / 180) * (MAX_DUTY_CYCLE - MIN_DUTY_CYCLE)) + MIN_DUTY_CYCLE

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
p = GPIO.PWM(26, 50)
p.start(0)

try:
    # Read angle from command line argument
    angle = float(sys.argv[1])
    
    # Check if angle is within bounds
    if angle < MIN_ANGLE or angle > MAX_ANGLE:
        print(f"Angle out of range. Please enter a value between {MIN_ANGLE}° and {MAX_ANGLE}°.")
    else:
        # Set servo to the specified angle
        duty_cycle = angle_to_duty_cycle(angle)
        p.ChangeDutyCycle(duty_cycle)
        sleep(1)
        p.ChangeDutyCycle(0)  # Stop the servo from jittering

except IndexError:
    print("Please provide an angle as an argument. Example usage: python3 servo.py 90")
except ValueError:
    print("Invalid input. Please provide a numeric value for the angle.")

finally:
    p.stop()
    GPIO.cleanup()
