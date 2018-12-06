#!/usr/bin/python3.7

from util import get_input_lines
import re

def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def is_point_safe(i, j, points):
    distance = 0
    for point in points:
        distance += get_distance(point, (i, j))
    return distance < 10000

c = re.compile(r'(\d{1,3}), (\d{1,3})')
lines = get_input_lines('input6.txt')

points = []
for line in lines:
    m = c.search(line)
    points.append((int(m.group(1)), int(m.group(2))))

max_x = max(points, key = lambda p:p[0])[0]
max_y = max(points, key = lambda p:p[1])[1]

min_x = min(points, key = lambda p:p[0])[0]
min_y = min(points, key = lambda p:p[1])[1]

adjusted_points = []
for point in points:
    adjusted_points.append(( point[0] - min_x, point[1] - min_y ))

size_x = max_x - min_x
size_y = max_y - min_y

safe = [0 for i in range(size_y * size_x)]

for j in range(size_y):
    for i in range(size_x):
        if is_point_safe(i, j, adjusted_points):
            safe[i + j * size_x] = 1

print(safe.count(1))
