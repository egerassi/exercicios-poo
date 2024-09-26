numJogadores, partidas = [int(w) for w in input().split()]
jogadoresQualificados = 0

for i in range(numJogadores):

    golsPorPartida = [int(w) for w in input().split()]

    if 0 in golsPorPartida:
        pass
    else:
        jogadoresQualificados += 1

print(jogadoresQualificados)