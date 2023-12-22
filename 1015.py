import math

x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("%.4f" % distancia)
