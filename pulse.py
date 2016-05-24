import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

pins = [2, 27, 3]
pins_dir = [16, 20, 21]

# setup all pins to output
for p in pins:
    GPIO.setup(p, GPIO.OUT)

for p in pins_dir:
    GPIO.setup(p, GPIO.OUT)

wait = 0.002


def pulse(pin):
    GPIO.output(pin, True)
    time.sleep(wait)
    GPIO.output(pin, False)
    time.sleep(wait)


def pulse_x():
    pulse(pins[0])


def pulse_y():
    pulse(pins[1])


def pulse_z():
    pulse(pins[2])

def direction(pin, flag):
    GPIO.output(pin, flag)

def dir_x(flag):
    direction(pins_dir[0], flag)

def dir_y(flag):
    direction(pins_dir[1], flag)

def dir_z(flag):
    direction(pins_dir[2], flag)

def cleanup():
    GPIO.cleanup()
