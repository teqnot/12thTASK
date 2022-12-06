import random

board = []
posWords = []
arr = []

while True:
    m = int(input())
    if (m < 2) or (m > 5):
        continue
    else:
        break

with open('C:/CPP_PROJECTS/12task/2-11Words.txt') as f:
    posWords = f.read().splitlines()

foo = input()

for i in range(m):
    board.append([])

if foo == 'r':
    for j in range(m):
        for k in range(m):
            board[j].append((random.choice(posWords)).lower())

else:
    for j in range(m):
        for k in range(m):
            board[j].append(input())

print(board)

for s in range(m):
    for h in range(m):
        arr.append(sum(ch in "aeiouy" for ch in board[s][h]))

arr.sort()
print(arr)