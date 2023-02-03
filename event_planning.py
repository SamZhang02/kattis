import sys
participants, budget, hotels, weeks = [int(x) for x in input().split()]
minimum = float('inf') 

for i in range(hotels):
    price = int(input())
    bed = [int(x) for x in input().split()]
    for num in bed:
        if num < participants:
            continue
        total = participants * price
        if total < minimum: 
            minimum = total 

if minimum > budget:
    print("stay home")
else:
    print(minimum)

