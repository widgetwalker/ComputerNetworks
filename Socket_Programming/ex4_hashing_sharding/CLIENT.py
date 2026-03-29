import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5003))

print("--- Sharding & Hashing Cluster Client ---")
print("Commands: 'PUT:key:value' (e.g., PUT:user1:Alice) or 'GET:key'")
print("Type 'exit' to quit.")

while True:
    cmd_input = input("\nEnter Command: ")
    if cmd_input.lower() == 'exit':
        client.send(b"exit")
        break
        
    client.send(cmd_input.encode())
    response = client.recv(1024).decode()
    print(f"Cluster Response: {response}")

client.close()
print("Client exiting.")
