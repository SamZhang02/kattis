import sys

def dp(s, sum, d, curr):
    for k in d:
        if k in s:
            continue
        sum += d[k][0]
        s.add(k)
        dp()
    pass
    

for line in sys.stdin:
    d = {}
    capacity, num = [int(x) for x in line.split()]
    for i in range(num):
        a,b = [int(x) for x in input().split()]
        d[i] = (a,b)
    ans = set()
    dp(ans,d[k][0],d,k)
    print(" ".join(ans))
    pass