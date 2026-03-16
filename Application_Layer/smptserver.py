import socket

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)
print("[Server] Waiting for client connection...")

conn, addr = server.accept()
print(f"[Server] Connected with {addr}\n")

conn.send(b"220 Simple SMTP Server Ready\r\n")

mail_data = []

while True:
    data = conn.recv(1024).decode().strip()
    if not data:
        break

    print(f"[Client]: {data}")

    if data.upper().startswith("HELO"):
        conn.send(b"250 Hello, pleased to meet you\r\n")
    elif data.upper().startswith("MAIL FROM"):
        conn.send(b"250 OK - Sender accepted\r\n")
    elif data.upper().startswith("RCPT TO"):
        conn.send(b"250 OK - Receiver accepted\r\n")
    elif data.upper().startswith("DATA"):
        conn.send(b"354 End data with <CR><LF>.<CR><LF>\r\n")
    elif data == ".":
        conn.send(b"250 Message accepted for delivery\r\n")
        # Save message to file
        with open("received_mail.txt", "w") as f:
            f.write("\n".join(mail_data))
        print("[Server] Message saved to received_mail.txt\n")
        mail_data.clear()
    elif data.upper().startswith("QUIT"):
        conn.send(b"221 Closing connection\r\n")
        break
    else:
        # Treat as part of email content
        mail_data.append(data)
        conn.send(b"250 OK\r\n")

conn.close()
server.close()
print("[Server] Connection closed.")