#!/usr/bin/python3.7

from util import get_input_lines
import re

def get_closest_point(i, j, points):
    def get_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    distances = []
    for point in points:
        distances.append(get_distance(point, (i, j)))

    shortest = min(distances)
    if distances.count(shortest) > 1:
        return 0
    else:
        return distances.index(shortest) + 1

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

closest = [0 for i in range(size_y * size_x)]

for j in range(size_y):
    for i in range(size_x):
        closest[i + j * size_x] = get_closest_point(i, j, adjusted_points)

#with open('output6_1.txt', 'w') as o:
#    for j in range(size_y):
#        for i in range(size_x):
#            o.write('{0:4d}'.format(closest[i + j * size_x]))
#        o.write('\n')

excluded = set()
for j in range(size_y - 1):
    excluded.add(closest[j * size_x])
    excluded.add(closest[(j + 1) * size_x - 1])
for i in range(size_x):
    excluded.add(closest[i])
    excluded.add(closest[(size_y - 1) * size_x + i])
print(excluded)

areas = []
for p in range(len(adjusted_points)):
    if p+1 not in excluded:
        areas.append(closest.count(p+1))

print(max(areas))
