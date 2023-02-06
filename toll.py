import sys
from collections import defaultdict
n, m, q = [int(x) for x in input().split()]
adj = defaultdict(list)
for i in range(m):
    a, b, c = [int(x) for x in input().split()]
    adj[a].append((b, c))
    adj[b].append((a, c))

for i in range(q):
    start, end = [int(x) for x in input().split()]