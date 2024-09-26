nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3
conceito = ''

if media < 6:
    conceito = 'Insuficiente'
elif media < 7.5:
    conceito = 'Satisfatório'
elif media < 9:
    conceito = 'Bom'
elif media <= 10:
    conceito = 'Ótimo'

print(conceito)