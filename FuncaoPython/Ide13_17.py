def funcao():
    idade = []
    filhos = []
    salario = []
    sexo = []
    
    for i in range(0,15):
        idade = idade + [i]
        filhos = filhos + [i]
        salario = salario + [i]
        sexo = sexo + [i]

        idade[i] = int(input('\nIdade: '))
        filhos[i] = int(input('\nNúmero de Filhos: '))
        salario[i] = float(input('\nSalário: '))
        sexo[i] = str(input('\nSexo (M ou F): '))
        print('\n')

        somasal = sum(salario)

        if i == 0:
            maioridade = idade[i]
            menoridade = idade[i]
            maiorsalario = salario[i]

        if idade[i] > maioridade:
            maioridade = idade[i]

        if idade[i] < menoridade:
            menoridade = idade[i]

        if salario[i] > maiorsalario:
            maiorsalario = salario[i]
            maiosal = round(maiorsalario, 2)
         
        if ((sexo[i] == 'f') or (sexo[i] == 'F')) and (filhos[i] > 3) and (salario[i] <= 500):
            Qui_mulheres3f = 0
            Qui_mulheres3f = Qui_mulheres3f + 1

        if salario[i] <= 380:
            TreOt_pessoas = 0
            TreOt_pessoas = TreOt_pessoas + 1

    mediasal = somasal/15
    mds = round(mediasal, 2)
    percent_TreOt_pessoas = 100 * TreOt_pessoas/15
    pTreOt_p = round(percent_TreOt_pessoas, 2)

    print('\nMaioridade: ' + str(maioridade))
    print('\nMenoridade: ' + str(menoridade))
    print('\nMulheres com mais de 3 filhos com salário de até R$ 500,00: ' + str(Qui_mulheres3f))
    print('\nMédia Salarial: R$ ' + str(mds))
    print('\nMaior Salario: R$ ' + str(maiosal))
    print('\nPercentual de pessoas com salário inferior a R$ 380,00: ' + str(pTreOt_p) + '%')
 
funcao()
