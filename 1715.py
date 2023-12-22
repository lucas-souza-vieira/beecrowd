l, n = [int(x) for x in input().split()]

m = [0]*l
for j in range(l):
    m[j] = [0]*n

for j in range(l):
    m[j] = input().split()

total = 0
for i in range(l):
    soma = 0
    for j in range(n):
        if m[i][j] == '0':
            soma += 0
        else:
            soma += 1
    if soma == n:
        total += 1

print(total)
