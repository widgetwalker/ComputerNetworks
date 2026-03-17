## Lab 3 – Application-layer protocols (SMTP, FTP)

### Goals

- Observe simple application-layer protocols on top of TCP.
- Understand SMTP-style command/response and basic FTP actions.

### Pre-lab

- Read:
  - `python/04_application_layer/PROBLEM.md`
  - `smtp_socket_sim/` and `ftp_client/` READMEs.

### Tasks

1. **SMTP socket simulation**

   - Run the SMTP server and client on localhost.
   - Capture the conversation shown by server and client.
   - Locate the file where the message body is stored.

2. **SMTP via Ethereal (optional, requires internet)**

   - Use an Ethereal test account.
   - Send a test email and inspect the message in the Ethereal web UI.

3. **FTP client**

   - Connect to a public or test FTP server.
   - List the directory contents.
   - Download a small file.

### Questions

- How does the SMTP dialog differ from a simple raw socket echo?
- What information does the FTP client show about files and directories?

