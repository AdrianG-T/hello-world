#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

# use RGB values to define colors
yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)

speed = 0.05

message = "Hello World!"

sense.show_message(message, speed, text_colour=blue, back_colour=green)

sense.clear()
