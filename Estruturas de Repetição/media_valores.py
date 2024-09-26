quantidade = int(input())

soma = 0

for valor in range(quantidade):
    valor = float(input())
    soma += valor

media = soma/quantidade

print(media)