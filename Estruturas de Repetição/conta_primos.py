from math import sqrt

from eh_primo import verificaPrimo

inicio_interv = int(input())
fim_interv = int(input())
count = 0

for i in range(inicio_interv,fim_interv + 1):
    if verificaPrimo(i):
        count +=1

print(count)