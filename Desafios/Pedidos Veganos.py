numPedidos = int(input())
pedidos = ""
for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()
    if ehVegano == "s":
        prato += " (Vegano)"
    elif ehVegano == "n":
         prato += " (Nao-vegano)"
    pedidos += f"Pedido {i}: {prato} - {calorias} calorias\n"

print(pedidos)