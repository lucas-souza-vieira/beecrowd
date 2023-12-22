largura, comprimento, altura = input().split()
largura1, comprimento1, altura1 = input().split()

largura = int(largura)
comprimento = int(comprimento)
altura = int(altura)
largura1 = int(largura1)
comprimento1 = int(comprimento1)
altura1 = int(altura1)

larg = largura1//largura
comp = comprimento1//comprimento
alt = altura1//altura

total = larg*comp*alt
print("%i" % total) 