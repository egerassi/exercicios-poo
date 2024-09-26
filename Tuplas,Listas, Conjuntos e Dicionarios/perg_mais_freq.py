from collections import Counter

tupla = (1,1,2,3,4,5)

tupla = Counter(tupla)

mais_frequente = tupla.most_common(1)

print(min(min(mais_frequente)))