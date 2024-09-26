tempo_segundos = int(input())

horas = int(tempo_segundos/3600)
minutos = int(tempo_segundos/60) - (60*int(horas))
segundos = tempo_segundos - (3600*int(horas)) - (60*int(minutos))

print(f"{horas}:{minutos}:{segundos}")