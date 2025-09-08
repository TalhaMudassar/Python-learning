class chai:
    temprature = "hot"
    strenght = "strong"
    
cutting = chai()
print(cutting.temprature)

cutting.temprature = "Mild"
cutting.cup = "small"
print(f"After Changing",cutting.temprature)
print("cup size is",cutting.cup)
print("Direct look into the class",chai.temprature)

del cutting.temprature
del cutting.cup


print(cutting.temprature)
print(cutting.cup)  #attribute error 