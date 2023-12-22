# Leio o numero de entradas e crio o vetor
n = int(input())
v = [None]*n

# Leio o numero de cada aluno
for i in range(n):
    v[i] = int(input())

# Uso a função set para remover os itens duplicados
c = set(v)

# Defino os alunos presentes como o tamanho de c
presentes = len(c)

# Imprimo a resposta
print(presentes)
