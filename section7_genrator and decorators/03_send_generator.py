def chai_customer():
    print("! what chai would you like ")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield
        
stall = chai_customer()
next(stall) # start the generator

stall.send("Masala chai")
    