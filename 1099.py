n = int(input())

for i in range(0, n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x <= y:
        soma = 0
        for a in range(x + 1, y):
            if a % 2 == 1:
                soma = soma + a
        print("%i" % soma)
    else:
        soma = 0
        for a in range(y + 1, x):
            if a % 2 == 1:
                soma = soma + a
        print("%i" % soma)
