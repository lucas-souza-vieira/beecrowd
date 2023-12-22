while True:

    n = int(input())
    if n == 0:
        break

    for l in range(0, n):

        v = input().split()
        soma = 0

        for i in range(0, len(v)):
            v[i] = int(v[i])

        for i in range(0, len(v)):
            if v[i] <= 127:
                v[i] = 1
            else:
                v[i] = 0

        for i in range(0, len(v)):
            soma += v[i]
        if soma == 1 and v[0] == 1:
            print("A")
        elif soma == 1 and v[1] == 1:
            print("B")
        elif soma == 1 and v[2] == 1:
            print("C")
        elif soma == 1 and v[3] == 1:
            print("D")
        elif soma == 1 and v[4] == 1:
            print("E")
        else:
            print("*")
