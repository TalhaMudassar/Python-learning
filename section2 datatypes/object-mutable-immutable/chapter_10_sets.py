#sets 
essencial_Species= {"cardimom","ginger","specie"}
optional_species= {"colve","ginger","black paper"}

# union are 
all_specie = essencial_Species | optional_species
print(f"All specie are : {all_specie}")


#intersection
intersection_specie = essencial_Species & optional_species
print(f"intersection are : {intersection_specie}")

#difference
only_in_essential = essencial_Species - optional_species
print(f"difference are : {only_in_essential}")

print(f"is 'colve' in essential specie : {'colve' in optional_species} ")

