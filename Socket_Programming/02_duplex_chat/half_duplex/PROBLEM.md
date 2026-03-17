## Problem: Half-duplex TCP chat

### Definition

Implement a **turn-based** chat over TCP:

- Server receives first, then replies.
- Client sends first, then waits for reply.

### Assumptions

- Server starts before the client.
- Only one message in flight at a time.
- Typing `bye` ends the conversation.

### Sample interaction

| Step | Side   | Message    |
|------|--------|------------|
| 1    | Client | `hello`    |
| 2    | Server | `hi`       |
| 3    | Client | `bye`      |
| 4    | Both   | connection closes |

### Pseudocode (server)

```text
accept connection
loop:
    recv message
    if message == "bye": break
    print message
    read reply
    send reply
close sockets
```

