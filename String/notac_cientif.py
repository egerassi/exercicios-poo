from math import fabs

n = float(input())

expoente = 0
sinal = '+' if n >= 0 else '-'
sinal_expoente = '-' if -1 < n < 0 or 0 < n < 1 else '+'

while n >= 10 or n <= -10:
    n /= 10
    expoente += 1

while  -1 < n < 0 or 0 < n < 1:
    n *= 10
    expoente -= 1

if -10 < expoente < 10:
    expoente = '0'+str(int(fabs(expoente)))

n = round(n,4)

print(f"{sinal}{abs(n):.4f}E{sinal_expoente}{expoente}")