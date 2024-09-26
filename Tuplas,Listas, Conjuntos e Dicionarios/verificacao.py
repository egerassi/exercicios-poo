conector1 = [int(w) for w in input().split()]
conector2 = [int(w) for w in input().split()]

funciona = "Y"

for i in range(len(conector1)):
    if conector1[i] + conector2[i] != 1:
        funciona = "N"
        break

print(funciona)