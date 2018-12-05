#!/usr/bin/python3.7
import string

line = list('dabAcCaCBAcCcaDA')
with open('input5.txt') as f:
    line = list(f.readline().strip())


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

def remove_letter(line, remove, letter):
    for i in range(len(line) - 1):
        if line[i].lower() == letter:
            remove[i] = 1
    return remove

def run(line, removed):
    i = 0
    while i < len(line) - 1:
        start = get_start(removed, i)
        end = get_end(removed, i + 1)
        while reductable(line, start, end):
            removed[start] = 1
            removed[end] = 1
            start = get_start(removed, i)
            end = get_end(removed, i + 1)
        i = get_end(removed, i + 1)

for l in string.ascii_lowercase:
    removed = [0 for i in range(len(line))]
    remove_letter(line, removed, l)
    run(line, removed)
    print('for letter {} reduced is {}'.format(l, removed.count(0)))
