import math

class Funcionario():
    def __init__(self, matricula, nome, salario, ativo):
        print('\nMatricula: ', matricula)
        print('\nNome: ', nome)
        print('\nSalario R$: ', salario)
        print('\nStatus: 0 - INATIVO e 1 - ATIVO: ', ativo)

    def ganhoAnual(self, salario):
        g12 = salario * 12
        tf = salario / 3
        dt = (g12 + tf) / 12
        anual = g12 + tf + dt
        an = round(anual,2)
        print('\nGanho Anual R$: ', an)

    def descontoIR(self, salario):
        if salario <= 1500:
            print('\nDesconto Mensal: ZERO\n')

        elif salario > 1500 and salario <= 5000:
            desconto = salario * 0.15
            desc = round(desconto,2)
            print('\nDesconto Mensal: R$ \n', desc)

        else:
            desconto = salario * 0.25
            desc = round(desconto,2)
            print('\nDesconto Mensal: R$ ', desc)

    def aumenta(self, ativo, percentual, salario):
        if ativo == 0:
            print('\nFUNCIONÁRIO INATIVO NÃO TEM AUMENTO DE SALÁRIO')

        elif ativo == 1:
            novosal =  salario * (percentual + 100) / 100
            print('\nNovo Salário: R$ ', round(novosal,2))

    def demite(self, ativo):
        if ativo == 0:
            print('\nFUNCIONÁRIO INATIVO\n')

        elif ativo == 1:
            print('\nFUNCIONÁRIO ATIVO\n')

f = Funcionario(601, 'Marcos', 1400.22,0)
f.ganhoAnual(1400.22)
f.descontoIR(1400.22)
f.aumenta(0, 15, 1400.22)
f.demite(0)

f1 = Funcionario(604, 'Mario', 2400.37,1)
f1.ganhoAnual(2400.37)
f1.descontoIR(2400.37)
f1.aumenta(1, 13, 2400.37)
f1.demite(1)

f2 = Funcionario(609, 'Messias', 6400.89,1)
f2.ganhoAnual(6400.89)
f2.descontoIR(6400.89)
f2.aumenta(1, 11, 6400.89)
f2.demite(1)





