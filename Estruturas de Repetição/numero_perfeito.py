q = int(input())

for i in range(q):
    n = int(input())
    soma = 1
    for i in range(2,n):
        if n % i == 0:
            soma += i
    if soma == n:
        print(f"{n} eh perfeito")
    else:
        print(f"{n} nao eh perfeito")