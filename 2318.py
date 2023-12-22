m = [None]*3
for i in range(3):
    m[i] = [int(x) for x in input().split()]


aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
aux5 = 0
soma = 0

linha_errada = 0
coluna_errada = 0

for i in range(1):
    for j in range(3):
        aux1 += m[i][j]

for i in range(1, 2):
    for j in range(3):
        aux2 += m[i][j]

if aux1 == aux2:
    soma = aux1
else:
    for i in range(2, 3):
        for j in range(3):
            aux3 += m[i][j]
    if aux3 == aux1:
        soma = aux1
    else:
        soma = aux2

for i in range(3):
    for j in range(3):
        aux4 += m[i][j]
    if aux4 == soma:
        aux4 = 0
    else:
        linha_errada = i
        break

for j in range(3):
    for i in range(3):
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

m[linha_errada][coluna_errada] = elemento_certo

for i in range(3):
    for j in range(3):
        print("%i" % (m[i][j]), end='')
        print(" ", end="")
    print()
