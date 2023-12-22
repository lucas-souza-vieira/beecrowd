n = int(input())
for i in range(0, n):
    a = int(input())
    b, c, d, e = input().split()
    f = int(input())
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    if a + f == 7 and b + d == 7 and c + e == 7 and a != b and a != c and a != d and a != e and b != c and b != e and b != f and c != d and c != f and a > 0 and b > 0 and c > 0 and d > 0 and e > 0 and f > 0:
        print("SIM")
    else:
        print("NAO")
