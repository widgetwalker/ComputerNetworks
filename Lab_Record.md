# Computer Networks Lab Record

## Index
1. **Experiment 1:** Single Threading in a Socket Layer using Python
2. **Experiment 2:** Multiple Threading in a Socket Layer using Python
3. **Experiment 3:** Cache Memory Mechanism using Python
4. **Experiment 4:** Hashing and Sharding Work using Python
5. **Experiment 5:** Implementing HTTP using the Requests Library in Python
6. **Experiment 6:** Implementing SMTP Protocol in a Server-Client Architecture using Python

---

## 1. Single Threading in a Socket Layer using Python

### Aim
To write a Python program to implement single threading in a socket layer architecture (Server-Client communication).

### Procedure
1.  **Initialize Socket**: Create a server script that initializes a TCP socket using `socket.AF_INET` and `socket.SOCK_STREAM` protocols.
2.  **Bind and Listen**: Bind the server to a local IP address (localhost) and a specific port (e.g., 5000) and set the server to listen for one connection at a time using `server.listen(1)`.
3.  **Establish Connection**: Implement the `accept()` method to wait for an incoming client request and establish a dedicated communication channel upon connection.
4.  **Data Exchange**: Create a client script to connect to the server's IP and port. Use a `while` loop in both scripts to exchange string-based data encoded in a standard format (UTF-8).
5.  **Interactive Logic**: Allow the user to manually input messages in the client terminal and receive dynamic acknowledgment responses from the server.
6.  **Closure Protocol**: Ensure both the client and server scripts can detect an 'exit' signal to gracefully close the socket connections and release system resources.

### Code (`Socket_Programming/ex1_single_thread/SERVER.py`)
```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)

print("Server waiting for connection on port 5000...")
conn, addr = server.accept()
print("Connected to:", addr)

while True:
    try:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print("Exit signal received.")
            break
        print("Client:", data)
        msg = f"ACK: Received '{data}'"
        conn.send(msg.encode())
    except ConnectionResetError:
        break

conn.close()
server.close()
print("Server closed.")
```

### Code (`Socket_Programming/ex1_single_thread/CLIENT.py`)
```python
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
```

### Result
The implementation of a single-threaded server-client model using Python sockets was successful. The server handled requests sequentially, maintaining a dedicated link with a single client as intended.

---

## 2. Multiple Threading in a Socket Layer using Python

### Aim
To write a Python program to implement multiple threading in a socket layer, allowing the server to handle multiple clients concurrently.

### Procedure
1.  **Thread Handler Setup**: Define a dedicated handler function `handle_client` that contains the communication logic for a single client, isolated from the main server loop.
2.  **Server Initialization**: Initialize a TCP server socket and bind it to a port (e.g., 5001), setting the backlog to support multiple queued connections via `server.listen(5)`.
3.  **Concurrency Loop**: Implement an infinite `while` loop that continuously waits for new connection requests using the `accept()` method.
4.  **Thread Instantiation**: For every successful connection, instantiate a new `threading.Thread` object, passing the specific client connection and the handler function.
5.  **Parallel Execution**: Start the thread using `thread.start()`, allowing the server to immediately return to the `accept()` state to handle the next client without waiting for the previous one to finish.
6.  **Resource Monitoring**: Print the current count of active threads using `threading.active_count()` to verify that multiple client connections are being processed in parallel.

### Code (`Socket_Programming/ex2_multi_thread/SERVER.py`)
```python
import socket
import threading

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data or data.lower() == 'exit':
                break
            print(f"[{addr}] Client says: {data}")
            msg = f"ACK from Multi-thread Server for: {data}"
            conn.send(msg.encode())
        except ConnectionResetError:
            break
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5001))
server.listen(5)

print("[STARTING] Multi-threaded server is starting on port 5001...")

try:
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
except KeyboardInterrupt:
    print("\n[STOPPING] Server is shutting down.")
finally:
    server.close()
```

### Code (`Socket_Programming/ex2_multi_thread/CLIENT.py`)
```python
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
```

### Result
Multi-threaded server architecture was successfully implemented, demonstrating that multiple concurrent clients can communicate with the server independently without blocking each other.

---

## 3. Cache Memory Mechanism using Python

