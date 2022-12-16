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
boardMerged = []
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

for s in range(4):
    boardMerged += board[s]
boardMerged = bubbleSort(boardMerged)

c = 4

leftHalf = boardMerged[:8]
rightHalf = boardMerged[8:]

print(board)

for n in range(len(leftHalf)):
    if n % 4 == 0 and n != 0:
        c -= 1
    newBoard[4 - c].append(leftHalf[n])

cou = n - 4

for b in range(len(rightHalf)):
    cou += 1
    if cou % 4 == 0:
        c -= 1
    newBoard[4 - c].append(rightHalf[b])

print(newBoard)


# by: teqnot
# under CC BY 4.0