salario_bruto = float(input())
dependentes = int(input())
desconto_dependentes = 137.99 * dependentes
inss = 264 ## inss se for acima de 2400, para economizar um else
aliquota = 0.275 ## aliquota no caso de salario_bruto se maior que 2743.25
deducao = 548.82 ## dedução no caso de salario_bruto se maior que 2743.25

if salario_bruto <= 720:
    inss = salario_bruto * 0.0765
elif salario_bruto <= 1200:
    inss = salario_bruto * 0.09
elif salario_bruto <= 2400:
    inss = salario_bruto * 0.11

if salario_bruto <= 1372.82:
    aliquota = 0
    deducao = 0
elif salario_bruto <= 2743.25:
    aliquota = 0.15
    deducao = 205.92

irrf = (salario_bruto - desconto_dependentes - inss) * aliquota - deducao

print(f"{irrf:.2f}")