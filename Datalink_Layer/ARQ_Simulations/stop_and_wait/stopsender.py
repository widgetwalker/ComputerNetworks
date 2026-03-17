import socket
import time

HOST = 'localhost'
PORT = 3300
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

message = input("Enter message: ")
seq_no = 0

for char in message:
    packet = f"{seq_no}:{char}"
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

sock.close()