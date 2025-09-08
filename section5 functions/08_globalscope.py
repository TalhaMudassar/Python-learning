chai_type = "plain"

def front_Desk():
    def kitchen():
        global chai_type
        chai_type = "Irani"
        
    kitchen()
    
    
front_Desk()
print(f"Final global chai:  {chai_type}")