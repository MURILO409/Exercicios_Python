import random

n = 2
m = 3

print ("\nMatriz 1: \n")
matriz1 = []
for i in range(n):
     matriz1.append([])
     for j in range(m):
        matriz1[i].append(random.randint(0,100))

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        print(matriz1[i][j], end=" ")
    print ("\n")

print ("\nMatriz 2: \n")
matriz2 = []
for i in range(n):
     matriz2.append([])
     for j in range(m):
        matriz2[i].append(random.randint(0,100))

for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        print(matriz2[i][j], end=" ")
    print ("\n")
    
def somarMatrizes(matriz1, matriz2):
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return None
    result = []
    for i in range(len(matriz1)):   
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] + matriz2[i][j])
    return result

print ("\nSoma: \n")    
soma = somarMatrizes(matriz1, matriz2) # soma e retorno
if soma is not None:
    for i in soma:
        print(i)


def subrairMatrizes(matriz1, matriz2):
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return None
    result = []
    for i in range(len(matriz1)):   
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] - matriz2[i][j])
    return result

print ("\nDiferença: \n")    
diferenca = subrairMatrizes(matriz1, matriz2) # dif e retorno
if diferenca is not None:
    for i in diferenca:
        print(i)
