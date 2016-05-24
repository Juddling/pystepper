import sys
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# assuimng Rpi on the left
# label boards A, B, C
# GPIO 3 drives motor C
# GPIO 27 drives motor B
# GPIO 2 drives motor A

# direction GPIO: 16, 20, 21
pins = [2]

# setup all pins to output
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

wait = 0.002

i = 0
direction_a = True
direction_b = False


while True:
    #print "pulse high"
    
    GPIO.output(pins[0], True)
    time.sleep(wait)
    GPIO.output(pins[0], False)
    time.sleep(wait)


GPIO.cleanup()
