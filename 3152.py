# leio os pontos de cada vertice

x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
x3, y3 = [int(x) for x in input().split()]
x4, y4 = [int(x) for x in input().split()]

x5, y5 = [int(x) for x in input().split()]
x6, y6 = [int(x) for x in input().split()]
x7, y7 = [int(x) for x in input().split()]
x8, y8 = [int(x) for x in input().split()]

# Calculo a area pelo formula do determinante
area1 = 0.5 * abs((x1*y2 + x2*y3 + x3*y4 + x4*y1) -
                  (y1*x2 + y2*x3 + y3*x4 + y4*x1))

area2 = 0.5 * abs((x5*y6 + x6*y7 + x7*y8 + x8*y5) -
                  (y5*x6 + y6*x7 + y7*x8 + y8*x5))

# Printo o maior resultado
if area1 > area2:
    print("terreno A")
elif area2 >= area1:
    print("terreno B")
