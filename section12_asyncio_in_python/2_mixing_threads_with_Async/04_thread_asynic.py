import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# This is a normal (blocking) function — not async
def check_stock(item):
    print("Checking items in store...")
    time.sleep(3)  # Simulate a slow, blocking operation
    return f"Item found: {item}"

# Async function — runs inside the asyncio event loop
async def main():
    # Get the currently running event loop
    loop = asyncio.get_running_loop()

    # Create a thread pool so we can run blocking functions without freezing the async loop
    with ThreadPoolExecutor() as pool:
        # Run the blocking function in a separate thread
        # run_in_executor returns an awaitable Future
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")

    # Once the blocking task is done, print the result
    print(result)

# Start the asyncio program
asyncio.run(main())
