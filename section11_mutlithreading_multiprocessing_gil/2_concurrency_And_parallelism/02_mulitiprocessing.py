from multiprocessing import Process
import time

def brew_chai(name):
    print(f"start of {name} chai browing")
    time.sleep(3)
    print(f"End of {name}  chai browing")
    
    
if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai,args=(f"Chai Maker # {i+1}",))
        for i in range(3)       
    ]
    
    #start the process
    for p in chai_makers:
        p.start()
    
    #wait for all the process
    for p in chai_makers:
        p.join()
        
        
    print("All chai served ")
    
    