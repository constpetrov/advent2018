#!/usr/bin/python3.7

from util import get_input_lines
import re
from functools import cmp_to_key
import string

class Comp:
    def __init__(self, rules):
        self._rules = rules
    def steps_compare(self, s1, s2):
        if s1 in self._rules and s2 in self._rules[s1]:
            return -1
        elif s2 in self._rules and s1 in self._rules[s2]:
            return 1
        elif s1 < s2:
            return -1
        else:
            return 1

lines = get_input_lines('input7.txt')
c = re.compile(r'Step (\w) must be finished before step (\w) can begin.')

rules = {}
for line in lines:
    m = c.search(line)
    step = m.group(2)
    rule = m.group(1)
    if step not in rules:
        rules[step] = set(rule)
    else:
        rules[step].add(rule)

print(rules)

steps = list(string.ascii_uppercase)
print(steps, len(steps))

comparator = Comp(rules)
result = ''
for c in sorted(steps, key = cmp_to_key(comparator.steps_compare)):
    result = result + c

print(result)
