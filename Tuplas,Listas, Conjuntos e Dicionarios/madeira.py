n_casos = int(input())
input()

for i in range(n_casos):

    arvore_qtd = {}
    
    try:
        userInput = input()
        while userInput != '':
            arvore_qtd[userInput] = arvore_qtd.get(userInput, 0) + 1
            userInput = input()
    except:
        print()

    total_arvores = sum(arvore_qtd.values())
    sortedArvoreQtd = sorted(arvore_qtd.keys())

    for arvore in sortedArvoreQtd:
        print(f"{arvore} {((arvore_qtd[arvore]/total_arvores)*100):.4f}")