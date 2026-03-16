import socket
import time

PORT = 12345
TOTAL_FRAMES = 10

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', PORT))

expected_frame = 0

while expected_frame < TOTAL_FRAMES:
    data, addr = s.recvfrom(1024)
    frame_num = int(data.decode().split()[1])

    if frame_num == expected_frame:
        print(f"Received Frame {frame_num}")
        expected_frame += 1
    else:
        print(f"Out of order Frame {frame_num} — Discarded")

    choice = input(f"Send ACK {expected_frame - 1}? (y/n): ").strip().lower()

    if choice != 'y':
        print("ACK dropped\n")
        continue

    ack = f"ACK {expected_frame - 1}"
    s.sendto(ack.encode(), addr)
    print(f"Sent ACK {expected_frame - 1}\n")

    time.sleep(1)

s.close()
