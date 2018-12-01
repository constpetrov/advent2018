#!/usr/bin/python3.7
with open('input1-1.txt') as f:
    lines = f.readlines()

c = 0
reached = False
freqs = set()

while not reached:
    for l in lines:
        if l != '\n':
            c = c + int(l.strip())
            if c not in freqs:
                freqs.add(c)
            else:
                reached = True
                break

print(c)
