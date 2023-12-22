n = int(input())
v = input().split()

fav = 0
des = 0

for i in range(0, len(v)):
    v[i] = int(v[i])
    if v[i] == 0:
        fav += 1
    else:
        des += 1

if fav > des:
    print("Y")
else:
    print("N")
