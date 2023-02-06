n, s, k = [int(x) for x in input().split()]

points = []
for i in range(n):
    points.append(int(input()))
points.sort()

if n == 1:
    print(k)
    exit()

total_length = 0
for i in range(n):
    if i == 0:
        if (points[i+1] - points[i]) * 2 < s:
            print(-1)
            exit()
        end = points[i+1] - points[i] - s / 2
        end = min(end, k / 2)
        total_length += end * 2
        points[i] = points[i] + end
    elif i == n - 1:
        if (points[i] - points[i-1]) * 2 < s:
            print(-1)
            exit()
        end = points[i] - points[i-1]
        end = min(end, k / 2)
        total_length += end * 2
    else:
        min_dist = min(points[i+1] - points[i] - s / 2, points[i] - points[i-1])
        end = min(min_dist, k / 2)
        max_length = end * 2
        if max_length < s:
            print(-1)
            exit()
        total_length += max_length
        points[i] = points[i] + end
print(int(total_length))
        
