quantidade = int(input())

marias = 0

for i in range(quantidade):
    nome = input()
    if 'Maria ' in nome or ' Maria' in nome:
        marias += 1

print(marias)