### Aim
To write a Python program to demonstrate the working of cache memory using a server-side dictionary to store and retrieve frequently accessed data efficiently.

### Procedure
1.  **Cache Storage Setup**: Initialize a global dictionary on the server side to serve as the high-speed Cache Memory for storing processed results.
2.  **Server Logic**: Implement a server that listens on port 5002 and accepts a data "key" from the client (representing a request for specific information).
3.  **Cache Search**: Upon receiving a key, the server first searches the local dictionary. If the key exists (Cache Hit), the server retrieved the value instantly to send back.
4.  **Latency Simulation**: If the key is missing (Cache Miss), simulate a slow retrieval process (e.g., from a database) using `time.sleep(2)` before storing the new value in the cache.
5.  **Timed Retrieval**: In the client script, implement a timing mechanism using `time.time()` to measure the interval between sending a request and receiving the response.
6.  **Efficiency Verification**: Contrast the 2-second delay of the first request (Miss) with the near-zero delay of the second request for the same key (Hit) to demonstrate performance gains.

### Code (`Socket_Programming/ex3_cache_memory/SERVER.py`)
```python
import socket
import time

server_cache = {}
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5002))
server.listen(1)

print("[CACHE SERVER] Waiting for client on port 5002...")
conn, addr = server.accept()

while True:
    try:
        key = conn.recv(1024).decode()
        if not key or key.lower() == 'exit': break
        if key in server_cache:
            response = f"HIT:{server_cache[key]}"
        else:
            time.sleep(2)
            data = f"Value_for_{key}"
            server_cache[key] = data
            response = f"MISS:{data}"
        conn.send(response.encode())
    except ConnectionResetError: break

conn.close()
server.close()
```

### Code (`Socket_Programming/ex3_cache_memory/CLIENT.py`)
```python
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5002))

while True:
    key = input("\nEnter data key to fetch: ")
    client.send(key.encode())
    if key.lower() == 'exit': break
    
    start = time.time()
    response = client.recv(1024).decode()
    end = time.time()
    
    status, data = response.split(":", 1)
    print(f"Status: [{status}] | Time: {end - start:.4f}s")

client.close()
```

### Result
The simulation successfully demonstrated caching logic, where subsequent requests for the same item were served instantly via a Cache Hit, significantly reducing overhead.

---

## 4. Hashing and Sharding Work using Python

### Aim
To write a Python program demonstrating database sharding by using a hash function to distribute and retrieve data across multiple simulated storage nodes.

### Procedure
1.  **Cluster Configuration**: Initialize a list containing three separate dictionaries to simulate three distinct Database Shards (Shard 0, Shard 1, and Shard 2).
2.  **Hash Function Implementation**: Define a hash algorithm that calculates the sum of ASCII values of a key string and applies a modulo operation (`index % 3`) to determine the target shard.
3.  **Server Command Processing**: Develop a server that parses client commands in the format `COMMAND:KEY:VALUE` (for PUT) or `COMMAND:KEY` (for GET).
4.  **Targeted Storage**: For a `PUT` command, the server calculates the hash, locates the specific shard index, and stores the key-value pair within that shard's dictionary.
5.  **Sharding-Aware Retrieval**: For a `GET` command, the server uses the same hash function to jump directly to the correct shard, avoiding a full scan of all storage nodes.
6.  **Interactive Validation**: Execute several insertions (PUT) and retrievals (GET) via the client and observe the server terminal to see how data is partitioned across shards.

### Code (`Socket_Programming/ex4_hashing_sharding/SERVER.py`)
```python
import socket

NUM_SHARDS = 3
shards = [{"shard_id": i, "data": {}} for i in range(NUM_SHARDS)]

def get_shard_index(key):
    return sum(ord(c) for c in key) % NUM_SHARDS

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5003))
server.listen(1)

print("[SHARDING SERVER] Cluster online on port 5003...")
conn, addr = server.accept()

while True:
    raw_data = conn.recv(1024).decode()
    if not raw_data or raw_data.lower() == 'exit': break
    parts = raw_data.split(":")
    cmd, key = parts[0].upper(), parts[1]
    shard_idx = get_shard_index(key)
    
    if cmd == "PUT":
        val = parts[2]
        shards[shard_idx]["data"][key] = val
        msg = f"STORED in Shard {shard_idx}"
    elif cmd == "GET":
        val = shards[shard_idx]["data"].get(key, "NOT_FOUND")
        msg = f"FOUND in Shard {shard_idx}: {val}"
    conn.send(msg.encode())
conn.close()
```

