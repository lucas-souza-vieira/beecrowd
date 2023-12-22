# Defino o numero que vou printar ao lado da palavra teste
l = 1

while True: 
    # Leio as entradas
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    
    # Se elas forem 0 eu paro o programa
    if x1 == 0 & y1 == 0 & x2 == 0 & y2 == 0:
        break

    # Calculo o maximo e minimo para x e y
    x_minimo = min(x1, x2)
    x_maximo = max(x1, x2)
    y_minimo = min(y1, y2)
    y_maximo = max(y1, y2)


    # Leio a quantidade de casos de teste e defino o total de meteoros em 0
    n = int(input())
    total = 0

    # Para cada caso teste leio a coordenada do meteoro e verifico se ela pertence a area do sitio, se pertencer somo 1 em total
    for i in range(n):
        x, y = [int(x) for x in input().split()]

        if  x >= x_minimo and x <= x_maximo and y >= y_minimo and y <= y_maximo:
            total += 1
    # Printo o Teste com o total, e depois somo a L +1 para o proximo caso de teste
    print("Teste %i" % l)
    print(total)
    l += 1

