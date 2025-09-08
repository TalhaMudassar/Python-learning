# # while (value := input("Enter something: ")) != "quit":
# #     print(f"You typed: {value}")


# # value = 13
# # reminder = value  % 5

# # if reminder:
# #     print(f" not divisble ,reminder is {reminder}")

# value = 13 
# if (reminder := value % 5):
#     print(f" not divisble ,reminder is {reminder}")
    
# avaiable_size = ["small","medium","large"]

# if ( requested_Size := input("enter your chai cup size")) in  avaiable_size:
#     print(f"serving {requested_Size} chai")
# else:
#     print(f"size is unavilable - {requested_Size}")
  
flavours = ["masala","ginger","lemon","mint"]
print("Avilable flavour:",flavours)    
while(flavour := input("choose your flavour: ")) not in flavours:
    print(f"Sorry!  {flavour} : is not avilable ")
print(f"you choose the : {flavour} : flabour")
    