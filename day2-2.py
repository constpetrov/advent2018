#!/usr/bin/python3.7
lines = []
with open('input2.txt') as f:
    for l in f.readlines():
         if l != '\n':
             lines.append(l.strip())

length = len(lines[0])
            
def lines_close(l1, l2, l_len):
    i, c = 0, 0
    while c <= 1 and i in range(l_len):
        if l1[i] != l2[i]:
            c = c + 1
            
        i = i + 1
        
    return c == 1
    
def clean_line(l1, l2, l_len):
    result = ""
    for i in range(l_len):
        if l1[i] == l2[i]:
            result = result + l1[i]
    return result
        
found = False
for line1 in lines:
    for line2 in lines:
        if lines_close(line1, line2, length):
            found = True
            found1 = line1
            found2 = line2
            break
    if found:
        break
        
print(found1)
print(found2)

print(clean_line(found1, found2, length))
        