#!/usr/bin/python3.7
from util import get_input_lines
from array import array
import re

def count_fabric_overlap(f, f_size):
    counter = 0
    for i in range(f_size):
        if f[i] > 1:
            counter = counter + 1
    return counter

lines = get_input_lines('input3.txt')
# lines = ["#15 @ 0,0: 11x10", "#15 @ 0,1: 11x10"]

fabric = array('B', [0 for i in range(10**6)])
c = re.compile(r'#(\d{1,4})\s@\s(\d{1,3}),(\d{1,3}):\s(\d{1,3})x(\d{1,3})')

for line in lines:
    m = c.search(line)
    x, y, width, height = int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
    out = 'X = {}, Y = {}, Width = {}, Height = {}'.format(x, y, width, height)
    print(line)
    print(out)
    for i in range(x, x + width):
        for j in range(y, y + height):
            fabric[i + 1000 * j] = fabric[i + 1000 * j] + 1

print(count_fabric_overlap(fabric, 10**6))
