def funcao():
  temp = []
  for m in range(0,12):
    temp = temp + [m]
    
    print('\nInforme a temperatura no Mês ' + str(m+1) + ': ')
    temp[m] = float(input())

    if m == 0:
        maior = temp[m]
        menor = temp[m]
        
    if maior < temp[m]:
        maior = temp[m]
        mai = round(maior,1)
        mmaior = m + 1
        
    if menor > temp[m]:
        menor = temp[m]
        men = round(menor,1)
        mmenor = m + 1

  media = sum(temp)/12
  med = round(media,1)
  print('\nA média de tempratura anual é: ' + str(med) + 'ºC')

  if mmaior == 1:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Janeiro')
  elif mmaior == 2:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Fevereiro')
  elif mmaior == 3:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Março')
  elif mmaior == 4:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Abril')
  elif mmaior == 5:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Maio')
  elif mmaior == 6:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Junho')
  elif mmaior == 7:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Julho')
  elif mmaior == 8:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Agosto')
  elif mmaior == 9:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Setembro')
  elif mmaior == 10:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Outubro')
  elif mmaior == 11:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Novembro')
  elif mmaior == 12:
    print('\nMaior temperatura = ' + str(mai) + 'ºC no mês ' + str(mmaior) + ' = Dezembro')
  else:
    print('\nMês Inválido')

  if mmenor == 1:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Janeiro')
  elif mmenor == 2:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Fevereiro')
  elif mmenor == 3:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Março')
  elif mmenor == 4:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Abril')
  elif mmenor == 5:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Maio')
  elif mmenor == 6:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Junho')
  elif mmenor == 7:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Julho')
  elif mmenor == 8:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Agosto')
  elif mmenor == 9:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Setembro')
  elif mmenor == 10:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Outubro')
  elif mmenor == 11:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Novembro')
  elif mmenor == 12:
    print('\nMenor temperatura = ' + str(men) + 'ºC no mês ' + str(mmenor) + ' = Dezembro')
  else:
    print('\nMês Inválido')

funcao()
    

