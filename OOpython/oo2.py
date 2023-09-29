import math

class AlunoAcademia():
    def __init__(self, peso, altura):
        print('\nPeso: ' + str(peso) + ' KG')
        print('\nAltura: ' + str(altura) + 'm')
  
    def imc(self, peso, altura):
        imc = peso / (altura * altura)
        ic = round(imc,2)
        print ('\nIMC: ', ic)

    def pesoMinimo(self, altura):
        mini = 18.5 * altura * altura
        mn = round(mini,2)
        print ('\nPeso Mínimo: ', mn)

    def pesoMaximo(self, altura):
        maxi = 24.9 * altura * altura
        ma = round(maxi,2)
        print ('\nPeso Mínimo: ', ma)

    def pesoMedio(self, altura):
        medio = (altura * altura * (18.5 + 24.9)) / 2
        md = round(medio,2)
        print ('\nPeso Medio: ', md)

num = AlunoAcademia(60, 1.63)
num.imc(60, 1.63)
num.pesoMinimo(1.63)
num.pesoMaximo(1.63)
num.pesoMedio(1.63)



