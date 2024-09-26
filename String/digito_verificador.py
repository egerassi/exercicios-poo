n = input()

peso = len(n)
soma = 0

for digit in n[:-1]:
    soma += int(digit) * peso
    peso -= 1

resto = soma % 11

dig_ver = 11 - resto if 1 < resto < 11 else 0

verificado = True if dig_ver == int(n[-1]) else False

print(verificado)