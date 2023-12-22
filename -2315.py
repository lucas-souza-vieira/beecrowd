d1, m1 = input().split()
d2, m2 = input().split()

d1 = int(d1)
d2 = int(d2)
m1 = int(m1)
m2 = int(m2)

 
    
aux1 = 30 - d1
aux2 = (m2 - m1 - 1)*30
soma = aux1 + aux2 + d2

print("%i" % soma)
