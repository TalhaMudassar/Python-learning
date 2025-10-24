import threading 
import time

def moniter_tea_temprature():
    while True:
        print(f"Montering tea temprature ")
        time.sleep(2)
        
t = threading.Thread(target=moniter_tea_temprature)
t.start()

print("Main program done ")