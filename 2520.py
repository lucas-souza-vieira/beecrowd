while True:
    try:
        l, c = [int(x) for x in input().split()]

        m = [0]*l
        for i in range(l):
            m[i] = [int(x) for x in input().split()]

        for i in range(l):
            for j in range(c):
                if m[i][j] == 1:
                    ia = i
                    ja = j
                if m[i][j] == 2:
                    ip = i
                    jp = j
        x = abs(jp - ja)
        y = abs(ip - ia)
        resposta = x + y
        print(resposta)

    except EOFError:
        break
