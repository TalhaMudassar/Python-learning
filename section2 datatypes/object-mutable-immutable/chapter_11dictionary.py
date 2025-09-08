#dictionary
chai_order = dict(type= "masala chai",size = "large" ,sugar = 2)
print(f"chai order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"recipe base :{chai_recipe['base']}")
print(f"recipe :{chai_recipe}")

del chai_recipe["liquid"]
print(f"Recipe : {chai_recipe}")


print(f"is sugar in the  order? {'sugar' in chai_order} ")

chai_order = dict(type= "Ginger chai1",size = "medium1" ,sugar = 1)
chai_order = dict(type= "Ginger chai2",size = "medium2" ,sugar = 2)
print(f"order detail (keys) :{chai_order.keys()}")  

print(f"order detail (values) :{chai_order.values()}")  

print(f"order detail (items) :{chai_order.items()}")  

last_item =  chai_order.popitem()
print(f"removed last item : {last_item}")

extra_specie = {"cardimum":"crushed" ,"ginger":"siliced"}
chai_recipe.update(extra_specie)
print(f"updated specie are : {chai_recipe}")


customer_note = chai_recipe.get("note","No note")
print(f"chai size is : {customer_note}")
 