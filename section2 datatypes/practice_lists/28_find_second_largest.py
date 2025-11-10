def second_smallest(numbers):
    if len(numbers) < 2:
        return
    
    if len(numbers) == 2 and numbers[0] == numbers[1]:
        return
    
    dup_items = set()
    unique_items = []
    
    for x in numbers:
        if x not in dup_items:
            unique_items.append(x)
            dup_items.add(x)
            
        
    unique_items.sort()
    
    return unique_items[-2]



print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2, 2])) 
print(second_smallest([2]))             