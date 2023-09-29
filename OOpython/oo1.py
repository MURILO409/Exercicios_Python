import math

class Numero():
    def __init__(self, N, x):
        print('\nNúmero Qualquer: ' + str(N))
        print('\nNúmero Inteiro: ' + str(x))
  
    def Fatorial(self, N):
        fatorial = 1
        i = 2
        while i <= N:
           fatorial = fatorial*i
           i = i + 1
        print ('\nFatorial: ', fatorial)

    def Potencia(self, N, x):
        a = int(x)
        pot = N ** a
        pt = round(pot, 2)
        print ('\nPotencia: ', pt)

    def parteInteira(self, N):
        into = int(N)
        print ('\nParte Inteira: ', into)


    def parteDecimal(self, N):
        into = int(N)
        dec = N - into
        print ('\nParte Decima: ', dec)

num = Numero(6.5, 8.3)
num.Fatorial(6.5)
num.Potencia(6.5, 8.3)
num.parteInteira(6.5)
num.parteDecimal(6.5)



