# Leitura das quantidades dos ingredientes e do bolo:
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
bolo = 0

# Loop com a condicional de que enquanto a quantidade de ingredientes de entrada for maior que a necessaria continua subtraindo ate que algum
# ou todos os ingredientes falte.
while True:
    if a >= 2 and b >= 3 and c >= 5:
        a -= 2
        b -= 3
        c -= 5
        bolo += 1
    else:
        break
print("%i" % bolo)
