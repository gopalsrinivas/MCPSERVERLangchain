import asyncio
from multiprocessing import Process
import os
import sys

# print(sys.executable)


def run_math_server():
    """Start math server in separate process"""
    from servers.math_server import mcp

    mcp.run(transport="stdio")


def run_weather_server():
    """Start weather server in separate process"""
    from servers.weather_server import mcp

    mcp.run(transport="streamable-http")


async def run_client():
    """Run the client application"""
    from client.client import main

    await main()


async def main():
    # Start servers
    math_proc = Process(target=run_math_server)
    weather_proc = Process(target=run_weather_server)

    math_proc.start()
    weather_proc.start()

    # Wait for servers to initialize
    await asyncio.sleep(2)

    try:
        await run_client()

        print("✅ Servers are running. Press Ctrl+C to stop...")
        await asyncio.Event().wait()  # Keeps running until manually stopped

    except KeyboardInterrupt:
        print("🔴 KeyboardInterrupt received. Shutting down...")

    finally:
        math_proc.terminate()
        weather_proc.terminate()
        math_proc.join()
        weather_proc.join()
        print("🔁 Servers terminated cleanly.")


if __name__ == "__main__":
    asyncio.run(main())
