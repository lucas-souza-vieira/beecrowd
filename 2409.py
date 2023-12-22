a, b, c = input().split()
h, l = input().split()

a = int(a)
b = int(b)
c = int(c)
h = int(h)
l = int(l)

if (a <= h and b <= l):
    print("S")
elif (a <= h and c <= l):
    print("S")
elif (b <= h and a <= l):
    print("S")
elif (b <= h and c <= l):
    print("S")
elif (c <= h and a <= l):
    print("S")
elif (c <= h and b <= l):
    print("S")
else:
    print("N")
