import time as tm

print(tm.time())
antes = tm.time()
lista = []
for i in range(0, 10000):
    lista.append(i)
depois = tm.time()
intervalo = depois - antes
print(f'Começo: {antes}, depois: {depois}, diferença: {intervalo}')

print('Finalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Ate a proxima!')