import random

n = 4
m = 4

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
    
sodiapri = [
    [v[0][0]],
    [v[1][1]],
    [v[2][2]],
    [v[3][3]],
    [v[4][4]]
]
sodiasec = [
    [v[4][0]],
    [v[3][1]],
    [v[2][2]],
    [v[1][3]],
    [v[0][4]]
]
if (sodiapri == sodiasec):
    print('\nA matriz principal é igual a secundária')
else:
    print('\nA matriz principal é diferente da secundária')
