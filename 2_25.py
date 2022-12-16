import random

def getHex():
    alph = "0123456789ABCDEF"
    ans = random.choice(alph)
    ans += random.choice(alph)
    return ans

def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if int(n, 16) < int(q, 16):
                s_nums.append(n)
            elif int(n, 16) > int(q, 16):
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quickSort(s_nums) + e_nums + quickSort(m_nums)

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
        newBoard[j] = quickSort(board[j])
        if j % 2 != 0:
            newBoard[j].reverse()

print(newBoard)


# by: teqnot
# under CC BY 4.0