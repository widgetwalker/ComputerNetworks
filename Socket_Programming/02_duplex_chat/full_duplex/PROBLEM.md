## Problem: Full-duplex TCP chat

### Definition

Implement a **simultaneous two-way chat** over TCP using threads:

- One thread handles receiving.
- One thread handles sending user input.

### Assumptions

- Server starts before the client.
- Both sides may type at any time.
- Typing `bye` on either side gracefully closes the connection.

### Sample interaction

| Step | Side   | Message    |
|------|--------|------------|
| 1    | Client | `hello`    |
| 2    | Server | `yo`       |
| 3    | Both   | can type freely |

### Pseudocode (simplified)

```text
on connection established:
    start receiver thread:
        loop: recv and print messages
    start sender loop:
        loop: read from keyboard and send
        if "bye": close socket
```

