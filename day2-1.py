#!/usr/bin/python3.7

from util import get_input_lines
lines = get_input_lines('input2.txt')
length = len(lines[0])
two_times = 0
three_times = 0

for line in lines:
    s = {}
    for i in range(length):
        if line[i] in s:
            s[line[i]] = s[line[i]] + 1
        else:
            s[line[i]] = 1
            
    found_two = False
    found_three = False
    
    for v in s.values():
        if not found_two and v == 2:
            two_times = two_times + 1
            found_two = True
        elif not found_three and v == 3:
            three_times = three_times + 1
            found_three = True
        elif found_two and found_three:
            break
    
print(three_times * two_times)
