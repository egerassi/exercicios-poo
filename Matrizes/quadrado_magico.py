dim = int(input())

matriz = []
#cria a matriz
for i in range(dim):
    matriz.append([int(w) for w in input().split()])

resultado = True

while True:
    valor_magico = sum(matriz[0][0:dim])

#Soma as linhas, da segunda pra frente
    for i in range(1,dim):
        if sum(matriz[i][0:dim]) != valor_magico:
            resultado = False
            break
    if not resultado:
        break

#Soma as colunas
    for i in range(dim):
        soma = 0
        for t in range(dim):
            soma += matriz[t][i]
        
        if soma != valor_magico:
            resultado = False
            break

#Soma a diagonal principal
    soma = 0
    for i in range(dim):
        soma += matriz[i][i]

    if soma != valor_magico:
        resultado = False
        break

#Soma a diagonal secundária
    soma = 0
    cursor = dim - 1
    for i in range(dim):
        soma += matriz[i][cursor]
        cursor -= 1
    
    if soma != valor_magico:
        resultado = False
        break
    break
print(resultado)