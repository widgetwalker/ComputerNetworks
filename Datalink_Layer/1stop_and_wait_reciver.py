import socket
import time

HOST = '127.0.0.1'
PORT = 5050

receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind((HOST, PORT))

expected_seq = 0

print(f"Receiver ready on {HOST}:{PORT}")

while True:
    data, addr = receiver.recvfrom(1024)
    packet = data.decode()

    try:
        seq_str, msg = packet.split(":", 1)
        seq = int(seq_str)
    except:
        print("Corrupted packet received")
        continue

    print(f"Received packet {seq}: {msg}")

    if seq == expected_seq:
        choice = input(f"Send ACK{seq}? (y/n): ").strip().lower()
        if choice == "y":
            receiver.sendto(f"ACK{seq}".encode(), addr)
            print(f"Sent ACK{seq}")
        else:
            print("ACK dropped")

        expected_seq = 1 - expected_seq

    else:
        last_ack = 1 - expected_seq
        choice = input(f"Duplicate packet {seq}. Resend ACK{last_ack}? (y/n): ").strip().lower()
        if choice == "y":
            receiver.sendto(f"ACK{last_ack}".encode(), addr)
            print(f"Resent ACK{last_ack}")
        else:
            print("ACK dropped")

    time.sleep(0.3)
