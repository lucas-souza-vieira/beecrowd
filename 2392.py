pedras, sapos = input().split()
pedras = int(pedras)
sapos = int(sapos)

v = [0]*pedras

for i in range(0, sapos):
    inicial, pulo = input().split()
    inicial = int(inicial) - 1
    pulo = int(pulo)
    inicial2 = inicial

    for i in range(0, pedras):
        if inicial == i:
            v[i] = 1

    while True:
        if (inicial + pulo) < pedras:
            v[inicial + pulo] = 1
            inicial += pulo
        else:
            break

    while True:
        if (inicial2 - pulo) >= 0:
            v[inicial2 - pulo] = 1
            inicial2 -= pulo
        else:
            break


for i in range(0, pedras):
    print(v[i])
