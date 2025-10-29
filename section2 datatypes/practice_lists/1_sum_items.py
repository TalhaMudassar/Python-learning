list1 = [1,2,3,4,5,6,7]


def sum_list(lst1):
    total = 0
    for i in lst1:
        total += lst1[i]
    return total

print(f"the sum of list elements are {sum(list1)}")
        
    
    