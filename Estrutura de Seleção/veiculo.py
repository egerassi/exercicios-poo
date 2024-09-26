dias = int(input())
km = int(input())

div = km / dias
taxa = dias * 45


if div > 60:
    taxa += dias*((div - 60)*0.5)

print(taxa)