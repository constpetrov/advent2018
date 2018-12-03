#!/usr/bin/python3.7
from util import get_input_lines
from array import array
import re

lines = get_input_lines('input3.txt')

fabric = array('B', [0 for i in range(10**6)])
c = re.compile(r'#(\d{1,4})\s@\s(\d{1,3}),(\d{1,3}):\s(\d{1,3})x(\d{1,3})')

for line in lines:
    m = c.search(line)
    x, y, width, height = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
    out = 'X = {}, Y = {}, Width = {}, Height = {}'.format(x, y, width, height)
    for i in range(x, x + width):
        for j in range(y, y + height):
            fabric[i + 1000 * j] = 1

print(fabric.count(1))
