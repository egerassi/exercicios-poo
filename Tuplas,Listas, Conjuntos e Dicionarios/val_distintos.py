numeros = []

for i in range(4):
    
    n = int(input())

    if n not in numeros:
        numeros.append(n)

print(len(numeros))