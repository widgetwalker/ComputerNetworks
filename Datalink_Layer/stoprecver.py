import socket

HOST = ''
PORT = 3300
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)
print(f"[LISTENING] on port {PORT}...")
conn, addr = sock.accept()
print(f"[CONNECTED] from {addr}")

conn.settimeout(5)  # 5 second timeout for receiving data
expected_seq = 0
received = []

while True:
    try:
        data = conn.recv(1024).decode()
        if not data:
            break

        seq, char = data.split(":")
        seq = int(seq)

        if seq == expected_seq:
            received.append(char)
            print(f"[RECV] {data}")
            conn.send(f"ACK:{seq}".encode())
            expected_seq = 1 - expected_seq
        else:
            print("[DUPLICATE] Ignored")
            conn.send(f"ACK:{1 - expected_seq}".encode())
    except socket.timeout:
        print("[TIMEOUT] No data received, closing connection")
        break
    except Exception as e:
        print(f"[ERROR] {e}")
        break

print("Final message:", "".join(received))
conn.close()
sock.close()