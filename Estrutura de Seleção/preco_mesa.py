comprimento = float(input())
largura = float(input())
gavetas = int(input())
madeira = str(input())

superficie = comprimento * largura

if superficie > 2 :
    preco = superficie * 100 + 50
else:
    preco = superficie * 100

if madeira == "mogno":
    preco += 150
elif madeira == "carvalho":
    preco += 125

preco += gavetas * 30

if preco < 200:
    preco = 200

print(preco)