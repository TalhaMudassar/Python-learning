seat_type = input("Enter seat type (sleeper /AC/General/Luxery)").lower()

match seat_type:
    case "sleeper":
        print("sleeper - No AC, beds avaiable")
    case "ac":
        print("AC- air conditioner comfy ride")
    case "general":
        print("general -cheaper option no  reservation")
    case "luxery":
        print("luxery = premium seats with meal")
    case _:
        print("invalid seat type")