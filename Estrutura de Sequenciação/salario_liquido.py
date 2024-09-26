horas_normais = int(input())
horas_extras = int(input())

salario_bruto = 12.5 * horas_normais + 15 * horas_extras

inss = salario_bruto * 0.09
ir = salario_bruto * 0.13

salario_liquido = salario_bruto - inss - ir

round(salario_bruto,2)
round(inss,2)
round(ir,2)
round(salario_liquido,2)

print(f"- Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (13%) : R$ {ir:.2f}")
print(f"- INSS (9%) : R$ {inss:.2f}")
print(f"- Salário Líquido : R$ {salario_liquido:.2f}")