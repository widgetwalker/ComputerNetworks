## Problem: Socket basics (TCP vs UDP)

### Definition

Introduce simple **client–server communication** using:

- **TCP** (connection-oriented, reliable byte stream).
- **UDP** (connectionless, best-effort datagrams).

### Assumptions

- All programs run on **localhost**.
- Fixed ports are used, hard-coded in the scripts.
- One client and one server per demo.

### Sample interaction (TCP chat)

| Step | Side   | Action                  |
|------|--------|-------------------------|
| 1    | Server | Listens and accepts     |
| 2    | Client | Connects and sends text |
| 3    | Server | Prints and replies      |
| 4    | Either | Types `bye` to close    |

### Pseudocode (TCP server)

```text
create TCP socket
bind to (localhost, port)
listen for connection
accept client
loop:
    recv data
    if data is empty or "bye": break
    display data
    read reply from keyboard
    send reply
close sockets
```

### Pseudocode (UDP server)

```text
create UDP socket
bind to (localhost, port)
loop:
    recvfrom data, client_addr
    if data is "exit": break
    display data
    (optionally) send response with sendto
close socket
```

