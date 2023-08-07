import numpy as np
#ex 1
lista = []
soma = 0
for i in range(1,6):
    valor = int(input(f'Digite o {i}° valor: '))
    lista.append(valor)
    
print(lista)
for item in lista:
    soma += item
    
print(soma)

#ex 2
dicionario = {}

for i in range(1,4):
    nome = input('Digite o nome do Aluno: ')
    nota = int(input(f'Digite a nota do {nome}: '))
    dicionario2 = {nome:nota}
    dicionario.update(dicionario2)
    
print(dicionario)
total = 0
for valores in dicionario.values():
    total += valores
    
print(f'A media é: {total/3}')
#ex 3
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
resultado = 0

print(matriz[0])
print(matriz[1])

for i in matriz[0]:
    resultado += i
    print(i)
for j in matriz[1]:
    resultado += j
    print(j)
    
print(resultado)
