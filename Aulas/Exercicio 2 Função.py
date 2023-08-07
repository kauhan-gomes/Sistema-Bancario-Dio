def ler():
    tempo = float(input('Qual o tempo gasto na viagem: '))
    velocidade = float(input('Qual a velocidade media da viagem: '))
    return tempo, velocidade
tempo, velocidade = ler()

def calcular_distancia(tempo, velocidade):
    distancia = tempo*velocidade
    return distancia
distancia = calcular_distancia(tempo, velocidade)

def calcular_litros(distancia):
    litros = distancia/12
    return litros
litros = calcular_litros(distancia)

def apresentar(tempo, velocidade, distancia, litros):
    return print(f'O tempo total gasto na viagem foi de: {tempo}h, a velocidade media dela: {velocidade}Km/h, a distancia percorrida: {distancia}KM, e o consumo de: {litros}L')
    
apresentar(tempo, velocidade, distancia, litros)