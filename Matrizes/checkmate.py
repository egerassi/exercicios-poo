n = int(input())

pecas = input().split()

rei = input()

matriz = [[0 for l in range(8)] for c in range(8)]

index = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

for peca in pecas:
    if peca[0] == 'P':
        matriz[peca[2]][index[peca[1]]] = 1
        try:
            matriz[peca[2]-1][index[peca[1]]+1] = 1
            matriz[peca[2]-1][index[peca[1]]-1] = 1
        except:
            pass
    if peca[0] == 'B':
        matriz[peca[2]][index[peca[1]]] = 1
        l = matriz[peca[2]]
        c = matriz[peca[index[peca[1]]]]
        
    if peca[0] == 'R':
        matriz[peca[2]][index[peca[1]]] = 1
        try:
            matriz[][] = 1
        except:
            pass
    if peca[0] == 'T':
        matriz[peca[2]][index[peca[1]]] = 1
        try:
            matriz[][] = 1
        except:
            pass
    if peca[0] == 'W':
        matriz[peca[2]][index[peca[1]]] = 1
        try:
            matriz[][] = 1
        except:
            pass