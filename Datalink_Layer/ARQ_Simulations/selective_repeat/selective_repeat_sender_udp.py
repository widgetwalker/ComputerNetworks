import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ('localhost', 9999)

items = input("Enter items separated by commas: ")
data = [x.strip() for x in items.split(",") if x.strip()]

WINDOW = 4
base = 0
next_seq = 0
acked = set()

def recv_ack():
    global base
    while True:
        raw, _ = s.recvfrom(1024)
        text = raw.decode()
        _, seq_str = text.split("|")
        seq = int(seq_str)

        print(f"ACK {seq} received")
        acked.add(seq)

        while base in acked:
            base += 1

threading.Thread(target=recv_ack, daemon=True).start()

while base < len(data):
    while next_seq < base + WINDOW and next_seq < len(data):
        msg = f"{next_seq}|{data[next_seq]}"
        s.sendto(msg.encode(), addr)
        print(f"Sent Seq {next_seq}: {data[next_seq]}")
        next_seq += 1

    time.sleep(1)

print("All packets sent!")
s.close()
