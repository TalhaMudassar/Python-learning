#strings
chai_type = "ginger chai"
customer_name = "talha"
print(f"order for{customer_name} : {chai_type} please!")


#indexing
chai_description = "Aromatic and Bold"
print(f"First_word  with[0:8] : {chai_description[0:8]}")
print(f"First_word  with[0:8:1] :  {chai_description[0:8:1]}")
print(f"First_word  with[0:8:2] : {chai_description[0:8:2]}")
print(f"First_word  with[:8] : {chai_description[:8]}")
    # take character and after that character printing all 
print(f"word with [3:] :{chai_description[3:]}")
    # here we reverse the string 
print(f"revverse the string using [::-1]{chai_description[::-1]}")



#encoded label
chai_des = "pyth𝔄n"
encoded_des = chai_des.encode(utf-8)
 