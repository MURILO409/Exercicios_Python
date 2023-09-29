import math

def funcao():
    print('Escolha o Sexo:')
    print('\nM - Masculino')
    print('\nF - Feminino')

    sexo = input('\nSexo: ')
    altura = float(input('\nQual é sua altura? '))

    if ((sexo == 'M') or (sexo == 'm')):
        peso = (72.7 * altura) - 58
    elif ((sexo == 'F') or (sexo == 'f')):
        peso = (62.1 * altura) - 44.7
    else:
        print('\nOpção Inválida')

    ideal = round(peso, 2)
    print('\nSeu peso ideal é: ', ideal)
funcao()
