import socket
import time

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024
WINDOW_SIZE = 4
TIMEOUT = 2

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(TIMEOUT)

# Get user input messages
frames = []
print("💬 Enter messages to send (type 'exit' to finish):")
while True:
    msg = input("Message: ")
    if msg.lower() == 'exit':
        break
    frames.append(msg)

base = 0
next_seq = 0

while base < len(frames):
    # Send frames within the window
    while next_seq < base + WINDOW_SIZE and next_seq < len(frames):
        packet = str(next_seq).encode() + frames[next_seq].encode()
        client_socket.sendto(packet, (HOST, PORT))
        print(f"📤 Sent frame {next_seq}: {frames[next_seq]}")
        next_seq += 1

    try:
        ack, _ = client_socket.recvfrom(BUFFER_SIZE)
        ack_num = int(ack.decode())
        print(f"📥 Received ACK for frame {ack_num}")
        base = ack_num + 1
    except socket.timeout:
        print("⏱️ Timeout! Resending window...")
        next_seq = base  # Go back and resend from base