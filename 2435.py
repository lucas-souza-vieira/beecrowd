n1, d1, v1 = input().split()
n2, d2, v2 = input().split()

n1 = int(n1)
n2 = int(n2)
d1 = int(d1)
d2 = int(d2)
v1 = int(v1)
v2 = int(v2)

t1 = d1/v1
t2 = d2/v2

if t1 < t2:
    print("%i" % n1)
else:
    print("%i" % n2)
