while True:
    try:
        n = int(input('Digite um numero inteiro: '))
    except:
        print('Valor invalido')
        break
    else:
        print(f'Valor digitado é: {n}')
    

while True:
    try:
        p = int(input('Digite um numero inteiro: '))
    except ValueError:
        print('Valor invalido')
    except KeyboardInterrupt:
        print('Usuario Interrompeu a execução')
        break
    else:
        print(f'Valor digitado foi: {p}')
        break