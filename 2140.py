while True:
    
    # Leios os valores
    n, m = [int(x) for x in input().split()]

    if n == 0 and m == 0:
        break
    
    # Calculo o troco
    r = m - n
    notas = 0

    # Enquanto o troco for maior que zero, verifico se da pra usar a nota e desconto o valor dessa nota indo para o teste com a proxima nota de valor menor
    while r > 0:
        if (r - 100) >= 0:
            r -= 100
            notas += 1
        elif (r - 50) >= 0:
            r -= 50
            notas += 1
        elif (r - 20) >= 0:
            r -= 20
            notas += 1
        elif (r - 10) >= 0:
            r -= 10
            notas += 1
        elif (r - 5) >= 0:
            r -= 5
            notas += 1
        elif (r - 2) >= 0:
            r -= 2
            notas += 1
        elif (r - 1) >= 0:
            r -= 1
            notas += 1
    
    # Se o a quantidade de notas for iguala a 2 imprimo possible se não imprimo impossible
    if notas == 2:
        print("possible")
    else:
        print("impossible")
