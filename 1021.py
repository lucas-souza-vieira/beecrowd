valor = float(input())

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0

while valor >= 100:
    valor = valor - 100
    a = a + 1
while valor >= 50:
    valor = valor - 50
    b = b + 1
while valor >= 20:
    valor = valor - 20
    c = c + 1
while valor >= 10:
    valor = valor - 10
    d = d + 1
while valor >= 5:
    valor = valor - 5
    e = e + 1
while valor >= 2:
    valor = valor - 2
    f = f + 1
while valor >= 1:
    valor = valor - 1
    g = g + 1
while valor >= 0.5:
    valor = valor - 0.5
    h = h + 1
while valor >= 0.25:
    valor = valor - 0.25
    i = i + 1
while valor >= 0.1:
    valor = valor - 0.1
    j = j + 1
while valor >= 0.05:
    valor = valor - 0.05
    k = k + 1
while valor > 0:
    valor = valor - 0.01
    l = l + 1

print("NOTAS:")
print("%i nota(s) de R$ 100.00" % a)
print("%i nota(s) de R$ 50.00" % b)
print("%i nota(s) de R$ 20.00" % c)
print("%i nota(s) de R$ 10.00" % d)
print("%i nota(s) de R$ 5.00" % e)
print("%i nota(s) de R$ 2.00" % f)
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" % g)
print("%i moeda(s) de R$ 0.50" % h)
print("%i moeda(s) de R$ 0.25" % i)
print("%i moeda(s) de R$ 0.10" % j)
print("%i moeda(s) de R$ 0.05" % k)
print("%i moeda(s) de R$ 0.01" % l)
