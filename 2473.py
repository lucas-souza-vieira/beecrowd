# Recebo o numeros escolhidos pelo flavinho e os numeros sorteados
flavinho = input().split()
sorteados = input().split()
total = 0

# Conto o numero de numeros que flavinho escolheu que pertence aos sorteados
for i in range(6):
    if flavinho[i] in sorteados:
        total += 1

# Vejo no qual se encaixa o caso de flavinho
if total < 3:
    print("azar")
if total == 3:
    print("terno")
if total == 4:
    print("quadra")
if total == 5:
    print("quina")
if total == 6:
    print("sena")
