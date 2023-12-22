a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

while True:
    try:
        if (a == b == c):
            print("*")
        elif (a == b):
            print("C")
        elif (a == c):
            print("B")
        elif (b == c):
            print("A")
        a, b, c = input().split()
    except EOFError:
        break
