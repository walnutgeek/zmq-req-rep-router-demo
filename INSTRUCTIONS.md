# ZMQ REQ/REP Demo - Setup and Usage Instructions

## Project Overview

This project demonstrates the ZeroMQ REQ/REP (Request-Reply) pattern using Python's asyncio and pyzmq library. The server receives positive integers, waits a calculated amount of time, and returns the incremented value.

## Prerequisites

- Python 3.9 or higher
- `uv` package manager (install from https://docs.astral.sh/uv/)

## Setup Instructions

1. **Clone or extract the project**:
   ```bash
   cd zmq-req-rep-demo
   ```

2. **Install dependencies using uv**:
   ```bash
   uv sync
   ```
   This will create a virtual environment and install pyzmq.

3. **Verify installation**:
   ```bash
   uv run test.py
   ```

## Usage

### Method 1: Run Server and Client Separately (Recommended)

1. **Start the server** in one terminal:
   ```bash
   uv run server.py
   ```
   You should see:
   ```
   Server started on tcp://127.0.0.1:5555
   Waiting for requests...
   ```

2. **Start the client** in another terminal:
   ```bash
   uv run client.py
   ```
   The client will send 10 random integers and display the responses.

### Method 2: Run Demo Script

Run both server and client automatically:
```bash
uv run demo.py
```

## Expected Behavior

### Server Output Example:
```
Server started on tcp://127.0.0.1:5555
Waiting for requests...
Received: 42
Waiting 1 seconds...
Sending back: 43
Received: 17
Waiting 3 seconds...
Sending back: 18
...
```

### Client Output Example:
```
Client connected to tcp://127.0.0.1:5555

Request 1/10: Sending 42
Received: 43

Request 2/10: Sending 17
Received: 18
...
Client finished sending all requests!
```

## How It Works

1. **Server Logic**:
   - Receives positive integer N from client
   - Calculates wait time: `N % 3 + 1` seconds (1-3 seconds)
   - Waits the calculated time
   - Returns `N + 1` to client
   - Prints received N and sent response

2. **Client Logic**:
   - Connects to server on localhost:5555
   - Sends 10 random positive integers (1-100)
   - Waits for each response before sending next request
   - Prints sent and received values

## Technical Details

- **Pattern**: ZeroMQ REQ/REP (Request-Reply)
- **Transport**: TCP on localhost:5555
- **Async Framework**: Python asyncio
- **Library**: pyzmq >= 26.0.0

## Troubleshooting

1. **"Address already in use" error**:
   - Make sure no other process is using port 5555
   - Wait a few seconds and try again

2. **Import errors**:
   - Run `uv sync` to install dependencies
   - Ensure you're using `uv run` to execute scripts

3. **Connection refused**:
   - Make sure the server is running before starting the client
   - Check that both use the same address (127.0.0.1:5555)

## Files Description

- `server.py`: REP socket server implementation
- `client.py`: REQ socket client implementation  
- `demo.py`: Runs both server and client for demonstration
- `test.py`: Validates server calculation logic
- `pyproject.toml`: Project configuration and dependencies
- `README.md`: Basic project description
- `.python-version`: Python version specification for uv

## Customization

To modify the behavior:

1. **Change port**: Update both server.py and client.py with new port number
2. **Change wait formula**: Modify the calculation in server.py
3. **Change number of requests**: Update the range in client.py
4. **Change random range**: Modify `random.randint(1, 100)` in client.py
