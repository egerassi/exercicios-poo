linhaIn = int(input())

operacao = input()

matriz = []
soma = 0

matriz = [[float(input()) for a in range(12)] for b in range(12)]

for e in range(12):
    soma += matriz[linhaIn][e]

if operacao == 'S':
    print(f"{soma:.1f}")
else:
    print(f"{soma/12:.1f}")