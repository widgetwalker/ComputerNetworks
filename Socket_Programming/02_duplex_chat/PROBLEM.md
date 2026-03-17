## Problem: Duplex communication (chat)

### Definition

Compare **half-duplex** and **full-duplex** chat over TCP:

- Half-duplex: only one side talks at a time (turn-based).
- Full-duplex: both sides can send and receive concurrently (threads).

### Assumptions

- Communication over **localhost**.
- Single client connects to a single server.
- Messages are plain text, ended by newline.

### Sample interaction (half-duplex)

| Step | Side   | Example action           |
|------|--------|--------------------------|
| 1    | Client | sends `hello`           |
| 2    | Server | prints `hello`, replies |
| 3    | Client | prints reply            |
| 4    | Either | sends `bye` to close    |

### Pseudocode (full-duplex side)

```text
start TCP connection (server or client)
start thread A: loop receiving messages and printing them
start thread B: loop reading keyboard input and sending it
if user types "bye":
    close socket and stop both loops
```

