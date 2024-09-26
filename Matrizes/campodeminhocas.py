linhas, colunas = [int(w) for w in input().split()]

matriz = [[int(w) for w in input().split()] for i in range(linhas)]

maiorSoma = sum(matriz[0])

for i in range(1,linhas):
    if sum(matriz[i]) > maiorSoma:
        maiorSoma = sum(matriz[i])
        
for c in range(colunas):
    soma = 0
    for l in range(linhas):
        soma += matriz[l][c]
    if soma > maiorSoma:
        maiorSoma = soma

print(maiorSoma)