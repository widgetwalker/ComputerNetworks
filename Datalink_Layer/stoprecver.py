import socket

HOST = ''
PORT = 3300
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, _ = sock.accept()

expected_seq = 0
received = []

while True:
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

print("Final message:", "".join(received))
conn.close()
sock.close()