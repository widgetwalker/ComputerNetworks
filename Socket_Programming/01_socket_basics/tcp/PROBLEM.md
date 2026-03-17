## Problem: TCP chat and request–response

### Definition

Implement **connection-oriented communication** where a TCP server and client:

- Establish a reliable connection.
- Exchange messages interactively or in a single request–response round.

### Assumptions

- Both server and client run on **localhost**.
- Server must be started **before** the client.
- Only one client connects at a time.

### Sample interaction (interactive chat)

| Step | Side   | Example message |
|------|--------|-----------------|
| 1    | Client | `hello`         |
| 2    | Server | `hi there`      |
| 3    | Client | `bye`           |
| 4    | Both   | Close sockets   |

### Pseudocode (client)

```text
create TCP socket
connect to (localhost, port)
loop:
    read line from keyboard
    send line
    if line == "bye": break
    recv reply
    print reply
close socket
```

