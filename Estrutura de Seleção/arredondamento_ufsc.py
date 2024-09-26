nota = float(input())

nota_inteira = int(nota)

nota_diminuida = nota - nota_inteira

if nota_diminuida < 0.25:
    nota_final = nota_inteira
elif nota_diminuida < 0.75:
    nota_final = nota_inteira + 0.5
elif nota_diminuida < 1:
    nota_final = nota_inteira + 1

print(nota_final)