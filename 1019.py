segundos = int(input())

if (segundos > 3600):
    horas = segundos//3600
    segundos = segundos % 3600
else:
    horas = 0

if (segundos > 60):
    minutos = segundos//60
    segundos = segundos % 60
else:
    minutos = 0

if (segundos > 0):
    segundos = segundos
else:
    segundos = 0

print("%i:%i:%i" % (horas, minutos, segundos))
