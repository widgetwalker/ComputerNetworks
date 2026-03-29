import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting for connection on port 5000...")
conn, addr = server.accept()
print("Connected to:", addr)

while True:
    try:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print("Exit signal received.")
            break
        print("Client:", data)
        msg = f"ACK: Received '{data}'"
        conn.send(msg.encode())
    except ConnectionResetError:
        break

conn.close()
server.close()
print("Server closed.")
