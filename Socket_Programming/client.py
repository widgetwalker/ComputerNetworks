import socket

# Configuration (must match the server's HOST and PORT)
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print(f"Connected to server on {HOST}:{PORT}")
        
        # Send a message to the server
        message = "Hi server, I'm the client!"
        s.sendall(message.encode())
        print(f"Sent to server: {message}")
        
        # Receive the server's response
        data = s.recv(1024)
        print(f"Received from server: {data.decode()}")
        
    except ConnectionRefusedError:
        print("Connection refused. Ensure the server is running first.")

print("Client finished.")