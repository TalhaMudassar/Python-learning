list_1 = ["talha","aba","1221","ali" ,"umar"]

def check_word(list1):
    count = 0
    
    
    for i in list1:
        if len(i) > 0 and i[0] == i[-1]:
            count +=1
            
    return count

if check_word(list_1) == 0:
    print(f"No element with same start and end word")
    
elif check_word(list_1) > 0:
    print(f"Element with same start and end are : {check_word(list_1) }")