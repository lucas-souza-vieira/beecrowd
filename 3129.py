n = int(input())
v = [None]*n
c = [None]*1

# Leio os numeros das figurinhas
for i in range(n):
    v[i] = int(input())

# Confiro se a figurinha ja pertence ao vetor c, se não eu adiciono ela
for i in range(n):
    if v[i] in c:
        continue
    else:
        c.insert(i, v[i])
c.remove(None)

# Conto quantas figurinhas diferentes e repetidas eu tenho
diferentes = len(c)
repetidas = len(v) - diferentes

print(diferentes)
print(repetidas)
