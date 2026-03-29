import socket
import time

# Dictionary to act as our server-side cache memory
server_cache = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5002))  # Using Port 5002 for Cache Experiment
server.listen(1)

print("[CACHE SERVER] Waiting for client on port 5002...")
conn, addr = server.accept()
print(f"[CACHE SERVER] Connected to: {addr}")

while True:
    try:
        key = conn.recv(1024).decode()
        if not key or key.lower() == 'exit':
            break
            
        print(f"\n[CACHE SERVER] Request for key: '{key}'")
        
        # Check if data is already in cache
        if key in server_cache:
            print(" -> [CACHE HIT] Data found in cache. Sending instantly.")
            response = f"HIT:{server_cache[key]}"
        else:
            print(" -> [CACHE MISS] Data not found. Simulating slow fetch (2s)...")
            time.sleep(2)  # Simulating a slow database/resource fetch
            data = f"Value_for_{key}"
            server_cache[key] = data
            response = f"MISS:{data}"
            
        conn.send(response.encode())
    except ConnectionResetError:
        break

conn.close()
server.close()
print("[CACHE SERVER] Server shut down.")
