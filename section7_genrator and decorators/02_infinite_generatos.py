def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        
refill = infinite_chai()

for _ in range(3):
    print(refill)