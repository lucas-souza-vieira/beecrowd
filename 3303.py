# Recebo a string e converto para lista
palavra = input()
palavra = list(palavra)

# Se a lista tiver mais que 9 elementos ira retornar palavrão, se nao retorna palavrinha
if len(palavra) > 9:
    print("palavrao")
else:
    print("palavrinha")
