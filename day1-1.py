#!/usr/bin/python3.7
from util import get_input_lines
lines = get_input_lines('input1-1.txt')

c = 0

for l in lines:
    c = c + int(l.strip())

print(c)
