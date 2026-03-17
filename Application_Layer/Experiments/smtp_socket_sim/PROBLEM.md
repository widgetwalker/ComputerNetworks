## Problem: SMTP-like dialog over raw sockets

### Definition

Implement a **very simplified SMTP conversation** using your own TCP server and client:

- Server sends greeting and responds to commands.
- Client sends commands like `HELO`, `MAIL FROM`, `RCPT TO`, `DATA`, `QUIT`.

### Assumptions

- All communication is on `127.0.0.1` on a fixed port.
- Protocol is simplified and not RFC-compliant.
- Message body is short and saved to a local file.

### Sample interaction (high level)

| Step | Side   | Line sent                     |
|------|--------|-------------------------------|
| 1    | Server | `220 Simple SMTP ready`       |
| 2    | Client | `HELO localhost`              |
| 3    | Server | `250 Hello`                   |
| 4    | Client | `MAIL FROM:<alice@example>`   |
| ...  | ...    | ...                           |

### Pseudocode (server, simplified)

```text
accept connection
send greeting
loop:
    recv line
    parse command
    update state (MAIL FROM, RCPT TO, DATA)
    send appropriate reply
    if command == QUIT: break
write message body to file
close connection
```

