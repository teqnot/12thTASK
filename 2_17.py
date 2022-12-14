import random

board = []
gl = 0
sogl = 0
posWords = []

while True:
    m = int(input())
    if (m < 2) or (m > 5):
        continue
    else:
        break

with open('C:/CPP_PROJECTS/12task/2-17Words.txt') as f:
    posWords = f.read().splitlines()

foo = input()

for i in range(m):
    board.append([])

if foo == 'r':
    for j in range(m):
        for k in range(m):
            board[j].append(random.choice(posWords))

else:
    for j in range(m):
        for k in range(m):
            board[j].append(input())

print(board)

for s in range(m):
    for n in range(m):
        board[s][n] = ''.join(sorted(board[s][n], key=str.lower))
        for c in board[s][n]:
            if c.lower() in 'aeiouy':
                gl += 1
            else:
                sogl += 1


print(gl, sogl)
print(board)


# by: teqnot
# under CC BY 4.0