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

def exibir_mensagem(nome):
    print(f'O meu nome é: {nome}')

exibir_mensagem("Kauhan")

def adicao(*args):
    resultado = 0
    
    for argumento in args:
        resultado += argumento
    return resultado

print(adicao(1, 2))
print(adicao(1, 2, 4, 6))
print(adicao(1, 2, 4, 6, 8, 10))