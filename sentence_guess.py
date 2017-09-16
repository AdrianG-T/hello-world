#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

s = "Lemme get it boneless"
speed = 0.01

while True:
    sense.show_message(s, speed)
    print('Enter the sentence')
    guess = raw_input()
    if guess == s:
        print "You win!"
        sense.show_message("YOU WIN!!!")
        break
    else:
        print "Try again"
        speed = speed +0.01
