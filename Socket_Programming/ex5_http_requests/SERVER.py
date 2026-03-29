import socket
import json

# Minimal HTTP Server response
HTTP_RESPONSE = """HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: *

{{
  "status": "success",
  "message": "Hello from your local Python HTTP Server!",
  "your_data": {data}
}}
"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5004))
server.listen(5)

print("[HTTP SERVER] Listening on http://localhost:5004")

while True:
    try:
        conn, addr = server.accept()
        request = conn.recv(1024).decode()
        
        if not request: break
        
        print(f"\n[HTTP SERVER] Received Request from {addr}")
        # Extract basic info
        lines = request.split("\n")
        method = lines[0].split(" ")[0]
        print(f"Method: {method}")
        
        # Create a mock response
        body = json.dumps({"method_received": method, "server_info": "Python Socket HTTP"})
        response = HTTP_RESPONSE.format(data=body)
        
        conn.sendall(response.encode())
        conn.close()
    except KeyboardInterrupt:
        break

server.close()
print("[HTTP SERVER] Server closed.")
