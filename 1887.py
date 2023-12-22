n, k = input().split()
n = int(n)
k = int(k)

v = input().split()
for i in range(0, n):
    v[i] = int(v[i])

picos = False
vales = False
quantp = 0
quantv = 0

for i in range(1, n):
    if v[i] > v[i - 1]:
        if not picos:
            quantp += 1
            picos = True
            vales = False

    if v[i] < v[i - 1]:
        if not vales:
            quantv += 1
            vales = True
            picos = False

if k == quantp and k == quantv:
    print("beautiful")
else:
    print("ugly")
