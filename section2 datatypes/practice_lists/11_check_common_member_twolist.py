def checkcommonlist(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result


x=checkcommonlist([1, 2, 3, 4, 5], [10, 6, 7, 8, 9])
if x==True:
    print(" Common members in these two lists ")
else:
    print(" Non common members ")
                
                