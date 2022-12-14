import random

board = []
arrOdd = []
arrEven = []

while True:
    m = int(input())
    if (m < 2) or (m > 5):
        continue
    else:
        break

foo = input()

for i in range(m):
    board.append([])

if foo == 'r':
    for j in range(m):
        for k in range(m):
            board[j].append(random.randrange(1, 101))

else:
    for j in range(m):
        for k in range(m):
            board[j].append(int(input()))

print(board)

for l in range(m):
    for q in range(m):
        if (board[l][q] % 2 == 0):
            arrEven.append(board[l][q])
        else:
            arrOdd.append(board[l][q])

arrEven.sort()
arrOdd.sort(reverse=True)

if (len(arrEven) > 0 and len(arrOdd) > 0):
    a = arrEven + arrOdd
elif (len(arrEven) == 0):
    a = arrOdd
else:
    a = arrEven
print(a)


# by: teqnot
# under CC BY 4.0