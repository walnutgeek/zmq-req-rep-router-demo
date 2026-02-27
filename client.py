#!/usr/bin/env python3
"""
ZMQ REQ Client using asyncio
Sends 10 random positive integers to server and quits
"""

import asyncio
import zmq
import zmq.asyncio
import random
import sys


async def main():
    """Main client function"""
    # Create asyncio context and REQ socket
    context = zmq.asyncio.Context()
    socket = context.socket(zmq.REQ)
    socket.setsockopt(zmq.LINGER, 0)

    # Connect to server
    socket.connect("tcp://127.0.0.1:5555")
    print("Client connected to tcp://127.0.0.1:5555")

    try:
        # Send 10 random positive integers
        for i in range(10):
            # Generate random positive integer (1-100)
            n = random.randint(1, 100)
            print(f"\nRequest {i+1}/10: Sending {n}")

            # Send request
            await socket.send(str(n).encode('utf-8'))

            # Wait for response (times out after 1s if server not listening)
            try:
                response = await asyncio.wait_for(socket.recv(), timeout=1.0)
                result = response.decode('utf-8')

                if result.startswith("ERROR"):
                    print(f"Server error: {result}")
                else:
                    response_num = int(result)
                    print(f"Received: {response_num}")

            except asyncio.TimeoutError:
                print("No response from server (timed out after 1s). Is the server running?")
                return
            except Exception as e:
                print(f"Error receiving response: {e}")
                break

        print("\nClient finished sending all requests!")

    except KeyboardInterrupt:
        print("\nClient interrupted by user")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        socket.close()
        context.term()


if __name__ == "__main__":
    asyncio.run(main())
