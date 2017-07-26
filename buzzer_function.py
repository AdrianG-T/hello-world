#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,3000)

def buzz(freq, seconds):
    Buzz.start(50)
    Buzz.ChangeFrequency(freq)
    time.sleep(1)
    Buzz.stop()

frequences = [196, 293.66, 246.94, 246.94]
times = [1, 2, 3, 1]
for i in range(len(frequences)):
    buzz(frequences[i], times[i])
