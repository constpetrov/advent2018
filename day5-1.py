#!/usr/bin/python3.7

line = []
with open('input5.txt') as f:
    line = list(f.readline().strip())

r_counter = 0

def reductable(line, first, second):
    if line[first].lower() == line[second].lower():
        return True
    return False

for i in range(len(line) - 1):
    if reductable(line, i, i + 1):
        r_counter += 2

print(r_counter)
