lista = []
try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))
    divisao = lista[0]/lista[1]
except ValueError:
    print('Valor digitado é diferente do necessario')
except ZeroDivisionError:
    print('Erro, Zero não é divisivel')
except IndexError:
    print('Posisão incorreta da lista')
except KeyboardInterrupt:
    print('Usuario interrompeu a execução')
else:
    print(f'O resultado da divisão é: {divisao}')

