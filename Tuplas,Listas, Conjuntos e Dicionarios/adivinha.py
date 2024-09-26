from math import inf

num_casos = int(input())

for caso in range(num_casos):
    qtd_alunos, num_magico = [int(w) for w in input().split()]
    adivinhacoes = [int(w) for w in input().split()]
    mais_perto = inf

    for numero in range(qtd_alunos):
        if adivinhacoes[numero] == num_magico:
            vencedor = numero + 1
            break
        else:
            if abs(adivinhacoes[numero] - num_magico) < mais_perto:
                mais_perto = abs(adivinhacoes[numero] - num_magico)
                vencedor = numero + 1
    print(vencedor)