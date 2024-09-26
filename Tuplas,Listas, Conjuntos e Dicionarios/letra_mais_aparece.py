from collections import Counter

frase = input()

frase = frase.lower()

contagem_frase = Counter(car for car in frase if car.isalpha())

mais_repete = contagem_frase.most_common(1)

for i in mais_repete:
    print(i[0])