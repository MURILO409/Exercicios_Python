import random

n = 6
m = 3

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

maior = 0
menor = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
         if maior < matriz[i][j]:
              maior = matriz[i][j]
              
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
         if menor > matriz[i][j]:
              menor = matriz[i][j]

print('\nMaior elemento: ' + str(maior))
print('\nMenor elemento: ' + str(menor))







