# leitura das idades
m = int(input())
a = int(input())
b = int(input())

# Somando as idades dos filhos e subtraindo com a da mão para descobrir a idade do ultimo filho
soma = a + b
c = m - soma

# Condicional para descobrir qual é o filho mais velho
if c > a and c > b:
    print("%i" % c)
elif a > b:
    print("%i" % a)
else:
    print("%i" % b)
