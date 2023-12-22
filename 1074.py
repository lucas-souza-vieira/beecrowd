n = int(input())

for i in range(0, n):
    a = int(input())

    if a == 0:
        print("NULL")
    elif a % 2 == 0 and a > 0:
        print("EVEN POSITIVE")
    elif a % 2 == 0 and a < 0:
        print("EVEN NEGATIVE")
    elif a % 2 == 1 and a > 0:
        print("ODD POSITIVE")
    elif a % 2 == 1 and a < 0:
        print("ODD NEGATIVE")
