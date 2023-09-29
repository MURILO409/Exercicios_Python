class Onibus():
    def entrar(self,qtdPassageiro):
        capacidade = 46
        ocupado = 22
        vazio = capacidade - ocupado
        print('\nEntrar passageiro? ')

        if qtdPassageiro <= vazio and qtdPassageiro > 0:
           print('\True')
        else:
           print('\False')

    def sair(self,qtdPassageiro):
        ocupado = 25
        print('\Sair passageiro? ')
        if qtdPassageiro < ocupado and qtdPassageiro > 0:
           print('\True')
        else:
           print('\False')

    def Faturamento(self, roletaInicial, roletaFinal):
        total = roletaFinal - roletaInicial
        faturamento = 5.45 * total
        fat = round(faturamento,2)
        print('\nFaturamento: R$ ', fat)

    def qtdePassageiros(self, ocupado, entrar, sair):
        total = ocupado + entrar - sair
        print('\nQtde Passageiros: \n', total)


o = Onibus()
o.entrar(20)
o.sair(13)
o.Faturamento(60012,60089)
o.qtdePassageiros(26,21,19)

o1 = Onibus()
o1.entrar(30)
o1.sair(33)

o2 = Onibus()
o2.entrar(0)
o2.sair(0)
        
    
