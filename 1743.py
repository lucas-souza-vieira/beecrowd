n = input().split()
m = input().split()
aux = 0

for i in range(0, len(n)):
    n[i] = int(n[i])
    m[i] = int(m[i])
    if n[i] != m[i]:
        aux += 0
    elif n[i] == m[i]:
        aux += 1

if aux != 0:
    print("N")
else:
    print("Y")
