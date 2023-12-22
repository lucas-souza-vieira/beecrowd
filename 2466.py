n = int(input())

m = [None]*n

m = [int(x) for x in input().split()]

while True:
    if n == 1:
        break

    for i in range(n - 1):
        if m[i] == m[i+1]:
            m[i] = 1
        else:
            m[i] = -1
    n -= 1

if m[0] == 1:
    print("preta")
else:
    print("branca")
