from datetime import timedelta
from datetime import datetime

class Hora():

    def ehValida(self, hour, minute, second):
        if hour < 24 and  minute < 60 and second < 60:
            print('\nHora Válida')
        else:
            print('\nHora Inválida\n')

    def imprime(self, hour, minute, second):
        print('\nHora - ' + str(hour) + ':' + str(minute) + ':' + str(second) + '\n')

    def diferenca(self, hour, minute, second, hour1, minute1, second1):
        t1 = (hour * 60 * 60) + (minute * 60) + second
        t2 = (hour1 * 60 * 60) + (minute1 * 60) + second1

        if t2 > t1:
            t3 = t2 - t1
        elif t2 < t1:
            t3 = t2 - t1 + (24 * 60 * 60)
        else:
            t3 = 0

        hora = t3 % 24
        minuto = hora % 60
        segundo = minuto % 60

        print('\nDiferença - ' + str(hora) + ':' + str(minuto) + ':' + str(segundo) + '\n')


hor = Hora()
hor.ehValida(15,3,29)
hor1 = Hora()
hor1.ehValida(25,63,129)

hor = Hora()
hor.imprime(11,4,54)

hor = Hora()
hor.diferenca(15,3,29,21,10,13)
hor1 = Hora()
hor1.diferenca(15,3,29,2,36,10)
hor2 = Hora()
hor2.diferenca(2,2,2,2,2,2)
