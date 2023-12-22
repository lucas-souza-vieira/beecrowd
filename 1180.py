n = int(input())
v = input().split()

for i in range(0, len(v)):
    v[i] = int(v[i])
    if i == 0:
        menor = v[i]
        posicao = i
    elif v[i] < menor:
        menor = v[i]
        posicao = i
print("Menor valor: %i" % menor)
print("Posicao: %i" % posicao)
