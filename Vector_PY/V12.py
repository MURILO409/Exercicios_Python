import random

n = 12
m = 13

print ("\nMatriz : \n")
mat = []
for i in range(n):
     mat.append([])
     for j in range(m):
        mat[i].append(random.randint(1,10))

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")
    print ("\n")

maior = 0
menor = 0

for i in range(len(mat)):
    for j in range(len(mat[i])):
         if maior < mat[i][j]:
              maior = mat[i][j]
              
print('\nMaior elemento: ' + str(maior))

mat2 = [
     [maior/mat[0][0], maior/mat[0][1], maior/mat[0][2], maior/mat[0][3], maior/mat[0][4], maior/mat[0][5], maior/mat[0][6], maior/mat[0][7], maior/mat[0][8], maior/mat[0][9], maior/mat[0][10], maior/mat[0][11], maior/mat[0][12]],
     [maior/mat[1][0], maior/mat[1][1], maior/mat[1][2], maior/mat[1][3], maior/mat[1][4], maior/mat[1][5], maior/mat[1][6], maior/mat[1][7], maior/mat[1][8], maior/mat[1][9], maior/mat[1][10], maior/mat[1][11], maior/mat[1][12]],
     [maior/mat[2][0], maior/mat[2][1], maior/mat[2][2], maior/mat[2][3], maior/mat[2][4], maior/mat[2][5], maior/mat[2][6], maior/mat[2][7], maior/mat[2][8], maior/mat[2][9], maior/mat[2][10], maior/mat[2][11], maior/mat[2][12]],
     [maior/mat[3][0], maior/mat[3][1], maior/mat[3][2], maior/mat[3][3], maior/mat[3][4], maior/mat[3][5], maior/mat[3][6], maior/mat[3][7], maior/mat[3][8], maior/mat[3][9], maior/mat[3][10], maior/mat[3][11], maior/mat[3][12]],
     [maior/mat[4][0], maior/mat[4][1], maior/mat[4][2], maior/mat[4][3], maior/mat[4][4], maior/mat[4][5], maior/mat[4][6], maior/mat[4][7], maior/mat[4][8], maior/mat[4][9], maior/mat[4][10], maior/mat[4][11], maior/mat[4][12]],
     [maior/mat[5][0], maior/mat[5][1], maior/mat[5][2], maior/mat[5][3], maior/mat[5][4], maior/mat[5][5], maior/mat[5][6], maior/mat[5][7], maior/mat[5][8], maior/mat[5][9], maior/mat[5][10], maior/mat[5][11], maior/mat[5][12]],
     [maior/mat[6][0], maior/mat[6][1], maior/mat[6][2], maior/mat[6][3], maior/mat[6][4], maior/mat[6][5], maior/mat[6][6], maior/mat[6][7], maior/mat[6][8], maior/mat[6][9], maior/mat[6][10], maior/mat[6][11], maior/mat[6][12]],
     [maior/mat[7][0], maior/mat[7][1], maior/mat[7][2], maior/mat[7][3], maior/mat[7][4], maior/mat[7][5], maior/mat[7][6], maior/mat[7][7], maior/mat[7][8], maior/mat[7][9], maior/mat[7][10], maior/mat[7][11], maior/mat[7][12]],
     [maior/mat[8][0], maior/mat[8][1], maior/mat[8][2], maior/mat[8][3], maior/mat[8][4], maior/mat[8][5], maior/mat[8][6], maior/mat[8][7], maior/mat[8][8], maior/mat[8][9], maior/mat[8][10], maior/mat[8][11], maior/mat[8][12]],
     [maior/mat[9][0], maior/mat[9][1], maior/mat[9][2], maior/mat[9][3], maior/mat[9][4], maior/mat[9][5], maior/mat[9][6], maior/mat[9][7], maior/mat[9][8], maior/mat[9][9], maior/mat[9][10], maior/mat[9][11], maior/mat[9][12]],
     [maior/mat[10][0], maior/mat[10][1], maior/mat[10][2], maior/mat[10][3], maior/mat[10][4], maior/mat[10][5], maior/mat[10][6], maior/mat[10][7], maior/mat[10][8], maior/mat[10][9], maior/mat[10][10], maior/mat[10][11], maior/mat[10][12]],
     [maior/mat[11][0], maior/mat[11][1], maior/mat[11][2], maior/mat[11][3], maior/mat[11][4], maior/mat[11][5], maior/mat[11][6], maior/mat[11][7], maior/mat[11][8], maior/mat[11][9], maior/mat[11][10], maior/mat[11][11], maior/mat[11][12]]
]

print('\nNova Matriz:\n')
print(mat2)







