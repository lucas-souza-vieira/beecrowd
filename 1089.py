while True:

    n = int(input())
    if n == 0:
        break

    qtpicos = 0
    japicos = 0

    v = input().split()
    for i in range(0, n):
        v[i] = int(v[i])

    for i in range(1, n - 1):
        if (v[i] > v[i + 1]) and (v[i] > v[i - 1]):
            qtpicos += 1

    if n != 2 and v[0] > v[1] and v[0] > v[n - 1]:
        qtpicos += 1
    if n != 2 and v[n - 1] > v[0] and v[n - 1] > v[n - 2]:
        qtpicos += 1
    if n == 2:
        qtpicos = 1

    resposta = 2*qtpicos
    print("%i" % resposta)
