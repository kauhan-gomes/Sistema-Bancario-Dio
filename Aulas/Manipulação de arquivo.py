with open('C:/Users/Kauhan/Desktop/Spyder/Aulas/texto2.txt') as tex:
    for linha in tex:
        print(linha)


with open('frase1.txt') as texto:
    r = texto.readlines()
    print(r)
    
with open('texto2.txt', 'w') as texto2:
    texto2.write('Olá a todos')