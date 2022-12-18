import random

board = [[], [], [], []]
count  = 0
columns = [[], [], [], []]
unq = []

def convert_to_int(string):
    try:
        int(string)
        return True

    except ValueError:
        return False

def qsort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem) 
            elif elem > q: 
                R.append(elem) 
            else: 
                M.append(elem)
        return qsort(L) + M + qsort(R)

arr = []

while True:
    s = input()
    arr.append(list(s.split(' ')))
    for i in range(len(arr) - 1, len(arr)):
        for j in arr[i]:
            if (len(j) == 4 and convert_to_int(j)):
                unq.append(j)
    if len(unq) >= 4:
        break

unq = unq[:4]

for s in range(4):
    for f in range(len(unq[s])):
        board[s].append(unq[s][f])  

for smt in range(4):    
    print(*board[smt], '\t')
print(' ')

for smt in range(4):    
    for sm in range(4):
        columns[smt].append(board[sm][smt])

for smn in range(4):    
    print(*columns[smn], '\t')
print(' ')

for qqq in range(4):
    for qq in range(4):
        if qqq % 2 == 0:
            columns[qqq] = qsort(columns[qqq])
        else:
            columns[qqq] = qsort(columns[qqq])[::-1]

rez = [[columns[j][i] for j in range(len(columns))] for i in range(len(columns[0]))]
for row in rez:
    print(row)