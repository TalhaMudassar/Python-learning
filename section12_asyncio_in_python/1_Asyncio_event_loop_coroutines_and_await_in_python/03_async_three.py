import asyncio
import aiohttp

# Asynchronous function to fetch a URL
async def fetch_url(session, url):
    """
    Fetch a URL asynchronously using aiohttp.
    Prints the URL and its HTTP response status.
    """
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")


# Main coroutine
async def main():
    """
    Creates an aiohttp session and concurrently fetches multiple URLs.
    """
    # List of URLs to fetch (same URL repeated 3 times)
    urls = ["https://httpbin.org/delay/2"] * 3

    # Create a single shared HTTP session
    async with aiohttp.ClientSession() as session:
        # Prepare coroutine tasks for each URL
        tasks = [fetch_url(session, url) for url in urls]

        # Run all tasks concurrently and wait for all to finish
        await asyncio.gather(*tasks)


# Entry point: start the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
