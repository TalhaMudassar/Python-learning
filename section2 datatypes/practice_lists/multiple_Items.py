list_1 = [1,2,3,4,5,6,7,8,9,10]


def multiple_list(list1):
    total = 1
    
    for i in list1:
        total *= i
    return total

print(f"Multiple of all items are {multiple_list(list_1)}")