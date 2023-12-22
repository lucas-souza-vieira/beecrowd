n = int(input())

casa = 0
trabalho = 0
comprarCasa = 0
comprarTrabalho = 0

for _ in range(n):
    sd, sn = input().split()

    if sd == "chuva":
        if casa > 0:
            casa -= 1
            trabalho += 1
        else:
            comprarCasa += 1
            trabalho += 1

    if sn == "chuva":
        if trabalho > 0:
            trabalho -= 1
            casa += 1
        else:
            comprarTrabalho += 1
            casa += 1

print("%d %d" % (comprarCasa, comprarTrabalho))
