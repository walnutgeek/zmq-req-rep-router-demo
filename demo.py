#!/usr/bin/env python3
"""
Demo script showing how to run the ZMQ REQ/REP example
This script runs both server and client concurrently for demonstration
"""

import asyncio
import subprocess
import sys
import time


async def run_server():
    """Run the server process"""
    print("Starting server...")
    process = await asyncio.create_subprocess_exec(
        sys.executable, "server.py",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # Read server output
    while True:
        line = await process.stdout.readline()
        if not line:
            break
        print(f"[SERVER] {line.decode().strip()}")


async def run_client():
    """Run the client process after a delay"""
    # Wait for server to start
    await asyncio.sleep(2)

    print("Starting client...")
    process = await asyncio.create_subprocess_exec(
        sys.executable, "client.py",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # Read client output
    while True:
        line = await process.stdout.readline()
        if not line:
            break
        print(f"[CLIENT] {line.decode().strip()}")

    await process.wait()
    return process.returncode


async def main():
    """Run both server and client"""
    print("ZMQ REQ/REP Demo")
    print("=" * 50)

    # Start server and client concurrently
    server_task = asyncio.create_task(run_server())
    client_task = asyncio.create_task(run_client())

    # Wait for client to finish
    client_result = await client_task

    # Give server a moment to process final request
    await asyncio.sleep(1)

    # Cancel server task
    server_task.cancel()

    try:
        await server_task
    except asyncio.CancelledError:
        pass

    print("=" * 50)
    print("Demo completed!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
