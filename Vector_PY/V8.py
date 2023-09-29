import random

n = 4
m = 6

print ("\nMatriz 1: \n")
matriz1 = []
for i in range(n):
     matriz1.append([])
     for j in range(m):
        matriz1[i].append(random.randint(0,10))

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        print(matriz1[i][j], end=" ")
    print ("\n")

o = 6
p = 4

print ("\nMatriz 2: \n")
matriz2 = []
for i in range(o):
     matriz2.append([])
     for j in range(p):
        matriz2[i].append(random.randint(0,10))

for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        print(matriz2[i][j], end=" ")
    print ("\n")
    
def somarMatrizes(matriz1, matriz2):
    soma = [
     [matriz1[0][0]+matriz2[0][0] , matriz1[0][1]+matriz2[1][0] , matriz1[0][2]+matriz2[2][0] , matriz1[0][3]+matriz2[3][0] , matriz1[0][4]+matriz2[4][2] , matriz1[0][5]+matriz2[5][0]],
     [matriz1[1][0]+matriz2[0][1] , matriz1[1][1]+matriz2[1][1] , matriz1[1][2]+matriz2[2][1] , matriz1[1][3]+matriz2[3][1] , matriz1[1][4]+matriz2[4][2] , matriz1[1][5]+matriz2[5][1]],
     [matriz1[2][0]+matriz2[0][2] , matriz1[2][1]+matriz2[1][2] , matriz1[2][2]+matriz2[2][2] , matriz1[2][3]+matriz2[3][2] , matriz1[2][4]+matriz2[4][2] , matriz1[2][5]+matriz2[5][2]],
     [matriz1[3][0]+matriz2[0][3] , matriz1[3][1]+matriz2[1][3] , matriz1[3][2]+matriz2[2][3] , matriz1[3][3]+matriz2[3][3] , matriz1[3][4]+matriz2[4][3] , matriz1[3][5]+matriz2[5][3]]
    ]
    return soma
print ("\nSoma: \n")    
soma = somarMatrizes(matriz1, matriz2) # soma e retorno
if soma is not None:
    for i in soma:
        print(i)

