nome = input()
salario = float(input())
vendas = float(input())

bonus = vendas*0.15
salario_bonus = salario + bonus

print("TOTAL = R$ %.2f" % salario_bonus)
