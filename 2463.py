# Leio a quantidade de salas
n = int(input())

# Leio os numeros da sala e transformo em inteiro 
l = [int(x) for x in input().split()]

# Defino as minhas variaveis em 0
soma = 0
maior = 0

# Percorro o vetor a
for i in l:
   # Somo cada i a soma
   soma += i
   # Pego o maior valor entre o auxiliar e a soma
   maior = max(maior,soma) 
   # Se a soma for menor 0, passo pra ela o valor 0
   if soma < 0:
    soma = 0

print(maior)


