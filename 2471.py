n = int(input())

m = [None]*n
for i in range(n):
    m[i] = [int(x) for x in input().split()]


aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
aux5 = 0
soma = 0

for i in range(0, 1):
    for j in range(n):
        aux1 += m[i][j]

for i in range(1, 2):
    for j in range(n):
        aux2 += m[i][j]

if aux1 == aux2:
    soma = aux1
else:
    for i in range(2, 3):
        for j in range(n):
            aux3 += m[i][j]
    if aux3 == aux1:
        soma = aux1
    else:
        soma = aux2

for i in range(n):
    for j in range(n):
        aux4 += m[i][j]
    if aux4 == soma:
        aux4 = 0
    else:
        linha_errada = i
        break

for j in range(n):
    for i in range(n):
        aux5 += m[i][j]
    if aux5 == soma:
        aux5 = 0
    else:
        coluna_errada = j
        break

elemento_errado = m[linha_errada][coluna_errada]
if soma <= aux4:
    elemento_certo = abs(elemento_errado - abs(aux4 - soma))
elif soma >= aux4:
    elemento_certo = abs(elemento_errado + abs(aux4 - soma))

print("%i %i" % (elemento_certo, elemento_errado))
