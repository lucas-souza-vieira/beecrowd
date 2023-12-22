p, n = input().split()
v = input().split()

for i in range(0, len(v)):
    v[i] = int(v[i])
p = int(p)
n = int(n)
win = 0

for i in range(1, len(v)):
    if abs(v[i] - v[i - 1]) <= p:
        win += 0
    else:
        win += 1

if win != 0:
    print("GAME OVER")
else:
    print("YOU WIN")
