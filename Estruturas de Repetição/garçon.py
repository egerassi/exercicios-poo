bandejas = int(input())
derrubou = 0

for bandeja in range(bandejas):
    latas, copos = [int(w) for w in input().split()]
    if latas > copos:
        derrubou += copos

print(derrubou)