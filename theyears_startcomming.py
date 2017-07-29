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
D = 293.66
C = 261.63
B = 246.94
A = 220
G = 196
e = 164.8
d = 146.83

# Eight dotted
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.2)
Buzz.stop()
time.sleep(0.2)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,e)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.055)

# Eighth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.05)

# Eighth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.05)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.055)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.055)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.055)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.055)

# Eighth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.05)

# Eighth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.05)

# Eight dotted
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.2)
Buzz.stop()
time.sleep(0.2)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.055)

# Eighth
Buzz = GPIO.PWM(buzz_pin,e)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.05)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.055)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.055)

# Eighth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.05)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.055)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.055)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.05)
Buzz.stop()
time.sleep(0.055)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.055)

# Eighth
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.05)

# Sixteenth
Buzz = GPIO.PWM(buzz_pin,B)
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.055)

# Eight dotted
Buzz = GPIO.PWM(buzz_pin,G)
Buzz.start(50)
time.sleep(0.2)
Buzz.stop()
time.sleep(0.2)
