n = int(input())

quociente = 1
numeros = []
binario = ''

while quociente != 0:
    resto = n % 2
    quociente = n // 2
    n = quociente
    numeros.append(resto)

for numero in reversed(numeros):
    binario += str(numero)

print(binario)