while True: 
    try:
        n = int(input())

        d = { "EHD" : 1,
            "EPR" : 2,
            }
        EHD = 0
        EPR = 0
        intrusos = 0

        for i in range(n):
            e = input().split()
            if e[1] == "EHD":
                EHD += 1
            elif e[1] == "EPR":
                EPR += 1
            else:
                intrusos += 1

        print("EPR: %i" % EPR)
        print("EHD: %i" % EHD)
        print("INTRUSOS: %i" % intrusos)
    except EOFError:
        break