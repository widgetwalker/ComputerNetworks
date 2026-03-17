import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8888))
server_socket.listen(1)
print("TCP Server is waiting for connection...")

conn, addr = server_socket.accept()
print("Connected to:", addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Client:", data)
    reply = input("Server: ")
    conn.send(reply.encode())

conn.close()
server_socket.close()
