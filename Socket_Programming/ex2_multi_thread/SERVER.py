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
