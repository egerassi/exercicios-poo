qtd_postos, limite = [int(w) for w in input().split()]
dist_postos = [int(w) for w in input().split()]

consegue = "S"

for i in range(qtd_postos-1):
    if dist_postos[i+1] - dist_postos[i] > limite:
        consegue = "N"
        break

print(consegue)