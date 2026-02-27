# ZMQ REQ/REP/ROUTER Demo

A simple demonstration of ZeroMQ REQ/REP vs ROUTER pattern using pyzmq with asyncio.

## Installation

```bash
uv sync
```

## Usage

Run the server REP server:
```bash
uv run server.py
```


Run the server ROUTER server:
```bash
uv run router_server.py
```

In another terminals, run the client:
```bash
uv run client.py
```

## Description

- **Server**: Receives positive integers N, waits `N % 3 + 1` seconds, returns `N+1`
- **Client**: Sends 10 random positive integers to server and quits

The server prints each received N and the number sent back after the wait time.
