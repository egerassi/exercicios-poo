mediaTodos = ""

for i in range(12):
    mes = [int(w) for w in input().split()]
    mediaMes = sum(mes)/len(mes)
    mediaTodos +=f"{mediaMes:.2f} "

print(mediaTodos)