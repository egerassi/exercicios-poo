gabarito = input()
prova = input()

acertos = 0

for i in range(len(gabarito)):
    if gabarito[i] == prova[i]:
        acertos += 1

print(acertos)