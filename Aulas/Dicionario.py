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