#!/usr/bin/python3.7
with open('input1-1.txt') as f:
    lines = f.readlines()

c = 0

for l in lines:
    if l != '\n':
        c = c + int(l.strip())

print(c)
