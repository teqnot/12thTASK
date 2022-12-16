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
foo = input()

if foo == "r":
    for i in range(4):
        for _ in range(4):
            board[i].append(getHex())
else:
    for i in range(4):
        for _ in range(4):
            board[i].append(input())

print(board)

for j in range(4):
    for _ in range(4):
        newBoard[j] = bubbleSort(board[j])
        if j % 2 == 0:
            newBoard[j].reverse()

print(newBoard)


# by: teqnot
# under CC BY 4.0
