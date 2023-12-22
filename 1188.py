# Leio as entradas, crio a matriz e leio as entradas da matriz
n = input()

m = [0]*12
for i in range(12):
    m[i] = [0]*12

for i in range(12):
    for j in range(12):
        m[i][j] = float(input())

# Defino as constantes que eu vou usar, sendo o x e y usados para percorrer apenas a parte que eu desejo da matriz
soma = 0
x = 5
y = 7

# Percorro a parte inferios da martriz, diminuindo o x e aumentando o y, enquanto somo os valores de casa casa
for i in range(7, 12):
    for j in range(x, y):
        soma = m[i][j] + soma
    x -= 1
    y += 1

# Se a operação desejada for S eu printo a soma, se não eu printo a média
if n == "S":
    print(soma)
else:
    media = soma/12
    print(media)