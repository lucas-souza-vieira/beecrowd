n = input()

m = [0]*12
for i in range(12):
    m[i] = [0]*12

for i in range(12):
    for j in range(12):
        m[i][j] = float(input())

soma = 0
x = 11
for i in range(1, 6):
    x -= 1
    for j in range(11, x, -1):
        soma += m[i][j]

x = 5
for i in range(6, 11):
    x += 1
    for j in range(11, x, -1):
        soma += m[i][j]

if n == 'S':
    print("%.1f" % soma)
else:
    print("%.1f" % (soma/30))
