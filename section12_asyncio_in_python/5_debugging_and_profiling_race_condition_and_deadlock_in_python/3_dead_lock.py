import threading
lock_a = threading.Lock()
lock_b = threading.Lock()

def task_1():
    with lock_a:
        print("Task 1 is acquired lock a ")
        with lock_b:
            print("Task 1 accquired lock b")
            

def task_2():
    with lock_a:
        print("Task 1 is acquired lock a ")
        with lock_b:
            print("Task 1 accquired lock b")
            
            
t1 = threading.Thread(target=task_1)
t2 = threading.Thread(target=task_2)

t1.start()
t2.start()