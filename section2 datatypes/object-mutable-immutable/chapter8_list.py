#lists
ingridents = ["water","milk","black tea"]
ingridents.append("sugar")
print(f"ingridents list are : {ingridents}")
ingridents.remove("water")
print(f"ingridents list are after removing : {ingridents}")



spice_options =["ginger","cardmon"]
chai_ingridents=["water","milk"]
chai_ingridents.extend(spice_options)
print(f"chai : {chai_ingridents}")

last_added = chai_ingridents.pop()
print(f"last added : {last_added}")

print(f"ingridents list are after removing : {ingridents}")
ingridents.insert(2,"WATER")
print(f"ingridents list are after removing : {ingridents}")


ingridents.reverse()
print(f"reverse => {ingridents}")
ingridents.sort()
print(f"sorted  => {ingridents}")

sugar_levels = [1,2,3,6,4,5]
print(f"maxium sugar level are : {max(sugar_levels)}")
print(f"minimum sugar level are : {min(sugar_levels)}")