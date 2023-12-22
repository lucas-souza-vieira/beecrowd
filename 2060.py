n = int(input())

v = [int(x) for x in input().split()]

dois = 0
tres = 0
quatro = 0
cinco = 0

for i in range(n):
    if v[i] % 2 == 0:
        dois += 1
    if v[i] % 3 == 0:
        tres += 1
    if v[i] % 4 == 0:
        quatro += 1
    if v[i] % 5 == 0:
        cinco += 1

print("%i Multiplo(s) de 2" % dois)
print("%i Multiplo(s) de 3" % tres)
print("%i Multiplo(s) de 4" % quatro)
print("%i Multiplo(s) de 5" % cinco)
