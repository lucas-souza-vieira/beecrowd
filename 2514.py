# Importo a biblioteca math pra usar o a função mdc pronta deles
import math

while True:
    try:
        # Leio a quanto anos aconteceu o ultimo alinhamento
        n = int(input())

        # Leio os anos das 3 luas
        a, b, c = [int(x) for x in input().split()]

        # Calculo o mdc de a e b e depois o mmc de a e b pelo algoritmo de euler
        mdc1 = math.gcd(a,b) 
        mmc1 = (a*b)//mdc1

        # Faço a mesma coisa, mas agora com o mmc de a e b e c
        mdc = math.gcd(mmc1, c)
        mmc = (mmc1*c)// mdc

        # Desconto o ultimo ano que aconteceu, e printo em quantos anos acontecera de volta
        anos = mmc - n
        print(anos)

    except EOFError:
        break