conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4, 1, 5}
conjunto_c = {1, 0}
sorteio = {1, 23, 0}

conjunto_a.intersection(conjunto_b)

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)
#symmetric faz o serviço dos dois difference
conjunto_a.symmetric_difference(conjunto_b)

conjunto_a.issubset(conjunto_b)
conjunto_b.issubset(conjunto_a)

conjunto_a.issuperset(conjunto_b)
conjunto_b.issuperset(conjunto_a)

conjunto_a.isdisjoint(conjunto_b) #True
conjunto_a.isdisjoint(conjunto_c) #False

sorteio.add(25)
sorteio.add(52)
sorteio.add(25) #não repete
len(sorteio) #tamanho
0 in sorteio #confirmar se esta no conjunto
23 in sorteio
sorteio.copy() #copia a lista
sorteio.discard(52)#remove o numero da lista, se não tiver o numero não da erro
sorteio.remove(0)#remove o numero da lista, se não tiver o numero da erro
sorteio.pop() #vai removendo um por um, desde o começo
sorteio.clear() #Apaga tudo

