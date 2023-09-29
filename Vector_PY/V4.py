import random

n = 2
m = 4

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

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
         if (matriz[i][j]) %2 == 0:
              par = par + 1
              
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
         if matriz[i][j] >= 12 and matriz[i][j] <= 20:
              cont = cont + 1

print('\nO total de Nº entre 12 e 20 eh: ' + str(cont))
print('\nO total de Nº pares: ' + str(par))







