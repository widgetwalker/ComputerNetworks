import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 9999))

WINDOW = 4
base = 0
buffer = {}

print("Receiver ready...")

while True:
    data, addr = s.recvfrom(1024)
    text = data.decode()

    seq_str, msg = text.split("|", 1)
    seq = int(seq_str)

    print(f"Received Seq {seq} → {msg}")

    if seq < base:
        choice = input(f"Send ACK {seq}? (y/n): ").strip().lower()
        if choice == "y":
            s.sendto(f"ACK|{seq}".encode(), addr)
        else:
            print("ACK dropped")
        continue

    if seq < base + WINDOW:
        buffer[seq] = msg

        choice = input(f"Send ACK {seq}? (y/n): ").strip().lower()
        if choice == "y":
            s.sendto(f"ACK|{seq}".encode(), addr)
        else:
            print("ACK dropped")

        while base in buffer:
            del buffer[base]
            base += 1

    else:
        print(f"Ignored Seq {seq} (out of window)")
