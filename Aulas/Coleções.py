#tuplas
tupla = ('Homo sapiens', 'Canis familiaris', 'Felis catus')
print(tupla[2])


for elemento in tupla:
    print(elemento)

#Listas

l1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
l2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']

l3 = l1 +l2
print(l3)
print('----------------------')
l2_2 = l2 *2
print(l2_2)
print('----------------------')
print(l1[0:2])
print('----------------------')
l1.append('Gorila gorila')
print(l1)
print('----------------------')
l1.remove('Felis catus')
print(l1)
print('----------------------')

for item in l2_2:
    print(item)
    print('----------------------')
    
#Dicionario

coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
print(coleta['Aedes aegypt'])
print('----------------------')
coleta['Rhodnius montenegrensis'] = 11
print(coleta)
print('----------------------')
del(coleta)['Aedes albopictus']
print('----------------------')
print(coleta)
print('----------------------')
print(coleta.items())
print('----------------------')
print(coleta.keys())
print('----------------------')
print(coleta.values())
print('----------------------')
coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
coleta.update(coleta2)
print(coleta)
print('----------------------')
for especie, num_especimes in coleta.items():
    print(f'Especie: {especie}, numero de especimes coletados: {num_especimes}')

#Conjuntos(set)

biomoleculas = ('proteína','ácidos nucleicos','caboidrato','lipídeo',
                'ácidos nucleicos','caboidrato','caboidrato','caboidrato','caboidrato')

print(biomoleculas)
print(set(biomoleculas))
c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)
print(c3)

c1.difference(c2)







