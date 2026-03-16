import socket
import time

HOST = 'localhost'
PORT = 5001
BUFFER_SIZE = 1024
WINDOW_SIZE = 4
TIMEOUT = 2

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(TIMEOUT)

# Get user input
frames = []
print("💬 Enter messages to send (type 'exit' to finish):")
while True:
    msg = input("Message: ")
    if msg.lower() == 'exit':
        break
    frames.append(msg)

base = 0
next_seq = 0
acks = [False] * len(frames)

while base < len(frames):
    # Send frames within window
    while next_seq < base + WINDOW_SIZE and next_seq < len(frames):
        packet = str(next_seq).encode() + frames[next_seq].encode()
        client_socket.sendto(packet, (HOST, PORT))
        print(f"📤 Sent frame {next_seq}: {frames[next_seq]}")
        next_seq += 1

    # Wait for ACKs
    try:
        ack, _ = client_socket.recvfrom(BUFFER_SIZE)
        ack_num = int(ack.decode())
        print(f"📥 Received ACK for frame {ack_num}")

        if 0 <= ack_num < len(acks):
            acks[ack_num] = True
        else:
            print(f"⚠️ Invalid ACK received: {ack_num}")

        # Slide window
        while base < len(frames) and acks[base]:
            base += 1
    except socket.timeout:
        print("⏱️ Timeout! Resending unacknowledged frames...")
        next_seq = base
