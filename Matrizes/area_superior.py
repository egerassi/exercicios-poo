op = input()

matriz = [[float(input()) for l in range(12)] for c in range(12)]

topslice = 11
soma = 0
divisor = (2+10)*5/2

for i in range(5):
    soma += sum(matriz[i][i+1:topslice])
    topslice -= 1

print(f"{soma}" if op == "S" else f"{round(soma/divisor,1)}")