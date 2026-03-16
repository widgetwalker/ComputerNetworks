import socket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

messages = []
while True:
    msg = input("Enter message (or 'quit' to stop): ")
    if msg.lower() in ["quit", "exit"]:
        break
    messages.append(msg)

total_frames = len(messages)
if total_frames == 0:
    print("No frames to send.")
    client_socket.close()
    raise SystemExit

for i, msg in enumerate(messages):
    packet = f"{i}:{msg}".encode()
    client_socket.sendto(packet, (HOST, PORT))
    print(f"Sent frame {i}: {msg}")

client_socket.sendto(b"END", (HOST, PORT))

acked_up_to = -1

while True:
    data, _ = client_socket.recvfrom(BUFFER_SIZE)
    msg = data.decode()

    if msg == "COMPLETE":
        print("All frames acknowledged by receiver. Closing.")
        break

    if msg == "ACKROUND_DONE":
        base = acked_up_to + 1
        if base >= total_frames:
            continue
        print(f"Retransmitting from frame {base} onwards...")
        for i in range(base, total_frames):
            packet = f"{i}:{messages[i]}".encode()
            client_socket.sendto(packet, (HOST, PORT))
            print(f"Resent frame {i}: {messages[i]}")
        client_socket.sendto(b"END", (HOST, PORT))
        continue

    try:
        ack_num = int(msg)
    except ValueError:
        continue

    if ack_num > acked_up_to and ack_num < total_frames:
        print(f"Received ACK for frame {ack_num}")
        if ack_num == acked_up_to + 1:
            acked_up_to += 1

client_socket.close()