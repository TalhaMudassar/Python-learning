chai_menu = {"masala":30,"giger":40}
# chai_menu["Elachi"] #key error
#tru except
try:
    chai_menu["Elachi"] 
except KeyError:
    print("The key that you are trying to access does not exist")
    
print("hello chai code ")
    