white = {'k':[], "q":[], "r":[], "b":[], "n":[], "p":[]}
black = {'K':[], "Q":[], "R":[], "B":[], "N":[], "P":[]}
chess_letters = 'abcdefgh'
count = 8
for i in range(1,18):
    line = input()
    if i % 2:
        continue
    line = line.strip('|').split('|')
    for j in range(len(line)):
        if line[j][1] in white:
            white[line[j][1]].append((chess_letters[j], count))
        if line[j][1] in black:
            black[line[j][1]].append((chess_letters[j], count))
    count -= 1

for k in white:
    white[k].sort(key=lambda x: (-int(x[1]),x[0]))
    black[k.upper()].sort(key=lambda x: (int(x[1]),x[0]))
w = "Black: "
b = "White: "

for k,v in white.items():
    for l in v:
        if k != 'p':
            w += k.upper()
        w += l[0]
        w += str(l[1]) + ','
for k,v in black.items():
    for l in v:
        if k != 'P':
            b += k.upper()
        b += l[0]
        b += str(l[1]) + ','
print(b[:-1])
print(w[:-1])