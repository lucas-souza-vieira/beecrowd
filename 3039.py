# recebo o numero de cartas, e defino como 0 o numero de brinquedos
n = int(input())
carrinho = 0
boneca = 0

# recebo o nome e o genero da criança, se o genero for M soma 1 em carrinho e se for diferente de M, soma 1 em boneca
for i in range(n):
    v = input().split()
    if v[1] == 'M':
        carrinho += 1
    else:
        boneca += 1

# imprimo os valores de carrinhos e bonecas
print("%i carrinhos" % carrinho)
print("%i bonecas" % boneca)
