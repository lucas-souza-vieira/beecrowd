while True:
    try:
        n = int(input())
        # Salvo n em um auxiliar
        aux = n

        # Criei e ja prenchi com 3 a matriz
        m = [3]*n
        for i in range(n):
            m[i] = [3]*n

        # Preencho a diagonal principal com 1
        for i in range(n):
            for j in range(n):
                if i == j:
                    m[i][j] = 1

        # Preencho da diagonal secundaria com 2
        for i in range(n):
            m[i][n-1] = 2
            n -= 1

        # Printo a matriz
        for i in range(aux):
            for j in range(aux):
                print("%i" % (m[i][j]), end='')
            print()

    except EOFError:
        break
