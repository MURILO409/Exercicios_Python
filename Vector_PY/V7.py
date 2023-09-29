import random

n = 20
m = 10
def getLinha(matriz, n):
    return [i for i in matriz[n]]  # linha da matriz multiplicação

def getColuna(matriz, n):
    return [i[n] for i in matriz] # coluna da matriz multiplicação

print ("\nMatriz 1: \n")
mat = []
for i in range(n):
     mat.append([])
     for j in range(m):
        mat[i].append(random.randint(0,10))

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")
    print ("\n")
matlin = len(mat)                # retorna 20
matcol = len(mat[0])            # retorna 10

print ("\nMatriz 2: \n")
# uma matriz 10x1
mat2 = [
     [mat[0][0]+mat[0][1]+mat[0][2]+mat[0][3]+mat[0][4]+mat[0][5]+mat[0][6]+mat[0][7]+mat[0][8]+mat[0][9]],
     [mat[1][0]+mat[1][1]+mat[1][2]+mat[1][3]+mat[1][4]+mat[1][5]+mat[1][6]+mat[1][7]+mat[1][8]+mat[1][9]],
     [mat[2][0]+mat[2][1]+mat[2][2]+mat[2][3]+mat[2][4]+mat[2][5]+mat[2][6]+mat[2][7]+mat[2][8]+mat[2][9]],
     [mat[3][0]+mat[3][1]+mat[3][2]+mat[3][3]+mat[3][4]+mat[3][5]+mat[3][6]+mat[3][7]+mat[3][8]+mat[3][9]],
     [mat[4][0]+mat[4][1]+mat[4][2]+mat[4][3]+mat[4][4]+mat[4][5]+mat[4][6]+mat[4][7]+mat[4][8]+mat[4][9]],
     [mat[5][0]+mat[5][1]+mat[5][2]+mat[5][3]+mat[5][4]+mat[5][5]+mat[5][6]+mat[5][7]+mat[5][8]+mat[5][9]],
     [mat[6][0]+mat[6][1]+mat[6][2]+mat[6][3]+mat[6][4]+mat[6][5]+mat[6][6]+mat[6][7]+mat[6][8]+mat[6][9]],
     [mat[7][0]+mat[7][1]+mat[7][2]+mat[7][3]+mat[7][4]+mat[7][5]+mat[7][6]+mat[7][7]+mat[7][8]+mat[7][9]],
     [mat[8][0]+mat[8][1]+mat[8][2]+mat[8][3]+mat[8][4]+mat[8][5]+mat[8][6]+mat[8][7]+mat[8][8]+mat[8][9]],
     [mat[9][0]+mat[9][1]+mat[9][2]+mat[9][3]+mat[9][4]+mat[9][5]+mat[9][6]+mat[9][7]+mat[9][8]+mat[9][9]],
     [mat[10][0]+mat[10][1]+mat[10][2]+mat[10][3]+mat[10][4]+mat[10][5]+mat[10][6]+mat[10][7]+mat[10][8]+mat[10][9]],
     [mat[11][0]+mat[11][1]+mat[11][2]+mat[11][3]+mat[11][4]+mat[11][5]+mat[11][6]+mat[11][7]+mat[11][8]+mat[11][9]],
     [mat[12][0]+mat[12][1]+mat[12][2]+mat[12][3]+mat[12][4]+mat[12][5]+mat[12][6]+mat[12][7]+mat[12][8]+mat[12][9]],
     [mat[13][0]+mat[13][1]+mat[13][2]+mat[13][3]+mat[13][4]+mat[13][5]+mat[13][6]+mat[13][7]+mat[13][8]+mat[13][9]],
     [mat[14][0]+mat[14][1]+mat[14][2]+mat[14][3]+mat[14][4]+mat[14][5]+mat[14][6]+mat[14][7]+mat[14][8]+mat[14][9]],
     [mat[15][0]+mat[15][1]+mat[15][2]+mat[15][3]+mat[15][4]+mat[15][5]+mat[15][6]+mat[15][7]+mat[15][8]+mat[15][9]],
     [mat[16][0]+mat[16][1]+mat[16][2]+mat[16][3]+mat[16][4]+mat[16][5]+mat[16][6]+mat[16][7]+mat[16][8]+mat[16][9]],
     [mat[17][0]+mat[17][1]+mat[17][2]+mat[17][3]+mat[17][4]+mat[17][5]+mat[17][6]+mat[17][7]+mat[17][8]+mat[17][9]],
     [mat[18][0]+mat[18][1]+mat[18][2]+mat[18][3]+mat[18][4]+mat[18][5]+mat[18][6]+mat[18][7]+mat[18][8]+mat[18][9]],
     [mat[19][0]+mat[19][1]+mat[19][2]+mat[19][3]+mat[19][4]+mat[19][5]+mat[19][6]+mat[19][7]+mat[19][8]+mat[19][9]]
]      
mat2lin = len(mat2)                # retorna 10
mat2col = len(mat2[0])             # retorna 1
print(mat2)

matRes = []                        # deverá ser uma matriz 10x1
for i in range(matlin):           
    matRes.append([])

    for j in range(mat2col):
        # produto da linha de mat pela coluna de mat2;
        listMult = [x*y for x, y in zip(getLinha(mat, i), getColuna(mat2, j))]

        # e em seguida adiciona a matRes a soma das multiplicações
        matRes[i].append(sum(listMult))

print ("\nResultado: \n")
print(matRes)


