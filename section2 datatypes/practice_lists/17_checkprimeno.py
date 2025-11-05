list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in list_1:
    if i<=1:
        continue
    flag = True
    
    for j in range(2,i):
        if i%j == 0:
            flag = False
            break
        
    if flag:
        print(f"{i} is a prime Number") 
        
            
            
    
    