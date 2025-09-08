def server_chai():
    chai_type = "masala"
    print(f"inside function  {chai_type}")
    
    
chai_type = "Lemon"
server_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon" # enclosing scope 
    def print_order():
        chai_order = "ginger"
        print("inner:",chai_order)
    print_order()   
    print("Outer : ",chai_order)
    
chai_order = "tulsi" # Globel scope
chai_counter()
print("Global :",chai_order)