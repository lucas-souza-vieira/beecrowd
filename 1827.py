while True:
    try:
        n = int(input())
        aux = n

        m = [0]*n
        for i in range(n):
            m[i] = [0]*n

        for i in range(n):
            for j in range(n):
                if i == j:
                    m[i][j] = 2
        for i in range(n):
            m[i][n-1] = 3
            n -= 1

        for i in range(aux // 3, aux - aux // 3):
            for j in range(aux // 3, aux - aux // 3):
                m[i][j] = 1

        m[aux//2][aux//2] = 4

        for i in range(aux):
            for j in range(aux):
                print("%i" % (m[i][j]), end='')
            print()
        print()

    except EOFError:
        break
