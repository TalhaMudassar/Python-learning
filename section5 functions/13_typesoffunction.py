 #pure function
 
def pure_function(cups):
    return cups * 10


total_cups = 0
#impure functions
def impure_function(cups):
    global total_cups
    total_cups += cups
    
 
 
 #recusive function
def recursive_function(n):
    if n == 0:
        return "all cup pored "
    print(n)
    return recursive_function(n-1)

print(recursive_function(5))