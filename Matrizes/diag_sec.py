operacao = input()

matriz = [[float(input()) for l in range(12)] for c in range(12)]

soma = 0
divisor = (1+11)*11/2
cont = 0

for i in range(11,1,-1):
 soma += sum(matriz[cont][0:i])
 cont += 1

print(f"{soma}" if operacao == "S" else f"{round(soma/divisor,1)}")