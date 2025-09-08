class chaiorder:
    def __init__(self,type_,size):
        self.type = type_
        self.size = size
        
    def summary(self):
        return f"{self.size} ml of {self.type} chai"
    
order = chaiorder("Malsala",2000)
print(order.summary())

order1 = chaiorder("LEMON",1000)
print(order1.summary())