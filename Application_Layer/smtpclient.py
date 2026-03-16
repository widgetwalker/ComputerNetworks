import socket
import time

HOST = "127.0.0.1"
PORT = 8080

sender = input("Enter sender email: ")
receiver = input("Enter receiver email: ")
subject = input("Enter subject: ")
message = input("Enter message: ")

client = socket.socket()
client.connect((HOST, PORT))

print("\n[Client] Connected to SMTP server...")
print("[Server]:", client.recv(1024).decode().strip())

def send_cmd(cmd):
    print(f"[Client] >> {cmd}")
    client.send((cmd + "\r\n").encode())
    reply = client.recv(1024).decode().strip()
    print(f"[Server]: {reply}\n")
    time.sleep(0.3)

# ---- Step 3: SMTP conversation ----
send_cmd("HELO localhost")
send_cmd(f"MAIL FROM:<{sender}>")
send_cmd(f"RCPT TO:<{receiver}>")
send_cmd("DATA")

# ---- Step 4: Send message ----
print("[Client] Sending email content...")
client.send(f"Subject: {subject}\r\n".encode())
client.send(f"From: {sender}\r\n".encode())
client.send(f"To: {receiver}\r\n".encode())
client.send(f"\r\n{message}\r\n".encode())
client.send(b".\r\n")

reply = client.recv(1024).decode().strip()
print(f"[Server]: {reply}\n")

# ---- Step 5: Quit ----
send_cmd("QUIT")

client.close()
print("[Client] Connection closed.\n✅ Email simulation complete!")