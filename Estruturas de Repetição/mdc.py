n1 = int(input())
n2 = int(input())

resto = 1
dividendo = n1
divisor = n2

while resto != 0:
    resto = dividendo % divisor
    dividendo = divisor
    divisor = resto

print(dividendo)