while True:
    n = int(input())
    if n == 0:
        break

    v = input().split()
    maior = 0
    maior2 = 0

    for i in range(0, len(v)):
        v[i] = int(v[i])
        if v[i] > maior:
            maior = v[i]

    for i in range(0, len(v)):
        if v[i] > maior2 and v[i] != maior:
            maior2 = v[i]
            indice = i
    print(indice + 1)
