#tuples
masala_species =("cardmom","cloves","cinnamon")
(specie1,specie2,specie3) = masala_species
print(f"Main masala species : {specie1,specie2,specie3}")


ginger_ratio ,cardmon_ratio = (2,1)
print(f"ratio  is G:{ginger_ratio} and C :{cardmon_ratio}")
ginger_ratio ,cardmon_ratio=cardmon_ratio,ginger_ratio
print(f"ratio  is G:{ginger_ratio} and C :{cardmon_ratio}")


#membership
print(f"is cinnamon in masala specie ? {"cinnamon" in masala_species}")