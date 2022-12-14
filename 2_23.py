import random

def convertToNum(col1, col2):
    alph = 'abcdefgh'
    col1 = alph.index(col1)
    col2 = alph.index(col2)
    return [col1, col2]

def checkDirection(r1, c1, r2, c2):
    if (r1 > r2 and c1 < c2): # Up and Right
        return 0
    if (r1 > r2 and c1 > c2): # Up and Left
        return 1
    if (r1 < r2 and c1 < c2): # Down and Right
        return 2
    if (r1 < r2 and c1 > c2): # Down and Left
        return 3

def main():
    board = []
    newBoard = []
    d = {}
    dMerged = {}
    for smt in range(8):
        board.append([])
        newBoard.append([0, 0, 0, 0, 0, 0, 0, 0])

    for n in range(8):
        for nn in range(8):
            board[n].append(random.randrange(1, 101))

    print('Input the squares: ')
    s = input()
    column1 = (s[0]).lower()
    row1 = int(s[1]) - 1
    s1 = input()
    column2 = (s1[0]).lower()
    row2 = int(s1[1]) - 1

    foo  = convertToNum(column1, column2)
    column1 = foo[0]
    column2 = foo[1]

    print(row1, column1)
    print(row2, column2)

    if ((abs(row1 - row2) != abs(column1 - column2)) or (row1 - row2 == 0 and column1 - column2 == 0)):
        print("A DIAGONAL CANNOT EXIST")
        main()
    else:
        bar = checkDirection(row1, column1, row2, column2)
        print(bar, " <-")
        if bar == 0:
            j = column1
            for i in range(row1, row2 - 1, -1):
                d[(i, j)] = board[i][j]
                j += 1

        if bar == 1:
            j = column1
            for i in range(row1, row2 - 1, -1):
                d[(i, j)] = board[i][j]
                j -= 1

        if bar == 2:
            j = column1
            for i in range(row1, row2 + 1, 1):
                d[(i, j)] = board[i][j]
                j += 1

        if bar == 3:
            j = column1
            for i in range(row1, row2 + 1, 1):
                d[(i, j)] = board[i][j]
                j -= 1

    dSorted = dict(sorted(d.items(), key=lambda item: item[1]))


    keysD = list(d.keys())
    valuesDSorted = list(dSorted.values())

    for z in range(len(keysD)):
        dMerged[(keysD[z])] = valuesDSorted[z]

    for q in range(8):
        print(board[q])
        print(' ')

    print(d)
    print(' ')
    print(dSorted)
    print(' ')
    print(dMerged)

    for f in range(8):
        for p in range(8):
            if (f, p) in list(dMerged.keys()):
                newBoard[f][p] = dMerged[(f, p)]

    for qqq in range(8):
        print(newBoard[qqq])
        print(' ')

main()