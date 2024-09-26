n = int(input())

fim_intervalo = int(input())

r = ''

for i in range(1,fim_intervalo + 1):
    if i % n == 0:
        r += str(i)+' '

print(r)