A = [[], [], [], []]
aTransformed = [[], [], [], []]
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

def check(a):
    global alphabet
    for s in a:
        if s not in alphabet:
            return False
    return True

for i in range(4):
    for j in range(4):
       while True:
        a = (str(input())).lower()
        if check(a):
            A[i].append(a)
            print(A)
            break
        else:
            continue

for h in range(4):
    for k in range(4):
        aTransformed[h].append(alphabet.index(max(A[h][k])) + 1)

print(aTransformed)
