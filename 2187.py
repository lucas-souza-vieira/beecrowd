b50 = 0
b10 = 0
b5 = 0
b1 = 0
t = 1

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n, 0, -1):
            if n >= 50:
                b50 += 1
                n = n - 50
            elif n >= 10:
                b10 += 1
                n = n - 10
            elif n >= 5:
                b5 += 1
                n = n - 5
            elif n >= 1:
                b1 += 1
                n = n - 1
    print("Teste %i" % t)
    t += 1
    print("%i %i %i %i" % (b50, b10, b5, b1))
    print("")
    b50 = 0
    b10 = 0
    b5 = 0
    b1 = 0
