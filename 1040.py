a, b, c, d = input().split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = ((a * 2) + (b * 3) + (c * 4) + (d * 1)) / 10
print("Media: %.1f" % media)

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")

elif media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" % exame)
    media2 = (exame + media)/2
    if media2 >= 5:
        print("Aluno aprovado.")
        print("Media final: %.1f" % media2)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f" % media2)
