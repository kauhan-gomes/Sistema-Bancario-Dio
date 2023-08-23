linguaguens = ["python", "js", "Java", "C#", "HTML"]
lista = []
cores = ["Vermelho", "Roxo", "Vermelho", "Preto", "Azul"]
lista.append(21)
lista.append("Python")
lista.append([20, 546, 12, 5])
print(lista)
l2 = lista.copy()
lista.clear()
print(lista)
print(l2)
print(cores)
print(cores.count("Vermelho"))
cores.extend(["Vermelho", "Azul", "Preto"])
print(cores)
cores.extend(l2)
print(cores)
print(cores.index("Preto"))
cores.reverse()
print(cores)
print(len(cores))
print(linguaguens.pop(0))
print(linguaguens.pop(3))

linguaguens.remove("C#")

cores = ["Vermelho", "Roxo", "Vermelho", "Preto", "Azul"]
cores.sort()
print(cores)

cores.sort(reverse=True)
print(cores)

cores.sort(key=lambda x: len(x))
print(cores)

cores.sort(key=lambda x: len(x), reverse=True)
print(cores)

print(sorted(cores, key = lambda x: len(x)))