import sys

def compare(first,second):
    for i in range(len(first)):
        if first[i] != '9' and second[i] != '9':
            return [first[:i] + '9' + first[i+1:], second]
        if second[i] != '0' and first[i] != '0':
            if i != 0 or len(first) == 1:
                return [first, second[:i] + '0' + second[i+1:]]
        if second[i] != '0' and first[i] != '0' and first[i] != '1':
            return [first, second[:i] + '1' + second[i+1:]]

for line in sys.stdin:
    n = int(line)
    nums = input().split()
    for i in range(len(nums)-1):
        if len(nums[i+1]) == len(nums[i]):
            x = compare(nums[i], nums[i+1])
            if not x:
                continue
            a,b = x
            nums[i] = a
            nums[i+1] = str(b)
            print(" ".join(nums))
            exit()
    print('impossible')