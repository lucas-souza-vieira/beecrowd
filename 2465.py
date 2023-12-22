n = int(input())

#Crio essa matriz para armazenar o número da camisa
mat = [0] * n 
for i in range(n):
    mat[i] = [0] * n

#Crio essa matriz para armazenar se a bandeira está levantada ou não    
alta = [0] * n
for i in range(n):
    alta[i] = [0] * n

#Leio o aluno inicial
i,j = input().split()
i = int(i) -1 #Ajusto para poder trabalhar com a matriz iniciando em 0 e não em 1
j = int(j) -1

#Leio cada fileira de alunos
for k in range(n):
    mat[k] = input().split()
    for l in range(n):
        mat[k][l] = int(mat[k][l])
        alta[k][l] = False #Marco os alunos como não tendo bandeira levantada

somaAltas = 1 #Sempre algum aluno inicia com a bolinha, então posso dizer que ao menos 1 possui bandeira levantada
alta[i][j] = True #Marco o aluno inicial com bandeira levantada
novosAlunos = [] #Crio uma lista vazia
novosAlunos.append((i,j)) #Adiciono o aluno (i,j) na lista

while novosAlunos != []: #Enquanto tivermos alunos para analisar, fazemos o que segue abaixo:
    (k,l) = novosAlunos.pop(0) #Retiro um aluno da lista
    
    #Descubro abaixo cada um de seus vizinhos
    
    vizinhoK = k-1 #Vizinho acima
    vizinhoL = l
    if vizinhoK >= 0 and alta[vizinhoK][vizinhoL] == False and mat[k][l] <= mat[vizinhoK][vizinhoL]: #Só entrego a bolinha para esse vizinho caso a camisa dele for maior ou igual ao aluno (k,l) e também se ele ainda não possui bandeira levantada
        alta[vizinhoK][vizinhoL] = True #Marco esse vizinho com bandeira levantada
        novosAlunos.append((vizinhoK, vizinhoL)) #Adiciono ele na lista para verificar seus vizinhos
        somaAltas += 1 #Somo mais uma bandeira levantada

    vizinhoK = k+1 #Vizinho abaixo
    vizinhoL = l
    if vizinhoK < n and alta[vizinhoK][vizinhoL] == False and mat[k][l] <= mat[vizinhoK][vizinhoL]: #É o mesmo caso acima
        alta[vizinhoK][vizinhoL] = True
        novosAlunos.append((vizinhoK, vizinhoL))
        somaAltas += 1
        
    vizinhoK = k #Vizinho esquerdo
    vizinhoL = l-1
    if vizinhoL >= 0 and alta[vizinhoK][vizinhoL] == False and mat[k][l] <= mat[vizinhoK][vizinhoL]: #É o mesmo caso acima
        alta[vizinhoK][vizinhoL] = True
        novosAlunos.append((vizinhoK, vizinhoL))
        somaAltas += 1
        
    vizinhoK = k #Vizinho direito
    vizinhoL = l+1
    if vizinhoL < n and alta[vizinhoK][vizinhoL] == False and mat[k][l] <= mat[vizinhoK][vizinhoL]: #É o mesmo caso acima
        alta[vizinhoK][vizinhoL] = True
        novosAlunos.append((vizinhoK, vizinhoL))
        somaAltas += 1

print(somaAltas) #Imprimo a resposta

