import socket
import time

SERVER_IP = '127.0.0.1'
PORT = 12345
WINDOW_SIZE = 4
TIMEOUT = 10

# Read input frames
frames = input("Enter items (comma-separated): ").split(',')
frames = [f.strip() for f in frames]
TOTAL_FRAMES = len(frames)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(TIMEOUT)

base = 0
next_frame = 0

print("\nGo-Back-N Sender Started\n")

while base < TOTAL_FRAMES:
    # Send frames within the window
    while next_frame < base + WINDOW_SIZE and next_frame < TOTAL_FRAMES:
        msg = f"FRAME {next_frame} {frames[next_frame]}"
        s.sendto(msg.encode(), (SERVER_IP, PORT))
        print(f"Sent Frame {next_frame}: {frames[next_frame]}")
        next_frame += 1

    # Wait for ACK
    try:
        ack, _ = s.recvfrom(1024)
        ack_num = int(ack.decode().split()[1])
        print(f"Received ACK {ack_num}")

        base = ack_num + 1
        time.sleep(1)

    except socket.timeout:
        print(f"Timeout. Resending from Frame {base}")
        next_frame = base

print("\nAll frames transmitted")
s.close()
