q = int(input())

praia_mais_distante, distancia1 = input().split(';')
distancia1 = int(distancia1)

praias_entre_15_e_20 = 0

soma_distancias = distancia1

if distancia1 <= 20 and distancia1 >= 15:
    praias_entre_15_e_20 += 1

for i in range(q-1):
    praia, distancia2 = input().split(';')
    distancia2 = int(distancia2)

    if distancia2 > distancia1:
        praia_mais_distante = praia
        distancia1 = distancia2

    if distancia2 <= 20 and distancia2 >= 15:
        praias_entre_15_e_20 += 1

    soma_distancias += distancia2

distancia_media = round(soma_distancias / q, 1)

print(f"{praia_mais_distante};{praias_entre_15_e_20};{distancia_media}")