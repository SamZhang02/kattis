#Only passed test group 1 and 2

import sys

for line in sys.stdin:
    l,k,s = [int(x) for x in line.split()]
    lapses = {}
    times = {}
    for i in range(1, s+1):
        lapses[i] = k
        times[i] = 0
    completed = set()
    for i in range(l):
        participant, time = input().split()
        participant = int(participant) 

        lapses[participant] -= 1

        minute, sec = [int(x) for x in time.split('.')]
        times[participant] += minute*60 + sec
        if lapses[participant] == 0: completed.add((participant, times[participant]))
    ans = list(completed)
    ans.sort(key= lambda x: (x[1], x[0]))
    for a in ans:
        print(a[0])
         
