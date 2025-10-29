list_1 =[1,2,3,4,5,5,4,3,6,7,8,9,10,10]

print(f"Orignal list are : {list_1}")

def removedupliate(list1):
    unique_element = []
    
    for i in list1:
        if i not in unique_element:
            unique_element.append(i) 
    return unique_element
        
            
updated_list = removedupliate(list_1)

print(f"unique element in the list are {updated_list}")
    