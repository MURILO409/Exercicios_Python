import math

def funcao():
    pi = 3.14159
    r = float(input('Digite o valor do raio da esfera: '))
    print('\n')
    v = pi * pow(r, 3) * (4/3)
    vol = round(v, 4)
    print('O volume da esfera é: ', vol)
funcao()
