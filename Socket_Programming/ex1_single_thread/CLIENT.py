import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))

print("Connected to Single Thread Server. Type 'exit' to quit.")

while True:
    msg = input("Enter message: ")
    client.send(msg.encode())
    
    if msg.lower() == 'exit':
        break
        
    data = client.recv(1024).decode()
    print("Server Response:", data)

client.close()
print("Client exiting.")
