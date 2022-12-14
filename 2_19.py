import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
board = [[], [], [], [], []]
arr = []

bar = input()

if bar == 'r':
    for j in range(5):
        s = ""
        for k in range(5):
            s += random.choice(alphabet)
        arr.append(s)

else:
    for j in range(5):
        s = ""
        for k in range(5):
            s += input()
        arr.append(s)

for i in range(5):
    for h in range(5):
        board[i].append(ord(arr[i][h]))

for l in range(5):
    board[l].sort(reverse=True)
    
print(board)