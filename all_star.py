#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

G = 196

# assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

# set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)


#G some
# create BUZZ function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,196)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(1)

# stop Passive Buzzer using Buzz funtion
Buzz.stop()
time.sleep(0.02)


#D bo-
# create BUZZ function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,293.66)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(0.5)

# stop Passive Buzzer using Buzz funtion
Buzz.stop()
time.sleep(0.05)


#B dy
# create BUZZ function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,246.94)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(0.5)

# stop Passive Buzzer using Buzz funtion
Buzz.stop()
time.sleep(0.05)


#B once
# create BUZZ function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,246.94)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(1)

# stop Passive Buzzer using Buzz funtion
Buzz.stop()
time.sleep(0.02)


#A told
# create BUZZ function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,220)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(0.5)

# stop Passive Buzzer using Buzz funtion
Buzz.stop()
time.sleep(0.05)


#G
# create BUZZ function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,196)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(0.5)

# stop Passive Buzzer using Buzz funtion
Buzz.stop()
time.sleep(0.05)


#G
# create BUZZ function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,196)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(0.5)

# stop Passive Buzzer using Buzz funtion
Buzz.stop()
time.sleep(0.05)


#C
# create BUZZ function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,261.63)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(1)

# stop Passive Buzzer using Buzz funtion
Buzz.stop()
time.sleep(0.05)

#D
# create BUZZ function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,146.83)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(1)

# stop Passive Buzzer using Buzz funtion
Buzz.stop()
time.sleep(0.2)


# reset GPIO resources used by script
GPIO.cleanup()
