#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random


x = random.randint(0,7)
y = random.randint(0,7)

while True:
    a = random.randint(0,255)
    b = random.randint(0,255)
    c = random.randint(0,255)
    color = (a, b, c)

    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, color)


    time.sleep(0.05)
sense.clear()

