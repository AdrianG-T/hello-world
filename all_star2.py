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
D = Buzz = GPIO.PWM(buzz_pin,293.66)
C = Buzz = GPIO.PWM(buzz_pin,261.63)
B = Buzz = GPIO.PWM(buzz_pin,246.94)
A = Buzz = GPIO.PWM(buzz_pin,220)
G = Buzz = GPIO.PWM(buzz_pin,196)

def buzz(freq, seconds):
	Buzz.start(50)
	Buzz.ChangeFrequency(freq)
	time.sleep(1)
	Buzz.stop()

frequencies = [G, D, B, B, A, G, G, C, B, ]
times = [1, 2, 3, 4, 5, 6, 7, 8, 1]
for i in range(len(frequencies)):
	buzz(frequences[i], times[i])