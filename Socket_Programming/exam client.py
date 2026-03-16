import socket

LISTEN_ADDR = ("127.0.0.1", 9999)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(LISTEN_ADDR)

expected_seq_num = 0

while True:
    data, addr = sock.recvfrom(1024)
    msg = data.decode()
    seq_num, payload = msg.split(":", 1)
    seq_num = int(seq_num)

    print(f"\nReceived packet {seq_num}: {payload}")

    if seq_num == expected_seq_num:
        print(f"Packet {seq_num} is in order.")
        choice = input("Send ACK? (y/n): ").strip().lower()
        if choice == "y":
            sock.sendto(str(seq_num).encode(), addr)
            expected_seq_num += 1
        else:
            print("ACK not sent (simulating loss).")
    else:
        print(f"Out-of-order packet {seq_num}, expecting {expected_seq_num}")
        choice = input("Send duplicate ACK for last received? (y/n): ").strip().lower()
        if choice == "y" and expected_seq_num > 0:
            sock.sendto(str(expected_seq_num - 1).encode(), addr)
