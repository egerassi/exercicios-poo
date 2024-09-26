n = int(input())

numeros = {}
index = 1

for i in range(n):
    numeros[index] = int(input())
    index += 1

for chave,valor in numeros.items():
    v1 = valor


print(numeros)
print(max(numeros))
