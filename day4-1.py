#!/usr/bin/python3.7
from util import get_input_lines
from array import array
from operator import itemgetter
import re

def get_sleep(i, s, e):
    if i in range(s,e):
        return 1
    else:
        return 0

c_shift = re.compile(r'\[\d{4}-\d{2}-\d{2}\s\d{2}:(\d{2})\]\sGuard\s#(\d{1,4}).*')
c_sleep = re.compile(r'\[\d{4}-\d{2}-\d{2}\s\d{2}:(\d{2})\]\sfall.*')
c_wake = re.compile(r'\[\d{4}-\d{2}-\d{2}\s\d{2}:(\d{2})\]\swake.*')

lines = sorted(get_input_lines('input4.txt'))
guard = 0
start = 0
end = 0
sleep = {}
for line in lines:
    if c_shift.match(line):
        r = c_shift.search(line)
        guard = int(r.group(2))
    elif c_sleep.match(line):
        r = c_sleep.search(line)
        start = int(r.group(1))
    elif c_wake.match(line):
        r = c_wake.search(line)
        end = int(r.group(1))
        if guard not in sleep:
            sleep[guard] = array('B', [get_sleep(i, start, end) for i in range(60)])
        else:
            for i in range(start, end):
                sleep[guard][i] = sleep[guard][i] +1

sleep_sum = {}
for k, v in sleep.items():
    sleep_sum[k] = sum(v)

max_sleep = max(sleep_sum.items(), key = itemgetter(1))[0]
max_minute = sleep[max_sleep].index(max(sleep[max_sleep]))
print(max_sleep * max_minute)
