class InvalidChaiError(Exception): pass

def bill(flavour,cups):
    menu = {"masala":20,"ginger":40}
    try:
        if flavour not in menu:
            raise InvalidChaiError("that chai is not avilable")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an interger")
        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai :  rupees {total}")
    except Exception as e:
        print("Error",e)
    finally:
        print("Thnak you for visiting chai code!")
        
bill("mint",2)
bill("masala","three")
bill("ginger",3)
        
    