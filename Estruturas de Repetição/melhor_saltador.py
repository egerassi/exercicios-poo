num_saltadores = int(input())

nome_maiorsalto= {}

for saltador in range(num_saltadores):
    salto1, salto2, salto3 , nome = [w for w in input().split()]
    maiorsalto = max(float(salto1),float(salto2),float(salto3))
    nome_maiorsalto[nome] = maiorsalto

salto_vencedor = 0
vencedor = ''

for chave,valor in nome_maiorsalto.items():
    if valor > salto_vencedor:
        salto_vencedor = valor
        vencedor = chave

print(vencedor)