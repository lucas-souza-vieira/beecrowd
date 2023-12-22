# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Neste problema, temos duas partes principais: a primeira é converter um número binário em decimal e a
segunda em como converter esse valor decimal em um caracter seguindo a tabela ASCII. Digitando tabela ASCII no Google
é possível verificar que há sempre um valor decimal que é mapeado para um caracter, assim apenas devemos implementar
esse mapeamento ou usar algo pronto. Numa breve pesquisa usando o termo "ascii to char Python3" já é possível encontrar
duas funções úteis ord e chr que permitem converter caracteres ASCII em valores decimais e vice-versa. Podemos usar elas!
'''
while True:
    try:
        n = int(input())
        x = ""
        for _ in range(n):
            # Leio o número binário como string, removendo espaços eventuais antes e depois
            s = input().strip()

            multiplicador = 1
            d = 0  # Inicio meu número decimal valendo 0
            # Trabalho com a string da direita para a esquerda, pois os pesos dos valores 1 são menores na direita
            for i in range(len(s)-1, -1, -1):
                if s[i] == '1':  # Se meu dígito atual for 1, devo somar o multiplicador atual no meu número decimal
                    d += multiplicador

                # A cada deslocamento à esquerda devo aumentar meu multiplicador, pois seu peso será maior
                multiplicador *= 2
            x += chr(d)

        print(x)  # Agora sim pulo linha para ir ao próximo caso de teste
    except EOFError:
        break
