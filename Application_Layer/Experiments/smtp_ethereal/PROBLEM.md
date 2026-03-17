## Problem: Sending email via Ethereal SMTP

### Definition

Use Python's `smtplib` to send an email through an **Ethereal test SMTP server**:

- Log in with temporary credentials.
- Compose a simple subject + body.
- Send to a test recipient.

### Assumptions

- Only Ethereal test credentials are used (no real accounts).
- Network access to the Ethereal SMTP host is available.

### Sample flow

| Step | Action                             |
|------|------------------------------------|
| 1    | Load SMTP host, port, user, pass  |
| 2    | Connect and start TLS (if needed) |
| 3    | Log in                            |
| 4    | Send message                      |

### Pseudocode

```text
create SMTP client
connect to (host, port)
start TLS if required
login(user, password)
create MIME message
sendmail(from_addr, to_addrs, message)
quit
```

