salario_atual = float(input())
salario_minimo = float(input())

salario_ajustado = 0

if salario_atual <= salario_minimo * 1.5:
    salario_ajustado = salario_minimo * 1.5
elif salario_atual <= salario_minimo * 3:
    salario_ajustado = salario_atual * 1.2
elif salario_atual <= salario_minimo * 5:
    salario_ajustado = salario_atual * 1.15
else:
    salario_ajustado = salario_atual * 1.10

if salario_ajustado > salario_minimo * 20:
    salario_ajustado = salario_minimo * 20

print(salario_ajustado)