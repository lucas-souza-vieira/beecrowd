l, c = [int(x) for x in input().split()]
i1, j1 = [int(x) for x in input().split()]

m = [0]*(l+2)
for j in range(l+2):
    m[j] = [0]*(c+2)

for i in range(1, (l+1)):
    m[i] = [int(x) for x in input().split()]
    m[i].append(0)
    m[i].insert(0, 0)


while True:
    if (m[i1][j1 - 1] == 0) and (m[i1][j1 + 1] == 0) and (m[i1 - 1][j1] == 0) and (m[i1 + 1][j1] == 0):
        break
    if (m[i1][j1 - 1] == 1):
        m[i1][j1] = 0
        j1 -= 1
    if (m[i1][j1 + 1] == 1):
        m[i1][j1] = 0
        j1 += 1
    if (m[i1 - 1][j1] == 1):
        m[i1][j1] = 0
        i1 -= 1
    if (m[i1 + 1][j1] == 1):
        m[i1][j1] = 0
        i1 += 1

print("%i %i" % (i1, j1))
