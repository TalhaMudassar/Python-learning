# Python: Generate and print a list of first and last 5 elements 
# where the values are square of numbers between two numbers

def generate_print():
    l = list()
    for i in range(1,21):
        multiplier = (i**2)
        l.append(multiplier)
        
    print(l[:5])
        
    print(l[-5:])
        
generate_print()