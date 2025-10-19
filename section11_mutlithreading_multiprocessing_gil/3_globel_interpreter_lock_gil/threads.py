import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} start brewing...")
    count = 0
    # Simulate a time-consuming CPU-bound task
    for _ in range(100_000_00): 
        count += 1
    # FIX: Access 'name' as an attribute
    print(f"{threading.current_thread().name} finish brewing")
    
    
thread_1 = threading.Thread(target=brew_chai, name="Barister_1")
thread_2 = threading.Thread(target=brew_chai, name="Barister_2")


start = time.time()
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
end = time.time()

print(f"total time taken: {end - start:.2f} seconds ")