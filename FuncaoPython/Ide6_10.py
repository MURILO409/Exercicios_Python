def funcao():

  soma = 0
  N = int(input('Digite a quantidade de elemntos (número > 0): '))
  i = 1

  if N > 0:
    for i in range(N+i):
       soma = soma + i
       print("\nPara N = ", i, ", a soma é: ", soma)
       media = soma / N
       m = round(media, 3)
    print("\nLogo, a soma dos ", i, ", números naturais é: ", soma)
    print("\nLogo, a média é: ", m)

  elif N < 0:
    print("\nSomente números positivos")
    
funcao()
