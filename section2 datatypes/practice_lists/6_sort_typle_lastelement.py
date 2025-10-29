new_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def get_lst_element_of_typle(word):
    return word[-1]

def list_sorted(newlist):
    return sorted(newlist,key=get_lst_element_of_typle)

print(f"sorted typle by last element are {list_sorted(new_list)}")