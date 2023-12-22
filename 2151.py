t = int(input())
p = 1
for a in range(t):
    linha, coluna, y, x = [int(x) for x in input().split()]

    x = x - 1
    y = y - 1

    m = [0]*linha
    for i in range(linha):
        m[i] = [int(x) for x in input().split()]
    for i in range(linha):
        for j in range(coluna):
            if i == y and j == x:
                m[i][j] += 10
            elif i == y:
                aux = 10 - abs(j - x)
                if aux < 1:
                    m[i][j] += 1
                else:
                    m[i][j] += aux
            elif j == x:
                aux = 10 - abs(i - y)
                if aux < 1:
                    m[i][j] += 1
                else:
                    m[i][j] += aux
            elif i != y and j != x:
                aux = 10 - abs(j - x)
                aux2 = 10 - abs(i - y)
                if aux <= aux2:
                    if aux < 1:
                        m[i][j] += 1
                    else:
                        m[i][j] += aux
                elif aux2 < aux:
                    if aux2 < 1:
                        m[i][j] += 1
                    else:
                        m[i][j] += aux2
    print("Parede %i:" % p)
    """for i in range(linha):
            for j in range(coluna):
                print("%i " % m[i][j], end="")
        print("")
    """
    for i in m:
        print(" ".join([str(x) for x in i]))

    p += 1
