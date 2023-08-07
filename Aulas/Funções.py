def mensagem(texto):
    print(texto)

mensagem('texto 1')

def soma(a, b):
    print(a+b)

soma(2, 6)


def multiplicacao(a, b):
    return a * b

multiplicacao(5, 9)
r = multiplicacao(5, 9)
print(r)

def calcula_energia_potencial_gravitacional(m, h, g = 10):
    e = g * m * h
    return e

print(calcula_energia_potencial_gravitacional(30, 12))