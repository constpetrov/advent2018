#!/usr/bin/python3.7
from util import get_input_lines
import re

class Sleep:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def length(self):
        return self.stop - self.start

c_shift = re.compile(r'\[\d{4}-\d{2}-\d{2}\s\d{2}:(\d{2})\]\sGuard\s#(\d{1,4}).*')

lines = sorted(get_input_lines('input4.txt'))
for line in lines:
    if c_shift.match(line):
        r = c_shift.search(line)
        print(r.group(2))
