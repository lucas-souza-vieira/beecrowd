while True:
    try:
        n = int(input())
        lista = []

        for i in range(n):
            numero = input()

            lista.append(numero)
        
        lista.sort()

        for i in range(n):
            print(lista[i])


    except EOFError:
        break

