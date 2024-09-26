cpf = input()

cpf_limpo = ''
peso_dv = 9
soma_primeiro_dv = 0

for char in cpf:
    if char.isnumeric():
        cpf_limpo += char

for num in cpf_limpo[-3::-1]:
    soma_primeiro_dv += peso_dv * int(num)
    peso_dv -= 1

primeiro_dv = (soma_primeiro_dv % 11) if soma_primeiro_dv % 11 != 10 else 0

soma_segundo_dv = primeiro_dv * 9
peso_dv = 8

for num in cpf_limpo[-3::-1]:
    soma_segundo_dv += peso_dv * int(num)
    peso_dv -= 1

segundo_dv = (soma_segundo_dv % 11) if soma_segundo_dv % 11 != 10 else 0

verificado = True if len(cpf_limpo) == 11 and primeiro_dv == int(cpf_limpo[-2]) and segundo_dv == int(cpf_limpo[-1]) and all(digito == cpf_limpo[0] for digito in cpf_limpo) == False else False

print(verificado)