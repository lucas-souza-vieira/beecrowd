while True:
    n = int(input())
    if n == 0:
        break
    retangulo = 0
    retangulopar = 0
    retanguloimpar = 0
    for i in range(0, n):
        c, v = input().split()
        c = int(c)
        v = int(v)
        if n == 1:
            retangulo = v // 4
        else:
            if i % 2 == 0:
                if retangulopar == 0:
                    retangulopar = v // 2
                else:
                    retangulopar = retangulopar + (v // 2)

            elif i % 2 == 1:
                if retanguloimpar == 0:
                    retanguloimpar = v // 2
                else:
                    retanguloimpar = retanguloimpar + (v // 2)
    if n != 1:
        retangulo = ((retangulopar + retanguloimpar) // 2)
        print(retangulo)
    else:
        print(retangulo)
