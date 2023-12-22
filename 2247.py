a = 0
while True:
    n = int(input())
    a += 1
    if n == 0:
        break
    else:
        print("Teste %i" % a)
        diferenca = 0
        for i in range(1, n + 1):
            j, z = input().split()
            j = int(j)
            z = int(z)
            diferenca = diferenca + (j - z)
            print("%i" % diferenca)
        print("")
