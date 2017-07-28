#!/usr/bin/enb python
import RPi.GPIO as GPIO
import time

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

# set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)

#Notes with pitches
D = GPIO.PWM(buzz_pin,293.66)
C = GPIO.PWM(buzz_pin,261.63)
B = GPIO.PWM(buzz_pin,246.94)
A = GPIO.PWM(buzz_pin,220)
G = GPIO.PWM(buzz_pin,196)

# Quarter
Buzz = G
Buzz.start(50)
time.sleep(1)
Buzz.stop()
time.sleep(0.02)

# Eighth
Buzz = D
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)

# Eighth
Buzz = B
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(1)

# Quarter
Buzz = B
Buzz.start(50)
time.sleep(1)
Buzz.stop()
time.sleep(0.02)

# Eighth
Buzz = A
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.05)

# Eighth
Buzz = G
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.05)

# Eighth
Buzz = G
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.05)

# Eighth
Buzz = C
Buzz.start(50)
time.sleep(1)
Buzz.stop()
time.sleep(0.02)

# Eighth
Buzz = B
Buzz.start(50)
time.sleep(1)
Buzz.stop()
time.sleep(0.02)

# reset GPIO resources used by script
GPIO.cleanup()