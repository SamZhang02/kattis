curr = 1
width = 1
blocks = int(input()) 
height = 1

while curr <= blocks:
    width += 2
    nxt = width**2

    if curr + nxt <= blocks: 
        curr += nxt
        height += 1
    else:
        break
print(height)