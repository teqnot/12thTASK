import random

def getHex():
    alph = "0123456789ABCDEF"
    ans = random.choice(alph)
    ans += random.choice(alph)
    return ans

def bubbleSort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if int(nums[j], 16) > int(nums[j + 1], 16):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

board = [[], [], [], []]
newBoard = [[], [], [], []]
temp = [[], [], [], []]
foo = input()

if foo == "r":
    for i in range(4):
        for _ in range(4):
            board[i].append(getHex())
else:
    for i in range(4):
        for _ in range(4):
            board[i].append(input())

for s in board:
    print(s)
print(' ')

for smt in range(4):    
    for sm in range(4):
        temp[smt].append(board[sm][smt])

for j in range(4):
    for _ in range(4):
        newBoard[j] = bubbleSort(temp[j])
        if j % 2 == 0:
            newBoard[j].reverse()

rez = [[newBoard[j][i] for j in range(len(newBoard))] for i in range(len(newBoard[0]))]
for row in rez:
    print(row)
