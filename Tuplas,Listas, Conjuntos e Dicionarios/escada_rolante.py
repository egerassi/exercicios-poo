from math import inf
quant_pessoas = int(input())

while quant_pessoas != 0:
    t = [int(w) for w in input().split()]
    t.append(inf)
    tempo_ativo = 0

    for i in range(quant_pessoas):
        if t[i+1] - t[i] >= 10:
            tempo_ativo += 10
        else:
            tempo_ativo += t[i+1] - t[i]
    
    print(tempo_ativo)
    quant_pessoas = int(input())