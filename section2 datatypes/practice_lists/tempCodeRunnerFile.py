list_1 =[1,2,3,4,5,5,4,3,6,7,8,9,10,10]

def removedupliate(list1):
    for i in list1:
        j=i+1
        for j in list1:
            if i==j:
                list1.remove(j)
                break
            else:
                continue
            
removedupliate(list_1)

print(list_1)
    