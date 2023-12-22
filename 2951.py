# Leio a quantidade de runas e o valor necessario e crio o dicionario
n, m = [int(x) for x in input().split()]
d = {}

# Leio cada runa e seu valor e adiciono elas ao dicionario
for i in range(n):
    r, v =  input().split()
    v = int(v)
    d.update({r: v})

# Leio a quantidade de runas recitadas e as runas
x = int(input())
faladas = input().split()

# Somo o valor de cada linha recitada
valor = 0
for i in range(x):
    valor += d[faladas[i]]

# Se o valor for maior ou igual ao necessario pra passar imprimo you shall pass se não imprimo my precious
if valor >= m:
    print(valor)
    print("You shall pass!")
else:
    print(valor)
    print("My precioooous")

