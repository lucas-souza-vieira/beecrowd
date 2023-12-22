# Leitura da quantidade dos casos testes
c = int(input())

# Loop para determinar a quantidade de casos teste:
for i in range(0, c):
    # Leitura da quantidade de bolas e da posição da bola branca:
    n = int(input())
    x, y = input().split()
    x = int(x)
    y = int(y)
    # Variavel auxiliar:
    aux = 1000000
    # Loop para leitura das bolas junto com calculo da distancia, condicional para salvar a menor distancia
    for l in range(1, n + 1):
        x1, y1 = input().split()
        x1 = int(x1)
        y1 = int(y1)
        dist = ((x - x1)**2 + (y - y1)**2)**0.5
        if dist < aux:
            aux = dist
            a = l
    print("%i" % a)
