teste = 1

while True:
    q = int(input())

    if q == 0:
        break
    else:
        cont = 1
        sequencia = [int(w) for w in input().split()]
        for numero in sequencia:
            if numero == cont:
                print(f"Teste {teste}\n{numero}")
                teste += 1
                break
            else:
                cont += 1