# Leio o tamanho da matriz
n = int(input())

m = [None]*n
v = []

# Leio as entradas da matriz
for i in range(n):
    m[i] = input().split()

# Para cada coordenada da matriz, adiciono o valor dentro do vetor se ele ainda não estiver lá
for x in range(n*2):
    i, j = [int(x) for x in input().split()]
    if m[i-1][j-1] not in v:
        v.append(m[i-1][j-1])

print(len(v))

