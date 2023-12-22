# Recebo a quantidade de peças do quebra cabeça, e a lista de peças que estãp presentes
n = int(input())
v = input().split()

# Criei uma segunda lista, e uma variavel
c = [0]*n
x = 1

# Transformo a primeira lista em intero
for i in range(n-1):
    v[i] = int(v[i])

# Preencho a segunda lista com n inteiros até o total de peças do quebra cabeça
for i in range(n):
    c[i] = x
    x += 1

# Removo da segunda lista todos os elementos em comum com a primeira, sobrando apenas o elemento que está faltando no quebra cabeça
for i in range(n - 1):
    aux = v[i]
    c.remove(aux)

print(c[0])
