#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

b = random.randint(0,255)

speed = 0.001

message = " "


while True:

    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)

    color = (a, b, c)

    sense.show_message(message, speed, text_colour= (0, 0, 0), back_colour=color)
    time.sleep(0.005)
    
