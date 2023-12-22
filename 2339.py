competidores, total, quantidade = input().split()
competidores = int(competidores)
total = int(total)
quantidade = int(quantidade)

if (total // competidores) >= quantidade:
    print("S")
else:
    print("N")
