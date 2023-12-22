a, b, c, raio = input().split()
a = int(a)
b = int(b)
c = int(c)
raio = int(raio)
diametro = 2*raio
diagonal = (a**2 + b**2 + c**2)**0.5

if diagonal <= diametro:
    print("S")
else:
    print("N")
