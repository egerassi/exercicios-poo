operacao = input()

matriz = [[float(input()) for l in range(12)] for c in range(12)]

soma = 0
divisor = (1+11)*11/2

for i in range(1,12):
 soma += sum(matriz[i][0:i])

print(f"{soma}" if operacao == "S" else f"{round(soma/divisor,1)}")