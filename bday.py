a,b = [int(x) for x in input().split()]

start = int("1" + '0' * (a-1))
end = int("9"*a)

while start % 225 != b:
    start += 1

while end % 225 != b:
    end -= 1 

print((end-start)/225)