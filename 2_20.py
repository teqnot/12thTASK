import random

def main():
    board = [[], [], [], [], [], []]
    board3by6 = [[], [], []]
    board3by3 = [[], [], []]

    bar = input()

    if bar == 'r':
        for j in range(6):
            for k in range(6):
                board[j].append(random.randrange(0, 101))

    else:
        for j in range(6):
            for k in range(6):
                board[j].append(int(input()))

    print(board)

    for i in range(5):
        for h in range(6):
            if i % 2 == 0:
                if board[i + 1][h] != 0:
                    board3by6[i//2].append(board[i][h] / board[i + 1][h])
                else:
                    print("Enter the desired mode again: ")
                    main()


    print(board3by6)

    for m in range(3):
        for s in range(5):
            if s % 2 == 0:
                if board3by6[m][s + 1] != 0:
                    board3by3[m].append(board3by6[m][s] / board3by6[m][s + 1])
                else:
                    print("Enter the desired mode again: ")
                    main()

    for m in range(3):
        board3by3[m].sort()
    
    rez = [[board3by3[j][i] for j in range(len(board3by3))] for i in range(len(board3by3[0]))]
    print(' ')
    for row in rez:
        print(row)
        
main()


# by: teqnot
# under CC BY 4.0