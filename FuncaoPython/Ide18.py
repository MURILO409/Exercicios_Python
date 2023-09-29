def funcao():
    a = float(input('Primeiro Lado: '))
    b = float(input('\nSegundo Lado: '))
    c = float(input('\nTerceiro Lado: '))

    if (a > 0) and (b > 0) and (c > 0):
        if (a == b) and (b == c) and (c == a):
            print('\nTRIÂNGULO EQUILÁTERO')
        elif (a == b) or (b == c) or (c == a):
            print('\nTRIÂNGULO ISÓSCELES')
        elif(a != b) and (b != c) and (c != a):
            print('\nTRIÂNGULO ESCALENO')
        else:
            print('\nTRIÂNGULO NÃO CLASSIFICADO')

    else:
        print('\nValor Inválido')

funcao()
