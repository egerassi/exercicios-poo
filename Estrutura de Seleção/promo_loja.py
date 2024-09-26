preco = float(input())

if preco < 500:
    preco_descontado = preco * 0.8
elif preco < 1000:
    preco_descontado = preco * 0.7
else:
    preco_descontado = 700 + 0.55 * (preco - 1000)

print(f"{preco_descontado:.2f}")