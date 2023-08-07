def ler():
    celsius = float(input('Digite: '))
    return celsius
celsius = ler()

def calculo(c = celsius):
    f = ( 9 * c + 160)/5
    return f
f = calculo()

def resultado(celsius, f):
    print(f'A temperatura em celsius é de: {celsius}C, e em Fahrenheit {f}F')
    
resultado(celsius, f)

