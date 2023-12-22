n = int(input())
o = input()

m = [0]*12
for i in range(12):
    m[i] = [0]*12

for i in range(12):
    for j in range(12):
        m[i][j] = float(input())

soma = 0
for j in range(12):
    soma += m[n][j]

if o == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma/12))
