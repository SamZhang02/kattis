cups = [1,0,0]

def A(cups):
    cups[0], cups[1] = cups[1], cups[0]

def B(cups):
    cups[1], cups[2] = cups[2], cups[1]

def C(cups):
    cups[0], cups[2] = cups[2], cups[0]

m = input()
for move in m:
    if move == 'A':
        A(cups)
    if move == 'B':
        B(cups)
    if move == 'C':
        C(cups)

for i in range(len(cups)):
    if cups[i] == 1:
        print(i+1)
        exit()
