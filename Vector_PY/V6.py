nota = [
    [5.8, 4.5, 7.0, 5.2, 6.1],
    [2.1, 6.5, 8.0, 7.0, 6.7],
    [8.6, 7.0, 9.1, 8.7, 9.3],
    [5.9, 4.5, 7.0, 5.2, 6.1],
    [2.1, 6.5, 8.8, 7.0, 6.7],
    [8.6, 7.0, 9.1, 8.7, 9.3],
    [5.1, 4.5, 7.9, 5.2, 6.1],
    [2.1, 6.5, 8.0, 7.1, 6.7],
    [8.6, 7.0, 9.1, 8.7, 9.3],
    [5.3, 4.5, 7.0, 5.2, 6.1],
    [2.1, 6.5, 8.2, 7.0, 6.7],
    [8.6, 7.0, 9.1, 8.7, 9.3],
    [5.6, 4.5, 7.9, 5.2, 6.1],
    [2.1, 6.5, 8.3, 7.0, 6.7],
    [8.6, 7.0, 9.1, 8.7, 9.3]
]

nome = [
    ['Lucas'],
    ['André'],
    ['Guilherme'],
    ['Carla'],
    ['Catia'],
    ['Lucia'],
    ['Elton'],
    ['Miguel'],
    ['Valentin'],
    ['Helena'],
    ['Edna'],
    ['Laís'],
    ['Estevão'],
    ['Gabriel'],
    ['Glória']
]

md00 = round(((nota[0][0] + nota[0][1] + nota[0][2] + nota[0][3] + nota[0][4])/5),1)
md01 = round(((nota[1][0] + nota[1][1] + nota[1][2] + nota[1][3] + nota[1][4])/5),1)
md02 = round(((nota[2][0] + nota[2][1] + nota[2][2] + nota[2][3] + nota[2][4])/5),1)
md03 = round(((nota[3][0] + nota[3][1] + nota[3][2] + nota[3][3] + nota[3][4])/5),1)
md04 = round(((nota[4][0] + nota[4][1] + nota[4][2] + nota[4][3] + nota[4][4])/5),1)
md05 = round(((nota[5][0] + nota[5][1] + nota[5][2] + nota[5][3] + nota[5][4])/5),1)
md06 = round(((nota[6][0] + nota[6][1] + nota[6][2] + nota[6][3] + nota[6][4])/5),1)
md07 = round(((nota[7][0] + nota[7][1] + nota[7][2] + nota[7][3] + nota[7][4])/5),1)
md08 = round(((nota[8][0] + nota[8][1] + nota[8][2] + nota[8][3] + nota[8][4])/5),1)
md09 = round(((nota[9][0] + nota[9][1] + nota[9][2] + nota[9][3] + nota[9][4])/5),1)
md10 = round(((nota[10][0] + nota[10][1] + nota[10][2] + nota[10][3] + nota[10][4])/5),1)
md11 = round(((nota[11][0] + nota[11][1] + nota[11][2] + nota[11][3] + nota[11][4])/5),1)
md12 = round(((nota[12][0] + nota[12][1] + nota[12][2] + nota[12][3] + nota[12][4])/5),1)
md13 = round(((nota[13][0] + nota[13][1] + nota[13][2] + nota[13][3] + nota[13][4])/5),1)
md14 = round(((nota[14][0] + nota[14][1] + nota[14][2] + nota[14][3] + nota[14][4])/5),1)

media = (md00+md01+md02+md03+md04+md05+md06+md07+md08+md09+md10+md11+md12+md13+md14)/15
print('Média da Turma: '+str(round(media,1))+'\n')

if md00 >= 6:
    situacao00 = 'Aprovado'
elif md00 < 6 and md00 >= 3:
    situacao00 = 'Em Exame'
else:
    situacao00 = 'Reprovado'

if md01 >= 6:
    situacao01 = 'Aprovado'
elif md01 < 6 and md01 >= 3:
    situacao01 = 'Em Exame'
else:
    situacao01 = 'Reprovado'

