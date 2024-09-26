nome_separado = input().split(' ')

nome_abreviado = nome_separado[0] + ' '

for nome in nome_separado[1:-1]:
    if len(nome) > 3:
        nome_abreviado += nome[0] + '. '
    else:
        nome_abreviado += nome + ' '

nome_abreviado += nome_separado[-1]

print(nome_abreviado)
