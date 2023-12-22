a = 0
for i in range(100):
    v = int(input())
    if v > a:
        aux = i + 1
        a = v
print("%i" % a)
print("%i" % aux)
