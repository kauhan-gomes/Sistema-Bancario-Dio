carros = ["Gol", "Palio", "Celta"]
numeros = [10, 5, 9, 3, 8, 2, 1, 4]
pares = []
impares = [i for i in numeros if i % 2 != 0]
quadrado = [q ** 2 for q in numeros]


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)
print(impares)
print(quadrado)
