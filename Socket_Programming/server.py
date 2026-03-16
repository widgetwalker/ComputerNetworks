import socket

# Configuration
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    
    # Wait for a connection
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        
        # Receive data from the client
        data = conn.recv(1024)
        if data:
            print(f"Received from client: {data.decode()}")
        
        # Send a response back to the client
        message = "Hello, client! Connection closed."
        conn.sendall(message.encode())
        
        print("Sent response and closing connection with client.")

print("Server finished.")