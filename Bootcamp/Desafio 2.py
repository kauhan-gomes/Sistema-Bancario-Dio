ativos = []

quantidadeAtivos = int(input())

for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
    
ativos_ordenados = sorted(ativos)

for j in ativos_ordenados:
  print(j)