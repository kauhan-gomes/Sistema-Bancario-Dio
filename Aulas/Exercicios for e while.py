#exercicio 1 com for
media = 0
for i in range(1, 6):
    nota = int(input(f'Digite a nota numero {i}: '))
    media += nota


print()
print(f'A media final é {media/5}')
print()

#exercicio 1 com while
numero = 1 
media = 0
while numero < 6:
    nota = int(input(f'Digite a nota numero {numero}: '))
    media += nota
    numero += 1
    print('------------------------')
print(f'A media final é de : {media/5}')
print('----------------------------------------------------------')


#exercicio 2 com for
for t in range(1, 11):
    print(f'3 x {t} = {3*t}')
    print('---------------')
    
numero = 1
media = 0
while numero < 11:
    print(f'3 * {numero} = {numero*3}')
    print('-------------')
    numero += 1