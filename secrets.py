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

Buzz = D
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)

Buzz = Fs
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)

Buzz = A
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)

Buzz = Fs
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)

Buzz = A
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)

Buzz = Fs
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)

Buzz = D
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)

Buzz = Fs
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)

Buzz = A
Buzz.start(50)
time.sleep(0.5)
Buzz.stop()
time.sleep(0.5)