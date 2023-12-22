# Leitura do valor e do numero das parcelas
v = int(input())
p = int(input())

# Se o resto da divisao do valor pela parcelas for diferente de zero, cai no primeiro caso:
# Variavel resto é o resto da divisao de v por p
# Variavel resto1 é a quantidade restante de parcelas
# Variavel div é a divisao inteira de v e p
# Variavel div1 é o valor acima de div
if v % p != 0:
    resto = v % p
    resto1 = p - resto
    div = v // p
    div1 = div + 1
# Loop pra impimir o valor de div1 de 0 até variavel resto
    for i in range(0, resto):
        print("%i" % div1)
# Loop pra imprimir o valor de div de 0 até variavel resto1
    for a in range(0, resto1):
        print("%i" % div)
# Caso o resto de v e p fosse zero, imprimi todas as parcelas iguais a divisao de v e p
else:
    divisao = v / p
    for b in range(0, p):
        print("%i" % divisao)
