alfa_normal = input()
alfa_dec = input()
mensagem_codificada = input()
mensagem_decodificada = ''

cod = {}

for i in range(len(alfa_normal)):
    cod[alfa_dec[i]] = alfa_normal[i]

for car in mensagem_codificada:
    if car.isalpha():
        mensagem_decodificada += cod[car]
    else:
        mensagem_decodificada += car
    
print(mensagem_decodificada)