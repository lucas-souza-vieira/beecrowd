c = 1
while True:
    n = int(input())
    at = 0
    bt = 0

    if n != 0:
        print("Teste %i" % c)
    else:
        break

    for i in range(0, n):
        a, b = input().split()
        a = int(a)
        b = int(b)
        at = at + a
        bt = bt + b

    c += 1
    if at > bt:
        print("Aldo")
        print("")
    else:
        print("Beto")
        print("")
