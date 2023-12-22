# leitura da quantidade de individous de cada exercito
h, e, a, o, w, x = input().split()
h = int(h)
e = int(e)
a = int(a)
o = int(o)
w = int(w)
x = int(x)

# Soma da quantidade de total do exercito do bem e do mal
bem = h + e + a + x
mal = o + w

# Condicional para imprimir se o valor da variavel bem é maior ou igual a variavel mal e imprimir o resultado da batalha
if bem >= mal:
    print("Middle-earth is safe.")
else:
    print("Sauron has returned.")
