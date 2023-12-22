n = int(input())
v = [0]*n

for i in range(0, n):
    a = int(input())
    v[i] = a

if n == 1:
    bomba = v[i]
    print(bomba)
else:
    for i in range(0, len(v)):
        if i == 0:
            bomba = v[i] + v[i + 1]
            print(bomba)
        elif i == n - 1:
            bomba = v[i] + v[i - 1]
            print(bomba)
        else:
            bomba = v[i - 1] + v[i] + v[i + 1]
            print(bomba)