if md02 >= 6:
    situacao02 = 'Aprovado'
elif md02 < 6 and md02 >= 3:
    situacao02 = 'Em Exame'
else:
    situacao02 = 'Reprovado'

if md03 >= 6:
    situacao03 = 'Aprovado'
elif md03 < 6 and md03 >= 3:
    situacao03 = 'Em Exame'
else:
    situacao03 = 'Reprovado'

if md04 >= 6:
    situacao04 = 'Aprovado'
elif md04 < 6 and md04 >= 3:
    situacao04 = 'Em Exame'
else:
    situacao04 = 'Reprovado'

if md05 >= 6:
    situacao05 = 'Aprovado'
elif md05 < 6 and md05 >= 3:
    situacao05 = 'Em Exame'
else:
    situacao05 = 'Reprovado'

if md06 >= 6:
    situacao06 = 'Aprovado'
elif md06 < 6 and md06 >= 3:
    situacao06 = 'Em Exame'
else:
    situacao06 = 'Reprovado'

if md07 >= 6:
    situacao07 = 'Aprovado'
elif md07 < 6 and md07 >= 3:
    situacao07 = 'Em Exame'
else:
    situacao07 = 'Reprovado'

if md08 >= 6:
    situacao08 = 'Aprovado'
elif md08 < 6 and md08 >= 3:
    situacao08 = 'Em Exame'
else:
    situacao0 = 'Reprovado'

if md09 >= 6:
    situacao09 = 'Aprovado'
elif md09 < 6 and md09 >= 3:
    situacao09 = 'Em Exame'
else:
    situacao09 = 'Reprovado'

if md10 >= 6:
    situacao10 = 'Aprovado'
elif md10 < 6 and md10 >= 3:
    situacao10 = 'Em Exame'
else:
    situacao10 = 'Reprovado'

if md11 >= 6:
    situacao11 = 'Aprovado'
elif md11 < 6 and md11 >= 3:
    situacao11 = 'Em Exame'
else:
    situacao11 = 'Reprovado'

if md12 >= 6:
    situacao12 = 'Aprovado'
elif md12 < 6 and md12 >= 3:
    situacao12 = 'Em Exame'
else:
    situacao12 = 'Reprovado'

if md13 >= 6:
    situacao13 = 'Aprovado'
elif md13 < 6 and md13 >= 3:
    situacao13 = 'Em Exame'
else:
    situacao13 = 'Reprovado'

if md14 >= 6:
    situacao14 = 'Aprovado'
elif md14 < 6 and md14 >= 3:
    situacao14 = 'Em Exame'
else:
    situacao14 = 'Reprovado'

print('\n|--------------------------|')
print('\n|NOME     |MÉDIA |SITUAÇÃO  |')
print('\n|--------------------------|')
print('\n|'+str(nome[0][0])+'    | '+str(md00)+'  |'+str(situacao00)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[1][0])+'    | '+str(md01)+'  |'+str(situacao01)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[2][0])+'| '+str(md02)+'  |'+str(situacao02)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[3][0])+'   | '+str(md03)+'  |'+str(situacao03)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[4][0])+'   | '+str(md04)+'  |'+str(situacao04)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[5][0])+'   | '+str(md05)+'  |'+str(situacao05)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[6][0])+'   | '+str(md06)+'  |'+str(situacao06)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[7][0])+'   | '+str(md07)+'  |'+str(situacao07)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[8][0])+'   | '+str(md08)+'  |'+str(situacao08)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[9][0])+'   | '+str(md09)+'  |'+str(situacao09)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[10][0])+'   | '+str(md10)+'  |'+str(situacao10)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[11][0])+'   | '+str(md11)+'  |'+str(situacao11)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[12][0])+'   | '+str(md12)+'  |'+str(situacao12)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[13][0])+'   | '+str(md13)+'  |'+str(situacao13)+'  |')
print('\n|--------------------------|')
print('\n|'+str(nome[14][0])+'   | '+str(md14)+'  |'+str(situacao14)+'  |')


