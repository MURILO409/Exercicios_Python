import math

def funcao():
    h = float(input('Digite o valor da hora: '))
    m = float(input('\nDigite o valor do minuto: '))
    s = float(input('\nDigite o valor do segundo: '))
    total = (60 * ((h * 60) + m)) + s
    print('\n')
    print(str(total) + ' segundos')
funcao()
