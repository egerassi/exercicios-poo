a, b = [int(w) for w in input().split()]

resultado = "Nao sao Multiplos"

if b % a == 0 or a % b == 0:
    resultado = "Sao Multiplos"

print(resultado)