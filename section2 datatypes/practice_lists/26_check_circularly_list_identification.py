list_1 = [10, 10, 0, 0, 10]
list_2 = [10, 10, 10, 0, 0]
list_3 = [1, 10, 10, 0, 0]

list_1_twice = ' '.join(map(str,list_1 * 2))
list_2_str = ' '.join(map(str,list_2))
list3_str = ' '.join(map(str,list_3))

print("Compare list1 and list2")
print(list_2_str in list_1_twice)


print("Compare list1 and list3")
print(list3_str in list_1_twice) 
