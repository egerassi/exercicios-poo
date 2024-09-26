# Leitura das regras
regras = []
while True:
    regra_completa = input()
    if regra_completa != "0 0":
        passo, regra, categoria, ordem = regra_completa.split(" ", 4)
    else:
        break
    ordem = ordem.split(";")
    regras.append((int(passo), int(regra), categoria, set(ordem)))

# Leitura das vagas por categoria
vagas = {}
d = 0
while True:
    vaga = input()
    if len(vaga) == 2:
        d = int(vaga)
        break
    categoria, quantidade = vaga.split()
    vagas[categoria] = int(quantidade)

# Leitura dos candidatos
candidatos = []
for i in range(d):
    candidato = input()
    ordem, inscricao, categorias = candidato.split(" ", 2)
    categorias = categorias.split(",")
    candidatos.append((int(ordem), int(inscricao), set(categorias)))

# Verificar aprovados
