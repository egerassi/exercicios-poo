dias_totais = int(input())

ano = int(dias_totais/365)
mes = int(dias_totais/30) - (ano*12)
dias = dias_totais - (ano*365) - (mes*30)

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")