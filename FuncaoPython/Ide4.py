def funcao():

 n = int(input('Escreva o 1º número: '))
 m = int(input('\nEscreva o 2º número: '))
 resto = int(n % m)

 if resto == 0:
   print('\nO número ' + str(n) + ' é divisível por ' + str(m))

 else:
   print('\nO número ' + str(n) + ' não é divisível por ' + str(m))

funcao()
