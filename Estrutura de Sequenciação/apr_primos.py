import math

n = int(input())

log_n = math.log(n)

minimo = n / log_n

maximo = 1.25506* minimo

print(f"{minimo:.1f}")

print(f"{maximo:.1f}")