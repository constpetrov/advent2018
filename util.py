#!/usr/bin/python3.7

def get_input_lines(name):
    lines = []
    with open(name) as f:
        for l in f.readlines():
            if l != '\n':
                lines.append(l.strip())
    return lines
