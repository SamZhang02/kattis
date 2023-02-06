a = int(input())
arr = []
for i in range(a):
    arr.append(int(input()))
arr.sort()    
prefix = [0]
for i in range(1, len(arr)):
    prefix.append(arr[i] + prefix[i-1])
total = prefix[-1]
postfix = []
for i in range(len(arr)):
    postfix.append(total - prefix[i])

total_removed = 0

while True:
    attacking = arr[-1]
    defending = arr[0]
    total_removed = arr[0]
    for i in range(1, len(arr) - 1):
        if postfix[i] < (prefix[i] - total_removed + arr[i]):
            attacking += arr[i]
        else:
            defending += arr[i]
    # print(attacking, defending)
    if attacking > defending:
        total_removed += arr.pop(0)
    else:
        break
print(len(arr))

