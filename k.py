import sys

a, b, c = map(int, input().split())

ans = sys.maxsize

ops = ['+', '-', '*', '/']

for x in ops:
    if x == '/' and a % b != 0:
        continue
    r1 = eval(f"{a}{x}{b}")
    for y in ops:
        if y == '/' and r1 % c != 0:
            continue

        result = eval(f'{r1}{y}{c}')

        if result >= 0:
            ans = min(ans, result)

print(ans)