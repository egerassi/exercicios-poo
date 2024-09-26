consumo = int(input())

if consumo < 31:
    preco = consumo * 0.09556

if consumo >= 31 and consumo < 101:
    preco = 30 * 0.09556 + (consumo - 30) * 0.16698

if consumo >= 101 and consumo < 201:
    preco = 30 * 0.09556 + (70 * 0.16698) + ((consumo - 100) * 0.25052)

if consumo >= 201:
    preco = 30 * 0.09556 + (70 * 0.16698) + (100 * 0.25052) + ((consumo - 200) * 0.27836)

print(round(preco,2))