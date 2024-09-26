n = int(input())

nota = []
quantidade = []
troco = []
troco_str = ''

for i in range(n):
    nota.append(float(input()))
    quantidade.append(int(input()))

saque = float(input())

for i in range(n-1,-1,-1):
    if saque // nota[i] <= quantidade[i]:
        troco.append(int(saque//nota[i]))
        saque %= nota[i]
    else:
        troco.append(0)

for i in range(n-1,-1,-1):
    troco_str += str(troco[i]) + ' '

print(troco_str)