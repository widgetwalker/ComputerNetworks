import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5001))

client_id = sys.argv[1] if len(sys.argv) > 1 else "Unknown"
print(f"Connected as {client_id}. Type 'exit' to quit.")

while True:
    msg = input(f"[{client_id}] Enter message: ")
    client.send(msg.encode())
    
    if msg.lower() == 'exit':
        break
        
    data = client.recv(1024).decode()
    print("Server Response:", data)

client.close()
print(f"Client {client_id} exiting.")
