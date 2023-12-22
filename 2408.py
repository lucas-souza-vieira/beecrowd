a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
    if b > c:
        print("%i" % b)
    else:
        print("%i" % c)
elif b > a and b > c:
    if a > c:
        print("%i" % a)
    else:
        print("%i" % c)
elif c > a and c > b:
    if a > b:
        print("%i" % a)
    else:
        print("%i" % b)
