#Logicos
a = True
b = False

print(a, b)

c = a and b
print(f'A e B são iguais: {c}')

c = a or b
print(f'A ou b é: {c}')

#Relacionais
#Comparação == 
#maior igual >= 
#Menor igual <= 
#maior >
#Menor <
#Diferente !=

# Condicional
#Se
if 5 > 3:
    print('5 é Maior que 3')

#se e se não    
if 5> 6:
    print('5 é maior')
else:
    print('5 não é maior')


n = 3
if n == 4:
    print('n é igual a 4')
else: 
    if n == 3:
        print('n é igual a três')
    else:
        print('n não é igual a 4 nem 3')

x = 2
y = 3
# se com and(e)
if (x>1) and (y % 2 == 0):
    print('x é maior que 1 e y é par')
else:
    print('Uma ou nenhuma das condições foram satisfeitas')
#se com or(ou)
if (x>1) or (y % 2 == 0):
    print('x é maior que 1 e y é par')
else:
    print('Uma ou nenhuma das condições foram satisfeitas')