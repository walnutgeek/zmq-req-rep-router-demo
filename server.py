#!/usr/bin/env python3
"""
ZMQ REP Server using asyncio
Receives positive integer N, waits N % 3 + 1 seconds, returns N+1
"""

import asyncio
import zmq
import zmq.asyncio
import sys


async def main():
    """Main server function"""
    # Create asyncio context and REP socket
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.REP)

    # Bind to localhost on port 5555
    socket.bind("tcp://127.0.0.1:5555")
    print("Server started on tcp://127.0.0.1:5555")
    print("Waiting for requests...")

    try:
        while True:
            # Wait for request from client
            try:
                message = await socket.recv()
                n = int(message.decode('utf-8'))
                print(f"Received: {n}")

                # Calculate wait time: N % 3 + 1 seconds
                wait_time = n % 3 + 1
                print(f"Waiting {wait_time} seconds...")

                # Wait the calculated time
                await asyncio.sleep(wait_time)

                # Calculate response: N + 1
                response = n + 1
                print(f"Sending back: {response}")

                # Send response back to client
                await socket.send(str(response).encode('utf-8'))

            except ValueError:
                print("Invalid integer received, ignoring...")
                await socket.send(b"ERROR: Invalid integer")
            except Exception as e:
                print(f"Error processing request: {e}")
                break

    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        socket.close()
        context.term()


if __name__ == "__main__":
    asyncio.run(main())
