# Criar um vetor a mais e subtrair um do outro pra chegar na resposta
while True:
    try:
        n, r = input().split()
        n = int(n)
        r = int(r)
        v = input().split()
        a = [0]*n

        if n == r:
            print("*")

        else:
            for i in range(r):
                v[i] = int(v[i])

            for x in range(0, n):
                a[x] = x + 1

            for i in range(r):
                a.remove(v[i])

            for x in range(len(a)):
                print("%s " % a[x], end="")
            print("")
    except EOFError:
        break
