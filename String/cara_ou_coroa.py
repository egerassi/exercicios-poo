q = int(input())

while q != 0:
    jogos = input()
    v_maria = 0
    v_joao = 0
    jogos_clean = ''
    for car in jogos:
        if car.isalnum():
            jogos_clean += car
    for i in range(q):
        if jogos_clean[i] == '0':
            v_maria += 1
        else:
            v_joao += 1
    print(f"Mary won {v_maria} times and John won {v_joao} times")
    q = int(input())