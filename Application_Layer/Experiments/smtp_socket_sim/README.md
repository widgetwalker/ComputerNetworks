## SMTP socket simulation (very simplified)

### Table of contents

- [Programs](#programs)
- [Notes](#notes)
- [How to run](#how-to-run)

### Programs

- **`smtp_server.py`**: listens on `127.0.0.1:8080` and responds to basic SMTP commands
- **`smtp_client.py`**: connects to the server and performs a simple SMTP-style dialog

### Notes

The server writes the received mail content to `received_mail.txt` in the folder where you run the server.

### How to run

In terminal 1:

```bash
python smtp_server.py
```

In terminal 2:

```bash
python smtp_client.py
```

