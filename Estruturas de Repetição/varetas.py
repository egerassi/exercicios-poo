q = 1

while q != 0:
    q = int(input())
    soma_varetas = 0
    for i in range(q):
        Ci, Vi = [int(w) for w in input().split()]
        if Vi % 2 == 0: ##ou seja, se Vi for par
            soma_varetas += Vi
        else:
            soma_varetas += Vi - 1
    print(soma_varetas//4)