import random

n = 8
m = 6

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
    
soma2 = (v[1][0] + v[1][1] + v[1][2] + v[1][3] + v[1][4] + v[1][5])/6
s2 = round(soma2,3)
soma4 = (v[3][0] + v[3][1] + v[3][2] + v[3][3] + v[3][4] + v[3][5])/6
s4 = round(soma4,3)
soma6 = (v[5][0] + v[5][1] + v[5][2] + v[5][3] + v[5][4] + v[5][5])/6
s6 = round(soma6,3)
soma8 = (v[7][0] + v[7][1] + v[7][2] + v[7][3] + v[7][4] + v[7][5])/6
s8 = round(soma8,3)

solinha = [[s2],[s4],[s6],[s8]]
print('\nMatriz de soma das linhas pares é:\n')
print(solinha)
