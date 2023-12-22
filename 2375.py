diametro = int(input())
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if diametro <= a and diametro <= b and diametro <= c:
    print("S")
else:
    print("N")
