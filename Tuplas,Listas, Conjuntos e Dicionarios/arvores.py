n_casos = int(input())

for i in range(n_casos):

    arvore_qtd = {}
    userInput = input()
    
    while userInput:
        if not userInput in arvore_qtd:
            arvore_qtd[userInput] = 1
        else:
            arvore_qtd[userInput] += 1
        userInput = input()

    total_arvores = sum(arvore_qtd.values())
    sortedArvoreQtd = sorted(arvore_qtd)

    for arvore in sortedArvoreQtd:
        print(f"{arvore} {(arvore_qtd[arvore]/total_arvores):.4f}")