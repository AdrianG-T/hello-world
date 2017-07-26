#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,3000)
# this script uses the Touch Switch to toggle on/off sensors

import RPi.GPIO as GPIO
import time

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Touch Switch;  pin 31 = GPIO 6
touch_pin = 31

# set Touch Switch pin's mode as input
GPIO.setup(touch_pin,GPIO.IN)

# create infinite loop that reads Touch Switch input
while True:
    if GPIO.input(touch_pin) == 0:
        # create BUZZ function and set initial sound frequency to 1000 Hz
        Buzz = GPIO.PWM(buzz_pin,900)

        # start Passive Buzzer using Buzz function with 50% duty for 1 second
        Buzz.start(50)
        time.sleep(1)

    if GPIO.input(touch_pin) == 1:
        # stop Passive Buzzer using Buzz funtion
        Buzz.stop()

GPIO.cleanup()
