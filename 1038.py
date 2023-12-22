codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
    valor = quantidade * 4.0
    print("Total: R$ %.2f" % valor)
elif codigo == 2:
    valor = quantidade * 4.5
    print("Total: R$ %.2f" % valor)
elif codigo == 3:
    valor = quantidade * 5.0
    print("Total: R$ %.2f" % valor)
elif codigo == 4:
    valor = quantidade * 2.0
    print("Total: R$ %.2f" % valor)
elif codigo == 5:
    valor = quantidade * 1.5
    print("Total: R$ %.2f" % valor)
