l, c = [int(x) for x in input().split()]
sim = 0

m = [0]*l
for i in range(l):
    m[i] = [int(x) for x in input().split()]

for i in range(l):
    for j in range(c):
        if m[i][j] == 0 and m[]:
            for x in range(l - i):
                if m[x][j] != 0:
                    sim += 1
        

if sim == 0:
    print("S")
else:
    print("N")
