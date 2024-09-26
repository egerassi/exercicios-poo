limite, qtd = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]

venceu = True

for i in range(1,qtd):
    if abs(alturas[i] - alturas[i-1]) > limite:
        venceu = False
        print("GAME OVER")
        break

if venceu:
    print("YOU WIN")