#!/usr/bin/env python

x = int(raw_input("Enter a positive integer B"))
while (x <= 0):
    x = int(raw_input("Enter a positive integer B"))
i = 1
while (i <= x):
    print i
    i = i+1

y = int(raw_input("Enter an integer smaller than x"))
while (y >= x):
    y = int(raw_input("Enter an integer smaller than x"))
i = -y
while (i <= x-y):
    print i
    i = i+1
