import sys

i = 0
for line in sys.stdin:
    if i == 1:
        arr = [int(x) for x in line.split()]
        break
    i += 1

out = 0 
for j in arr:
    if j < 0:
        out += 1

print(out)