def comparar(a, b):
    if (abs(a-b) < 0.0000001):
        return 0
    if a > b:
         return 1
    return -1

while True:
    x = input().strip()
    if x == '*':
        break

    dicionario = {"W" : 1,
                  "H" : 1/2,
                  "Q" : 1/4,
                  "E" : 1/8,
                  "S" : 1/16,
                  "T" : 1/32,
                  "X" : 1/64} 
    total = 0
    aux = 0
    for i in range(len(x)):
        if x[i] != "/":
            total += dicionario[x[i]]
        else:
            if comparar(total, 1) == 0:
                aux += 1
                total = 0
            else:
                total = 0
    print(aux)
    


