## Problem: Application-layer protocols (SMTP, FTP)

### Definition

Demonstrate simple **application-layer** behavior on top of sockets or standard libraries:

- Custom SMTP-like dialog over raw sockets.
- Real SMTP using Ethereal test accounts.
- FTP client using `ftplib`.

### Assumptions

- Localhost or public test servers only (no sensitive credentials).
- Messages are small and text-based.

### Example questions

- How does the SMTP command/response flow look?
- How does a simple FTP client list and download files?

See each subfolder’s `PROBLEM.md` for protocol-specific details.

