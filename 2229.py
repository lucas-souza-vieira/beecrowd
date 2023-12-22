i = 1
while True:
    n = int(input())
    if n > -1 and n < 16:
        print("Teste %i" % i)
        i += 1
        resposta = (2**n + 1)**2
        print("%i" % resposta)
        print("")
    elif n == -1:
        break
