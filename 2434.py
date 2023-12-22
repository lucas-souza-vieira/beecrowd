n, s = input().split()
n = int(n)
s = int(s)

for i in range(0, n):
    if i == 0:
        a = int(input())
        s2 = s + (a)
        if s2 < s:
            aux = s2
        else:
            aux = s
    else:
        a = int(input())
        s2 = s2 + (a)
        if s2 < aux:
            aux = s2
        else:
            aux = aux
print("%i" % aux)
