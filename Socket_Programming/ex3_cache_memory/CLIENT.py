import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5002))

print("--- Cache Client Connected ---")
print("Instructions: Request a key (e.g., 'user101'). Request it again to see CACHE HIT.")
print("Type 'exit' to quit.")

while True:
    key = input("\nEnter data key to fetch: ")
    client.send(key.encode())
    
    if key.lower() == 'exit':
        break
        
    start_time = time.time()
    response = client.recv(1024).decode()
    end_time = time.time()
    
    status, data = response.split(":", 1)
    
    print(f"Server Response Status: [{status}]")
    print(f"Data Received: {data}")
    print(f"Time Taken for Retrieval: {end_time - start_time:.4f} seconds")

client.close()
print("Client exiting.")
