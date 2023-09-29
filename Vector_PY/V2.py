def getLinha(matriz, n):
    return [i for i in matriz[n]]  # linha da matriz multiplicação

def getColuna(matriz, n):
    return [i[n] for i in matriz] # coluna da matriz multiplicação

mat1 = [[2, 3], [4, 6],[41,8]]            # matriz 3x2
mat1lin = len(mat1)                # retorna 3
mat1col = len(mat1[0])             # retorna 2

mat2 = [[1, 3, 0], [2, 1, 1]]      # uma matriz 2x3
mat2lin = len(mat2)                # retorna 2
mat2col = len(mat2[0])             # retorna 3

matRes = []                        # deverá ser uma matriz 3x3
for i in range(mat1lin):           
    matRes.append([])

    for j in range(mat2col):
        # produto da linha de mat1 pela coluna de mat2;
        listMult = [x*y for x, y in zip(getLinha(mat1, i), getColuna(mat2, j))]

        # e em seguida adiciona a matRes a soma das multiplicações
        matRes[i].append(sum(listMult))

print(matRes)
