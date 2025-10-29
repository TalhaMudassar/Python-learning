# list_1 = [1,2,3,4,5,10,9,8,7,6]

# list_1.sort()
# number  = list_1[::-1]
# print(number[0])



# second method 
list_1 = [1,2,3,4,5,10,9,8,7,6]

max_element = list_1[0]

for i in list_1:
    if  i > max_element:
        max_element = i
    
print(f" max element in this list are {max_element}")