### Result
The distributed storage pattern was successfully modeled through hashing, effectively demonstrating how large datasets are partitioned across multiple servers for horizontal scaling.

---

## 5. Implementing HTTP using the Requests Library in Python

### Aim
To write a Python program to communicate with a local HTTP server using the `requests` library to handle RESTful GET and POST methodologies.

### Procedure
1.  **Local HTTP Simulation**: Setup a custom Python script that utilizes raw sockets to listen on port 5004 and simulate a basic HTTP/1.1 response protocol.
2.  **Request Parsing**: Configure the server to receive incoming request headers, parse the HTTP method (GET or POST), and display the method type in the server logs.
3.  **JSON Response Generation**: Program the server to wrap processing metadata in a JSON string and send it back with appropriate HTTP status codes (e.g., 200 OK).
4.  **Library Integration**: In the client script, import the `requests` module, which abstracts low-level socket handling into simple function calls like `requests.get()`.
5.  **Active Interrogation**: Implement a menu-driven client that allows the user to trigger a GET request or a POST request (with a JSON payload) to the local server.
6.  **Status and Body Inspection**: Print the returned `status_code` and the `json()` payload from the response object to verify successful application-layer communication.

### Code (`Socket_Programming/ex5_http_requests/CLIENT.py`)
```python
import requests

url = "http://localhost:5004"

while True:
    choice = input("\n1. GET\n2. POST\n3. Exit\nChoice: ")
    if choice == '1':
        r = requests.get(url)
        print(f"Status: {r.status_code} | Body: {r.json()}")
    elif choice == '2':
        r = requests.post(url, json={"id": 101})
        print(f"Status: {r.status_code} | Body: {r.json()}")
    elif choice == '3': break
```

### Result
The program correctly demonstrated the use of the `requests` library for high-level web communication, proving its efficiency over manual socket-level HTTP header handling.

---

## 6. Implementing SMTP Protocol in a Server-Client Architecture using Python

### Aim
To write a Python program to simulate the Simple Mail Transfer Protocol (SMTP) handshake and message delivery sequence between a client and a server.

### Procedure
1.  **SMTP Server Blueprint**: Develop a server that follows the SMTP state machine, responding with code `220` upon connection and `250` for successful command acknowledgments.
2.  **Handshake Implementation**: Create a client that initiates a conversation starting with the `HELO` command to identify itself to the SMTP server.
3.  **Envelope Configuration**: Prompt the user to provide "Sender" and "Receiver" emails, then transmit them using the `MAIL FROM:` and `RCPT TO:` standard SMTP commands.
4.  **Data Transmission**: Initiate the email body sequence using the `DATA` command, sending the subject and message content, and ending the block with the protocol standard period on a new line (`.`).
5.  **Conversation Logging**: Record the interaction in both terminal windows to observe the step-by-step negotiation of the email transfer protocol.
6.  **Termination Phase**: Use the `QUIT` command to signal the end of the session, ensuring a clean disconnection from the simulated mail transport agent.

### Code (`Application_Layer/Experiments/smtp_socket_sim/smtp_client.py`)
```python
import socket

# ... (Input gathering for sender, receiver, subject, message) ...

client = socket.socket()
client.connect(("127.0.0.1", 8080))
print(client.recv(1024).decode())

def send_cmd(cmd):
    client.send((cmd + "\r\n").encode())
    print(f"Server: {client.recv(1024).decode()}")

send_cmd("HELO localhost")
send_cmd(f"MAIL FROM:<{sender}>")
send_cmd(f"RCPT TO:<{receiver}>")
send_cmd("DATA")

# Finalizing data transmission
client.send(f"Subject: {subject}\n\n{message}\n.\n".encode())
print(f"Server: {client.recv(1024).decode()}")
send_cmd("QUIT")
client.close()
```

### Result
The SMTP protocol simulation was completed successfully, replicating the authentic 5nd-to-end workflow of an email delivery system through interactive socket programming.
