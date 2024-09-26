carros, voltas = [int(w) for w in input().split()]

dic = {}

for i in range(carros):
    t_voltas = [int(w) for w in input().split()]
    dic[sum(t_voltas)] = i + 1

temposSorted = sorted(dic)

print(dic[temposSorted[0]])
print(dic[temposSorted[1]])
print(dic[temposSorted[2]])