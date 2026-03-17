import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))
print("Connected to server.")

while True:
    msg = input("Client: ")
    if msg.lower() == "exit":
        break
    client_socket.send(msg.encode())
    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

client_socket.close()
