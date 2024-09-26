area_pintada = int(input())

galoes = area_pintada/64.8

if galoes <= 0:

    galoes_arredondado = 0

elif galoes < 1:
    galoes_arredondado = 1

else:
    galoes_arredondado = round(galoes,0)


preco = galoes_arredondado * 25

print(f"- área de cobertura: {area_pintada:.0f}")
print(f"- número de galões: {galoes_arredondado:.0f}")
print(f"- valor a ser pago: R$ {preco:.2f}")