valor = float(input())
sexo = str(input())
idade = int(input())

seguro = valor * 0.1

if sexo == "M":
    if idade >= 25 and idade <= 33:
        seguro *= 0.9
    elif idade > 33:
        seguro *= 0.8

if sexo == "F":
    if idade <= 24:
        seguro *= 0.95
    elif idade >= 25 and idade <= 33:
        seguro *= 0.8
    elif idade > 33:
        seguro *= 0.65

print(f"{seguro:.2f}")