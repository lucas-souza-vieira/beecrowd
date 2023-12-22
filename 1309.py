# Loop até acabar os casos de teste
while True:
    try:
        # Leio as entradas e transformo em vetores
        d = input()
        c = input()

        d = list(d)
        c = list(c)

        # Se c for igual a 1, eu adiciono um 0 na frente
        if len(c) == 1:
            c.insert(0, "0")

        # Se d for maior ou igual a 3, eu adiciono uma virgula a cada 3 posições começando do final do vetor
        if len(d) >= 3:
            for i in range(len(d) - 3, 0, -3):
                d.insert(i,",")

        # Transformo em string de novo e concateno com o $ e o .
        c = "".join(c)
        d = "".join(d)

        junto = "$" + d + "." + c
        print(junto)
        

    
    except EOFError:
        break