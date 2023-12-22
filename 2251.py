t = 1
while True:
    n = int(input())
    
    if n == 0:
        break
    
    print("Teste %d" % (t))
    print("%d" % (2**n -1))
    print()
    t += 1
