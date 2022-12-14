import random

def main():
    board = [[], [], [], [], [], []]
    board3by6 = [[], [], []]
    board3by3 = [[], [], []]
    boardCol = [[], [], []]

    bar = input()

    if bar == 'r':
        for j in range(6):
            for k in range(6):
                board[j].append(random.randrange(0, 101))

    else:
        for j in range(6):
            for k in range(6):
                board[j].append(int(input()))

    for u in board:
        print(u)
    print(' ')

    for i in range(5):
        for h in range(6):
            if i % 2 == 0:
                if board[i + 1][h] != 0:
                    board3by6[i//2].append(board[i][h] / board[i + 1][h])
                else:
                    print("Enter the desired mode again: ")
                    main()

    for r in board3by6:
        print(r)
    print(' ')

    for m in range(3):
        for s in range(5):
            if s % 2 == 0:
                if board3by6[m][s + 1] != 0:
                    board3by3[m].append(board3by6[m][s] / board3by6[m][s + 1])
                else:
                    print("Enter the desired mode again: ")
                    main()

    for m in range(3):
        print(board3by3[m])
        for mm in range(3):
            boardCol[m].append(board3by3[mm][m])
    
    print(' ')
    
    for kk in range(3):
        boardCol[kk].sort()

    print(' ')
    
    rez = [[boardCol[j][i] for j in range(len(boardCol))] for i in range(len(boardCol[0]))]
    for row in rez:
        print(row)

main()


# by: teqnot
# under CC BY 4.0