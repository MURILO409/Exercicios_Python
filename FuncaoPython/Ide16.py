def funcao():
    inicio = 101
    fim = 150
  
    for i in range(inicio, (fim + 1)): 
       if i > 1: 
          for j in range(2,i): 
             if((i % j) == 0): 
                break
          else: 
             print(i) 

funcao()
