import random

board = []
boardMerged = []
newBoard = []
count = 0
leftHalf = []
rightHalf = []

while True:
    m = int(input())
    if (m < 2) or (m > 8):
        continue
    else:
        break

c = m
foo = input()

for i in range(m):
    board.append([])
    newBoard.append([])

if foo == 'r':
    for j in range(m):
        for k in range(m):
            board[j].append(random.randrange(1, 101))

else:
    for j in range(m):
        for k in range(m):
            board[j].append(int(input()))

print(board)

for s in range(m):
    boardMerged += board[s]
boardMerged.sort(reverse=True)

rightHalf = boardMerged[:((m * m) - 1)//2]
leftHalf = boardMerged[((m * m) - 1)//2:]

for n in range(len(leftHalf)):
    if n % m == 0 and n != 0:
        c -= 1
    newBoard[m - c].append(leftHalf[n])

cou = n - m

for b in range(len(rightHalf)):
    cou += 1
    if cou % m == 0:
        c -= 1
    newBoard[m - c].append(rightHalf[b])

print(newBoard)