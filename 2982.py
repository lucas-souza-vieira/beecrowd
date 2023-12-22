# Leitura e definição das variaveis
n = int(input())
gasto = 0
verba = 0

# Loop até a quantidade de valores citados na reunião
for i in range(0, n):
    # Leitura da letra e do numero, com condicional para somar na letra digitada
    t, c = input().split()
    c = int(c)
    if t == 'G':
        gasto += c
    elif t == 'V':
        verba += c
# Condicional para decidir se a verba é maior que o gasto, printando a resposta correta
if verba >= gasto:
    print("A greve vai parar.")
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")
