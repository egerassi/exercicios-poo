capital = float(input())
n = int(input())
i = float(input())

taxa = 1 + (i/100)

montante = capital * ((taxa)**n)

round(montante, 2)

print(f"{montante:.2f}")