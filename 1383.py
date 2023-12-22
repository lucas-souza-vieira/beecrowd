# -*- coding: utf-8 -*-
''' IDEIA DA SOLUÇÃO
Nesse problema, devo verificar se a solução de sudoku dada é válida ou não. Note que podemos quebrar esse problema em vários subproblemas pequenos.
Assim, podemos dizer que inicialmente 'sim' é uma solução válida até encontrarmos alguma coisa que indique que na verdade a solução é inválida, ou
seja, se algum número apareceu na linha, coluna ou quadrado pequeno mais e uma vez. Dessa forma, podemos dividir o problema em etapas, sendo que 
em uma primeira etapa verificamos todas as linhas, depois todas as colunas e depois todos os quadrados pequenos. Em todos os casos devemos sempre
marcar os valores já encontrados para verificar se não encontramos eles novamente. Por exemplo, ao verificar a linha 4 devemos inicializar um vetor
onde o índice do vetor é um valor entre 1 e 9 e o valor do vetor naquela posição indica se esse valor entre 1 e 9 está ou não presente na linha 4.
Inicialmente todos os valores desse vetor devem ser False (indicando que nenhum valor entre 1 e 9 está presente na linha 4). Depois, percorrendo
cada coluna daquela linha devemos anotar True para os valores encontrados. Note que se um valor já estiver presente devemos simplesmente abortar tudo 
indicando que a solução da entrada não é uma solução válida. Fazemos isso por meio de break (conforme estará escrito no código abaixo).
'''

mat = [None] * 9

n = int(input())
for k in range(1,n+1):
    
    
    for i in range(9):
        mat[i] = input().split()
        for j in range(9):
            mat[i][j] = int(mat[i][j])
    
    sim = True
    presente = [0] * 10 #Uso esse vetor para dizer se um valor de 1 até 9 está presente
    
    #Testo cada linha
    for i in range(9):
        
        for x in range(1,10): #Marco inicialmente todos os valores de 1 até 9 como não presentes
            presente[x] = False
        
        for j in range(9):
            if presente[mat[i][j]]: #Se o valor atual já está presente, então é porque ele apareceu antes, assim já não é um sudoku válido
                sim = False
                break
            else: #Caso contrário, digo que o valor atual está presente
                presente[mat[i][j]] = True
        if not sim: #Assim que descobrir que não é mais uma solução válida posso dar um break
            break
    
    if sim:
        #Testo cada coluna
        for j in range(9):
            
            for x in range(1,10): #Marco inicialmente todos os valores de 1 até 9 como não presentes
                presente[x] = False
            
            for i in range(9):
                if presente[mat[i][j]]: #Se o valor atual já está presente, então é porque ele apareceu antes, assim já não é um sudoku válido
                    sim = False
                    break
                else: #Caso contrário, digo que o valor atual está presente
                    presente[mat[i][j]] = True
            if not sim: #Assim que descobrir que não é mais uma solução válida posso dar um break
                break
    
    if sim:
        #Testo cada quadrado pequeno
        for o in range(0,3):
            for p in range(0,3):
                for x in range(1,10): #Marco inicialmente todos os valores de 1 até 9 como não presentes
                    presente[x] = False
                
                for i in range(o*3,(o+1)*3): #Percorro apenas as casas que estão dentro do quadrado 3x3 iniciado na linha o e coluna p
                    for j in range(p*3,(p+1)*3):
                        if presente[mat[i][j]]: #Se o valor atual já está presente, então é porque ele apareceu antes, assim já não é um sudoku válido
                            sim = False
                            break
                        else: #Caso contrário, digo que o valor atual está presente
                            presente[mat[i][j]] = True  
                    if not sim:
                        break
                if not sim:
                    break
            if not sim:
                break        
    
    print("Instancia %d" % (k))
    if sim:
        print("SIM")
    else:
        print("NAO")
    print()
