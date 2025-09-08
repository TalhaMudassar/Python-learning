class OutOfIngridentsError(Exception):
    pass

def make_chai(milk,sugar):
    if milk == 0 and sugar == 0:
        raise OutOfIngridentsError("Missing Milk or sugar")
    print("chai is ready")
    
make_chai(0,0)