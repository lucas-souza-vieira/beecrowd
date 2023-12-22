pessoas, orcamento, hoteis, semanas = [int(x) for x in input().split()]
minimo = 0

for i in range(hoteis):
    preço = int(input())
    camas = input().split()
    custo = 0

    for x in range(semanas):
        camas[x] = int(camas[x])

    for x in range(semanas):
        if camas[x] >= pessoas:
            custo += pessoas*preço
            break

    if i == 0 or minimo == 0:
        minimo = custo
    elif custo <= minimo:
        minimo = custo

if minimo <= orcamento:
    print(minimo)
else:
    print("stay home")


