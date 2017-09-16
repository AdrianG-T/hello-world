#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

speed = 0.05
message = "Hello World!"

sense.show_message(message, speed)
