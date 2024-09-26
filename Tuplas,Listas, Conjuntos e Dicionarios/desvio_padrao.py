from math import sqrt

qtd = int(input())

numeros = []
somatorio = 0

for i in range(qtd):
    n = float(input())
    numeros.append(n)

media = sum(numeros)/qtd

for i in range(qtd):
    somatorio += (numeros[i] - media)**2

desvio_padrao = sqrt(somatorio/(qtd-1))

print(desvio_padrao)