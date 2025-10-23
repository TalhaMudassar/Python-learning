import asyncio
import threading
import time

def background_threading():
    while True:
        time.sleep(1)
        print("Logging the system health win ")
        
async def fetch_order():
    await asyncio.sleep(3)
    print(f"order fetched ")
    
    
threading.Thread(target=background_threading, daemon=True).start()
asyncio.run(fetch_order())