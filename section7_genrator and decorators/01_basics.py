def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"
    
    
chai = get_chai_gen()

print(f"Here are adress : ",chai,"here are value :",next(chai))
print(f"Here are adress : ",chai,"here are value :",next(chai))
print(f"Here are adress : ",chai,"here are value :",next(chai))
# print(f"Here are adress : ",chai,"here are value :",next(chai)) # gives the error