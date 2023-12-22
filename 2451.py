# Leio o tamanho da matriz

n = int(input())

# Leio as entradas da matriz
m = []
for i in range(n):
    a = input()
    temp = []
    for j in range(n):
        temp.append(a[j])
    m.append(temp)    

# Defino minhas variaveis
comida = 0
max = 0


# Percorro o caminho inteiro:
for i in range(n):
        # Se for uma linha par, percoro da esquerda da direita
        if i % 2 == 0: 
            for j in range(n):
                if m[i][j] == 'o': # Se encontrar comida somo mais 1
                    comida += 1
                    if comida > max: # Vou testando para ver qual a quantidade maxima de comida que ele acumula
                        max = comida
                elif m[i][j] == 'A': # Se encontrar fantasmo, zero a quantidade de comidas
                    comida = 0
        # Se for uma linha impar, percorro da direita para esquerda
        else: 
            for j in range(n - 1, -1, -1):
                if m[i][j] == 'o':
                    comida += 1
                    if comida > max:
                        max = comida
                elif m[i][j] == 'A':
                    comida = 0

# Printo a maior quantidade de comida que ele acumulou
print(max)


