voos = [None] * 101
t = 1
while True:
    a, v = input().split()
    a = int(a)
    v = int(v)

    if a == 0 and v == 0:
        break

    for i in range(1, a+1):
        voos[i] = 0

    for i in range(v):
        x, y = input().split()
        x = int(x)
        y = int(y)

        voos[x] += 1
        voos[y] += 1

    maximoVoos = 0
    for i in range(1, a+1):
        if voos[i] > maximoVoos:
            maximoVoos = voos[i]

    print("Teste %d" % (t))
    for i in range(1, a+1):
        if voos[i] == maximoVoos:
            print("%d " % (i), end='')
    print()
    print()

    t += 1
