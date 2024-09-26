q = int(input())

numeros = []

for i in range(q):
    numeros.append(int(input()))

numeros.remove(min(numeros))

print(min(numeros))