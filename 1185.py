o = input()

m = [0]*12
for i in range(12):
    m[i] = [0]*12

for i in range(12):
    for j in range(12):
        m[i][j] = float(input())

soma = 0
indice = 12
for i in range(0, 11):
    indice -= 1
    for j in range(0, indice):
        soma += m[i][j]


if o == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma/66))
