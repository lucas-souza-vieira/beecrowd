# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, similar ao problema 2465, devo verificar todas as casas que consigo atingir com o agente contaminante. Assim, inicialmente devo
descobrir todas as casas com T e armazenar as coordenadas delas (i,j) em uma lista. Depois, enquanto houverem casas com T nessa lista, devo marcar
todas as casas com A em sua vizinhança (os 4 vizinhos de sempre) agora com o símbolo T e armazenar essas novas casas com T também nessa lista. Eu repito
esse procedimento enquanto que essa lista contiver algum elemento. Note que também devo controlar para evitar que uma mesma posição (i,j) seja incluída
denovo nessa mesma lista. Assim, devo utilizar uma matriz auxiliar para marcar, por exemplo, as casas já participantes dessa lista em algum momento.
'''

#Crio as matrizes para usar em todos os casos de teste
mat = [None] * 51

while True:
    n, m = input().split()
    n = int(n)
    m = int(m)

    if n == 0 and m == 0:
        break
        
    for i in range(n):
        mat[i] = list(input().strip()) #Converto cada linha em uma lista de caracteres (fica mais fácil de manipular depois)

    #Inicialmente verifico todas as casas com valor T e armazeno na lista de contaminadas
    contaminadas = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 'T':
                contaminadas.append((i,j)) #Adiciono uma dupla contendo os valores de i e j
                
    while contaminadas != []:
        (a,b) = contaminadas.pop(0)
        
        #Abaixo verifico todos os 4 vizinhos da posição atual, verificando se algum deles possui valor 'A'
        #Vizinho acima
        vizinhoI = a -1
        vizinhoJ = b
        if vizinhoI >= 0 and mat[vizinhoI][vizinhoJ] == 'A': #Posso ir para cima
            contaminadas.append((vizinhoI,vizinhoJ)) #Adiciono uma dupla contendo os valores de vizinhoI e vizinhoJ
            mat[vizinhoI][vizinhoJ] = 'T' #Marco essa casa também como contaminada na matriz original (para imprimir no futuro)
            

        #Vizinho abaixo
        vizinhoI = a +1
        vizinhoJ = b
        if vizinhoI < n and mat[vizinhoI][vizinhoJ] == 'A': #Posso ir para baixo
            contaminadas.append((vizinhoI,vizinhoJ)) #Adiciono uma dupla contendo os valores de vizinhoI e vizinhoJ
            mat[vizinhoI][vizinhoJ] = 'T' #Marco essa casa também como contaminada na matriz original (para imprimir no futuro)
            
        #Vizinho direito
        vizinhoI = a
        vizinhoJ = b +1
        if vizinhoJ < m and mat[vizinhoI][vizinhoJ] == 'A': #Posso ir para a direita
            contaminadas.append((vizinhoI,vizinhoJ)) #Adiciono uma dupla contendo os valores de vizinhoI e vizinhoJ
            mat[vizinhoI][vizinhoJ] = 'T' #Marco essa casa também como contaminada na matriz original (para imprimir no futuro)
            
        #Vizinho esquerdo
        vizinhoI = a
        vizinhoJ = b -1
        if vizinhoJ >= 0 and mat[vizinhoI][vizinhoJ] == 'A': #Posso ir para a esquerda
            contaminadas.append((vizinhoI,vizinhoJ)) #Adiciono uma dupla contendo os valores de vizinhoI e vizinhoJ
            mat[vizinhoI][vizinhoJ] = 'T' #Marco essa casa também como contaminada na matriz original (para imprimir no futuro)

    for i in range(n):
        for j in range(m):
            print(mat[i][j], end='')
        print()
    print()
