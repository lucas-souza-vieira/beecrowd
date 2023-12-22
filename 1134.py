al = 0
ga = 0
di = 0
n = int(input())
while True:
    if n == 4:
        break
    elif n == 1:
        al += 1
        n = int(input())
    elif n == 2:
        ga += 1
        n = int(input())
    elif n == 3:
        di += 1
        n = int(input())
    elif n > 4 or n < 1:
        n = int(input())
print("MUITO OBRIGADO")
print("Alcool: %i" % al)
print("Gasolina: %i" % ga)
print("Diesel: %i" % di)
