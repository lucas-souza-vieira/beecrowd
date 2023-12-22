n = int(input())
q = 0

for i in range(0, n):
    l, c = input().split()
    l = int(l)
    c = int(c)
    if l > c:
        q += c
    else:
        q += 0
print("%i" % q)
