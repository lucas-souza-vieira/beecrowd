# Recebo o numero de alunos e o numero minimo de alunos e transforme em inteiros, defino o numero de atrasados em 0
a, m = [int(x) for x in input().split()]
atrasados = 0

# Recebo o tempo de chegada  dos alunos
v = input().split()

# Se o tempo de chegada for maior que 0, aumento a quantidade de atrasados
for i in range(a):
    v[i] = int(v[i])
    if v[i] > 0:
        atrasados += 1

# Se o total de alunos menos a quantidade de atrasados for maior ou igual a quantidade minima, eu imprimo YES se não, imprime NO
if (a - atrasados) >= m:
    print("YES")
else:
    print("NO")
