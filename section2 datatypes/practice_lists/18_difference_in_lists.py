# difference in lists:
list_1 = [1,3,5,7,9]
list_2 = [1,2,4,6,7,8]
differ_list = []

for i in list_1:
    if i not in list_2:
        differ_list.append(i)
            
for j in list_2:
    if j not in list_1:
        differ_list.append(j)
       
        
        
print(f"Updated list {differ_list}")