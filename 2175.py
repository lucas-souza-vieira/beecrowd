o, b, i = input().split()
o = float(o)
b = float(b)
i = float(i)

if o < b and o < i:
    print("Otavio")
elif o == b or o == i or i == b:
    print("Empate")
elif b < i:
    print("Bruno")
else:
    print("Ian")
