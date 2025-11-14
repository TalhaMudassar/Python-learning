# Get Unique Values from List

my_list = [1,1,3,2,2,4,5,6,3,7,7,8,5,9,10,10]

print(f" Original list: {my_list}")
my_set = set(my_list)

my_new_list = list(my_set)

print(f"New list with unique elements: {my_new_list}")