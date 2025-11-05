# Flatten Shallow List
# Write a Python program to flatten a shallow list.

def flatten(my_list):
    return[x for y in my_list for x in y]   

original_lists = [[1,2,3],[4,5,6,7],[8,9],[21,22,23,24,25]]
print("Original List Elements")
print(original_lists)

print("Flatten List are :")
print(flatten(original_lists))
