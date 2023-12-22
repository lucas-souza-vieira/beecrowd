x0, y0, s = [int(x) for x in input().split()]
forca1 = 0
forca2 = 0
m = y0/x0

for i in range(s):
    x, y, h = [int(x) for x in input().split()]
    if y > m*x:
        forca1 += h
    else:
        forca2 += h


print("%i %i" % (forca1, forca2))
