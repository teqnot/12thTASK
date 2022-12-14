import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
board = []
arr = []

def wordGen():
    foo = ''
    while len(foo) < 4:
        foo += random.choice(alphabet)
    return foo

while True:
    m = int(input())
    if (m < 2) or (m > 5):
        continue
    else:
        break

bar = input()

for i in range(m):
    board.append([])
    arr.append([])

if bar == 'r':
    for j in range(m):
        for k in range(m):
            board[j].append(wordGen())

else:
    for j in range(m):
        for k in range(m):
            board[j].append(input())

print(board)

for s in range(m):
    for n in range(m):
        buff = ''
        for ch in board[s][n]:
            buff += str(ord(ch)) # или str(alphabet.index(ch) + 10); не могу понять, что конкретно требуется
        arr[s].append(buff)

print(arr)


# by: teqnot
# under CC BY 4.0