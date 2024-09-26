nota1 = str(input())
nota2 = str(input())
nota3 = str(input())
nota4 = str(input())

notas = [nota1,nota2,nota3,nota4]
soma = 0
aprovação = False

for nota in notas:
    if nota == 'A':
        soma += 4
    elif nota == 'B':
        soma += 3
    elif nota == 'C':
        soma += 2

if soma / 4 >= 3 and not 'E' in notas:
    aprovação = True

print(aprovação)