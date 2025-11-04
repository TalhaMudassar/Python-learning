# difference in lists:


list_1 = [1,3,5,7,9]
list_2 = [1,2,4,6,7,8]
differ_list = []

for i in list_1:
    for j in list_2:
        if i == j:
            pass
        else:
            differ_list.append(i)
            break
            
for i in list_2:
    for j in list_1:
        if i == j:
            pass
        else:
            differ_list.append(i)
            break
        
        
print(f"Updated list {differ_list}")