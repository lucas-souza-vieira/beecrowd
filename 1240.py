# Leio a entrada
n = int(input())

# Faço cada caso teste até o numero necessario
for i in range(n):
    a, b = input().split()

    # Transformo a string de numeros em vetor
    a = list(a)
    b = list(b)

    # Vejo se o vetor A é maior que B, se não for ja quer dizer que não encaixa
    if len(a) >= len(b):
        # Calculo a diferenca de tamanho entre os dois, e removo os primeiros elementos de A para que ele tenha o mesmo tamamnho de B
        diferenca = len(a) - len(b)
        for i in range(diferenca):
            a.pop(0)
        # Se  forem iguais, significa que a parte que sobrou de A é igual a B, então b encaixa em A, se não ele não encaixa
        if a == b:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")

