## Problem: Basic FTP client

### Definition

Use Python's `ftplib` to:

- Connect to an FTP server.
- List directory contents.
- Optionally download a file.

### Assumptions

- Public or test FTP server only.
- Anonymous login or test credentials.

### Sample interaction

| Step | Action                    |
|------|---------------------------|
| 1    | Connect to FTP host      |
| 2    | Log in (user/password)   |
| 3    | Run `LIST` to show files |
| 4    | Download a test file     |

### Pseudocode

```text
connect to FTP(host)
login(user, password) or anonymous
print directory listing
optionally retrieve a file to local disk
quit
```

