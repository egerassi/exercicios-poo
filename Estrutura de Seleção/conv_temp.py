origem = str(input())
valor = float(input())
destino = str(input())

def celsius(x):
    if x == 'f':
        return valor * 1.8 + 32
    if x == 'k':
        return valor + 273.15
    if x == 'r':
        return valor * 1.8 + 491.67

def fahrenheit(x):
    if x == 'c':
        return (valor - 32) / 1.8
    if x == 'k':
        return (valor + 459.67) / 1.8
    if x == 'r':
        return valor + 459.67
def kelvin(x):
    if x == 'c':
        return valor - 273.15
    if x == 'f':
        return valor * 1.8 - 459.67
    if x == 'r':
        return valor * 1.8

def rankine(x):
    if x == 'c':
        return valor / 1.8 + 273.15
    if x == 'f':
        return valor - 459.67
    if x == 'k':
        return valor / 1.8

if origem == 'c':
    print(celsius(destino))

if origem == 'f':
    print(fahrenheit(destino))

if origem == 'k':
    print(kelvin(destino))

if origem == 'r':
    print(rankine(destino))