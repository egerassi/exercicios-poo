n = int(input())

soma = 1

for i in range(n):
    soma *= float(input())

print(soma**(1/n))