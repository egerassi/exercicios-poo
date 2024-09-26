qtd_calouros = int(input())

calouros = []
doadores = []
calouros_doadores = []

for i in range(qtd_calouros):
    calouros.append(input())

qtd_doadores = int(input())

for i in range(qtd_doadores):
    doadores.append(input())

for nome in calouros:
    if nome in doadores:
        calouros_doadores.append(nome)

print(len(calouros_doadores)/len(calouros))