class tealeaf:
    def __init__(self,age):
        self._age = age
        
    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self,age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea age must be bw 1 and 5")
    
leaf = tealeaf(2)
print(leaf.age)

# leaf.age = 6  it shows the error 
print(leaf.age)
    