def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai ....")
        if flavour == "unknown":
            raise ValueError("i dont know about this flavour")
    except ValueError as e:
        print("Error",e)   
    else:
        print(f"{flavour} chai is served")
    finally:
        print("Next Customer please ")
        
serve_chai("Masala")
print("----------------")
serve_chai("unknown")
        