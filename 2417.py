cv, ce, cs, fv, fe, fs = input().split()

cv = int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)

pc = (cv * 3) + (ce * 1)
pf = (fv * 3) + (fe * 1)

if pc > pf:
    print("C")
elif pf > pc:
    print("F")
elif pc == pf:
    if cs > fs:
        print("C")
    elif fs > cs:
        print("F")
    elif fs == cs:
        print("=")
