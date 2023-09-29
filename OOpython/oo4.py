import math

class Produto():
    def __init__(self, codigo, descricao, custo, venda):
        MGlucro = (venda - custo) * (100/custo)
        print('\nCódigo: ' + str(codigo))
        print('\nDescrição: ' + str(descricao))
        print('\nCusto: R$ ' + str(custo))
        print('\nPreço de Venda: R$ ' + str(venda))
        print('\nMargem de Lucro: ' + str(round(MGlucro,2)) + '%')

    def setMargemLucro(self, percentual, custo):
        venda = custo * (100 + percentual)/100
        print('\nNovo Preço de Venda: R$ ' + str(round(venda,2)))

    def setPrecoVenda(self, custo, venda):
        MGlucro = (venda - custo) * (100/custo)
        print('\nNova Margem de Lucro: ' + str(round(MGlucro,2)) + '%')


p = Produto(25,'Alface',0.86,1.70)
p.setMargemLucro(31.3,0.86)
p.setPrecoVenda(0.86,1.60)
    
