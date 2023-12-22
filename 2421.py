a, l = input().split()
a1, l1 = input().split()
a2, l2 = input().split()

a = int(a)
l = int(l)
a1 = int(a1)
l1 = int(l1)
a2 = int(a2)
l2 = int(l2)

if (a1 + a2 <= a and l1 <= l and l2 <= l) or (l1 + l2 <= a and a1 <= l and a2 <= l) or (a1 + l2 <= a and l1 <= l and a2 <= l) or (a2 + l1 <= a and l2 <= l and a2 <= l) or (a1 + a2 <= l and l1 <= a and l2 <= a) or (l1 + l2 <= l and a1 <= a and a2 <= a) or (a1 + l2 <= l and l1 <= a and a2 <= a) or (a2 + l1 <= l and l2 <= a and a1 <= a):
    print("S")
else:
    print("N")
