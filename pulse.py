import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

pins = [5, 6, 13, 19]

# setup all pins to output
for p in pins:
    GPIO.setup(p, GPIO.OUT)

wait = 0.002


def pulse(pin):
    GPIO.output(pin, True)
    time.sleep(wait)
    GPIO.output(pin, True)
    time.sleep(wait)


def pulse_x():
    pulse(pins[0])


def pulse_y():
    pulse(pins[1])


def pulse_z():
    pulse(pins[2])


GPIO.cleanup()
