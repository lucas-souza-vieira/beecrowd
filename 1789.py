while True:
    try:
        cpf = input().strip().replace('.', '').replace('-', '')
        cpf = list(cpf)

        aux = 1
        aux2 = 9
        soma2 = 0
        soma3 = 0

        for i in range(11):
            cpf[i] = int(cpf[i])

        for i in range(9):
            soma2 += cpf[i]*aux
            aux += 1
        for i in range(9):
            soma3 += cpf[i]*aux2
            aux2 -= 1

        if (soma2 % 11 == 10):
            resultado = 0
        else:
            resultado = soma2 % 11

        if (soma3 % 11 == 10):
            resultado2 = 0
        else:
            resultado2 = soma3 % 11

        if (resultado == cpf[9]) and (resultado2 == cpf[10]):
            print("CPF valido")
        else:
            print("CPF invalido")

    except EOFError:
        break
