n = int(input())

while n != 0:
    matriz = [[] for i in range(n)]
    j = 0
    
    for i in range(n):
        matriz[i] = [2**t for t in range(j,n+j)]
        j += 1
  
    for lista in matriz:
        for num in lista:
            print(num, end = ' ')
        print()
    n = int(input())