n = int(input())
for i in range(0, n):
    cont = 0
    p = int(input())
    for a in range(2, (p//2 + 1)):
        if p % a == 0:
            cont += 1
        else:
            cont += 0
    if cont == 0:
        print("Prime")
    elif cont > 0:
        print("Not Prime")
