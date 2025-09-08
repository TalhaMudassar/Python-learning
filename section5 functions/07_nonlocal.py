def update_order():
    chai_type = "elachi"
    def kitechen():
        nonlocal chai_type
        chai_type = "kesar"
    kitechen()
    print("After kitchen Update: ",chai_type)
    
update_order()