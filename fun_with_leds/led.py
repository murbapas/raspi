#! /usr/bin/env python3

import RPi.GPIO as GPIO
import time

# use the BCM-numbering (e.g. #18 and not 'pin 12')
GPIO.setmode(GPIO.BCM)

# don't print warnings
GPIO.setwarnings(False)

# set GPIO #18 as an output port
GPIO.setup(18,GPIO.OUT)

print("blue LED on")

# set output level to high
GPIO.output(18,GPIO.HIGH)

time.sleep(1)
print("LED off")

# set output level to low
GPIO.output(18,GPIO.LOW)


