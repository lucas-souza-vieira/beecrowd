n = int(input())

positivo = 0
negativo = 0
lista = []

for i in range(n):
    comportamento, nome = input().split()
    if comportamento == "+":
        positivo += 1
    else:
        negativo += 1
    
    lista.append(nome)

lista.sort()

for i in range(n):
    print(lista[i])

print("Se comportaram: %i | Nao se comportaram: %i" % (positivo, negativo))