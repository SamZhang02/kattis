import sys
n, m = (int(x) for x in input().split()) 
visited = set()

maze = []

for i in range(n):
    maze.append(input())

def traverse(row, col, m, n, visited, maze) -> int:
    n_dots = 0
    queue = []
    queue.append((row, col))
    while queue:
        r, c = queue.pop(0)
        if (not (0 <= row < n) or not (0 <= c < m) or (r, c) in visited or maze[r][c] in "ABCDEFGHIJKLMNOPQRSTUVWX"):
            continue
        visited.add((r, c))
        if maze[r][c] == ".":
            n_dots += 1
        queue.append((r + 1, c))
        queue.append((r - 1, c))
        queue.append((r, c + 1))
        queue.append((r, c - 1))
    return n_dots

total_dots = 0
reachable_dots = 0
min_entrances = 0
for i in range(n):
    for j in range(m):
        c = maze[i][j]
        if c == ".":
            total_dots += 1
        elif c in "ABCDEFGHIJKLMNOPQRSTUVW":
            if i == 0:
                start_dir = (0, 1)
            elif i == n - 1:
                start_dir = (0, -1)
            elif j == 0:
                start_dir = (1, 0)
            elif j == m - 1:
                start_dir = (-1, 0)
            n_eaten = traverse(i + start_dir[1], j + start_dir[0], m, n, visited, maze)
            if n_eaten > 0:
                reachable_dots += n_eaten
                min_entrances += 1
print(f"{min_entrances} {total_dots - reachable_dots}")
            