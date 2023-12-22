a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b and b == c:
        print("Valido-Equilatero")
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
            print("Retangulo: S")
        else:
            print("Retangulo: N")

    elif a == b or b == c or c == a:
        print("Valido-Isoceles")
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
            print("Retangulo: S")
        else:
            print("Retangulo: N")

    elif a != b and b != c and c != a:
        print("Valido-Escaleno")
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
            print("Retangulo: S")
        else:
            print("Retangulo: N")

else:
    print("Invalido")
