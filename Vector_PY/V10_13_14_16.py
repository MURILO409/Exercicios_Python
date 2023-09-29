import random
#10,13,14,16

n = 5
m = 5

print ("\nMatriz : \n")
v = []
for i in range(n):
     v.append([])
     for j in range(m):
        v[i].append(random.randint(0,10))

for i in range(len(v)):
    for j in range(len(v[i])):
        print(v[i][j], end=" ")
    print ("\n")
    
soma4 = v[3][0] + v[3][1] + v[3][2] + v[3][3] + v[3][4]
soma2 = v[0][1] + v[1][1] + v[2][1] + v[3][1] + v[4][1]
sodiapri = v[0][0] + v[1][1] + v[2][2] + v[3][3] + v[4][4]
sodiasec = v[0][4] + v[1][3] + v[2][2] + v[3][1] + v[4][0]
total = v[0][0]+v[0][1]+v[0][2]+v[0][3]+v[0][4]+v[1][0]+v[1][1]+v[1][2]+v[1][3]+v[1][4]+v[2][0]+v[2][1]+v[2][2]+v[2][3]+v[2][4]+v[3][0]+v[3][1]+v[3][2]+v[3][3]+v[3][4]+v[4][0]+v[4][1]+v[4][2]+v[4][3]+v[4][4]
invertida = [v[4][4],v[3][3],v[2][2],v[1][1],v[0][0]]

solinha = [
    [v[0][0]+v[0][1]+v[0][2]+v[0][3]+v[0][4]],
    [v[1][0]+v[1][1]+v[1][2]+v[1][3]+v[1][4]],
    [v[2][0]+v[2][1]+v[2][2]+v[2][3]+v[2][4]],
    [v[3][0]+v[3][1]+v[3][2]+v[3][3]+v[3][4]],
    [v[4][0]+v[4][1]+v[4][2]+v[4][3]+v[4][4]]
]

socoluna = [
    v[0][0]+v[1][0]+v[2][0]+v[3][0]+v[4][0],
    v[0][1]+v[1][1]+v[2][1]+v[3][1]+v[4][1],
    v[0][2]+v[1][2]+v[2][2]+v[3][2]+v[4][2],
    v[0][3]+v[1][3]+v[2][3]+v[3][3]+v[4][3],
    v[0][4]+v[1][4]+v[2][4]+v[3][4]+v[4][4]
]
     
print('\nA soma dos elementos da linha 4 é: ', soma4)
print('\nA soma dos elementos da coluna 2 é: ', soma2)
print('\nA soma dos elementos da diagonal principal é: ', sodiapri)
print('\nA soma dos elementos da diagonal secundária é: ', sodiasec)
print('\nA soma de todos os elementos da matriz é: ', total)
print('\nDiagonal Principal invertida: ', invertida)
print('\nMatriz de soma das linhas: ', solinha)
print('\nMatriz de soma das colunas: ', socoluna)
