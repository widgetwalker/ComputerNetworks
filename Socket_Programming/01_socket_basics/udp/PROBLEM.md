## Problem: UDP message exchange

### Definition

Demonstrate **connectionless** communication using UDP where:

- A server waits for datagrams.
- A client sends short messages without establishing a connection.

### Assumptions

- Both processes run on **localhost**.
- Messages may be lost or arrive out of order (in real networks).
- This lab assumes simple, short messages with no reliability mechanism.

### Sample interaction

| Step | Side   | Example message |
|------|--------|-----------------|
| 1    | Client | `hello`         |
| 2    | Server | prints `hello`  |
| 3    | Client | `exit`          |
| 4    | Server | exits loop      |

### Pseudocode (server)

```text
create UDP socket
bind to (localhost, port)
loop:
    recvfrom data, addr
    if data == "exit": break
    print data and addr
close socket
```

