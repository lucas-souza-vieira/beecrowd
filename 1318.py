while True:
    n, m = input().split()
    m = int(m)
    n = int(n)
    repetido = 0
    
    if n == 0 and m == 0:
        break
    v = input().split()

    for i in range(m):
        v[i] = int(v[i])

    for i in range(1, n + 1):
        if i in v:
            v.remove(i)
            if i in v:
                v.remove(i)
                repetido += 1
    print(repetido)
