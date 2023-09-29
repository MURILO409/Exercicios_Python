import math

def funcao():

  a = int(input('Digite a constante A: '))
  b = int(input('\nDigite a constante B: '))
  c = int(input('\nDigite a constante C: '))
  print('\n')
  delta = (b * b) - (4 * a * c)
  raiz = pow(delta, 1/2)

  if raiz > 0:
    x1 = (raiz - b)/(2 * a)
    x2 = ((-1) * (raiz + b))/(2 * a)
    x11 = round(x1, 2)
    x22 = round(x2, 2)
    print('\nX1 = ', x11)
    print('\nX2 = ', x22)

  elif raiz == 0:
    x = (-1) * (b/(2 * a))
    xx = round(x, 2)
    print('\nX1 = X2 = ', xx)

  else:
    print('\nNão existe raízes reais')
    
funcao()
