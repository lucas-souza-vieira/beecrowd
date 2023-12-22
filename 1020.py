dias = int(input())

if (dias >= 365):
    anos = dias//365
    dias = dias % 365
else:
    anos = 0

if (dias >= 30):
    meses = dias//30
    dias = dias % 30
else:
    meses = 0

if (dias > 0):
    dias = dias
else:
    dias = 0

print("%i ano(s)" % anos)
print("%i mes(es)" % meses)
print("%i dia(s)" % dias)
