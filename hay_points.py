import sys

x,y = input().split()
x,y = int(x), int(y)

d = {}
for line in sys.stdin:
    a,b = line.split()
    d[a] = int(b)
    x -= 1
    if x == 0:
        break
out = 0

for line in sys.stdin:
    if line == ".\n":
        y -= 1
        print(out) 
        out = 0
    else:
        for word in line.strip().split():
            if word in d:
                out += d[word]
    if y == 0:
        break
