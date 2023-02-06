n, s, k = [int(x) for x in input().split()]

points = []
for i in range(n):
    points.append(int(input()))
points.sort()
print(points)
total = 0
left, right = 0,0 
while right != len(points)-1:
    dist = points[left] - points[right]
    if dist < s:
        print(-1)
        exit()
    if dist >= s and dist <= k:
        right += 1
    else:


