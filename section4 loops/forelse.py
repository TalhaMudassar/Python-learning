staff = [("amit",16),("zara",13),("talha",22),("asif",)]

for name,age in staff:
    if age >=18:
        print(f"{name}is manage the staff")
        break
        
else:
    print("No one is eligible to manage the staff")
    