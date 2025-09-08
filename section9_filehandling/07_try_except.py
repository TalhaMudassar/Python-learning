# file = open("order.txt","w")

# try:
#     file.write("Masala chai - 2 cups")
# except:
#     file.close()

#her are the method 2:
with open("order.txt","w") as file:
    file.write("ginger tea -4 cups")
    
    
