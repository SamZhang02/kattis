from fractions import Fraction
taxi,spider = [int(x) for x in input().split()]

total_taxi = 2*taxi**2 + 2*taxi + 1
moves = [(1,1,0),(1,0,1),(1.5,1,1),(1.5,-1,-1),(1,-1,0),(1,0,-1),(1.5,1,-1),(1.5,-1,1)]
coord = (0,0)
visited = {coord}

def dfs(moves,curr, visited, distance_left):
    if distance_left < 1:
        return

    for y in moves:
        cost = y[0]
        add = (y[1], y[2])
        nxt = (curr[0] + add[0], curr[1] + add[1]) 
        if distance_left >= cost:
            visited.add(nxt)
            dfs(moves, nxt, visited, distance_left - cost)

dfs(moves, coord, visited, spider)
total_spider = len(visited)

if total_taxi > total_spider:
    print(1)
    exit()

out = Fraction(total_taxi, total_spider)
print(str(out.numerator) + "/" + str(out.denominator))