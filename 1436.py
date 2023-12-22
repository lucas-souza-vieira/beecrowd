# Leio a entrada
n = int(input())

# Faço a quantidade de casos teste necessaria
for i in range(n):
    # Ja leio cada entrada e transformo em inteiro
    v = [int(x) for x in input().split()]
    # Ordeno o vetor
    v.sort()
    # Printo o numero do caso e o numero do meio do vetor
    print("Case %i: %i" % ((i+1, v[len(v)//2])))