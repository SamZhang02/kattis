board = []
for i in range(4):
    row = [x for x in input().split()]
    board.append(row)

move = input()

if move == '0':
    for i in range(len(board)):
        for j in range(4):
            for j in range(len(board[i])-1, 0, -1):
                if board[i][j-1] == '0':
                    board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
        for j in range(len(board[i])-1):
            if board[i][j] == board[i][j+1]:
                board[i][j] = str(int(board[i][j]) * 2)
                board[i][j+1] = '0'
        for j in range(4):
            for j in range(len(board[i])-1, 0, -1):
                if board[i][j-1] == '0':
                    board[i][j-1], board[i][j] = board[i][j], board[i][j-1]

if move == '1':
    for k in range(4):
        for j in range(len(board[0])):
            for i in range(len(board)-1,0,-1):
                if board[i-1][j] == '0':
                    board[i-1][j], board[i][j] = board[i][j], board[i-1][j]
    for j in range(len(board[0])):
        for i in range(len(board)-1):
            if board[i][j] == board[i+1][j]:
                board[i][j] = str(int(board[i][j])*2)
                board[i+1][j] = '0'
    for k in range(4):
        for j in range(len(board[0])):
            for i in range(len(board)-1,0,-1):
                if board[i-1][j] == '0':
                    board[i-1][j], board[i][j] = board[i][j], board[i-1][j]

if move == '2':
    for i in range(len(board)):
        for j in range(4):
            for j in range(len(board)-1):
                if board[i][j+1] == '0':
                    board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
        for j in range(len(board)-1, 0, -1):
            if board[i][j-1] == board[i][j]:
                board[i][j] = str(int(board[i][j])*2)
                board[i][j-1] = '0'
        for j in range(4):
            for j in range(len(board)-1):
                if board[i][j+1] == '0':
                    board[i][j+1], board[i][j] = board[i][j], board[i][j+1]

if move == '3':
    for k in range(4):
        for j in range(len(board[0])):
            for i in range(len(board)-1):
                if board[i+1][j] == '0':
                    board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
    for j in range(len(board[0])):
        for i in range(len(board)-1, 0, -1):
            if board[i][j] == board[i-1][j]:
                board[i][j] = str(int(board[i][j])*2)
                board[i-1][j] = '0'
    for k in range(4):
        for j in range(len(board[0])):
            for i in range(len(board)-1):
                if board[i+1][j] == '0':
                    board[i+1][j], board[i][j] = board[i][j], board[i+1][j]

for row in board:
    print(" ".join(row))
