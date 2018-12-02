#!/usr/bin/python3.7
from util import get_input_lines
lines = get_input_lines('input1-1.txt')

c = 0
reached = False
freqs = set()

while not reached:
    for l in lines:
        c = c + int(l.strip())
        if c not in freqs:
            freqs.add(c)
        else:
            reached = True
            break

print(c)
