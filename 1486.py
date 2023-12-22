while True:
    p, n, c = input().split()
    p = int(p)
    n = int(n)
    c = int(c)
    comprimentoPalito = [None] * p

    if p == 0 and n == 0 and c == 0:
        break

    maioresPalitos = 0
    for i in range(p):
        comprimentoPalito[i] = 0

    for _ in range(n):
        medicoes = input().split()
        for i in range(p):
            if medicoes[i] == '1':
                comprimentoPalito[i] += 1
            else:
                if comprimentoPalito[i] >= c:
                    maioresPalitos += 1
                comprimentoPalito[i] = 0

    for i in range(p):
        if comprimentoPalito[i] >= c:
            maioresPalitos += 1

    print(maioresPalitos)
