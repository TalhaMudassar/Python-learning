class chai:
    origin = "india"

print(chai.origin)  # india
chai.is_hot = True
print(chai.is_hot)  #True
# creating object from class chai 
masala = chai()
print(f"Masala {masala.origin}") #masala {india}
print(f"Masala {masala.is_hot}") #masala {True}

print("-----------------------------------------")
masala.is_hot = False
print("Class: ",chai.is_hot)
print(f"Masala {masala.is_hot}")

masala.flavour = "masala"
print(masala.flavour)