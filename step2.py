import sys
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

pins = [5,6,13,19]

# setup all pins to output
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

wait = 0.002

i = 0
direction_a = True
direction_b = False


while True:
    #print "pulse high"
    
    GPIO.output(5, True)
    time.sleep(wait)
    GPIO.output(13, True)
    time.sleep(wait)
    GPIO.output(5, False)
    time.sleep(wait)
    GPIO.output(13, False)
    time.sleep(wait)

    if i >= 1000:
        direction_a = not direction_a
        direction_b = not direction_b
        
        GPIO.output(6, direction_a)
        GPIO.output(19, direction_b)
        i = 0
        #print "changing direction"

    i += 1

GPIO.cleanup()
