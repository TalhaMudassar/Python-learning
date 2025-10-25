from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock:bool = True
    
price_one = Product(id=1,name="laptop", price=999.9,in_stock=True)
price_one = Product(id=1,name="mouse", price=24.9)
price_one = Product(name="KEYBOARDD")#ERROR
