qtd1 = int(input())

nomes1 = []
nomes2 = []

for nome in range(qtd1):
    nome = input()
    nomes1.append(nome)

qtd2 = int(input())

for nome in range(qtd2):
    nome = input()
    nomes1.append(nome)

for nome in sorted(nomes1):
    print(nome)