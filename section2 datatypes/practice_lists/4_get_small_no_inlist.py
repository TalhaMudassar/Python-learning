list_2 = [1,2,3,4,5,6,9,10,8,7]

small_element = list_2[0]

for i in list_2:
    if i < small_element:
        small_element = i
        
print(f"Smallest element in this list are : {small_element}")