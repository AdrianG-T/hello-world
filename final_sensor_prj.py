#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led_pin = 11
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,3000)

def buzz(freq, seconds):
    Buzz.start(50)
    Buzz.ChangeFrequency(freq)
    time.sleep(1)
    Buzz.stop()

n = random.randint (1,10)

while True:
    print('Guess of a number from 1 to 10')
    guess = raw_input()
    guess = int(guess)
    if guess > n:
        print "Your guess is too high"

frequences = [4000]
times = [1]
for i in range(len(frequences)):
    buzz(frequences[i], times[i])

   elif guess < n:
        print "Your guess is to low"

frequences = [200]
times = [1]
for i in range(len(frequences)):
    buzz(frequences[i], times[i])

    else:

GPIO.output(led_pin,True)
        time.sleep(2)
    
        # turn off Auto Flash LED
        GPIO.output(led_pin,False)

        # reset GPIO resources used by script
        GPIO.cleanup()

        print "Correct!"
        break
