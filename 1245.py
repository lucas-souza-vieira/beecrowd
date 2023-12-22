while True:
    try:
        n = int(input())
        
        direito = [0]*61
        esquerdo = [0]*61

        for i in range(n):
            t, p = input().split()

            if p == 'D':
                direito[int(t)] += 1
            else:
                esquerdo[int(t)] += 1

        total = 0
        for i in range(30, 61):
            if direito[i] < esquerdo[i]:
                total += direito[i]
            else:
                total += esquerdo[i]

        print(total)

    except EOFError:
        break
