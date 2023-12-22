n = int(input())

for i in range(n):
    palavra = input()
    traduzido = ""
    for x in range(len(palavra) - 1, -1, -1):
        if palavra[x].islower():
            traduzido += palavra[x]
    print(traduzido)
