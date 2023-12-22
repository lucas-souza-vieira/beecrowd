while True:
    try:
        l, c = [int(x) for x in input().split()]

        m = ['a']*(l+2)
        for i in range(l+2):
            m[i] = ['a']*(c+2)

        for i in range(1, l+1):
            m[i] = input().split()
            m[i].append('a')
            m[i].insert(0, 'a')

        for i in range(1, l+1):
            vizinhos = 0
            for j in range(1, c+1):
                if m[i][j] == '1':
                    vizinhos = 0
                    print(9, end="")
                else:
                    vizinhos = 0
                    if m[i+1][j] == '1':
                        vizinhos += 1
                    if m[i-1][j] == '1':
                        vizinhos += 1
                    if m[i][j+1] == '1':
                        vizinhos += 1
                    if m[i][j-1] == '1':
                        vizinhos += 1
                    print("%i" % vizinhos, end="")
            print("")

    except EOFError:
        break
