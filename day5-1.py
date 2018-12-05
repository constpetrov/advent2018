#!/usr/bin/python3.7

line = list('dabAcCaCBAcCcaDA')
with open('input5.txt') as f:
    line = list(f.readline().strip())

removed = [0 for i in range(len(line))]

def get_start(removed, start):
    res = start
    while removed[res] == 1:
        res -= 1
    return res

def get_end(removed, end):
    res = end
    while res < len(removed) and removed[res] == 1:
        res += 1
    return res

def reductable(line, first, second):
    if first < 0:
        return False
    elif second > len(line) - 1: 
        return False
    elif line[first].lower() == line[second].lower() and line[first] != line[second]:
        return True
    return False

i = 0
while i < len(line) - 1:
    start = get_start(removed, i)
    end = get_end(removed, i + 1)
    while reductable(line, start, end):
        print('Line is reductable by letters on positions {} and {}'.format(start, end))
        removed[start] = 1
        removed[end] = 1
        start = get_start(removed, i)
        end = get_end(removed, i + 1)
    i = get_end(removed, i + 1)

print(removed.count(0))
