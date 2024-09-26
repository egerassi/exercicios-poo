regras = [] #Input total das regras
vagas = {} # Vagas vinculadas a quantidade
matriculas = [] # Matriculas no formato POS / NUMERO DE MATRICULA / OPCOES DE VAGAS
aprovados = [] # Lista de aprovados, somente o numero de matricula

#Inputs das regras
while True:
    regras_categorias = input().split()
    if not "0" in regras_categorias:        
       regras_categorias[-1] = regras_categorias[-1].split(";")
    else:
        break
    
    for i in range(len(regras_categorias[-1])):
        regras_categorias[-1][i] = set(regras_categorias[-1][i].split(","))

    regras.append(regras_categorias)

#Inputs das quantidades de vagas
while True:
    categoria_qtd = input()

    if not categoria_qtd[0].isnumeric():
        categoria_qtd = categoria_qtd.split()
        vagas[categoria_qtd[0]] = int(categoria_qtd[1])
    else:
        qtd_matriculas = int(categoria_qtd)
        break

#Inputs das matriculas
for i in range(qtd_matriculas):
    matricula = input().split()
    matriculas.append(matricula)
    matriculas[i][-1] = [set(matriculas[i][-1].split(","))]

def removeMatriculas():
    for numero in aprovados:
        for num in matriculas:
            if str(numero) == num[1]:
                matriculas.remove(num)
                break

#regra 1
for regra in regras:
    for candidato in matriculas:
        if vagas[regra[2]] == 0:
            break
        else:
            for conjunto in candidato[2]:
                for i, regraconj in enumerate(regra[-1]):
                    if conjunto & regraconj:
                        vagas[regra[2]] -= 1
                        aprovados.append(int(candidato[1]))
                        break
    removeMatriculas()

for matricula in sorted(aprovados):
    print(matricula)