q = int(input())

praias = {}
praias_entre_15_e_20 = 0
praia_mais_distante = ''
soma_distancias = 0

for i in range(q):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    praias[praia] = distancia

for chave,valor in praias.items():
    soma_distancias += valor
    if valor >= 15 and valor <= 20:
        praias_entre_15_e_20 += 1

praia_mais_distante = max(praias, key=praias.get) ##pega o chave associada ao valor maximo
media_distancias = round(soma_distancias/q,1)

print(f"{praia_mais_distante};{praias_entre_15_e_20};{media_distancias}")