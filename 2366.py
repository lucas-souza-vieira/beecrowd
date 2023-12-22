postos, dix = input().split()
postos = int(postos)
dix = int(dix)
aux = 0

v = input().split()
for i in range(0, len(v)):
    v[i] = int(v[i])

v.append(42195)

for i in range(0, len(v)):
    if i == 0:
        if v[i] > dix:
            aux += 1
    elif (v[i] - v[i - 1]) > dix:
        aux += 1

if aux != 0:
    print("N")
else:
    print("S")
