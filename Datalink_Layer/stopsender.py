import socket
import time

HOST = 'localhost'
PORT = 3300
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)  # 5 second timeout

try:
    sock.connect((HOST, PORT))
    print(f"[CONNECTED] to {HOST}:{PORT}")
except socket.error as e:
    print(f"[ERROR] Connection failed: {e}")
    sock.close()
    exit(1)

message = input("Enter message: ")
seq_no = 0

for char in message:
    packet = f"{seq_no}:{char}"
    try:
        sock.send(packet.encode())
        print(f"[SENT] {packet}")

        ack = sock.recv(1024).decode()
        while ack != f"ACK:{seq_no}":
            print("[TIMEOUT] Resending...")
            sock.send(packet.encode())
            ack = sock.recv(1024).decode()

        print(f"[RECV] {ack}")
        seq_no = 1 - seq_no
        time.sleep(1)
    except socket.timeout:
        print(f"[TIMEOUT] No ACK received for {packet}")
        break
    except Exception as e:
        print(f"[ERROR] {e}")
        break

print("[CLOSING] connection")
sock.close()