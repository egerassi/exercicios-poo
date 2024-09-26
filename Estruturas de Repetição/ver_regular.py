n = int(input())

regular = False
divisor = 2
divisores = []

while n > 1:
    if n % divisor == 0:
        divisores.append(divisor)
        n /= divisor
    else:
        divisor += 1

for numero in divisores:
    if numero != 2 and divisor != 3 and divisor != 5:
        continue
    else:
        regular = True

print(regular)