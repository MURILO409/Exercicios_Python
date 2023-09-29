def funcao():

  print('Escolhas as figuras geometricas para saber o valor da área: \n')
  print('\n1 - CÍRCULO')
  print('\n2 - RETÂNGULO')
  print('\n3 - TRIÂNGULO')
  print('\n')
  opcao = int(input())

  if opcao == 1:
    raio = float(input('\nDigite o raio da circunfrência: '))
    pi = 3.1459
    area = pi * (raio ** 2)
    a = round(area, 2)
    print('\nO comprimento da circunferência é: ', a)

  elif opcao == 2:
    base = float(input('\nDigite o valor da base: '))
    altura = float(input('\nDigite o valor da altura: '))
    area = base * altura
    a = round(area, 2)
    print('\nA Área do retângulo é: ', a)

  elif opcao == 3:
    base = float(input('\nDigite o valor da base: '))
    altura = float(input('\nDigite o valor da altura: '))
    area = (base * altura) / 2
    a = round(area, 2)
    print('\nA Área do triângulo é: ', a)

  else:
    print('Opção Inválida')
    
funcao()
