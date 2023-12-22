while True:
    n = int(input())
    if n == 0:
        break
    v = input().split()
    maria = 0
    joao = 0
    for i in range(0, n):
        v[i] = int(v[i])
        if v[i] == 0:
            maria += 1
        else:
            joao += 1
    print("Mary won %i times and John won %i times" % (maria, joao))
