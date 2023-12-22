# recebo o nuemro e converto ele para uma lista, defino a variavel masorte como falsa
n = input()
n = list(n)
masorte = False

# percorro a lista procurando se existe um 1 seguido por um 3, se isso ocorrer a varivel masorte torna-se verdadeira
for i in range(len(n)):
    if n[i] == '1':
        if i < (len(n) - 1):
            if n[i + 1] == '3' and i < (len(n) - 1):
                masorte = True

# converto n para string de volta pra imprimir ele
n = ''.join(n)

# Se masorte for verdadeiro, imprime que o numero é de má sorte, se nao imprime que ele nao é de má sorte
if masorte:
    print("%s es de Mala Suerte" % n)
else:
    print("%s NO es de Mala Suerte" % n)
