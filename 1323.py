total = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(1, n+1):
            total = total + (i*i)

    print("%i" % total)
    total = 0
