#!/usr/bin/env python
import random
import RPi.GPIO as GPIO
import time

#generate a random number from 1 to 10
n = random.randint (1,10)

# keep running until number is  guessed
while True:
    print('Guess of a number from 1 to 10')
    guess = raw_input()
    guess = int(guess)
    if guess > n:
        print "Your guess is too high"
    elif guess < n:
        print "Your guess is to low"
    else:

        # breadboard setup
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
    
        # assign pin number for Auto Flash LED pin's mode as output
        led_pin = 11
    
        # set Auto Flash LED pin's mode as output
        GPIO.setup(led_pin,GPIO.OUT)
    
        # turn on Auto Flash LED
        GPIO.output(led_pin,True)
        time.sleep(2)
    
        # turn off Auto Flash LED
        GPIO.output(led_pin,False)

        # reset GPIO resources used by script
        GPIO.cleanup()

        print "Correct!"
        break
