import RPi.GPIO as GPIO
from time import sleep

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)  # Replace 26 with the GPIO pin you are using
p = GPIO.PWM(26, 50)      # PWM at 50Hz (20ms period)
p.start(0)

# Function to calculate duty cycle from angle
def angle_to_duty_cycle(angle):
    return (angle / 18) + 2.5  # Adjust this formula as per your servo's specifications

try:
    while True:
        # Sweep from 0 to 180 degrees
        for angle in range(0, 181, 1):  # Increment by 1 degree
            duty_cycle = angle_to_duty_cycle(angle)
            p.ChangeDutyCycle(duty_cycle)
            sleep(0.01)  # Small delay to smooth out the motion

        # Sweep from 180 back to 0 degrees
        for angle in range(180, -1, -1):  # Decrement by 1 degree
            duty_cycle = angle_to_duty_cycle(angle)
            p.ChangeDutyCycle(duty_cycle)
            sleep(0.01)  # Small delay to smooth out the motion

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    print("Program stopped")

finally:
    p.stop()  # Stop PWM
    GPIO.cleanup()  # Clean up GPIO

