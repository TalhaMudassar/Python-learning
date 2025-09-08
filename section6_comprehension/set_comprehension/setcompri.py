# favourite_chai = [
#     "Masala chai","Green Tea","Masala chai",
#     "Lemon Tea","Green Tea","Elachi chai"
# ]

# unique_chai = {chai for chai in favourite_chai if len(chai) > 8}
# print(unique_chai)


Recipes = {
    "Masala chai" : ["ginger","cardmon","sinamon"],
    "Elachi chai" : ["cardmon","milk"],
    "Spicy chai" : ["ginger","black paper","sinamon"],
}
unique_spice = {speice for ingridents in Recipes.values() for speice in ingridents}
print(unique_spice)