n, c = input().split()
n = int(n)
c = int(c)
r = 0
total = 0

for i in range(0, n):
    s, e = input().split()
    s = int(s)
    e = int(e)
    total = total + (e - s)
    if total > c:
        r += 1
    else:
        r += 0

if r > 0:
    print("S")
else:
    print("N")
