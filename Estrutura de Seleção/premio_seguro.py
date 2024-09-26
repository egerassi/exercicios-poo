valor = float(input())
classe = str(input())
nac_ou_imp = str(input())
idade = int(input())

premio = 0.1 * valor
desconto_idade = 0

if nac_ou_imp == 'estrangeira':
    premio = 0.15 * valor

if idade > 24:
    desconto_idade = premio * 0.1

if classe == 'A':
    premio *= 0.7
elif classe == 'B':
    premio *= 0.8
elif classe == 'C':
    premio *= 0.9
elif classe == 'D':
    premio *= 0.95

premio -= desconto_idade

print(f"{round(premio,2):.2f}")