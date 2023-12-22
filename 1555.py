# Leio a entrada de dados e faço o for para o numero de testes
n = int(input())

for i in range(n):

    # Leio cada valor
    x, y = [int(x) for x in input().split()]

    # Calculo o resultado de cada formula
    rafael = (3*x)**2 + y**2
    beto = 2*(x**2) + (5*y)**2
    carlos = y**3 -100*x

    # Printo o maior
    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    elif beto > rafael and beto > carlos:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")