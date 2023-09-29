def funcao():
  ano = int(input('Digite ano entre 1 e 2010: '))

  quoc = int(ano / 4)



  if ((ano >= 1) and (ano <= 2010)):
   
    print('\nO total de anos bissexto eh: ', quoc)

  else:
   
   print('\nAno invalido')
  
funcao()
