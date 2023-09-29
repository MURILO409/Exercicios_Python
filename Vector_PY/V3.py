import random

n = 3
m = 5

print ("\nMatriz : \n")
matriz = []
for i in range(n):
     matriz.append([])
     for j in range(m):
        matriz[i].append(random.randint(0,100))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print ("\n")

for i in range(n):
    for j in range(m):
         if matriz[i][j] >= 15 and matriz[i][j] <= 20:
              cont = 0
              cont = cont + 1

print('\nO total de Nº entre 15 e 20 eh: ' + str(cont))







