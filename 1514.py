while True:
    part, perg = [int(x) for x in input().split()]
    if part + perg == 0:
        break

    m = [0]*perg
    for i in range(perg):
        m[i] = [0]*part

    for i in range(part):
        m[i] = [int(x) for x in input().split()]

    um = 1
    for i in range(part):
        soma1 = 0
        for j in range(perg):
            soma1 += m[i][j]
            if soma1 == perg:
                um = 0
                break

    dois = 0
    soma2 = 0
    for j in range(perg):
        for i in range(part):
            if m[i][j] == 1:
                soma2 += 1
                break
    if soma2 == perg:
        dois = 1

    tres = 1
    for j in range(perg):
        soma3 = 0
        for i in range(part):
            soma3 += m[i][j]
            if soma3 == part:
                tres = 0
                break

    quatro = 0
    soma4 = 0
    for i in range(part):
        for j in range(perg):
            if m[i][j] == 1:
                soma4 += 1
                break
    if soma4 == part:
        quatro = 1

    total = um + dois + tres + quatro
    print(total)
