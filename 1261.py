n_palavras, n_descricao = [int(x) for x in input().split()]
d = {}


for i in range(n_palavras):
    palavra, valor = input().split()
    valor = int(valor)
    d[palavra] = valor



for j in range(n_descricao):
    total = 0
    
    while True:
        texto = input().split()
        if texto[0] == '.':
            break
        else:
            for palavra in texto:
                if palavra in d:
                    total += d[palavra]
    print(total)

        
        

