n = int(input())
aux = 0
s = 0


for i in range(0, n):
    p = int(input())
    if (i == 0 and (p - aux) < 10) or (i == 0 and (p - aux) >= 10):
        s = s
    elif p - aux < 10:
        s = s + (p - aux)
    else:
        s = s + 10
    aux = p


s += 10
print("%i" % s)
