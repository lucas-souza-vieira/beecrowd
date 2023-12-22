while True:
    try:
        # leio o tamanho da matriz, e defino as variaveis em 0
        l, c = [int(x) for x in input().split()]
        litros = 0
        saca = 0

        # leio a quantidade de cafe em cada celula
        m = [None]*l
        for i in range(l):
            m[i] = [int(x) for x in input().split()]

        # Somo todos os litros na variaveis litros
        for i in range(l):
            for j in range(c):
                litros += m[i][j]

        # Enquanto litros for maior que 60, ou seja, uma saca, eu adiciono uma saca e retiro 60 litros
        while litros >= 60:
            saca += 1
            litros -= 60

        # Imprimo a resposta
        print("%i saca(s) e %i litro(s)" % (saca, litros))

    except EOFError:
        break
