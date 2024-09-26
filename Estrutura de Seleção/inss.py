salario = float(input())

if salario <= 720:
    inss = salario * 0.0765
elif salario <= 1200:
    inss = salario * 0.09
elif salario <= 2400:
    inss = salario * 0.11
else:
    inss = 264 ## 11% de 2400

print(f"{inss:.2f}")