while True:
    n = int(input())
    if n == 0:
        break

    m = [None]*n
    for i in range(n):
        m[i] = [None]*n

    y = -1
    for i in range(n):
        y += 1
        x = 0
        x += y
        for j in range(n):
            m[i][j] = 2**x
            x += 1

    # for i in range(n):
    #     m[i] = " ".join(str(x) for x in m[i])
    #     print(m[i])
    # print("")

    T = len(str(m[n-1][n-1]))
    for i in range(n):
        for j in range(n):
            m[i][j] = str(m[i][j])
            while len(m[i][j]) < T:
                m[i][j] = ' ' + m[i][j]
        M = ' '.join(m[i])
        
        print(M)
    print()